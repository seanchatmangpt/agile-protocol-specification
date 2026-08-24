---
description: Serve the mdBook documentation locally with live reload
allowed-tools: Bash
argument-hint: "[port]"
---

# Serve Documentation Locally

Start a local development server for the APS documentation with live reload.

## Instructions

1. Navigate to specification-guide directory
2. Run mdbook serve (default port 3000, or use $1 if provided)
3. Report the URL for accessing the documentation

```bash
cd specification-guide && mdbook serve ${1:---port 3000}
```

Access the documentation at http://localhost:3000
