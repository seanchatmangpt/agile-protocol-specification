# Governance, Compliance, and Auditability

Governance assigns who may define law, admit exceptions, authorize transitions, and revoke standing. Compliance maps external obligations into local claims and evidence without pretending APS itself grants certification. Auditability requires object-centric lineage capable of reconstructing why a state changed.

## Formal lens

```text
compliance(o) = map(obligation, controls, evidence, exceptions, coordinate)
```

## Governance Model for APS Document Management

This section defines constitutional governance for APS repositories and programs.

### Policy hierarchy

**Requirement APS-09-01.** The implementation SHALL represent **policy hierarchy** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `POLICY_HIERARCHY_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict policy hierarchy while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Delegated authority

**Requirement APS-09-02.** The implementation SHALL represent **delegated authority** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `DELEGATED_AUTHORITY_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict delegated authority while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Exception admission

**Requirement APS-09-03.** The implementation SHALL represent **exception admission** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `EXCEPTION_ADMISSION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict exception admission while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Governance as code

**Requirement APS-09-04.** The implementation SHALL represent **governance as code** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `GOVERNANCE_AS_CODE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict governance as code while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Cross-organization federation

**Requirement APS-09-05.** The implementation SHALL represent **cross-organization federation** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CROSS_ORGANIZATION_FEDERATION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict cross-organization federation while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Compliance Requirements and Audit Trails

Maps APS evidence to compliance obligations without pretending equivalence to certification.

### Control objectives

**Requirement APS-09-06.** The implementation SHALL represent **control objectives** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CONTROL_OBJECTIVES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict control objectives while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Evidence provenance

**Requirement APS-09-07.** The implementation SHALL represent **evidence provenance** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `EVIDENCE_PROVENANCE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict evidence provenance while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Retention and access

**Requirement APS-09-08.** The implementation SHALL represent **retention and access** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `RETENTION_AND_ACCESS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict retention and access while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Separation of duties

**Requirement APS-09-09.** The implementation SHALL represent **separation of duties** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `SEPARATION_OF_DUTIES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict separation of duties while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### External assurance

**Requirement APS-09-10.** The implementation SHALL represent **external assurance** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `EXTERNAL_ASSURANCE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict external assurance while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Maintaining Transparency with Audit Trails and Documentation

This section defines receipt DAGs, event evidence, and replayable audits.

### Receipts versus logs

**Requirement APS-09-11.** The implementation SHALL represent **receipts versus logs** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `RECEIPTS_VERSUS_LOGS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict receipts versus logs while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Parent-child lineage

**Requirement APS-09-12.** The implementation SHALL represent **parent-child lineage** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `PARENT_CHILD_LINEAGE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict parent-child lineage while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### OCEL-compatible events

**Requirement APS-09-13.** The implementation SHALL represent **ocel-compatible events** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `OCEL_COMPATIBLE_EVENTS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict ocel-compatible events while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Tamper evidence

**Requirement APS-09-14.** The implementation SHALL represent **tamper evidence** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `TAMPER_EVIDENCE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict tamper evidence while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Auditor experience

**Requirement APS-09-15.** The implementation SHALL represent **auditor experience** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `AUDITOR_EXPERIENCE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict auditor experience while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.
