# APS Constitution

The constitution fixes the distinctions that every APS projection, schema, ticket, review, and implementation must preserve. Later chapters may specialize these laws but may not silently weaken them.

## Root problem

Classical agile practice assumes that implementation capacity is scarce and coordination capacity is the principal bottleneck. Generative systems invert part of that premise. Candidate code, plans, documentation, and reviews can be produced faster than an organization can determine whether they correspond to the intended object. The new bottleneck is not generation. It is lawful admission.

APS addresses this by replacing narrative completion with protocol standing. Every material claim is represented as an object whose meaning is bounded by declared scope and whose promotion is controlled by evidence.

## Constitutional objects

An APS system SHALL distinguish at least these object classes:

- **Intent** `I`: a desired consequence stated by an authorized source.
- **Observation** `O`: partial or stale information available to a producer.
- **Admitted observation** `O*`: the subset of observation admitted under explicit law and boundary.
- **Work order** `W`: a deterministic contract describing a bounded transformation.
- **Candidate artifact** `C`: the proposed result of executing the work order.
- **Evidence bundle** `E`: coordinate-bound observations produced by verifiers.
- **Standing decision** `S`: a bounded classification of the candidate.
- **Receipt** `R`: a tamper-evident record binding operation, coordinate, evidence, decision, and lineage.
- **Repair packet** `P`: a typed delta that can produce a lawful successor work order.

These classes MUST NOT collapse into a single ticket description. In particular, `C ≠ E`, `E ≠ S`, and `S ≠ R`.

## Constitutional morphisms

```text
parse     : Intent × Context → CandidateWorkOrder ∪ ParseRefusal
route     : CandidateWorkOrder → AuthorityDomain ∪ RouteRefusal
admit     : CandidateWorkOrder × Law → WorkOrder ∪ AdmissionRefusal
diagnose  : CandidateArtifact × WorkOrder → DeltaSet
verify    : CandidateArtifact × EvidenceContract → EvidenceBundle ∪ Unsupported
stand     : DeltaSet × EvidenceBundle × Policy → StandingDecision
receipt   : StandingDecision × Coordinate × Lineage → Receipt
repair    : Refusal × DeltaSet → SuccessorWorkOrder
```

A conforming implementation MUST make refusals first-class outputs. Exceptions and prose warnings are insufficient where the caller must distinguish malformed input, missing authority, unsupported verification, failed verification, and an implementation defect.

## Six constitutional laws

### Law 1 — Intent is not implementation

A requirement, plan, prompt, or ticket describes a target. It does not establish that a target exists. A work order may receive `Accepted` standing as a declaration while its implementation remains `UNKNOWN`.

### Law 2 — Implementation is not evidence

Existence of code or documentation proves only existence at a coordinate. Evidence must identify the observer, command or method, environment, inputs, outputs, and scope of the claim.

### Law 3 — Evidence is bounded

A passing unit test supports the tested behavior under its coordinate. It does not prove system-wide correctness, security, performance, or production suitability. Standing SHALL be no stronger than the weakest missing evidence class required by policy.

### Law 4 — SELECT is not DO

Planning authority selects a lawful target and constructs a work order. An implementation agent performs the bounded delta. Selection does not actuate, and an implementer does not silently enlarge the selected scope.

### Law 5 — Refusal preserves authority

A refused candidate MUST NOT mutate the accepted baseline. Refusal produces evidence and a repair path; it does not erase history or convert a failed candidate into a partial success.

### Law 6 — Zero unreceipted actuation

Any operation that changes an authoritative or external state SHALL produce a receipt or an explicitly typed `UNSUPPORTED_RECEIPT` result. Logs alone are not receipts because they need not bind the declared object, authority, exact input, output digest, and decision.

## Standing algebra

Operational standing uses the canonical vocabulary:

| Standing | Meaning |
|---|---|
| `ALIVE` | The declared capability was observed executing at the stated coordinate and satisfied its bounded acceptance contract. |
| `PARTIAL_ALIVE` | A proper subset executed, or the evidence ladder closed only below the requested crown. |
| `BLOCKED` | A known external or prerequisite condition prevents lawful completion. |
| `BUILD_BROKEN` | The admitted tree does not compile, build, or assemble under the declared command. |
| `UNKNOWN` | Required observation has not been made or cannot be interpreted. |
| `UNSUPPORTED` | The available substrate cannot perform the requested operation or verification. |

These states form neither a simple success/failure boolean nor a total order. `UNKNOWN` is not less successful than `BLOCKED`; it means a different epistemic condition. `UNSUPPORTED` is not refusal of the work; it is a capability boundary. `PARTIAL_ALIVE` is not permission to claim the crown.

## Lifecycle state versus operational standing

Artifact lifecycle and operational standing are orthogonal:

```text
Lifecycle ∈ {Draft, Provisional, InReview, Accepted, Final, Superseded, Refused}
Standing  ∈ {PARTIAL_ALIVE, ALIVE, BLOCKED, BUILD_BROKEN, UNKNOWN, UNSUPPORTED}
```

An accepted specification can have `UNKNOWN` implementation standing. A draft prototype can be `ALIVE` at a narrow experimental coordinate. Conflating these axes creates documentation theater: the document’s approval status becomes a substitute for observed execution.

## Independence and authority

The producer of a material artifact SHALL NOT be the sole authority assigning its final standing. Independence is a graph property, not a job title. Two agents running the same prompt, model, toolchain, and hidden assumptions are not necessarily independent. An implementation SHOULD declare verifier diversity across at least one of: method, toolchain, model family, execution substrate, data source, or organizational authority.

## Nonclaims

Conformance to APS does not prove moral legitimacy, regulatory approval, universal correctness, or freedom from defects. APS proves only that declared protocol objects were admitted, transformed, verified, classified, and receipted under a bounded coordinate.
