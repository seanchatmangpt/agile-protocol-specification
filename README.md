# Agile Protocol Specification

**Current candidate:** v26.7.30

The Agile Protocol Specification (APS) is a machine-readable operating constitution for converting intent into deterministic, bounded work orders for human and agentic delivery systems. APS defines identity, lifecycle, authority, falsifiers, evidence contracts, typed outcomes, receipts, and replay.

APS is the input model for Gall checkpoint execution. APS declares what must be attempted and what evidence would count; Gall observes checkpoint execution and assigns bounded standing.

## Read the book

The canonical source is `specification-guide/src/`. The v26.7.30 edition is split into 15 substantive mdBook chapters beginning at `specification-guide/src/v26_7_30/00_source_admission.md`.

## Validate

```bash
python3 specification-guide/scripts/verify_v26_7_30.py
```

The verifier checks chapter closure, schema validity, constitutional invariants, duplicate boilerplate, and emits `receipts/APS-v26.7.30-verifier.json`.

The release branch compiles mdBook and the PDF backend from Rust crates, then runs a single mdBook build:

```bash
cargo install mdbook --version 0.5.4 --locked
cargo install mdbook-pdf --version 0.1.13 --locked
cd specification-guide
mdbook build
```

Compiled outputs are committed at `specification-guide/book/` and `specification-guide/dist/APS-v26.7.30.pdf`. The Markdown under `specification-guide/src/` remains canonical.
