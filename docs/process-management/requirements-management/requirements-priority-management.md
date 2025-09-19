# 需求优先级管理规范 Requirements Priority Management

[![文档版本](https://img.shields.io/badge/Version-2.0.0-blue.svg)](https://github.com/nesnilnehc/project-documentation-template)
[![更新状态](https://img.shields.io/badge/Status-Active-green.svg)](https://github.com/nesnilnehc/project-documentation-template)

本文档定义了项目需求优先级管理的标准化流程，基于行业成熟的优先级框架，帮助团队做出科学的优先级决策。

## 🎯 概述

需求优先级管理确保团队专注于最有价值的工作。本规范采用多种行业验证的优先级框架 <mcreference link="https://www.atlassian.com/agile/product-management/prioritization-framework" index="1">1</mcreference>，为不同场景提供合适的评估方法。

## 📋 行业优先级框架

### 1. MoSCoW 方法 <mcreference link="https://www.altexsoft.com/blog/most-popular-prioritization-techniques-and-methods-moscow-rice-kano-model-walking-skeleton-and-others/" index="3">3</mcreference>

**适用场景**: 小型项目、快速决策、跨职能团队协作

| 分类 | 标识 | 描述 | 示例 |
|------|------|------|------|
| **Must Have** | 🔴 M | 产品核心功能，缺失则无法发布 | 用户登录、支付功能 |
| **Should Have** | 🟠 S | 重要但非关键，可延后发布 | 密码重置、用户资料编辑 |
| **Could Have** | 🟡 C | 锦上添花功能，资源充足时实现 | 主题切换、快捷键 |
| **Won't Have** | ⚪ W | 本版本不实现，避免范围蔓延 | 高级报表、AI 推荐 |

### 2. RICE 评分法 <mcreference link="https://productschool.com/blog/product-fundamentals/ultimate-guide-product-prioritization" index="2">2</mcreference>

**适用场景**: 数据驱动决策、成熟产品、需要量化评估

**计算公式**: `RICE 分数 = (Reach × Impact × Confidence) / Effort`

- **Reach (覆盖面)**: 每月影响的用户数量
- **Impact (影响力)**: 对用户的影响程度 (3=巨大, 2=高, 1=中等, 0.5=低, 0.25=最小)
- **Confidence (信心度)**: 对估算的信心 (100%=高, 80%=中, 50%=低)
- **Effort (工作量)**: 开发所需的人月数

### 3. 价值-复杂度矩阵 <mcreference link="https://www.productboard.com/glossary/product-prioritization-frameworks/" index="5">5</mcreference>

**适用场景**: 可视化决策、资源有限、需要快速识别机会

```
高价值 + 低复杂度 = 🟢 快速胜利 (立即执行)
高价值 + 高复杂度 = 🟡 重大项目 (规划执行)  
低价值 + 低复杂度 = 🔵 填充项目 (有空时做)
低价值 + 高复杂度 = 🔴 时间陷阱 (避免执行)
```

### 4. Kano 模型 <mcreference link="https://www.productboard.com/glossary/product-prioritization-frameworks/" index="5">5</mcreference>

**适用场景**: 以客户满意度为中心、新产品开发

- **基本需求**: 必须满足，否则用户不满
- **期望需求**: 满足度与功能表现成正比
- **兴奋需求**: 超出预期的功能，带来惊喜

## 🔧 项目个性化配置

### 配置文件位置

在项目根目录创建 `.priority-config.yml` 文件，定义项目特定的优先级规则：

```yaml
# 项目优先级配置文件
project_name: "示例项目"
priority_framework: "RICE"  # 主要使用的框架

# 自定义权重 (仅适用于 RICE)
weights:
  reach_multiplier: 1.0
  impact_multiplier: 2.0
  confidence_multiplier: 1.0
  effort_divisor: 1.0

# 项目特定规则
custom_rules:
  - condition: "security_related == true"
    action: "upgrade_to_must_have"
  - condition: "technical_debt == true && impact > 3"
    action: "upgrade_priority"
  - condition: "compliance_required == true"
    action: "set_priority_high"

# 团队约定
team_agreements:
  max_must_have: 5
  max_should_have: 10
  sprint_capacity: 20  # Story Points
```

### 规则优先级

1. **项目配置文件规则** (最高优先级)
2. **团队约定规则**
3. **通用框架规则** (最低优先级)

## 📊 实施指南

### 选择合适的框架

| 项目特征 | 推荐框架 | 原因 |
|----------|----------|------|
| 小型项目，时间紧迫 | MoSCoW | 简单快速，易于沟通 <mcreference link="https://www.altexsoft.com/blog/most-popular-prioritization-techniques-and-methods-moscow-rice-kano-model-walking-skeleton-and-others/" index="3">3</mcreference> |
| 数据充足，需要量化 | RICE | 科学客观，便于比较 <mcreference link="https://productschool.com/blog/product-fundamentals/ultimate-guide-product-prioritization" index="2">2</mcreference> |
| 资源有限，需要可视化 | 价值-复杂度矩阵 | 直观明了，快速决策 |
| 新产品，关注用户体验 | Kano 模型 | 以用户满意度为中心 |

### 混合使用策略

**推荐组合** <mcreference link="https://productschool.com/blog/product-fundamentals/ultimate-guide-product-prioritization" index="2">2</mcreference>:

1. **MoSCoW + 价值-复杂度矩阵**: 先用 MoSCoW 分类，再用矩阵排序
2. **RICE + Kano**: 用 Kano 识别用户需求类型，用 RICE 量化评估
3. **阶段性切换**: MVP 阶段用 MoSCoW，成熟期用 RICE

## 📝 需求标识格式

```
[框架][优先级] [日期] [ID] 需求标题 - 简要描述 [估算]

示例：
[M] M 202401151408 REQ-001 用户登录功能 - 邮箱密码登录 5SP
[R] 85.2 202401161408 REQ-002 搜索优化 - 提升搜索响应速度 3SP
[V] 高/低 202401171408 REQ-003 主题切换 - 明暗主题切换 2SP
```

## 🔄 优先级评审流程

### 每周优先级评审会

1. **回顾上周完成情况** (10 分钟)
2. **评估新增需求** (20 分钟)
3. **调整现有优先级** (15 分钟)
4. **确认下周计划** (10 分钟)
5. **更新项目看板** (5 分钟)

### 调整触发条件

- 用户反馈重大问题
- 竞争对手发布新功能
- 技术架构重大变更
- 业务目标调整
- 资源约束变化

## 📈 度量指标

### 框架效果评估

- **决策速度**: 从需求提出到优先级确定的时间
- **预测准确性**: 实际价值与预期价值的匹配度
- **团队满意度**: 对优先级决策过程的满意度评分
- **业务价值实现**: 高优先级功能的实际业务影响

### 定期回顾

- **每月**: 优先级分布和完成率分析
- **每季度**: 框架选择和配置优化
- **每半年**: 整体优先级策略评估

## 🛠️ 工具推荐

- **Jira**: 支持自定义优先级字段和 RICE 评分
- **Productboard**: 专业的产品优先级管理工具
- **Notion**: 灵活的表格和看板功能
- **Miro/Figma**: 价值-复杂度矩阵可视化

## 📚 相关文档

- <mcfile name="backlog.sample.md" path="docs/process-management/project-board/backlog.sample.md"></mcfile>
- <mcfile name="README.md" path="README.md"></mcfile>
- [项目看板管理](../project-board/README.md)

## 📝 版本历史

| 版本 | 日期 | 变更内容 | 作者 |
|------|------|----------|------|
| 2.0.0 | 2024-01-15 | 重构文档，引入行业框架，简化流程 | 项目团队 |
| 1.0.0 | 2024-01-10 | 初始版本 | 项目团队 |

---

> **注意**: 选择适合项目的框架比完美执行单一框架更重要。根据项目阶段和团队情况灵活调整。