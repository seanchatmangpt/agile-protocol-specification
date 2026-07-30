# Tools, Automation, and System Integration

Tools are replaceable implementations of protocol morphisms. APS specifies capabilities and interfaces rather than blessing a vendor stack. Automation may parse, validate, project, route, or request actuation, but it must preserve authority boundaries and typed failures.

## Formal lens

```text
tool failure → UNSUPPORTED|BLOCKED, never truth-value collapse
```

## Recommended Tools for Managing APS Files

Provides a tool architecture rather than a frozen vendor list.

### Source control

**Requirement APS-10-01.** The implementation SHALL represent **source control** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `SOURCE_CONTROL_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict source control while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Schema validation

**Requirement APS-10-02.** The implementation SHALL represent **schema validation** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `SCHEMA_VALIDATION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict schema validation while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Artifact generation

**Requirement APS-10-03.** The implementation SHALL represent **artifact generation** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `ARTIFACT_GENERATION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict artifact generation while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### AST and dependency scanning

**Requirement APS-10-04.** The implementation SHALL represent **ast and dependency scanning** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `AST_AND_DEPENDENCY_SCANNING_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict ast and dependency scanning while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Mutation testing

**Requirement APS-10-05.** The implementation SHALL represent **mutation testing** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `MUTATION_TESTING_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict mutation testing while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Receipt stores

**Requirement APS-10-06.** The implementation SHALL represent **receipt stores** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `RECEIPT_STORES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict receipt stores while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Automation of Workflow Transitions and AI Integrations

This section defines safe automation of state transitions and agent workflows.

### Trigger conditions

**Requirement APS-10-07.** The implementation SHALL represent **trigger conditions** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `TRIGGER_CONDITIONS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict trigger conditions while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Condition watches

**Requirement APS-10-08.** The implementation SHALL represent **condition watches** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CONDITION_WATCHES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict condition watches while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Automated dispatch

**Requirement APS-10-09.** The implementation SHALL represent **automated dispatch** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `AUTOMATED_DISPATCH_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict automated dispatch while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Human authorization points

**Requirement APS-10-10.** The implementation SHALL represent **human authorization points** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `HUMAN_AUTHORIZATION_POINTS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict human authorization points while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Failure isolation

**Requirement APS-10-11.** The implementation SHALL represent **failure isolation** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `FAILURE_ISOLATION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict failure isolation while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Integration with Existing Agile and AI Systems

Shows how APS interoperates with Jira, GitHub, CI, LLM agents, and enterprise platforms.

### Adapters and projections

**Requirement APS-10-12.** The implementation SHALL represent **adapters and projections** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `ADAPTERS_AND_PROJECTIONS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict adapters and projections while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Bidirectional synchronization

**Requirement APS-10-13.** The implementation SHALL represent **bidirectional synchronization** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `BIDIRECTIONAL_SYNCHRONIZATION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict bidirectional synchronization while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Avoiding dual authority

**Requirement APS-10-14.** The implementation SHALL represent **avoiding dual authority** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `AVOIDING_DUAL_AUTHORITY_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict avoiding dual authority while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Ticket generation

**Requirement APS-10-15.** The implementation SHALL represent **ticket generation** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `TICKET_GENERATION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict ticket generation while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Evidence ingestion

**Requirement APS-10-16.** The implementation SHALL represent **evidence ingestion** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `EVIDENCE_INGESTION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict evidence ingestion while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.
