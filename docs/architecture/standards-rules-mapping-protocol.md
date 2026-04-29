---
artifact_type: architecture-doc
lifecycle: living
---

# Standards-Rules Mapping Protocol

本文件定义 `engram` 工程规范与 `ai-cortex` agent rules 之间的对应协议，是 G2「规范对人和 Agent 均直接可用」目标的核心设计文档（M4 交付物）。

## 协议目标

- 每条工程规范在 ai-cortex 中有明确对应的 rule（1:1 可追溯）
- 规范是唯一 source of truth；rule 引用规范，不复制内容
- 规范更新后，agent 侧通过引用机制自动获得最新版本，无需手动同步

## 对应关系格式

每条规范与 rule 的对应关系用以下元数据描述：

| 字段 | 类型 | 说明 |
|------|------|------|
| `standard_path` | string | 规范文件路径（相对于 engram 根目录） |
| `rule_path` | string | 对应 rule 文件路径（相对于 ai-cortex 根目录） |
| `sync_method` | enum | `reference`（rule 引用规范 URL）/ `embed`（rule 内嵌核心约束摘要） |
| `coverage` | enum | `full`（rule 覆盖整条规范）/ `partial`（覆盖部分，需注明范围） |
| `partial_scope` | string | 仅 `coverage: partial` 时填写，说明覆盖的约束范围 |

### 示例（YAML 格式）

```yaml
mappings:
  - standard_path: docs/development-guide/development-standards/configuration-management/environment-variable-management-strategy.md
    rule_path: rules/engineering/environment-variable-management.md
    sync_method: reference
    coverage: full
```

## 同步机制

### Reference 模式（推荐）

Rule 文件头部声明 `source:` 字段，指向规范文件的 canonical URL；rule 正文仅保留 agent 执行所需的约束摘要，不复制规范原文。

```markdown
---
source: https://github.com/nesnilnehc/engram/blob/main/<standard-path>
---

# Rule: <name>

[可执行约束摘要，从规范中提取]
```

**适用场景**：规范以叙述形式为主，agent 需要提取关键约束时。

### Embed 模式

将规范中的机器可读约束直接内嵌在 rule 中；须在 rule 中标注 `last_synced_from` 和 `source_path`，并在规范更新时手动同步 embed 内容。

**适用场景**：规范中有结构化的可执行约束列表（如命名规则、字段要求），直接嵌入 rule 更高效。

## 追溯路径

**从 rule 追溯到规范：**

```
ai-cortex/rules/<category>/<rule-name>.md
  └─ source: <engram 规范 URL>
       └─ docs/<standard-path>（本地检出路径）
```

**从规范追溯到 rule：**

```
engram/docs/<standard-path>
  └─ docs/architecture/standards-rules-mapping-protocol.md（本文件 mappings 表）
       └─ ai-cortex/rules/<rule-path>
```

## 当前映射状态

> M5 交付物：完成下表所有 rule 的建立，并更新对应状态。

| 规范 | 规范路径 | 对应 rule 路径 | 同步方式 | 状态 |
|------|----------|----------------|----------|------|
| 环境变量管理策略 | `docs/development-guide/development-standards/configuration-management/environment-variable-management-strategy.md` | `rules/engineering/environment-variable-management.md` | reference | 待建立 |
| 语义化版本规范 | `docs/development-guide/release-management/versioning-standards.md` | `rules/engineering/versioning-standards.md` | reference | 待建立 |
| 发布质量门禁 | `docs/development-guide/release-management/release-quality-gate.md` | `rules/engineering/release-quality-gate.md` | reference | 待建立 |
| 依赖管理策略 | `docs/architecture/system-architecture/technology-stack/dependency-management/dependency-management-strategy.md` | `rules/engineering/dependency-management.md` | reference | 待建立 |
| 需求优先级管理 | `docs/requirements-planning/requirements-management/requirements-priority-management.md` | `rules/process/requirements-priority-management.md` | reference | 待建立 |
| ADR 模板 | `docs/process-management/decisions/ADR-TEMPLATE.md` | `rules/process/adr-template.md` | embed | 待建立 |
