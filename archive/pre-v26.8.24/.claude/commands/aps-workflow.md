---
description: Execute APS document lifecycle workflow (Draft → Review → Accept → Final)
---

# APS Document Lifecycle Workflow

Execute the Agile Protocol Specification document lifecycle workflow for a document or set of documents.

## Arguments

- `$ARGUMENTS` - Document path and target state (e.g., "docs/spec.md:review" or "src/:accept")

## Task

Parse the document path and target state from arguments.

### State Transitions

Valid transitions follow this flow:
```
Draft → Provisional → In Review → Accepted → Final
         ↑_______________↓
         (Revision cycle)
```

### Workflow Steps

1. **Validate Current State**
   - Read document metadata
   - Verify transition is valid
   - Check prerequisites

2. **Execute Transition**

   **Draft → Provisional:**
   - Validate document structure
   - Check required sections exist
   - Update metadata with provisional date
   - Create initial review checklist

   **Provisional → In Review:**
   - Assign reviewers (from config or prompt)
   - Create review branch if git-enabled
   - Generate review template
   - Notify stakeholders

   **In Review → Accepted:**
   - Verify all review comments addressed
   - Check approval threshold met
   - Update document state in metadata
   - Archive review artifacts

   **Accepted → Final:**
   - Lock document (set immutable flag)
   - Generate final version number
   - Create archive copy
   - Update change log

3. **Update Metadata**

   Rename file following APS conventions:
   ```
   {DocumentType}_{Version}_{State}_{Date}_{Author}.md
   ```

4. **Generate Artifacts**
   - State transition log entry
   - Updated SUMMARY.md if needed
   - Notification message

### AAP Integration

Apply Adversarial Agile Process checks:
- Challenge incomplete sections
- Verify claims and assumptions
- Suggest improvements
- Document concerns

## Output

Report the state transition, updated filename, and any issues found during the process.
