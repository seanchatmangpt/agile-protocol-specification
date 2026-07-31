# Agile Protocol Specification

**Current candidate:** v26.7.31

The Agile Protocol Specification (APS) is a machine-readable operating constitution for converting intent into deterministic, bounded work orders for human and agentic delivery systems. APS defines identity, lifecycle, authority, falsifiers, evidence contracts, typed outcomes, receipts, and replay.

APS is the input model for Gall checkpoint execution. APS declares what must be attempted and what evidence would count; Gall observes checkpoint execution and assigns bounded standing.

## Read the book

The canonical source is `specification-guide/src/`. The v26.7.31 candidate retains the v26.7.30 edition path and contains 18 top-level mdBook chapters plus one nested Enterprise Architecture as Strategy profile.

The enterprise execution chapter is `specification-guide/src/v26_7_30/15_mcp_a2a_safe_simulation.md`. It is backed by an executable Rust package at `simulation/fortune5-safe/`.

The ggen manufacturing profile is `specification-guide/src/v26_7_30/16_ggen_manufacturing_standard.md`, with a machine-readable conformance profile at `specification-guide/standards/ggen-v26.7.62.json`. It binds the standards admitted from `seanchatmangpt/ggen` release `26.7.62` at exact source revision `68952593c40214ac1a681073d65f3902a9cdfce4`.

The nested Enterprise Architecture as Strategy profile is `specification-guide/src/v26_7_30/17_enterprise_architecture_as_strategy.md`, with a machine-readable maturity and proof contract at `specification-guide/standards/ggen-enterprise-architecture-v26.7.31.json`. It preserves the four RWR operating models and four original maturity stages, then fences ggen Stage 5 as an explicit extension requiring 21 conjunctive dimensions and 63 proof obligations at one exact coordinate.

## Validate the specification

```bash
python3 specification-guide/scripts/verify_ggen_v26_7_31.py
python3 specification-guide/scripts/verify_ea_strategy_v26_7_31.py
python3 specification-guide/scripts/verify_v26_7_30.py
```

The focused ggen verifier checks source provenance, ontology authority, deterministic projection, maximal frontmatter, typed refusal precedence, zero direct actuation, Building Block composition, BLAKE3 obligations, deterministic non-LLM self-play, Gall work orders, logical-time OCEL evidence, exact-head release law, exclusions, and falsifiers. It emits `receipts/APS-v26.7.31-ggen-standard.json`.

The Enterprise Architecture as Strategy verifier checks the RWR fence, operating-model quadrants, original maturity stages, the explicit ggen Stage 5 extension, core-diagram closure, canonical graph authority, GBB/ABB/SBB distinctions, provider profiles, `gpc` aliasing, 21 maturity dimensions, exactly 63 proof obligations, Gall checkpoints, BRCE-only actuation, and same-object falsification. It emits `receipts/APS-v26.7.31-ggen-enterprise-architecture.json`.

The book verifier checks chapter closure, schema validity, constitutional invariants, duplicate boilerplate, the MCP/A2A enterprise work order, and the simulation source surface. It emits `receipts/APS-v26.7.30-verifier.json`.

## Run the Fortune-5-scale SAFe simulation

The fictional scale profile contains 5 portfolios, 20 development value streams, 40 Solution Trains, 80 ARTs, 800 teams, and 7,200 delivery personnel. MCP is the tool and context plane. A2A is the peer-agent task plane. All policy-governed state mutation passes through an exclusive actuation broker and hash-chained receipt ledger.

```bash
cargo test --manifest-path simulation/fortune5-safe/Cargo.toml --all-targets
python3 simulation/fortune5-safe/scripts/verify.py --require-cargo
```

The MCP server can also run as a persistent stdio JSON-RPC session, while the A2A harness preserves task state across JSONL requests:

```bash
cargo run --manifest-path simulation/fortune5-safe/Cargo.toml -- mcp-stdio \
  --config simulation/fortune5-safe/config/fortune5-enterprise.json \
  --scenario simulation/fortune5-safe/config/global-core-modernization.json
```

A deterministic scenario can be run directly:

```bash
cargo run --manifest-path simulation/fortune5-safe/Cargo.toml -- \
  simulate \
  --config simulation/fortune5-safe/config/fortune5-enterprise.json \
  --scenario simulation/fortune5-safe/config/global-core-modernization.json \
  --out simulation/fortune5-safe/target/aps-safe-sim/simulation-report.json
```

The simulator is company-neutral and does not represent a real Fortune 5 corporation. Its MCP 2025-11-25 and A2A 1.0.0 surfaces are bounded semantic profiles, not full network conformance or certification claims.

## Build the book and PDF

The release branch compiles mdBook and the PDF backend from Rust crates, then runs a single mdBook build:

```bash
cargo install mdbook --version 0.5.4 --locked
cargo install mdbook-pdf --version 0.1.13 --locked
cd specification-guide
mdbook build
```

Compiled outputs are committed at `specification-guide/book/` and `specification-guide/dist/APS-v26.7.30.pdf`. The Markdown under `specification-guide/src/` remains canonical. This change does not hand-edit compiled book or PDF outputs; release automation must regenerate them from canonical source.
