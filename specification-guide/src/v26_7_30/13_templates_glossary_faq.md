# Templates, Glossary, and Frequently Asked Questions

Templates are executable interfaces, not prose decorations. The glossary fixes distinctions that must survive tool projection. The FAQ fences APS against predictable category errors, especially the belief that a passing test, an accepted document, or an AI-generated artifact is automatically ALIVE.

## Formal lens

```text
template validity = schema ∧ closure ∧ falsifier ∧ authority
```

## Glossary of Terms in APS

This section defines the normative vocabulary used throughout APS.

### Admission

**Requirement APS-13-01.** The implementation SHALL represent **admission** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `ADMISSION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict admission while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Claim

**Requirement APS-13-02.** The implementation SHALL represent **claim** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CLAIM_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict claim while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Falsifier

**Requirement APS-13-03.** The implementation SHALL represent **falsifier** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `FALSIFIER_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict falsifier while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Standing

**Requirement APS-13-04.** The implementation SHALL represent **standing** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `STANDING_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict standing while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Receipt

**Requirement APS-13-05.** The implementation SHALL represent **receipt** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `RECEIPT_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict receipt while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Broker

**Requirement APS-13-06.** The implementation SHALL represent **broker** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `BROKER_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict broker while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### ConstitutionIR

**Requirement APS-13-07.** The implementation SHALL represent **constitutionir** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CONSTITUTIONIR_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict constitutionir while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Implementation delta

**Requirement APS-13-08.** The implementation SHALL represent **implementation delta** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `IMPLEMENTATION_DELTA_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict implementation delta while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Preserved constitutional material

The prior manuscript contained the following non-boilerplate material. v26.7.30 retains it as a specialized rule, example, definition, or algebra within the current coordinate.

### Core terms

**Admission** — The act of accepting an observation, rule, artifact, or proposal into a bounded authoritative model.

**Artifact contract** — A versioned agreement between a producer and consumer that identifies schema, digests, ordering, required checks, and refusal behavior.

**Broker** — The only component authorized to perform a declared class of consequential action after validating an action envelope.

**Claim** — A bounded proposition about a system at a named coordinate.

**Constitution** — The machine-readable collection of laws, roles, falsifiers, evidence requirements, authority transitions, and gates governing a system.

**ConstitutionIR** — A canonical intermediate representation of the constitution suitable for compilation into checks, tests, mutants, gates, and receipts.

**Evidence coordinate** — The source, toolchain, configuration, environment, feature set, and artifact identity under which evidence applies.

**Falsifier** — A same-object observation that would demonstrate that a claim is false, incomplete, or unsupported.

**Implementation delta** — A typed difference between the intended model and observed implementation.

**Receipt** — A tamper-evident record binding an operation, inputs, outputs, tool coordinate, and result.

**Standing** — The bounded status assigned to a claim after evaluating its required evidence.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Templates and Examples for APS Artifacts

Provides reusable templates for claims, implementation manifests, reviews, and receipts.

### Claim template

**Requirement APS-13-09.** The implementation SHALL represent **claim template** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CLAIM_TEMPLATE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict claim template while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Implementation claim template

**Requirement APS-13-10.** The implementation SHALL represent **implementation claim template** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `IMPLEMENTATION_CLAIM_TEMPLATE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict implementation claim template while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Adversarial review template

**Requirement APS-13-11.** The implementation SHALL represent **adversarial review template** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `ADVERSARIAL_REVIEW_TEMPLATE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict adversarial review template while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Receipt template

**Requirement APS-13-12.** The implementation SHALL represent **receipt template** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `RECEIPT_TEMPLATE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict receipt template while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Release gate template

**Requirement APS-13-13.** The implementation SHALL represent **release gate template** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `RELEASE_GATE_TEMPLATE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict release gate template while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Preserved constitutional material

The prior manuscript contained the following non-boilerplate material. v26.7.30 retains it as a specialized rule, example, definition, or algebra within the current coordinate.

### Claim template

```toml
[[claims]]
id = "payments.refund.requires-approval"
owner = "payments-implementation"
verifier = "payments-independent-verifier"
gates = ["release.G4"]

[claims.scope]
package = "payments-core"
symbol = "RefundService::execute"

[claims.law]
kind = "authority-transition"
required_predecessor = "ApprovedRefund"
forbidden_input = "RefundRequest"

[claims.evidence]
required = ["ast", "compile-test", "runtime-test", "mutation", "receipt"]
```

### Implementation claim template

```toml
schema = "aps-implementation-claim.v1"
mission = "refund-approval-2029-184"
implemented_claims = ["payments.refund.requires-approval"]
changed_files = ["crates/payments-core/src/refund.rs"]
changed_symbols = ["RefundService::execute"]
tests_added = ["refund_without_approval_is_refused"]
nonclaims = ["universal fraud prevention"]
```

### Repair packet template

```yaml
claim: payments.refund.requires-approval
standing: BLOCKED
observed_delta: FORBIDDEN_EDGE
location: crates/payments-core/src/refund.rs:142
expected: RefundService::execute accepts ApprovedRefund only
observed: RefundService::execute accepts RefundRequest
owner: payments-implementation
verifier: payments-independent-verifier
required_repair: remove the raw request path and preserve the refusal tests
```

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Frequently Asked Questions about APS

Answers common adoption, governance, AI, and tooling questions.

### Is APS another agile framework

**Requirement APS-13-14.** The implementation SHALL represent **is aps another agile framework** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `IS_APS_ANOTHER_AGILE_FRAMEWORK_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict is aps another agile framework while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Does APS require AI

**Requirement APS-13-15.** The implementation SHALL represent **does aps require ai** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `DOES_APS_REQUIRE_AI_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict does aps require ai while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Does a passing test mean ALIVE

**Requirement APS-13-16.** The implementation SHALL represent **does a passing test mean alive** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `DOES_A_PASSING_TEST_MEAN_ALIVE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict does a passing test mean alive while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### How much formal proof is required

**Requirement APS-13-17.** The implementation SHALL represent **how much formal proof is required** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `HOW_MUCH_FORMAL_PROOF_IS_REQUIRED_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict how much formal proof is required while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Can humans override the system

**Requirement APS-13-18.** The implementation SHALL represent **can humans override the system** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CAN_HUMANS_OVERRIDE_THE_SYSTEM_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict can humans override the system while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.
