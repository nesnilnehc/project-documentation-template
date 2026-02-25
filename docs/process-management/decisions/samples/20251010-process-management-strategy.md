# ADR-001: Process Management Strategy (Hybrid Model)

**Date:** 2025-10-10  
**Status:** Accepted  
**Decision Makers:** Project Core Team  
**Related Issue/PR:** -

## Context and Problem Statement

For projects that may run on multiple code hosting platforms (GitLab, GitHub, Gitea, etc.), especially open source projects, the project team needs to decide:

1. How to manage project tasks and boards?
2. How to ensure project management data isn't lost during platform migration?
3. How to balance platform feature utilization and data sovereignty?

## Considered Options

### Option 1: Fully Use Platform Issue/Project

**Description:**

- All task management uses GitLab/GitHub's Issue and Project Board
- No project management data retained in Git repository

**Pros:**

- ✅ Fully leverage platform features (automation, notifications, boards)
- ✅ Seamless integration with PR/MR
- ✅ Powerful collaboration features
- ✅ Aligns with industry standard practices

**Cons:**

- ❌ Platform lock-in, data may be lost during migration
- ❌ Depends on platform availability
- ❌ Large feature differences between platforms
- ❌ Historical records may not be fully preserved

### Option 2: Fully Use Git Repository Management

**Description:**

- Maintain all tasks and boards in `docs/process-management/project-board/`
- Use Markdown files to record project management information, including:
  - `backlog.md` - Backlog
  - `in-progress.md` - In Progress
  - `done.md` - Done
  - `blocked.md` - Blocked
  - `cancelled.md` - Cancelled
- All task status changes recorded through Git commits

**Pros:**

- ✅ Completely platform-independent
- ✅ Data sovereignty
- ✅ Complete version control
- ✅ Simple and transparent

**Cons:**

- ❌ Lacks automation
- ❌ No notification mechanism
- ❌ Limited collaboration features
- ❌ Requires significant manual maintenance
- ❌ Violates standard documentation management practices

### Option 3: Hybrid Model (Git + Platform Tools) ⭐

**Description:**

- **Git Repository**: Store strategic, long-term information
  - Product roadmap (`roadmap/`)
  - Milestone planning and archives (`archived/`)
  - Architecture Decision Records ADR (`docs/process-management/decisions/`)
  - Project board archives (optional, for platform migration backup)
  
- **Platform Tools** (GitLab/GitHub Issue and Project Board): Daily development task management
  - Feature development tasks (Issue + Labels)
  - Bug tracking (Issue + Bug Label)
  - Code review discussions (Merge Request/Pull Request)
  - Sprint boards (Project Board with Backlog/In Progress/Done)

**Pros:**

- ✅ Core information not lost (platform migration friendly)
- ✅ Fully leverage platform features
- ✅ Layered information management (strategic vs tactical)
- ✅ Avoid duplicate maintenance
- ✅ High development efficiency

**Cons:**

- ❌ Need to maintain two places (but minimal workload)
- ❌ Requires team understanding and adherence to standards

## Decision

Chose **Option 3: Hybrid Model (Git + Platform Tools)**

### Rationale

1. **Best Balance**
   - Ensures platform migration friendliness while fully leveraging platform features
   - Won't sacrifice development efficiency to preserve Git management

2. **Fits Actual Use Cases**
   - Open source projects may run on different platforms or be forked
   - Strategic planning needs long-term preservation and version control
   - Daily development needs platform tool automation capabilities

3. **Clear Information Layering**
   - **Strategic Layer** (Git): Product direction, architecture decisions → Long-term preservation
   - **Tactical Layer** (Platform): Daily tasks, bug tracking → Temporary information

4. **Minimize Maintenance Cost**
   - Product roadmap and ADR update frequency is low
   - Daily tasks managed on platform, no extra maintenance needed
   - Only need to archive when major milestones complete

## Consequences

### Positive Impacts

- ✅ Core information not lost during platform migration
- ✅ New contributors can quickly understand project background and planning
- ✅ Important decisions have complete records and traceability
- ✅ Daily development efficiency unaffected
- ✅ Aligns with open source project best practices

### Negative Impacts and Risks

- ⚠️ Team needs to understand when to use Git vs platform
  - **Mitigation:** Clearly explain in `process-management/README.md`

- ⚠️ Need to regularly maintain Git documents
  - **Mitigation:** Set regular update schedule (monthly/per version)

- ⚠️ Possible information desynchronization
  - **Mitigation:** Git only records decided content, platform records discussion process

### Technical Debt

No obvious technical debt. If hybrid model maintenance cost becomes too high in the future, can re-evaluate.

## Implementation Plan

Suggested implementation steps:

1. [ ] Regularly (monthly/per version) update strategic planning documents

## Validation Criteria

How to verify if this decision is successful:

- ✅ Team members can clearly distinguish when to use Git vs platform tools
- ✅ Strategic planning documents regularly updated (recommended at least once per month or version)
- ✅ Major technical decisions have corresponding ADR records
- ✅ Can quickly restore core project management data during platform migration
- ✅ New contributors can quickly understand project direction and background through Git documents
- ✅ Daily development task management efficiency hasn't decreased

## References

- [Architecture Decision Records (ADR)](https://adr.github.io/)
- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [GitLab Issue Boards](https://docs.gitlab.com/ee/user/project/issue_board.html)
- [Documentation Management Best Practices](https://www.writethedocs.org/guide/docs-as-code/)

## Related ADRs

- Predecessor: None
- Successor: May need ADR to decide specific platform migration strategy
- Supersedes: None

---

## Application Scenarios

This decision is particularly suitable for:

- ✅ **Open Source Projects** - May be forked or migrated to different platforms
- ✅ **Multi-Platform Projects** - Maintained on multiple code hosting platforms simultaneously
- ✅ **Long-Term Projects** - Need to preserve complete decision history
- ✅ **Team Collaboration Projects** - Need to balance documentation accumulation and collaboration efficiency

## Update History

- 2025-10-10: Created ADR (generic version)
- 2025-10-10: Updated status to "Accepted"
