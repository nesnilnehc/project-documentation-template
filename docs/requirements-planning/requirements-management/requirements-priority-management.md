<!--
Maintenance: This document is maintained with reference to the project documentation structure defined in [README.md](../../../README.md).
Structure: requirements-planning > requirements-management > requirements-priority
-->
# Requirements Priority Management

[![Version](https://img.shields.io/badge/Version-2.0.0-blue.svg)](https://github.com/nesnilnehc/project-documentation-template)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)](https://github.com/nesnilnehc/project-documentation-template)

This document defines standardized requirements priority management processes based on mature industry prioritization frameworks, helping teams make scientific priority decisions.

## Overview

Requirements priority management ensures teams focus on the most valuable work. This specification adopts multiple industry-validated prioritization frameworks, providing appropriate evaluation methods for different scenarios.

## Industry Prioritization Frameworks

### 1. MoSCoW Method

**Use Cases**: Small projects, quick decisions, cross-functional team collaboration

| Category | Identifier | Description | Example |
|----------|------------|-------------|---------|
| **Must Have** | 🔴 M | Core product features, cannot release without | User login, payment functionality |
| **Should Have** | 🟠 S | Important but not critical, can delay release | Password reset, user profile editing |
| **Could Have** | 🟡 C | Nice-to-have features, implement if resources allow | Theme switching, keyboard shortcuts |
| **Won't Have** | ⚪ W | Not implementing in this version, avoid scope creep | Advanced reports, AI recommendations |

### 2. RICE Scoring Method

**Use Cases**: Data-driven decisions, mature products, need quantitative evaluation

**Formula**: `RICE Score = (Reach × Impact × Confidence) / Effort`

- **Reach**: Number of users affected per month
- **Impact**: Impact level on users (3=Massive, 2=High, 1=Medium, 0.5=Low, 0.25=Minimal)
- **Confidence**: Confidence in estimates (100%=High, 80%=Medium, 50%=Low)
- **Effort**: Person-months required for development

### 3. Value-Complexity Matrix

**Use Cases**: Visual decision-making, limited resources, need to quickly identify opportunities

```
High Value + Low Complexity = 🟢 Quick Wins (Execute immediately)
High Value + High Complexity = 🟡 Major Projects (Plan execution)  
Low Value + Low Complexity = 🔵 Fill-ins (Do when available)
Low Value + High Complexity = 🔴 Time Sinks (Avoid execution)
```

### 4. Kano Model

**Use Cases**: Customer satisfaction-centered, new product development

- **Basic Needs**: Must satisfy, otherwise users dissatisfied
- **Performance Needs**: Satisfaction proportional to feature performance
- **Excitement Needs**: Features exceeding expectations, bring delight

## Project Customization

### Configuration File Location

Create `.priority-config.yml` file in project root to define project-specific priority rules:

```yaml
# Project Priority Configuration
project_name: "Example Project"
priority_framework: "RICE"  # Primary framework to use

# Custom Weights (RICE only)
weights:
  reach_multiplier: 1.0
  impact_multiplier: 2.0
  confidence_multiplier: 1.0
  effort_divisor: 1.0

# Project-Specific Rules
custom_rules:
  - condition: "security_related == true"
    action: "upgrade_to_must_have"
  - condition: "technical_debt == true && impact > 3"
    action: "upgrade_priority"
  - condition: "compliance_required == true"
    action: "set_priority_high"

# Team Agreements
team_agreements:
  max_must_have: 5
  max_should_have: 10
  sprint_capacity: 20  # Story Points
```

### Rule Priority

1. **Project Configuration Rules** (Highest priority)
2. **Team Agreement Rules**
3. **Generic Framework Rules** (Lowest priority)

## Implementation Guide

### Choosing the Right Framework

| Project Characteristics | Recommended Framework | Rationale |
|------------------------|----------------------|-----------|
| Small project, tight timeline | MoSCoW | Simple and fast, easy communication |
| Sufficient data, need quantification | RICE | Scientific and objective, easy comparison |
| Limited resources, need visualization | Value-Complexity Matrix | Intuitive, quick decisions |
| New product, focus on UX | Kano Model | User satisfaction-centered |

### Hybrid Usage Strategy

**Recommended Combinations**:

1. **MoSCoW + Value-Complexity Matrix**: First classify with MoSCoW, then sort with matrix
2. **RICE + Kano**: Use Kano to identify user need types, use RICE for quantitative evaluation
3. **Phased Switching**: Use MoSCoW for MVP phase, RICE for maturity phase

## Requirement Identification Format

```
[Framework][Priority] [Date] [ID] Requirement Title - Brief Description [Estimate]

Examples:
[M] M 202401151408 REQ-001 User Login Feature - Email/password login 5SP
[R] 85.2 202401161408 REQ-002 Search Optimization - Improve search response speed 3SP
[V] High/Low 202401171408 REQ-003 Theme Switching - Light/dark theme toggle 2SP
```

## Priority Review Process

### Weekly Priority Review Meeting

1. **Review Last Week Completion** (10 minutes)
2. **Evaluate New Requirements** (20 minutes)
3. **Adjust Existing Priorities** (15 minutes)
4. **Confirm Next Week Plan** (10 minutes)
5. **Update Project Board** (5 minutes)

### Adjustment Triggers

- User feedback on major issues
- Competitor releases new features
- Major technical architecture changes
- Business goal adjustments
- Resource constraint changes

## Metrics

### Framework Effectiveness Evaluation

- **Decision Speed**: Time from requirement proposal to priority determination
- **Prediction Accuracy**: Match between actual value and expected value
- **Team Satisfaction**: Satisfaction rating for priority decision process
- **Business Value Realization**: Actual business impact of high-priority features

### Regular Reviews

- **Monthly**: Priority distribution and completion rate analysis
- **Quarterly**: Framework selection and configuration optimization
- **Semi-annually**: Overall priority strategy evaluation

## Tool Recommendations

- **Jira**: Supports custom priority fields and RICE scoring
- **Productboard**: Professional product priority management tool
- **Notion**: Flexible table and board features
- **Miro/Figma**: Value-complexity matrix visualization

## Related Documents

- [Backlog](../../process-management/project-board/backlog.md)
- [README](../../../README.md)

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 2.0.0 | 2024-01-15 | Refactored document, introduced industry frameworks, simplified process | Project Team |
| 1.0.0 | 2024-01-10 | Initial version | Project Team |

---

> **Note**: Choosing a framework that fits the project is more important than perfectly executing a single framework. Flexibly adjust based on project stage and team situation.
