#!/usr/bin/env python3
"""Validate documentation governance rules for this repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
RULES_PATH = ROOT / "docs/specs/rules.yaml"


def load_rules() -> dict:
    return json.loads(RULES_PATH.read_text(encoding="utf-8"))


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def find_placeholder_violations(text: str, allow_patterns: list[str]) -> list[str]:
    sanitized = re.sub(r"```[\s\S]*?```", "", text)
    sanitized = re.sub(r"`[^`\n]+`", "", sanitized)
    bracket_tokens = re.findall(r"\[[^\]\n]{1,120}\]", sanitized)
    allowed = [re.compile(p) for p in allow_patterns]
    violations: list[str] = []
    for token in bracket_tokens:
        if any(p.fullmatch(token) for p in allowed):
            continue
        violations.append(token)
    return violations


def find_date_violations(text: str, date_pattern: str) -> list[str]:
    matches = re.findall(r"\b\d{4}[-/]\d{2}[-/]\d{2}\b", text)
    allowed = re.compile(date_pattern)
    return [m for m in matches if not allowed.fullmatch(m)]


def find_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def validate_link_target(file_path: Path, target: str) -> bool:
    if target.startswith(("http://", "https://", "#", "mailto:")):
        return True
    clean = target.split("#", 1)[0].strip()
    if not clean:
        return True
    resolved = (file_path.parent / clean).resolve()
    return resolved.exists()


def validate_naming(
    root: Path,
    check_roots: list[str],
    directory_pattern: str,
    filename_patterns: list[str],
    allow_filenames: list[str],
) -> list[str]:
    dir_re = re.compile(directory_pattern)
    file_res = [re.compile(p) for p in filename_patterns]
    allowed_files = set(allow_filenames)
    violations: list[str] = []

    for check_root in check_roots:
        absolute_root = (root / check_root).resolve()
        if not absolute_root.exists():
            continue

        for path in absolute_root.rglob("*"):
            if path.is_dir():
                if not dir_re.fullmatch(path.name):
                    violations.append(f"directory name is not kebab-case: {path.relative_to(root)}")
                continue

            if path.suffix != ".md":
                continue

            if path.name in allowed_files:
                continue

            if any(file_re.fullmatch(path.name) for file_re in file_res):
                continue

            violations.append(f"markdown filename is not allowed by naming policy: {path.relative_to(root)}")

    return violations


def main() -> int:
    rules = load_rules()
    enforced_paths = [ROOT / p for p in rules["enforced_paths"]]
    placeholder_paths = {
        (ROOT / p).resolve() for p in rules["placeholder"].get("check_paths", [])
    }
    date_paths = {(ROOT / p).resolve() for p in rules["date"].get("check_paths", [])}
    link_paths = {(ROOT / p).resolve() for p in rules["links"].get("check_paths", [])}
    allowed_missing_targets = set(rules["links"].get("allow_missing_targets", []))

    placeholder_rule = rules["placeholder"]["rule_id"]
    date_rule = rules["date"]["rule_id"]
    link_rule = rules["links"]["rule_id"]
    align_rule = rules["entry_alignment"]["rule_id"]
    conflict_rule = rules["entry_alignment"]["rule_id_conflict"]
    naming_rules = rules.get("naming", {})
    naming_rule = naming_rules.get("rule_id", "DOC-NAMING-003")

    failures: list[str] = []

    for path in enforced_paths:
        if not path.exists():
            failures.append(f"[{align_rule}] missing enforced file: {path.relative_to(ROOT)}")
            continue

        content = read_file(path)

        if rules["placeholder"]["enabled"] and path.resolve() in placeholder_paths:
            placeholder_violations = find_placeholder_violations(
                content, rules["placeholder"]["allow_patterns"]
            )
            for token in placeholder_violations:
                failures.append(
                    f"[{placeholder_rule}] {path.relative_to(ROOT)} unresolved placeholder: {token}"
                )

        if rules["date"]["enabled"] and path.resolve() in date_paths:
            date_violations = find_date_violations(content, rules["date"]["pattern"])
            for token in date_violations:
                failures.append(f"[{date_rule}] {path.relative_to(ROOT)} invalid date: {token}")

        if rules["links"]["enabled"] and path.resolve() in link_paths:
            for link in find_links(content):
                if link in allowed_missing_targets:
                    continue
                if not validate_link_target(path, link):
                    failures.append(
                        f"[{link_rule}] {path.relative_to(ROOT)} broken relative link target: {link}"
                    )

    if rules["entry_alignment"]["enabled"]:
        required = rules["entry_alignment"]["required_spec_reference"]
        for entry in ("README.md", "llms.txt", "AGENTS.md"):
            content = read_file(ROOT / entry)
            if required not in content:
                failures.append(f"[{align_rule}] {entry} missing spec reference: {required}")

        readme = read_file(ROOT / "README.md")
        llms = read_file(ROOT / "llms.txt")
        if "YYYYMMDD-{decision-title}.md" in readme and "ADR-001" in llms:
            failures.append(
                f"[{conflict_rule}] README.md and llms.txt define conflicting ADR naming policies"
            )

    if naming_rules.get("enabled"):
        naming_violations = validate_naming(
            root=ROOT,
            check_roots=naming_rules.get("check_roots", []),
            directory_pattern=naming_rules.get(
                "directory_pattern", r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
            ),
            filename_patterns=naming_rules.get("filename_patterns", []),
            allow_filenames=naming_rules.get("allow_filenames", []),
        )
        for violation in naming_violations:
            failures.append(f"[{naming_rule}] {violation}")

    if failures:
        print("Documentation spec validation failed:")
        for item in failures:
            print(f"- {item}")
        return 1

    print("Documentation spec validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
