# Jig Maturity: From Capability to Self-Improving Manufacture

APS uses a jig maturity model to prevent internal engine sophistication from being confused with manufacturing maturity.

The decisive question is operator-independent repeatability:

> Does the production system itself locate the work, constrain the operation, prevent invalid transformations, qualify the result, and improve from evidence without requiring tacit reconstruction by the inventor?

## Levels

### Level 0 — Capability without embodied method

Useful transformations exist, but the end-to-end manufacturing method remains substantially tacit. Experts can make the system work. New operators must reconstruct where to start, what is authoritative, what sequence is current, and how completion is proven.

### Level 1 — Defined workpiece

The system has one canonical definition of:

- what enters manufacture;
- what finished output means;
- which semantics and contracts are authoritative;
- which consequences are projections rather than independent sources of truth.

### Level 2 — Fixture

The system establishes canonical datums and location:

- project root;
- authority manifest;
- input locations;
- pack/capability bindings;
- target/output locations;
- environment and version coordinates.

An operator does not ask, 'Where does this go?'

### Level 3 — Jig

The system constrains the manufacturing operation itself:

- legal operations;
- tool selection;
- generator invocation;
- sequence;
- preconditions;
- postconditions;
- bounded actuation;
- refusals.

An operator does not ask, 'What do I run now?'

### Level 4 — Qualified jig

The jig includes independent metrology and poka-yoke:

- invalid operations are structurally refused;
- manufactured artifacts are independently qualified;
- evidence binds source, manufacturing law, observed consequence, and coordinate;
- replay and tamper detection exist;
- governance cost does not scale linearly with artifact count.

### Level 5 — Learning factory

Observed exceptions and successful novel mechanisms can become candidate reusable manufacturing knowledge.

```text
exception / novelty
  -> classify
  -> candidate contract or jig improvement
  -> falsify
  -> admit
  -> reusable manufacturing capability
```

The system improves the factory rather than merely patching the current artifact.

## Seven maturity dimensions

Each level must be considered across seven independent dimensions:

| Dimension | Governing question |
|---|---|
| Product knowledge | What should exist? |
| Work positioning | Where is the work and what is its datum? |
| Operation guidance | How is transformation performed? |
| Process sequence | In what order? |
| Error prevention | What must be impossible? |
| Measurement and qualification | How is correctness established independently? |
| Adaptation and learning | How does evidence improve reusable manufacture? |

Do not average the dimensions into a reassuring scalar. A high metrology score does not compensate for an undefined workpiece. A sophisticated engine can coexist with a Level-0 operator experience.

## Current ggen baseline as an APS case

The current ggen ecosystem is treated as a Level-0 baseline for jig design, irrespective of advanced internal capabilities. This is an intentional reset, not a dismissal of existing work.

The diagnostic is simple: if even an expert must reconstruct what a canonical ggen project looks like end to end, which documentation is current, where manufacturing authority resides, or which operation comes next, then the jig knowledge has not yet been embodied.

The next breakthrough is therefore not 'better templates'. It is an executable canonical fixture and operation law in which human and machine operators do not need repository archaeology to manufacture lawfully.

## L1 acceptance test for a manufacturing system

Give an operator only an objective, an empty workspace, and the manufacturing executable/capability endpoint.

Without private knowledge, historical chat, or archaeology, the system must make it possible to discover:

1. the canonical workpiece;
2. the authority surfaces;
3. the admitted inputs;
4. the available manufacturing capabilities;
5. the complete planned consequences;
6. the next legal operation;
7. the independent qualification route;
8. current standing;
9. the next lawful transition.

Any step that requires 'ask the inventor' is unembodied manufacturing knowledge.
