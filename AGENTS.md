# AI Agents Configuration

This document defines how AI agents should interact with this project documentation template repository.

## Agent Capabilities

### Documentation Generator Agent

**Purpose**: Generate and maintain project documentation using templates

**Capabilities**:

- Read and understand template structure from `llms.txt`
- Identify appropriate templates based on project type
- Fill structured placeholders with contextual information
- Maintain cross-document references and consistency
- Update version history and metadata

**Entry Point**: `llms.txt` for complete usage instructions

### Template Customization Agent

**Purpose**: Adapt templates to specific project needs

**Capabilities**:

- Analyze project requirements and scale
- Select minimal necessary template set
- Customize template fields and sections
- Generate project-specific documentation structure

### Documentation Validator Agent

**Purpose**: Ensure documentation quality and consistency

**Capabilities**:

- Detect unreplaced placeholders
- Validate Markdown syntax
- Check cross-document references
- Verify version number consistency
- Validate date formats

## Agent Workflows

### Workflow 1: Initialize New Project Documentation

```yaml
trigger: User requests project documentation setup
steps:
  1. Query project information (name, type, scale, tech stack)
  2. Read README.md to understand structure
  3. Select documents from docs/ based on project scale
  4. Copy samples into project and adapt content
  5. Fill common information (project name, dates)
  6. Prompt for missing critical information
  7. Validate generated documents
output: Complete documentation structure adapted from samples
```

### Workflow 2: Generate Architecture Decision Record

```yaml
trigger: User needs to document a technical decision
steps:
  1. Read ADR-TEMPLATE.md from docs/process-management/decisions
  2. Determine next ADR number
  3. Gather decision context from user
  4. Fill decision options and analysis
  5. Document rationale and consequences
  6. Update decision index
  7. Create cross-references if needed
output: New ADR document with proper numbering
```

### Workflow 3: Update Version Documentation

```yaml
trigger: Version number change
steps:
  1. Read versioning-standards.md from docs/development-guide/release-management
  2. Update VERSION file
  3. Search for version references across documents
  4. Update all version-related content
  5. Update version history in project-overview
  6. Validate consistency
output: Synchronized version information across all documents
```

### Workflow 4: Maintain Documentation Consistency

```yaml
trigger: Document modification
steps:
  1. Identify affected documents
  2. Update cross-references
  3. Synchronize common information
  4. Update version history
  5. Validate links and references
output: Consistent documentation set
```

## Agent Context

### Required Context Files

1. **llms.txt** - Complete usage guide and conventions
2. **README.md** - Project structure and overview
3. **Sample documents** - Files under docs/ for reference and adaptation

### Context Priority

When processing requests, agents should prioritize:

1. User explicit requirements
2. Project-specific configuration (if exists)
3. Conventions in llms.txt and README
4. Sample documents under docs/

## Agent Constraints

### Must Follow

- Preserve template structure and formatting
- Replace all placeholders before finalizing
- Maintain Markdown syntax correctness
- Keep cross-document references valid
- Follow semantic versioning rules
- Update version history for all changes

### Should Avoid

- Removing structural elements without user confirmation
- Mixing different date formats
- Creating broken internal links
- Inconsistent terminology across documents
- Overfilling optional sections unnecessarily

## Agent Communication

### Input Formats

Agents should accept:

- Natural language requests
- Structured queries (JSON/YAML)
- File paths for context
- Project metadata

### Output Formats

Agents should provide:

- Generated/updated Markdown files
- Change summaries
- Validation reports
- Suggested next actions

## Integration Points

### Git Integration

Agents can suggest Git operations:

```bash
git add docs/
git commit -m "docs: <description>"
git tag -a v<version> -m "Release v<version>"
```

### CI/CD Integration

Agents can generate validation scripts:

- Markdown linting
- Link checking
- Placeholder detection
- Version consistency validation

## Error Recovery

### Common Issues

| Issue | Detection | Recovery |
|-------|-----------|----------|
| Unreplaced placeholders | Regex scan for `\[.*?\]` | Prompt user for values |
| Broken links | Link validation | Fix relative paths |
| Format errors | Markdown parser | Auto-format or report |
| Version conflicts | Cross-document scan | Prompt for resolution |

### Validation Checkpoints

Run validation after:

- Template filling
- Document updates
- Version changes
- Batch operations

## Agent Collaboration

### Multi-Agent Scenarios

When multiple agents work together:

1. **Generator + Validator**: Generate then validate
2. **Customizer + Generator**: Customize templates then generate
3. **Generator + Git Agent**: Generate docs then commit

### Conflict Resolution

If agents produce conflicting changes:

1. Preserve user explicit requirements
2. Follow template conventions
3. Maintain document consistency
4. Prompt user for ambiguous cases

## Performance Guidelines

### Optimization

- Cache template structures
- Batch process multiple documents
- Reuse parsed metadata
- Minimize file I/O operations

### Scalability

- Support incremental updates
- Handle large documentation sets
- Process documents in parallel when possible
- Provide progress feedback for long operations

## Security Considerations

### Safe Operations

- Validate file paths before access
- Sanitize user input in templates
- Avoid executing arbitrary code
- Respect file permissions

### Data Privacy

- Don't expose sensitive information in templates
- Follow placeholder conventions for credentials
- Respect .gitignore patterns
- Warn about potential sensitive data

## Monitoring and Feedback

### Metrics to Track

- Template usage frequency
- Placeholder fill rate
- Validation error rate
- User satisfaction with generated docs

### Continuous Improvement

- Collect feedback on template quality
- Identify commonly missed placeholders
- Optimize frequently used workflows
- Update conventions based on usage patterns

---

**Version**: 1.0  
**Last Updated**: 2024-01-15  
**Maintained By**: Project Team
