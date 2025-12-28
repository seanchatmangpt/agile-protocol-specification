---
description: Review a chapter for APS compliance and quality
allowed-tools: Read, Grep, Glob
argument-hint: "[chapter-path]"
---

# Review Chapter

Perform a comprehensive review of an APS chapter for compliance with standards.

## Arguments
- `$1` - Path to the chapter file (e.g., specification-guide/src/introduction/introduction.md)

## Review Criteria

### 1. Structure Compliance
- Has proper title with single `#`
- Uses appropriate heading hierarchy (`##`, `###`)
- Includes introduction and conclusion sections
- Proper use of separators (`---`)

### 2. Content Quality
- Clear, concise writing
- Technical accuracy
- Consistent terminology (refer to glossary)
- Appropriate for target audience

### 3. APS Principles Alignment
- Supports human-AI collaboration
- Follows metadata-rich documentation approach
- Adheres to mutable/immutable state concepts
- Integrates AAP (Adversarial Agile Processes) where applicable

### 4. Cross-References
- Internal links are valid
- References to external resources are appropriate
- Related modules are properly linked

## Instructions

1. Read the chapter at `$1`
2. Evaluate against each review criterion
3. Provide specific feedback with line references
4. Suggest improvements following AAP principles
5. Rate overall compliance (Draft, Provisional, Ready for Review)
