# Engram

[![License: Unlicense](https://img.shields.io/badge/License-Unlicense-green.svg)](https://unlicense.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

跨项目工程规范库——为工程团队和 AI agent 提供统一、可复用的规范体系，使任何项目都能在启动时直接获得经过验证的工程标准，而无需从零建立。

## 规范类型

| 类型 | 说明 | 示例 |
|------|------|------|
| **结构性规范** | 文档应该有什么、如何组织和命名 | 项目文档结构、文档命名规则 |
| **操作性规范** | 具体工程实践如何执行 | 环境变量管理、版本控制、依赖管理 |
| **过程性规范** | 工作流程和决策方式 | ADR 格式、需求优先级框架 |

## 快速选用

根据项目情况按需选取，不需要全部采用：

| 规范 | 适用场景 | 路径 |
|------|----------|------|
| 文档结构 | 所有项目 | 本 README 的文档结构章节 |
| 环境变量管理 | 使用 .env 配置的项目 | `docs/development-guide/development-standards/configuration-management/environment-variable-management-strategy.md` |
| 语义化版本 | 需要版本管理的项目 | `docs/development-guide/release-management/versioning-standards.md` |
| 发布质量门禁 | 有发布流程的项目 | `docs/development-guide/release-management/release-quality-gate.md` |
| 依赖管理 | 有第三方依赖的项目 | `docs/architecture/system-architecture/technology-stack/dependency-management/dependency-management-strategy.md` |
| ADR 模板 | 需要记录架构决策的项目 | `docs/process-management/decisions/ADR-TEMPLATE.md` |
| 需求优先级 | 有产品规划需求的项目 | `docs/requirements-planning/requirements-management/requirements-priority-management.md` |

## AI Agent 使用

本规范库同时面向 AI agent。agent 读取入口：

- **`llms.txt`** — 完整使用说明与约定
- **`AGENTS.md`** — agent 配置与协作标准
- **`docs/specs/documentation-spec.md`** — 文档治理规范（命名、引用、验证）
- **`docs/specs/rules.yaml`** — 机器可读的验证规则

## 文档结构参考

`docs/` 下的文件为样例文档，复制到项目后按实际内容填写。文件名使用普通 `.md` 扩展名（无 `.template` 或 `.sample` 后缀）。

根据项目规模选用对应文档集：

| 文档模块 | 小型项目 | 中型项目 | 大型项目 |
|----------|:--------:|:--------:|:--------:|
| 📋 项目概述 | ✅ | ✅ | ✅ |
| 💻 开发指南 | ✅ | ✅ | ✅ |
| 👥 用户指南 | ✅ | ✅ | ✅ |
| 🏗️ 架构 | | ✅ | ✅ |
| 🎨 设计 | | ✅ | ✅ |
| 📝 需求与规划 | | ✅ | ✅ |
| 📊 过程管理 | | | ✅ |
| 🛠️ 运维指南 | | | ✅ |
| 🔒 合规 | | | ✅ |
| 🤝 社区与贡献 | | | ✅ |

```markdown
# 项目文档

## 📋 项目概述 [project-overview]

- 📄 目标与愿景 [goals-and-vision]
- 📄 商业模式 [business-model]
- 📁 路线图 [roadmap]
  - 📄 项目里程碑 [project-milestones]
  - 📄 功能路线图 [feature-roadmap]
- 📁 版本历史 [version-history]
  - 📄 发布说明 [release-notes]
  - 📄 废弃功能 [deprecated-features]

## 📝 需求与规划 [requirements-planning]

### 需求文档 [requirements-documentation]

- 📁 系统需求 [system-requirements]
  - 📄 硬件需求 [hardware-requirements]
  - 📄 软件需求 [software-requirements]
  - 📄 网络需求 [network-requirements]
  - 📄 安全需求 [security-requirements]
- 📁 业务需求 [business-requirements]
  - 📄 用户故事 [user-stories]
  - 📄 业务流程 [business-process-flow]
- 📄 可行性研究 [feasibility-studies]

### 需求管理 [requirements-management]

- 📄 需求收集 [requirements-gathering]
- 📄 需求评估 [requirements-assessment]
- 📄 需求优先级管理 [requirements-priority]

### 市场分析 [market-analysis]

- 📁 竞品分析 [competitive-analysis]
  - 📄 竞争格局 [competitor-landscape]
  - 📄 功能对比 [feature-comparison]
  - 📄 市场定位 [market-positioning]
- 📁 市场研究 [market-research]
  - 📄 目标用户 [target-audience]
  - 📄 市场趋势 [market-trends]
  - 📄 市场机会 [market-opportunities]

## 🏗️ 架构 [architecture]

### 系统架构 [system-architecture]

- 📁 基础设施架构 [infrastructure-architecture]
  - 📄 云基础设施 [cloud-infrastructure]
  - 📄 网络架构 [network-architecture]
  - 📄 资源规划 [resource-planning]
- 📁 部署架构 [deployment-architecture]
  - 📄 部署拓扑 [deployment-topology]
  - 📄 可扩展性设计 [scalability-design]
  - 📄 高可用设计 [high-availability]
- 📁 安全架构 [security-architecture]
  - 📄 认证与授权 [auth-architecture]
  - 📄 数据安全 [data-security]
  - 📄 网络安全 [network-security]
- 📁 技术栈 [technology-stack]
  - 📄 基础设施技术 [infrastructure-tech]
  - 📄 应用技术 [application-tech]
  - 📄 开发技术 [development-tech]
- 📁 依赖管理 [dependency-management]
  - 📄 第三方库 [third-party-libs]
  - 📄 版本管理 [version-management-deps]
  - 📄 License 合规 [license-compliance]

### 应用架构 [application-architecture]

- 📁 分层架构 [layered-architecture]
  - 📄 表现层 [presentation-layer]
  - 📄 业务逻辑层 [business-layer]
  - 📄 数据访问层 [data-layer]
- 📁 服务架构 [service-architecture]
  - 📄 微服务设计 [microservice-design]
  - 📄 服务接口 [service-interfaces]
  - 📄 服务通信 [service-communication]
- 📁 集成架构 [integration-architecture]
  - 📄 外部集成 [external-integrations]
  - 📄 API 网关 [api-gateway]
  - 📄 消息队列 [message-queue]
- 📁 横切关注点 [cross-cutting-concerns]
  - 📄 国际化 [internationalization]
  - 📄 日志策略 [logging-strategy]
  - 📄 缓存策略 [caching-strategy]
  - 📄 错误处理 [error-handling]
  - 📄 状态管理 [state-management]

### 数据架构 [data-architecture]

- 📁 数据库设计 [database-design]
  - 📄 数据模型 [data-models]
  - 📄 Schema 设计 [schema-design]
  - 📄 数据迁移 [data-migration]
- 📁 数据流 [data-flow]
  - 📄 数据管道 [data-pipeline]
  - 📄 数据转换 [data-transformation]

### API 架构 [api-architecture]

- 📁 API 设计 [api-design]
  - 📄 RESTful API [restful-api]
  - 📄 GraphQL API [graphql-api]
  - 📄 API 版本管理 [api-versioning]
- 📄 接口规范 [interface-specifications]
- 📄 API 文档 [api-documentation]

## 🎨 设计 [design]

### 品牌指南 [brand-guidelines]

- 📄 品牌标识 [brand-identity]
- 📄 品牌故事 [brand-story]
- 📄 视觉识别系统 [visual-identity-system]

### UI/UX 设计 [ui-ux-design]

- 📄 界面设计 [ui-design]
- 📄 交互设计 [interaction-design]
- 📄 用户体验设计 [ux-design]

### 设计流程 [design-process]

- 📄 设计系统 [design-system]
- 📄 原型与线框图 [prototypes-wireframes]
- 📄 可用性测试 [usability-testing]

## 💻 开发指南 [development-guide]

### 开发规范 [development-standards]

- 📁 编码规范 [coding-standards]
  - 📄 命名约定 [naming-conventions]
  - 📄 格式规则 [formatting-rules]
  - 📄 注释指南 [commenting-guidelines]
  - 📄 语言特定规范 [language-specific-standards]
- 📄 设计原则 [design-principles]
- 📄 架构模式 [architecture-patterns]
- 📄 代码审查指南 [code-review]
- 📄 安全规范 [security-standards]
- 📁 配置管理 [configuration-management]
  - 📄 环境变量管理 [environment-variable-management]
  - 📄 配置规范 [configuration-standards]

### 实现 [implementation]

- 📁 前端实现 [frontend-implementation]
  - 📄 组件架构 [component-architecture]
  - 📄 页面结构 [page-structure]
  - 📄 客户端路由 [client-routing]
- 📁 后端实现 [backend-implementation]
  - 📄 模块实现 [module-implementation]
  - 📄 服务实现 [service-implementation]
  - 📄 业务逻辑 [business-logic]

### 构建与测试 [build-test]

- 📁 构建流程 [build-process]
  - 📄 构建配置 [build-configuration]
  - 📄 构建工具 [build-tools]
- 📁 测试规范 [testing-standards]
  - 📄 测试计划 [test-plans]
  - 📄 测试用例 [test-cases]
  - 📄 自动化测试 [automated-testing]
  - 📄 性能测试 [performance-testing]
  - 📄 测试覆盖率要求 [test-coverage]
- 📁 质量保证 [quality-assurance]
  - 📄 代码质量规范 [code-quality]
  - 📄 安全扫描 [security-scanning]
  - 📄 质量指标 [quality-metrics]

### 发布管理 [release-management]

- 📁 版本规范 [versioning-standards]
  - 📄 版本生命周期 [version-lifecycle]
  - 📄 语义化版本 [semantic-versioning]
- 📁 发布流程 [release-process]
  - 📄 发布规划 [release-planning]
  - 📄 发布清单 [release-checklist]

### 故障排查 [dev-troubleshooting]

- 📄 环境搭建问题 [env-setup-issues]
- 📄 构建与编译问题 [build-issues]
- 📄 调试指南 [debugging-guide]
- 📄 开发者 FAQ [developer-faq]

## 📊 过程管理 [process-management]

### 敏捷工作流 [agile-workflow]

- 📁 Sprint 管理 [sprint-management]
  - 📄 Sprint 规划 [sprint-planning]
  - 📄 当前 Sprint [current-sprint]
  - 📄 Sprint 回顾 [sprint-retrospective]
  - 📄 Sprint 指标 [sprint-metrics]
- 📁 项目看板 [project-board]
  - 📄 Backlog [backlog]
  - 📄 进行中 [in-progress]
  - 📄 已完成 [done]
  - 📄 阻塞 [blocked]
- 📁 团队协作 [team-collaboration]
  - 📄 沟通指南 [communication-guidelines]
  - 📁 会议记录 [meeting-records]
    - 📄 每日站会 [daily-standup]
    - 📄 Sprint 评审 [sprint-review]
    - 📄 技术评审 [technical-review]

### 变更管理 [change-management]

- 📁 变更请求流程 [change-request-process]
  - 📄 需求变更 [requirements-change]
  - 📄 架构变更 [architecture-change]
  - 📄 变更请求模板 [change-request]
  - 📄 变更评估 [change-assessment]
  - 📄 变更实施 [change-implementation]
- 📁 架构决策记录 [architecture-decisions]
  - 📄 ADR 模板 [adr-template]
  - 📁 决策记录 [decision-records]
    - 规范文件名格式：`ADR-<3位数字>-<kebab-title>.md`（例：`ADR-001-service-boundary.md`）
    - 包含：背景、选项分析、决策依据、影响
  - ADR 适用场景：技术选型、架构变更、跨项目决策
  - 参考：[ADR 官方文档](https://adr.github.io/) · [为什么用 ADR](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

### 项目治理 [project-governance]

- 📄 项目启动 [project-kickoff]
- 📄 项目状态报告 [project-status]
- 📄 干系人沟通 [stakeholder-communication]

## 🛠️ 运维指南 [operations-guide]

### 部署 [deployment]

- 📁 部署策略 [deployment-strategy]
  - 📄 部署模式 [deployment-patterns]
  - 📄 回滚策略 [rollback-strategy]
- 📁 部署流程 [deployment-process]
  - 📄 部署前检查清单 [pre-deployment]
  - 📄 部署步骤 [deployment-steps]
  - 📄 部署后验证 [post-deployment]
- 📁 环境管理 [environment-management]
  - 📄 开发环境 [dev-environment]
  - 📄 预发环境 [staging-environment]
  - 📄 生产环境 [prod-environment]
  - 📄 环境配置 [environment-configuration]

### 监控与维护 [monitoring-maintenance]

- 📁 监控与告警 [monitoring-alerting]
  - 📄 指标与 KPI [metrics-kpis]
  - 📄 告警配置 [alert-configuration]
- 📁 日志管理 [log-management]
  - 📄 日志采集 [log-collection]
  - 📄 日志分析 [log-analysis]
- 📁 备份与恢复 [backup-recovery]
  - 📄 备份策略 [backup-strategy]
  - 📄 恢复流程 [recovery-procedures]
- 📁 系统维护 [system-maintenance]
  - 📄 更新策略 [update-strategy]
  - 📄 补丁管理 [patch-management]
  - 📄 维护窗口 [maintenance-windows]

### 故障排查 [ops-troubleshooting]

- 📄 部署问题 [deployment-issues]
- 📄 性能问题 [performance-issues]
- 📄 故障响应 [incident-response]
- 📄 运维 FAQ [operations-faq]

## 👥 用户指南 [user-guide]

### 快速入门 [getting-started]

- 📄 系统搭建 [system-setup]
- 📄 快速开始指南 [quick-start-guide]
- 📄 基础概念 [basic-concepts]

### 功能文档 [feature-documentation]

- 📄 核心功能 [core-features]
- 📄 高级功能 [advanced-features]
- 📄 功能教程 [feature-tutorials]

### 故障排查 [user-troubleshooting]

- 📄 FAQ [faq]
- 📄 错误信息 [error-messages]
- 📄 常见问题与解决方案 [common-issues]

### 学习资源 [learning-resources]

- 📄 视频教程 [video-tutorials]
- 📄 代码示例 [code-examples]
- 📄 最佳实践 [best-practices]
- 📄 外部资源 [external-resources]

## 🔒 合规 [compliance]

- 📁 License 协议 [license-agreements]
  - 📄 项目 License [project-license]
  - 📄 第三方依赖 [third-party-licenses]
- 📁 数据隐私 [data-privacy]
  - 📄 隐私政策 [privacy-policy]
  - 📄 GDPR 合规 [gdpr-compliance]
  - 📄 数据保护 [data-protection]

## 🤝 社区与贡献 [community-contributing]

### 贡献 [contributing]

- 📄 贡献指南 [contributing-guidelines]
- 📄 行为准则 [code-of-conduct]

### 支持 [support]

- 📁 技术支持 [technical-support]
  - 📄 支持渠道 [support-channels]
  - 📄 问题报告 [issue-reporting]
- 📄 社区资源 [community-resources]
```

## 许可证

本项目基于 [Unlicense](LICENSE) 协议开放。
