---
description: Validate APS documentation structure and content
allowed-tools: Bash, Read, Glob, Grep
---

# Validate Documentation

Validate the Agile Protocol Specification documentation for consistency and completeness.

## Checks Performed

1. **Structure Validation**
   - Verify SUMMARY.md references all chapters
   - Check for orphaned markdown files not in SUMMARY.md
   - Validate directory structure follows APS conventions

2. **Content Validation**
   - Check all chapters have proper heading hierarchy
   - Verify context files exist for major modules
   - Look for broken internal links

3. **Build Validation**
   - Run mdbook build to check for errors
   - Report any warnings

## Instructions

Execute the following validation steps:

```bash
# Check for files not in SUMMARY.md
echo "=== Checking for orphaned files ==="
find specification-guide/src -name "*.md" -not -name "SUMMARY.md" | while read f; do
  basename "$f" | grep -q "$(cat specification-guide/src/SUMMARY.md)" || echo "Orphaned: $f"
done

# Build check
echo "=== Build validation ==="
cd specification-guide && mdbook build 2>&1

echo "=== Validation complete ==="
```
