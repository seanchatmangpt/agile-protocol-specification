---
description: Generate .context.md file for a module following Codebase Context Specification
---

# Context File Generator

Generate a comprehensive `.context.md` file for the specified directory following the Codebase Context Specification.

## Arguments

- `$ARGUMENTS` - Target directory path (defaults to current directory if not specified)

## Task

1. **Analyze Directory Contents**
   - Scan all files in the target directory
   - Identify primary technologies used
   - Detect architectural patterns
   - Find related modules

2. **Extract Metadata**
   - Infer module name from directory
   - Determine version from package files if available
   - Identify conventions from existing code

3. **Generate Context File**

Create `.context.md` with this structure:

```yaml
---
module-name: [Inferred from directory]
version: [From package.json/mix.exs/pyproject.toml or 0.1.0]
description: |
  [Generated description based on file analysis]

related-modules:
  - name: [Sibling or parent modules]
    path: [Relative path]

technologies:
  - [Detected technologies]

conventions:
  - [Inferred from code patterns]

architecture:
  style: [Detected pattern]
  components:
    - [Key components found]
  data-flow: |
    [Inferred data flow]

development:
  setup-steps:
    - [From README or inferred]
  build-command: [Detected build command]
  test-command: [Detected test command]

business-requirements:
  key-features:
    - [Inferred features]
  target-audience: [If determinable]

quality-assurance:
  testing-frameworks:
    - [Detected test frameworks]
  coverage-threshold: [If configured]
---

# [Module Name]

[Extended description with architecture overview, key components, and usage examples]
```

4. **Validation**
   - Ensure YAML frontmatter is valid
   - Verify all paths are correct
   - Check for consistency with existing context files

## Output

Write the `.context.md` file to the target directory and report the generated content summary.
