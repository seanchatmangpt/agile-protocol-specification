# Agile Protocol Specification

**Current candidate:** v26.7.31  
**Last immutable published projection:** v26.7.30

The Agile Protocol Specification (APS) is a machine-readable operating constitution for converting intent into deterministic, bounded work orders for human and agentic delivery systems. APS defines identity, lifecycle, authority, falsifiers, evidence contracts, typed outcomes, receipts, and replay.

APS is the input model for Gall checkpoint execution. APS declares what must be true before work begins. Gall observes execution and assigns bounded standing. BRCE remains the exclusive consequential DO path.

## Canonical source

The canonical source is `specification-guide/src/`. The v26.7.31 candidate retains the v26.7.30 source path, with 18 top-level mdBook chapters and one nested Enterprise Architecture as Strategy chapter.

The principal current profiles are:

- Fortune-5 MCP/A2A simulation: `specification-guide/src/v26_7_30/15_mcp_a2a_safe_simulation.md`
- AI-native operating model: `specification-guide/src/v26_7_30/16_ai_native_operating_model.md`
- ggen manufacturing standard: `specification-guide/src/v26_7_30/16_ggen_manufacturing_standard.md`
- Enterprise Architecture as Strategy: `specification-guide/src/v26_7_30/17_enterprise_architecture_as_strategy.md`

The machine-readable ggen profiles are:

- `specification-guide/standards/ggen-v26.7.62.json`
- `specification-guide/standards/ggen-enterprise-architecture-v26.7.31.json`

The admitted ggen source coordinate is release `26.7.62` at revision `68952593c40214ac1a681073d65f3902a9cdfce4`.

## Syntax

The stable root syntax entry point is `.aps-syntax.md`. The normative semantics, lifecycle calculus, conformance profiles, work-order schema, and receipt schema remain in the mdBook and `specification-guide/schemas/`.

## Validate canonical source

```bash
python3 specification-guide/scripts/verify_ggen_v26_7_31.py
python3 specification-guide/scripts/verify_ea_strategy_v26_7_31.py
python3 specification-guide/scripts/verify_v26_7_31.py
python3 specification-guide/scripts/verify_wip_closure_v26_7_31.py
```

The focused verifiers emit deterministic source-set receipts:

- `receipts/APS-v26.7.31-ggen-standard.json`
- `receipts/APS-v26.7.31-ggen-enterprise-architecture.json`

The full candidate verifier expands mdBook includes before checking chapter substance and emits `receipts/APS-v26.7.31-book-verifier.json`. The WIP verifier emits `receipts/APS-v26.7.31-wip-closure.json` as an exact-tree workflow artifact.

## Run the Fortune-5 simulation

```bash
python3 simulation/fortune5-safe/scripts/verify.py --require-cargo
```

The verifier exercises Rust formatting and tests, MCP and A2A fixtures, stdio and JSONL sessions, deterministic simulation, negative fixtures, receipt-chain invariants, and same-coordinate replay.

## Build projections

```bash
mdbook build specification-guide
```

The Markdown source remains authority. HTML, PDF, diagrams, schemas generated from other authority, and workflow artifacts are projections or evidence surfaces.

The committed v26.7.30 book and PDF remain the last immutable published projections. Pull-request workflows build the v26.7.31 HTML, PDF, simulation receipts, and exact-head publication receipt as immutable GitHub Actions artifacts. They do not repair source, commit generated files, or push the PR branch. Promotion into committed release outputs requires a separate explicit release actuation after all exact-head checks pass.

## Hard invariants

- Generated outputs are not independent authority.
- Lifecycle and evidentiary standing are separate.
- `UNKNOWN` is not permission to claim success.
- Direct architecture autonomics may observe, diagnose, plan, and emit intent; BRCE owns DO.
- Zero unreceipted actuation.
- Exact-head evidence is required for promotion.
- Stage 5 is a ggen extension, not an original RWR maturity stage.
