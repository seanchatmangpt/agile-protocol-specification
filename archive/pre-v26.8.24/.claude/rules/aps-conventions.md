---
glob: "specification-guide/**/*"
---

# APS Naming and Structure Conventions

When working in the specification-guide directory:

## File Naming

1. **Lowercase**: Use all lowercase letters
2. **Hyphens or Underscores**: Separate words with `-` or `_`
3. **No Spaces**: Never use spaces in filenames
4. **Descriptive**: Names should indicate content clearly

## Directory Structure

Each section should contain:
- Main content files (`.md`)
- Optional `.context.md` for module metadata
- Related assets if needed

## Document Lifecycle

Respect document states when editing:
- **Mutable** (Draft, Provisional, In Review): Can be freely edited
- **Immutable** (Accepted, Final): Require explicit approval to modify

## SUMMARY.md Maintenance

When adding new files:
1. Create the content file first
2. Add entry to SUMMARY.md in appropriate section
3. Use proper indentation for nesting
4. Test with `mdbook build`

## Context Files

For new modules, create `.context.md` with:
- Module name and version
- Description
- Related modules
- Technologies used
- Conventions
