# CLAUDE.md - AI Assistant Guidelines for Agile Protocol Specification

## Project Overview

The **Agile Protocol Specification (APS)** is a comprehensive framework and documentation standard designed for agile software development in the age of AI. It provides a standardized, machine-readable approach to agile practices that enables seamless collaboration between human teams and AI agents.

**Author:** Sean Chatman
**License:** MIT
**Primary Technology:** mdBook (Rust-based documentation generator)

### Core Concepts

1. **Agile Protocol Specification (APS):** A standardized framework for managing agile methodologies, documents, and processes that maximizes both human expertise and AI assistance.

2. **Adversarial Agile Processes (AAP):** An extension of traditional agile practices where AI systems act as active participants, constantly challenging human decisions, solutions, and assumptions to promote higher standards of quality, security, and efficiency.

## Repository Structure

```
agile-protocol-specification/
├── CLAUDE.md                           # AI assistant guidelines (this file)
├── README.md                           # Project overview
├── LICENSE                             # MIT License
├── .gitignore                          # Git ignore patterns
├── .aps-syntax.md                      # APS syntax documentation
├── .service-colony.md                  # Service colony configuration
├── CUSTOM-GPT-CONTEXT.md               # CustomGPT context documentation
├── CUSTOMGPT-METAPROMPT-CONTEXT.md     # Meta-prompt creation guidelines
├── PLAN PRO CONVO.md                   # Planning documentation
├── .claude/                            # Claude Code configuration
│   ├── settings.json                   # Permissions, hooks, environment
│   ├── commands/                       # Custom slash commands
│   │   ├── build.md                    # /build - Build mdBook docs
│   │   ├── serve.md                    # /serve - Local dev server
│   │   ├── add-chapter.md              # /add-chapter - Add new content
│   │   ├── validate.md                 # /validate - Check structure
│   │   └── review-chapter.md           # /review-chapter - Review content
│   ├── agents/                         # Custom subagents
│   │   ├── documentation-writer.md     # Specialized doc writer
│   │   ├── aps-reviewer.md             # AAP-based reviewer
│   │   └── structure-analyzer.md       # Repository analyzer
│   ├── skills/                         # Auto-activated capabilities
│   │   ├── aps-documentation/          # APS doc creation skill
│   │   └── adversarial-review/         # AAP review skill
│   └── rules/                          # Path-specific guidelines
│       ├── markdown-standards.md       # Markdown formatting rules
│       └── aps-conventions.md          # APS naming conventions
└── specification-guide/                 # Main mdBook documentation
    ├── book.toml                       # mdBook configuration
    ├── .context.md                     # Repository context metadata
    ├── book/                           # Built HTML output
    └── src/                            # Source markdown files
        ├── SUMMARY.md                  # Book table of contents
        ├── introduction/               # Introduction chapters
        ├── conceptual_framework/       # Key principles and frameworks
        ├── document_lifecycle_management/  # Document states workflow
        ├── naming_conventions/         # File naming standards
        ├── file_directory_structure/   # Directory layout
        ├── versioning_strategy/        # Version numbering
        ├── review_and_approval_processes/  # Review workflows
        ├── governance_compliance/      # Governance and compliance
        ├── tools_and_automation/       # Recommended tools
        ├── best_practices/             # Tips and case studies
        ├── appendices/                 # Glossary, templates, FAQs
        ├── change_log/                 # Change history
        └── references/                 # External resources
```

## Key Principles

### 1. Document States (Mutable vs Immutable)

**Mutable States** (open to changes):
- **Draft:** Initial creation, open for editing
- **Provisional:** Temporary acceptance, pending review
- **In Review:** Under formal review process

**Immutable States** (finalized, locked):
- **Accepted:** Approved by stakeholders
- **Final:** Officially complete and archived

### 2. Metadata-Rich Documentation

All files should use metadata-rich names following this pattern:
```
{DocumentType}_{Version}_{State}_{Date}_{Author}.ext
```

Example: `product-requirements_v1.0.0_draft_2024-03-22_JS.md`

### 3. Context Files

Each module should have a `.context.md` file providing:
- Module name and version
- Description and purpose
- Related modules
- Technologies used
- Conventions to follow
- Architecture overview
- Development guidelines
- Business requirements
- Quality assurance details
- Deployment information

## Development Workflow

### Building the Documentation

```bash
# Navigate to the specification guide
cd specification-guide

# Build the book (generates HTML in book/ directory)
mdbook build

# Serve locally for development
mdbook serve
```

### File Formats

- **Markdown (.md):** Primary content format
- **YAML (.yaml/.yml):** Metadata and configuration
- **JSON (.json):** Structured data
- **TOML (.toml):** mdBook configuration

### Naming Conventions

1. Use lowercase letters for filenames
2. Use hyphens (-) or underscores (_) to separate words
3. Avoid spaces and special characters
4. Always include file extension
5. Include version information when applicable
6. Use descriptive, specific names (avoid generic names like "document1")

**Good examples:**
- `product-requirements_v1.0.0_JS.md`
- `customer-journey-map_draft_UX_2024-03-22.mermaid`
- `sprint-backlog_engineering_accepted_2024-04-05.xlsx`

## AI Assistant Guidelines

### When Working on This Repository

1. **Respect Document States:** Check the state of any document before modifying. Only modify mutable-state documents unless explicitly instructed otherwise.

2. **Maintain Context Files:** When adding new modules or sections, create corresponding `.context.md` files with appropriate metadata.

3. **Follow Naming Conventions:** Use metadata-rich filenames that include relevant information about the document's purpose, version, and state.

4. **Preserve Structure:** Maintain the established directory structure. New content should be placed in the appropriate section directory.

5. **Update SUMMARY.md:** When adding new chapters or sections, update `specification-guide/src/SUMMARY.md` to include them in the book navigation.

6. **Use Markdown Best Practices:**
   - Use appropriate heading levels (# for title, ## for sections, etc.)
   - Include clear section separators (---)
   - Write concise, clear content
   - Use code blocks with language identifiers

### Adversarial Agile Process (AAP) Integration

As an AI assistant, embody AAP principles:

1. **Challenge Assumptions:** Question unclear requirements or potentially problematic decisions.

2. **Suggest Alternatives:** When appropriate, propose alternative approaches or optimizations.

3. **Provide Justifications:** Document reasoning for suggestions and changes.

4. **Support Iteration:** Facilitate iterative improvement through feedback loops.

5. **Maintain Transparency:** Ensure all AI-generated content is clearly documented and explainable.

### Quality Standards

- **Accuracy:** Ensure factual correctness in all content
- **Consistency:** Maintain consistent style and terminology
- **Clarity:** Write for both human and machine readability
- **Completeness:** Provide thorough documentation with context

## Tools and Technologies

| Tool | Purpose |
|------|---------|
| mdBook | Documentation building |
| MarkdownLint | Markdown formatting validation |
| Prettier | Code and content formatting |
| Git | Version control |
| GitHub Actions | CI/CD pipeline |

## Content Templates

### New Chapter Template
```markdown
# Chapter Title

[Introduction paragraph explaining the chapter's purpose]

## Section 1

[Content]

## Section 2

[Content]

## Conclusion

[Summary and key takeaways]

---
```

### Context File Template
```yaml
---
module-name: [Module Name]
version: [X.Y.Z]
description: |
  [Description of the module's purpose and content]
related-modules:
  - name: [Related Module]
    path: [./path/to/module.md]
technologies:
  - [Technology 1]
  - [Technology 2]
conventions:
  - [Convention 1]
  - [Convention 2]
---
```

## Quick Reference Commands

```bash
# Build documentation
cd specification-guide && mdbook build

# Serve with live reload
cd specification-guide && mdbook serve

# Check git status
git status

# Standard commit flow
git add .
git commit -m "Description of changes"
git push origin branch-name
```

## Claude Code Configuration

This repository includes comprehensive Claude Code configuration in the `.claude/` directory.

### Available Slash Commands

| Command | Description |
|---------|-------------|
| `/build` | Build the mdBook documentation |
| `/serve` | Start local development server |
| `/add-chapter [section] [name]` | Create a new chapter |
| `/validate` | Check documentation structure |
| `/review-chapter [path]` | Review a chapter for APS compliance |

### Custom Agents

| Agent | Purpose |
|-------|---------|
| `documentation-writer` | Specialized for creating APS-compliant content |
| `aps-reviewer` | Implements AAP principles for rigorous review |
| `structure-analyzer` | Audits repository structure and SUMMARY.md alignment |

### Skills (Auto-Activated)

| Skill | Activates When |
|-------|----------------|
| `aps-documentation` | Creating or editing APS documentation |
| `adversarial-review` | Reviewing documents, PRs, or decisions |

### Rules (Path-Specific)

| Rule | Applies To |
|------|------------|
| `markdown-standards` | All `*.md` files |
| `aps-conventions` | All files in `specification-guide/` |

### Hooks

- **SessionStart**: Displays git status at session start
- **PostToolUse**: Logs markdown file updates
- **Stop**: Shows git status at session end

## Additional Resources

- **TOGAF Specification:** See `specification-guide/src/conceptual_framework/TOGAF-SPECIFICATION.md` for enterprise architecture context
- **Article Format:** See `specification-guide/src/conceptual_framework/ARTICLE-SPECIFICATION.md` for `.article.md` format
- **Meta-Prompt Guidelines:** See `CUSTOMGPT-METAPROMPT-CONTEXT.md` for CustomGPT prompt creation

## Contributing

1. Follow the established naming conventions and file structure
2. Create appropriate context files for new modules
3. Update SUMMARY.md when adding new content
4. Ensure all documentation passes linting checks
5. Submit changes through pull requests with clear descriptions
