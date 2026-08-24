# CLAUDE.md — APS v26.8.24 Contributor Constitution

## Repository purpose

APS defines a protocol for knowledge-work remanufacture under explicit authority, evidence, and standing.

The active doctrine is in `specification-guide/src/v26_8_24/`. Older material is predecessor evidence, not default design authority.

## Core laws

1. Everything is sunk cost at the next decision boundary.
2. Preserve truth, not implementations.
3. Zero continuation privilege.
4. Zero uninformed elimination.
5. Contract before implementation.
6. Prefer known reusable manufacturing patterns and compositions before novel mechanism.
7. Separate SELECT, CONSTRUCT, and DO.
8. No ambient DO authority.
9. Zero unreceipted actuation for claims of APS standing.
10. No prose outranks observed evidence.
11. Treat plausible adversarial objections as candidate falsifiers.
12. The manufacturing system itself must remain reconstitutable.

## Working method

Before editing an incumbent surface, ask whether it should exist in the successor at all. Historical effort is not a preservation argument.

For changes that affect architecture:

```text
observe predecessor
-> recover required truth
-> state contract
-> preserve lawful candidate space
-> construct
-> independently verify
-> assign standing
```

Do not silently equate compilation, generation, CI success, or a receipt with crown-level fitness.

## Documentation authority

- `README.md` is the public entry point.
- `specification-guide/src/SUMMARY.md` defines active mdBook navigation.
- `specification-guide/src/v26_8_24/` is the current candidate human-readable source.
- `archive/pre-v26.8.24/` preserves the predecessor repository tree.
- Generated HTML/PDF is projection, not independent authority.

## Standing vocabulary

Use `ALIVE`, `PARTIAL_ALIVE`, `BLOCKED`, `BUILD_BROKEN`, `UNKNOWN`, `UNSUPPORTED`, and typed `REFUSED` precisely.

If evidence is absent or stale, use `UNKNOWN` rather than narrative confidence.

## Public semantics

Prefer public ontologies and standards where they lawfully express the domain. Enterprise-specific facts and operational closure may extend/profile public semantics, but private reinvention requires justification.

Do not claim that any ontology, framework, generator, language, database, or APS itself is permanent authority. All are subject to Chatman's Law.

## Adversarial review

A reviewer should actively search for states in which a claimed standing would be false, especially:

- catastrophic consequence;
- ambiguous authority;
- unreconstructable decisions;
- process conformance without process fitness;
- artifact volume that defeats governance;
- evidence dependent on an ephemeral model/session;
- semantic drift;
- replay mismatch;
- hidden human decisions in allegedly manufactured output.

Convert plausible attacks into explicit falsifiers rather than arguments.

## Build

```bash
mdbook build specification-guide
```

A successful book build proves only that the current Markdown projection is structurally buildable.

## Change discipline

Prefer coherent first-principles replacement over additive prose accumulation. If a prior document is superseded, archive or version it rather than leaving multiple apparently-current authorities.
