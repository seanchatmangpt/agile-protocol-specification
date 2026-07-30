# Lifecycle and State Management

Lifecycle is the authority geometry of APS. Mutable states permit construction; immutable states preserve admitted baselines. Promotion is not a label change but a morphism with preconditions, authority, evidence, and a receipt. This part specifies the state machine, its refusal edges, and the invariant that a rejected candidate cannot corrupt the prior baseline.

## Formal lens

```text
transition(a, s₁, s₂) = authority ∧ criteria ∧ evidence ∧ receipt
```

## Document States: Draft, Provisional, In Review, Accepted, Final

This section defines the canonical APS document-state algebra.

### Draft

**Requirement APS-05-01.** The implementation SHALL represent **draft** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `DRAFT_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict draft while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Provisional

**Requirement APS-05-02.** The implementation SHALL represent **provisional** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `PROVISIONAL_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict provisional while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### In Review

**Requirement APS-05-03.** The implementation SHALL represent **in review** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `IN_REVIEW_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict in review while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Accepted

**Requirement APS-05-04.** The implementation SHALL represent **accepted** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `ACCEPTED_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict accepted while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Final

**Requirement APS-05-05.** The implementation SHALL represent **final** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `FINAL_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict final while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Superseded and Refused

**Requirement APS-05-06.** The implementation SHALL represent **superseded and refused** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `SUPERSEDED_AND_REFUSED_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict superseded and refused while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Preserved constitutional material

The prior manuscript contained the following non-boilerplate material. v26.7.30 retains it as a specialized rule, example, definition, or algebra within the current coordinate.

### State algebra

APS uses the following canonical states:

| State | Meaning | May change content? | May authorize downstream work? |
|---|---|---:|---:|
| Draft | Unadmitted working material | Yes | No |
| Provisional | Coherent candidate with known gaps | Yes | Limited |
| In Review | Frozen candidate under challenge | Only through reviewed revision | No |
| Accepted | Admitted baseline for bounded use | Through supersession only | Yes |
| Final | Accepted and sealed for the declared release coordinate | No | Yes |
| Superseded | Former accepted or final artifact replaced by a successor | No | Historical only |
| Refused | Candidate rejected with typed reasons | No, but may spawn a new draft | No |

The state machine SHALL reject silent transitions, including Draft directly to Final, and SHALL preserve the prior authoritative artifact when a candidate is refused.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Workflow for Document Lifecycle in AAP

Describes the end-to-end state transition workflow for APS artifacts.

### Creation and admission

**Requirement APS-05-07.** The implementation SHALL represent **creation and admission** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CREATION_AND_ADMISSION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict creation and admission while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Independent challenge

**Requirement APS-05-08.** The implementation SHALL represent **independent challenge** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `INDEPENDENT_CHALLENGE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict independent challenge while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Revision and reconciliation

**Requirement APS-05-09.** The implementation SHALL represent **revision and reconciliation** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `REVISION_AND_RECONCILIATION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict revision and reconciliation while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Approval and sealing

**Requirement APS-05-10.** The implementation SHALL represent **approval and sealing** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `APPROVAL_AND_SEALING_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict approval and sealing while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Operational observation

**Requirement APS-05-11.** The implementation SHALL represent **operational observation** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `OPERATIONAL_OBSERVATION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict operational observation while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Supersession

**Requirement APS-05-12.** The implementation SHALL represent **supersession** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `SUPERSESSION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict supersession while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Transition Criteria Between Document States

Provides mechanically testable criteria for each lifecycle transition.

### Required metadata

**Requirement APS-05-13.** The implementation SHALL represent **required metadata** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `REQUIRED_METADATA_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict required metadata while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Required evidence

**Requirement APS-05-14.** The implementation SHALL represent **required evidence** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `REQUIRED_EVIDENCE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict required evidence while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Required reviewers

**Requirement APS-05-15.** The implementation SHALL represent **required reviewers** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `REQUIRED_REVIEWERS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict required reviewers while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Refusal conditions

**Requirement APS-05-16.** The implementation SHALL represent **refusal conditions** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `REFUSAL_CONDITIONS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict refusal conditions while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Automatic versus human-authorized transitions

**Requirement APS-05-17.** The implementation SHALL represent **automatic versus human-authorized transitions** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `AUTOMATIC_VERSUS_HUMAN_AUTHORIZED_TRANSITIONS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict automatic versus human-authorized transitions while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.
