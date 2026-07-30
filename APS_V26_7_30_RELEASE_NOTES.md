# APS v26.7.30 Release Notes

## Classification

- Lifecycle: In Review
- Local structural standing: determined by verifier receipt
- Base: `7a713c199e23f7b24b4c2d0d80a86996dd106f5c`
- Release date: 2026-07-30

## Constitutional change

v26.7.30 replaces a heading-only mdBook scaffold with a complete normative edition. It preserves the inherited APS/AAP topic fence but rejects repeated boilerplate as a substitute for theory.

The release establishes:

- the admitted-source model `O → O*`;
- `A = μ(O*)` with receipt consequence `R ⊢ A = μ(O*)`;
- independent lifecycle and operational-standing axes;
- canonical standing vocabulary;
- a formal delta calculus for missing, extra, contradictory, and unevidenced work;
- an explicit APS→Gall ownership boundary;
- deterministic work-order and receipt JSON Schemas;
- falsifier, negative-fixture, mutation, evidence-coordinate, and replay requirements;
- a local verifier that refuses heading-only chapters and unsupported overclaims;
- a Rust/Cargo build workflow for mdBook and mdbook-pdf;
- a compiled HTML edition and repository PDF with a reproducible build receipt.

## Compatibility

Existing APS topics remain represented as named subsections. Tracker, BPMN, Gantt, C4, RDF, and other views remain projections. Consumers of the former empty chapter paths must update to the v26.7.30 SUMMARY.

## Nonclaims

This release does not claim regulatory certification or execution of downstream Gall checkpoints. Rust compilation, HTML rendering, PDF generation, and PDF witness checks receive standing only through `receipts/APS-v26.7.30-rust-build.json`.
