# Documentation Spec

## Purpose

This spec is the single source of truth for documentation governance in this repository.
It defines naming, references, placeholders, dates, and validation boundaries for template content.

## Scope

- In scope (enforced):
  - `README.md`
  - `llms.txt`
  - `AGENTS.md`
  - `docs/specs/**`
- Out of scope (sample content, not strictly enforced by CI in this repository):
  - `docs/**` except `docs/specs/**`

## Core Decisions (Frozen)

### DEC-001 ADR naming policy

- ADR identifier uses sequential format: `ADR-001`, `ADR-002`, ...
- Recommended ADR filename format: `ADR-<3digits>-<kebab-title>.md`
- Legacy date-prefixed ADR filenames may exist in historical samples, but new ADRs should use the canonical ADR format above.

### DEC-002 Reference syntax policy

- Default internal references must use Markdown links: `[name](relative/path.md)`.
- `<mcfile>` and `<mcreference>` are optional interoperability tags for specific tooling contexts, not required as repository-wide default syntax.

### DEC-003 Minimum document set by project scale

- Small: Project Overview, Development Guide, User Guide
- Medium: Small + Architecture + Design + Requirements & Planning
- Large: Medium + Process Management + Operations Guide + Compliance + Community & Contributing

## Rules

### Rule IDs

Each rule uses a stable identifier: `DOC-<category>-<number>`.

### Naming Rules

- `DOC-NAMING-001`:
  - Files in this template repository use `.md` for document files.
  - `.template` and `.sample` suffixes are not used.
- `DOC-NAMING-002`:
  - New ADR filenames should follow `ADR-<3digits>-<kebab-title>.md`.
- `DOC-NAMING-003`:
  - Directory names and Markdown filenames under `docs/` should use `kebab-case` (`lowercase-with-hyphens`).
  - Allowed filename exceptions:
    - `ADR-<3digits>-<kebab-title>.md` (ADR identifier policy)
    - `ADR-TEMPLATE.md` (legacy template entry kept for compatibility)

### Placeholder Rules

- `DOC-PLACEHOLDER-001`:
  - Enforced scope must not contain unresolved placeholders in square-bracket form, such as `[description]` or `[option1/option2]`.
  - Exception: markdown task checkboxes (`[ ]`, `[x]`, `[X]`).

### Date Rules

- `DOC-DATE-001`:
  - Dates in enforced scope must follow `YYYY-MM-DD`.

### Link Rules

- `DOC-LINK-001`:
  - Relative Markdown links in enforced scope must resolve to existing files.
  - External links (`http://`, `https://`) are not resolved by this rule.

### Entry-Document Alignment Rules

- `DOC-ALIGN-001`:
  - `README.md`, `llms.txt`, and `AGENTS.md` must reference this spec as the governing document.
- `DOC-ALIGN-002`:
  - These entry documents must not define conflicting instructions for ADR naming and default internal reference syntax.

## Validation Contract

Validation output maps each failure to a rule ID and file path.

### Quantitative Gates

- `placeholder = 0`
- `broken internal links = 0`
- `date format violations = 0`
- `entry-doc conflicts = 0`

## Implementation Notes

- Machine-readable rules are defined in `docs/specs/rules.yaml`.
- Automated checks are implemented in `scripts/validate_docs_spec.py`.
- CI gate runs in `.github/workflows/docs-spec-check.yml`.
