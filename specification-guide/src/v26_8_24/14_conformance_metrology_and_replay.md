# Conformance, Metrology, and Replay

A manufacturing system is not mature because it can produce artifacts. It is mature when it can distinguish product, process, authority, evidence, and standing and can independently measure the claims it makes about each.

## Software metrology

Industrial jigs became trustworthy through gauges, calibration, datum control, and independent inspection. APS applies the same idea to knowledge-work manufacture.

Measure at least:

- source identity;
- contract identity;
- manufacturing-law identity;
- toolchain/environment coordinate;
- input digest;
- output digest;
- observed external state;
- authority decision;
- process-event identity;
- verifier identity;
- standing.

A receipt binds observations. It does not automatically prove semantic fitness.

## Chicago-style state evidence

When a claim concerns state, verify state rather than mocking the path that supposedly created it.

Examples:

- if the claim is relational persistence, inspect the actual database state;
- if the claim is HTTP behavior, exercise the real endpoint boundary;
- if the claim is CLI interoperability, execute the compiled or declared command surface;
- if the claim is semantic mapping, query the produced/virtual semantic view;
- if the claim is deployment consequence, observe the target environment;
- if the claim is refusal, attempt the forbidden transition and observe denial without side effect.

Inspection of source is not execution evidence.

## Evidence ladder

A useful ordered program is:

```text
parse/static
  -> build/typecheck
  -> unit/property
  -> state-based integration
  -> negative/sabotage fixtures
  -> replay
  -> exact-head CI
  -> live bounded consequence where required
```

Higher rungs do not automatically erase failures below them; they answer different claims.

## Independent verification

The constructor should not be the sole judge of construction.

Independence can come from:

- separately implemented verifier logic;
- external state observation;
- standards validators;
- differential implementations;
- sabotage/mutation tests proving the verifier detects meaningful corruption;
- cryptographic binding of source/input/output coordinates.

## Replay contracts

Distinguish four replay claims:

1. same requested operation;
2. byte-identical artifact reproduction;
3. equivalent observable behavior;
4. equivalent external consequence.

They require different evidence and environmental controls.

## Fixed point for self-manufacture

A self-manufacturing system may claim a bounded fixed point only after demonstrating something like:

```text
factory_0 -> manufacture factory_1
factory_1 -> manufacture factory_2
qualify(factory_1, factory_2) -> admitted equivalence for declared boundary
```

Byte identity is strong evidence only where determinism is part of the contract. Behavioral equivalence and authority/evidence equivalence may still require separate courts.

## Poka-yoke and refusal

The best verifier catches a defect. A better jig prevents the invalid operation from becoming consequential at all.

Typed `REFUSED` should therefore be a first-class successful safety outcome when an inadmissible transition is requested.

## Exact-head law

Evidence for promotion must bind to the exact candidate being promoted. A green run on an ancestor, neighboring branch, or regenerated local tree is not evidence for the current head.

This requirement converts CI from a vague health signal into a manufacturing coordinate.
