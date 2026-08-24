# APS Constitution: Authority, Standing, and Consequence

APS is a protocol for converting admitted knowledge into bounded, independently qualified consequences without granting ambient authority to planners, models, transports, generated artifacts, or incumbent implementations.

## Core equation

```text
A = mu(O*)
```

where:

- `O*` is admitted, bounded knowledge;
- `mu` is a lawful manufacturing function;
- `A` is an artifact or consequence with only the standing justified by evidence.

The equation does not imply that every `mu` is deterministic, that every artifact is executable, or that generation itself proves fitness.

## SELECT / CONSTRUCT / DO

APS separates three classes of consequence:

### SELECT

Choose or rank candidates. Selection does not itself create external consequence.

### CONSTRUCT

Manufacture plans, code, manifests, schemas, work orders, scripts, configurations, tests, documentation, or other artifacts. Construction does not automatically possess authority to execute what it constructs.

### DO

Cause consequential change in an external or operational world.

No model output, generated artifact, network request, workflow definition, MCP call, or CLI manifest receives ambient DO authority merely because it exists.

## Authority law

Consequential execution requires an explicit authority path. The minimum structure is:

```text
proposal
  -> admission/refusal
  -> authorized executor
  -> observed consequence
  -> evidence
```

The identity of the planner — human, LLM, deterministic search, planner ensemble, or other mechanism — does not replace authority law.

## Zero unreceipted actuation

Any consequential action that claims APS standing must produce evidence sufficient to bind, at minimum where applicable:

- admitted input identity;
- contract/policy coordinate;
- executor identity;
- requested action;
- observed result;
- time/order information;
- integrity/provenance data;
- verifier coordinate.

A receipt is evidence, not automatically proof of correctness. Receipt integrity and semantic/process fitness are distinct claims.

## Standing vocabulary

APS uses explicit standing rather than optimistic narrative:

- `ALIVE`
- `PARTIAL_ALIVE`
- `BLOCKED`
- `BUILD_BROKEN`
- `UNKNOWN`
- `UNSUPPORTED`
- `REFUSED` for typed denial of an inadmissible requested transition or construction.

A system may define additional domain-specific states but must not collapse unknown or failed evidence into success.

## Independent verification

Whenever feasible, verifier logic should be independently implemented or independently observable from the implementation under test.

The crown claim is not:

```text
it compiled
```

nor:

```text
the generator says it succeeded
```

but a bounded evidence statement about observed consequence at an exact coordinate.

## Replay

Replay must distinguish:

- replaying the same requested operation;
- reproducing the same artifact bytes;
- reproducing equivalent observable behavior;
- reproducing the same external consequence.

These are different contracts and must not be conflated.

## Sunset admission

An incumbent may be sunset only when the admitted transition law permits it. Typical requirements include:

- required contract recovery complete or residual gaps explicitly admitted;
- successor standing sufficient for the intended boundary;
- evidence/replay requirements satisfied;
- migration or coexistence obligations satisfied;
- prospective risk of sunset within admitted tolerance.

Historical investment is not a sunset criterion.

## Constitutional principles

1. Everything is sunk cost at the next decision boundary.
2. Preserve truth, not implementations.
3. Zero continuation privilege.
4. Zero uninformed elimination.
5. Contract before implementation.
6. Known pattern before novel mechanism.
7. No ambient DO authority.
8. Zero unreceipted actuation.
9. No prose outranks evidence.
10. Adversarial objections are candidate falsifiers.
11. Governance must scale with law, not artifact count.
12. The factory itself must remain reconstitutable.
