# Versioning, Branch Worlds, and Reconciliation

A branch represents a candidate world, a commit identifies a coordinate, and a merge proposes reconciliation. None is proof of semantic preservation. APS versioning records both content evolution and authority evolution, then requires explicit handling of concurrent candidates and generated projections.

## Formal lens

```text
reconcile(G₁,G₂,B) → G₃ ∪ ConflictSet; commit ≠ semantic proof
```

## Overview of Version Control in APS

Explains how source control, artifact lineage, and standing interact.

### Repository truth versus conversation memory

**Requirement APS-07-01.** The implementation SHALL represent **repository truth versus conversation memory** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `REPOSITORY_TRUTH_VERSUS_CONVERSATION_MEMORY_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict repository truth versus conversation memory while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Branches as candidate worlds

**Requirement APS-07-02.** The implementation SHALL represent **branches as candidate worlds** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `BRANCHES_AS_CANDIDATE_WORLDS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict branches as candidate worlds while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Commits as coordinates, not proof

**Requirement APS-07-03.** The implementation SHALL represent **commits as coordinates, not proof** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `COMMITS_AS_COORDINATES_NOT_PROOF_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict commits as coordinates, not proof while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Merge gates and reconciliation

**Requirement APS-07-04.** The implementation SHALL represent **merge gates and reconciliation** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `MERGE_GATES_AND_RECONCILIATION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict merge gates and reconciliation while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Generated artifacts and source-of-truth boundaries

**Requirement APS-07-05.** The implementation SHALL represent **generated artifacts and source-of-truth boundaries** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `GENERATED_ARTIFACTS_AND_SOURCE_OF_TRUTH_BOUNDARIES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict generated artifacts and source-of-truth boundaries while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Version Numbering System for APS

This section defines calendar, semantic, schema, and evidence versioning.

### Release versions

**Requirement APS-07-06.** The implementation SHALL represent **release versions** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `RELEASE_VERSIONS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict release versions while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Schema versions

**Requirement APS-07-07.** The implementation SHALL represent **schema versions** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `SCHEMA_VERSIONS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict schema versions while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Artifact revisions

**Requirement APS-07-08.** The implementation SHALL represent **artifact revisions** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `ARTIFACT_REVISIONS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict artifact revisions while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Standing coordinates

**Requirement APS-07-09.** The implementation SHALL represent **standing coordinates** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `STANDING_COORDINATES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict standing coordinates while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Compatibility rules

**Requirement APS-07-10.** The implementation SHALL represent **compatibility rules** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `COMPATIBILITY_RULES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict compatibility rules while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Handling and Reconciliation of Multiple Versions

Explains how APS handles concurrent proposals, forks, and conflicting baselines.

### Candidate branches

**Requirement APS-07-11.** The implementation SHALL represent **candidate branches** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CANDIDATE_BRANCHES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict candidate branches while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Three-way semantic reconciliation

**Requirement APS-07-12.** The implementation SHALL represent **three-way semantic reconciliation** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `THREE_WAY_SEMANTIC_RECONCILIATION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict three-way semantic reconciliation while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Authority over merges

**Requirement APS-07-13.** The implementation SHALL represent **authority over merges** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `AUTHORITY_OVER_MERGES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict authority over merges while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Partial acceptance

**Requirement APS-07-14.** The implementation SHALL represent **partial acceptance** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `PARTIAL_ACCEPTANCE_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict partial acceptance while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Conflict receipts

**Requirement APS-07-15.** The implementation SHALL represent **conflict receipts** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CONFLICT_RECEIPTS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict conflict receipts while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Version Control and Reconciliation Processes

Specifies the exact reconciliation pipeline for artifacts and implementation claims.

### Intent model

**Requirement APS-07-16.** The implementation SHALL represent **intent model** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `INTENT_MODEL_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict intent model while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Observed model

**Requirement APS-07-17.** The implementation SHALL represent **observed model** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `OBSERVED_MODEL_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict observed model while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Evidence model

**Requirement APS-07-18.** The implementation SHALL represent **evidence model** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `EVIDENCE_MODEL_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict evidence model while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Delta taxonomy

**Requirement APS-07-19.** The implementation SHALL represent **delta taxonomy** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `DELTA_TAXONOMY_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict delta taxonomy while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Repair and reverification

**Requirement APS-07-20.** The implementation SHALL represent **repair and reverification** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `REPAIR_AND_REVERIFICATION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict repair and reverification while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Preserved constitutional material

The prior manuscript contained the following non-boilerplate material. v26.7.30 retains it as a specialized rule, example, definition, or algebra within the current coordinate.

### The reconciliation equation

APS defines three primary models:

- **I**, the intended model;
- **M**, the implemented model;
- **E**, the evidenced model.

It also permits an implementation report **R**, supplied by a human or agent.

The system computes:

```text
ΔIM = I ⊖ M
ΔME = M ⊖ E
ΔRO = R ⊖ O
```

where **O** is the independently observed repository or operational system. The operator `⊖` is a typed model difference, not a line diff. It identifies missing nodes, missing edges, forbidden nodes, forbidden edges, wrong properties, surviving legacy paths, missing evidence, and unreported collateral changes.

A reconciler SHALL never close a delta merely because a summary claims it was addressed. Closure requires the evidence declared by the governing claim.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.
