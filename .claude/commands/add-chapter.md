---
description: Add a new chapter to the APS specification
allowed-tools: Read, Write, Edit, Glob
argument-hint: "[section] [chapter-name]"
---

# Add New Chapter

Create a new chapter in the Agile Protocol Specification.

## Arguments
- `$1` - Section name (e.g., conceptual_framework, best_practices)
- `$2` - Chapter filename (e.g., new-feature.md)

## Instructions

1. Verify the target section exists in `specification-guide/src/`
2. Create the new chapter file with proper APS format:
   - Title with `#`
   - Introduction paragraph
   - Structured sections with `##`
   - Conclusion section
3. Update `specification-guide/src/SUMMARY.md` to include the new chapter
4. Optionally create a `.context.md` file if this starts a new module

## Chapter Template

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

## Context File Template (if needed)

```yaml
---
module-name: [Module Name]
version: 1.0.0
description: |
  [Description of the module's purpose and content]
related-modules:
  - name: [Related Module]
    path: [./path/to/module.md]
---
```
