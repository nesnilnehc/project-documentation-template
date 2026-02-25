<!--
Maintenance: 本文档以 [README.md](../../../README.md) 定义的项目文档结构为参考进行维护。
Structure: development-guide > release-management > versioning-standards
-->
# Semantic Versioning Standards

## Overview

This document defines complete version number management standards based on Semantic Versioning 2.0.0. It establishes a unified version management system by precisely specifying the mapping between version numbers and development stages, iteration cycles, build processes, branch strategies, and commit hashes, ensuring consistency, traceability, and practicality of version information throughout the software development lifecycle.

### Design Principles

1. **Semantic Clarity**: Version numbers clearly express the nature and scale of software changes
2. **Consistency Guarantee**: Version identification remains consistent across stages, branches, builds, and environments
3. **Traceability**: Any version can be traced back to specific code state and build information
4. **Compatibility Priority**: While following SemVer 2.0.0, prioritize practical application compatibility (Docker, package managers, etc.)

### Quick Reference

| Component | Format | Example |
|-----------|--------|---------|
| **Complete Version** | `<major>.<minor>.<patch>[-<prerelease>][-<buildmetadata>]` | `1.6.0-beta.1-20251010.256.4d798ed` |
| **Prerelease ID** | `<stage>[.<iteration>]` | `alpha.1`, `beta.2`, `rc.1` |
| **Build Metadata** | `<timestamp>.<buildnumber>[.<branch>].<githash>` | `20251010.256.4d798ed` |

## Version Number Format

### Basic Format

Based on Semantic Versioning 2.0.0, using a more compatible format:

```text
<major>.<minor>.<patch>[-<prerelease>][-<buildmetadata>]
```

### Important Note

This specification **deliberately abandons the `+` sign from SemVer** to ensure cross-platform compatibility, uniformly using `-` to separate build metadata.

#### Rationale

- Docker tag specification doesn't allow `+` sign
- Most package managers (npm, pip, maven, etc.) have limited support for `+`
- Kubernetes resource names don't support `+` sign
- File systems sometimes handle `+` sign improperly

#### Semantic Impact

- In SemVer, `+` is for build metadata, `-` is for prerelease versions
- This spec changes build metadata to use `-`, **altering version semantics**
- Example: `1.6.0-alpha.1-20250930.001.develop.a1b2c3d` would be parsed as prerelease in SemVer, not stable+metadata

#### Trade-off

While changing SemVer semantics, this ensures version number usability and consistency across various practical application scenarios.

### Component Descriptions

1. **Major Version**: Incremented for breaking changes
2. **Minor Version**: Incremented for backward-compatible new features
3. **Patch Version**: Incremented for backward-compatible bug fixes
4. **Prerelease Identifier**: Indicates version maturity and stability, affects version priority
5. **Build Metadata**: Contains build-related information, doesn't affect version priority, only for identification and tracing

## Version Increment Rules

### Basic Increment Rules

| Version Type | Increment Condition | Reset Rule | Example |
|--------------|---------------------|------------|---------|
| **Major** | Breaking changes (API incompatibility, data structure changes) | Reset minor and patch to 0 | `1.5.3` → `2.0.0` |
| **Minor** | Backward-compatible new features | Reset patch to 0 | `1.5.3` → `1.6.0` |
| **Patch** | Backward-compatible bug fixes | No reset | `1.5.3` → `1.5.4` |

### Prerelease Version Rules

- **Within Stage**: `1.6.0-alpha.1` → `1.6.0-alpha.2`
- **Between Stages**: `1.6.0-alpha.2` → `1.6.0-beta.1`
- **Stable Release**: `1.6.0-rc.3` → `1.6.0`
- **Stage Priority**: `alpha` < `beta` < `rc` < stable

### Identifier Structure

**Prerelease Identifier (`-<prerelease>`)**:

- **stage**: Development stage identifier (alpha, beta, rc)
- **iteration**: Iteration number within same stage (optional, numeric only, e.g., 1, 2, 3)
- **Format**: `<stage>[.<iteration>]`

**Build Metadata (`-<buildmetadata>`)**:

- **Build Timestamp**: Build time identifier (required, format: YYYYMMDD, date only)
- **Build Number**: Distinguish different builds on same day (required)
  - **CI/CD Build**: Use Jenkins BUILD_NUMBER (e.g., 93, 123, 156)
  - **Local Package**: Use HHMMSS format (e.g., 175357 for 17:53:57, temporary testing only)
- **Build Branch**: Include branch info for non-main branches (hidden for main/master)
- **Git Hash**: Commit hash (required, 7-character short hash)
- **Format**: `<timestamp>.<buildnumber>[.<branch>].<githash>`

### Important Constraints

- **Environment info** (dev, test, staging, prod) doesn't belong in version number, manage via deployment config
- **Branch info** (feature, hotfix, bugfix, etc.) doesn't belong in version number, place in build metadata
- **iteration is numeric only**: Doesn't include dev, hotfix, feat, or other branch type info
- Same version can deploy to different environments, environment shouldn't affect version identification

## Version Examples

### Common Version Examples

| Version Type | Version Example | Description |
|--------------|-----------------|-------------|
| **CI/CD Build (main)** | `1.5.0-beta.1-20251010.256.4d798ed` | Jenkins build, BUILD_NUMBER=256 |
| **CI/CD Build (dev)** | `1.6.0-alpha.1-20250930.93.develop.a1b2c3d` | develop branch, BUILD_NUMBER=93 |
| **Local Package (main)** | `1.5.0-beta.1-20251010.175357.4d798ed` | package.sh, timestamp 175357 (17:53:57) |
| **Local Package (feature)** | `1.6.0-alpha.1-20251010.143052.feature.e5f6g7h` | package.sh, time 143052 (14:30:52) |
| **Release Candidate** | `1.6.0-rc.1-20250930.156.release.c3d4e5f` | release branch rc version |
| **Stable Release** | `1.6.0-20250930.200.d4e5f6g` | main branch stable version |

**Build Number Explanation**:

- **CI/CD Build** (Jenkins): Use BUILD_NUMBER
  - Format: Pure numeric, e.g., `93`, `156`, `256`
  - Advantages: Strong uniqueness, auto-increment, easy tracking
  - Generation: Auto-obtained via `${BUILD_NUMBER}` in Jenkins Pipeline

- **Local Package**: Use HHMMSS format
  - Format: 6-digit time, e.g., `175357` (17:53:57), `143052` (14:30:52)
  - Advantages: No build server needed, time sortable, easy distinction
  - Purpose: Local temporary testing only (package.sh), production uses Jenkins builds

- **Branch Handling**:
  - Main branches (main, master): Hide branch info
  - Non-main branches (develop, feature, etc.): Include branch info

## Version File Management

### Project Version Files

Projects use two files to manage version information:

#### 1. `VERSION` - Original Version Number

**Purpose:** Store project's semantic version number

**Maintainer:** Development team manually maintains

**Format:** Follow semantic versioning specification

```
{MAJOR}.{MINOR}.{PATCH}[-{PRERELEASE}]

Examples:
1.5.0
1.5.0-beta.1
2.0.0-rc.1
```

**Use Cases:**
- Version planning and release management
- Git tag creation
- Documentation version identification
- Changelog recording

#### 2. `VERSION.build` - Build Version Number

**Purpose:** Store complete build version information

**Generator:** CI/CD system (e.g., Jenkins) auto-generates during build

**Format:**

- **CI/CD Build**: `{VERSION}-{TIMESTAMP}.{BUILD_NUMBER}[.{BRANCH}].{COMMIT_HASH}`

```
Examples:
1.5.0-beta.1-20251010.256.4d798ed    (main branch, BUILD_NUMBER=256)
1.6.0-alpha.1-20250930.93.develop.a1b2c3d  (develop branch, BUILD_NUMBER=93)
```

**Use Cases:**
- Actual deployment and runtime
- Docker image tags
- Issue tracking and rollback
- Build artifact management

### Version Workflow

| Stage | Responsibility | Key Artifacts |
|-------|----------------|---------------|
| **Development** | Version planning and semantic version management | `VERSION` file |
| **Build** | CI/CD auto-generates complete version, builds images and packages | `VERSION.build` file, Docker images, packages |
| **Deployment** | Use `VERSION.build` to deploy built versions | Runtime environment |

**Core Principles:**

- **Separation of Concerns**: VERSION for planning, VERSION.build for deployment
- **Build Once, Deploy Many**: Same build artifact deploys to different environments
- **Avoid Version Mismatch**: Deployment scripts use VERSION.build not VERSION, ensuring version matches image tags

### Common Commands

```bash
# View version information
cat VERSION        # Original semantic version
cat VERSION.build  # Complete build version

# Update version number
echo "1.6.0" > VERSION
git add VERSION
git commit -m "chore: bump version to 1.6.0"
git tag -a v1.6.0 -m "Release v1.6.0"
```

## References

- [Semantic Versioning 2.0.0](https://semver.org/) - This spec based on this standard, but uses `-` instead of `+` for compatibility
- [Git Branching Best Practices](https://nvie.com/posts/a-successful-git-branching-model/)
- [Continuous Integration and Deployment Guide](https://martinfowler.com/articles/continuousIntegration.html)
- [Software Configuration Management Best Practices](https://www.ibm.com/docs/en/engineering-lifecycle-management-suite/lifecycle-management/6.0.6)
- [Version Control System Design Principles](https://git-scm.com/book/en/v2)
