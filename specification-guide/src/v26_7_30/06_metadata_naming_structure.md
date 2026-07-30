# Metadata, Naming, and Repository Structure

Metadata gives protocol objects stable identity outside conversation memory. Names and directories are projections for human and tool navigation, while embedded identifiers and content digests provide canonical identity. This part makes the repository tree legible without pretending path names alone carry semantic authority.

## Formal lens

```text
identity(a) = ⟨stableId, schema, version, digest⟩; path(a) is a projection
```

## Metadata-Rich File Naming Format for APS

This section defines deterministic file naming that carries enough context for humans and automation.

### Canonical filename grammar

**Requirement APS-06-01.** The implementation SHALL represent **canonical filename grammar** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CANONICAL_FILENAME_GRAMMAR_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict canonical filename grammar while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Release and state tokens

**Requirement APS-06-02.** The implementation SHALL represent **release and state tokens** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `RELEASE_AND_STATE_TOKENS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict release and state tokens while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Owner and artifact-class tokens

**Requirement APS-06-03.** The implementation SHALL represent **owner and artifact-class tokens** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `OWNER_AND_ARTIFACT_CLASS_TOKENS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict owner and artifact-class tokens while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Digest suffixes

**Requirement APS-06-04.** The implementation SHALL represent **digest suffixes** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `DIGEST_SUFFIXES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict digest suffixes while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Migration from legacy names

**Requirement APS-06-05.** The implementation SHALL represent **migration from legacy names** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `MIGRATION_FROM_LEGACY_NAMES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict migration from legacy names while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Guidelines for Effective File Naming

Provides operational rules for names that remain stable across tools and repositories.

### Human readability

**Requirement APS-06-06.** The implementation SHALL represent **human readability** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `HUMAN_READABILITY_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict human readability while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Machine parseability

**Requirement APS-06-07.** The implementation SHALL represent **machine parseability** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `MACHINE_PARSEABILITY_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict machine parseability while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Avoiding semantic duplication

**Requirement APS-06-08.** The implementation SHALL represent **avoiding semantic duplication** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `AVOIDING_SEMANTIC_DUPLICATION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict avoiding semantic duplication while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Length limits and slugs

**Requirement APS-06-09.** The implementation SHALL represent **length limits and slugs** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `LENGTH_LIMITS_AND_SLUGS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict length limits and slugs while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Collision handling

**Requirement APS-06-10.** The implementation SHALL represent **collision handling** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `COLLISION_HANDLING_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict collision handling while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Examples of Metadata-Rich File Names

Shows compliant and noncompliant names across common APS artifacts.

### Product requirements

**Requirement APS-06-11.** The implementation SHALL represent **product requirements** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `PRODUCT_REQUIREMENTS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict product requirements while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Architecture decisions

**Requirement APS-06-12.** The implementation SHALL represent **architecture decisions** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `ARCHITECTURE_DECISIONS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict architecture decisions while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Mutant definitions

**Requirement APS-06-13.** The implementation SHALL represent **mutant definitions** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `MUTANT_DEFINITIONS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict mutant definitions while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Verification receipts

**Requirement APS-06-14.** The implementation SHALL represent **verification receipts** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `VERIFICATION_RECEIPTS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict verification receipts while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Release ledgers

**Requirement APS-06-15.** The implementation SHALL represent **release ledgers** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `RELEASE_LEDGERS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict release ledgers while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Standard Directory Layout for APS

This section defines the normative repository layout for APS projects.

### Constitution

**Requirement APS-06-16.** The implementation SHALL represent **constitution** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CONSTITUTION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict constitution while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Claims and falsifiers

**Requirement APS-06-17.** The implementation SHALL represent **claims and falsifiers** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CLAIMS_AND_FALSIFIERS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict claims and falsifiers while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Implementation manifests

**Requirement APS-06-18.** The implementation SHALL represent **implementation manifests** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `IMPLEMENTATION_MANIFESTS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict implementation manifests while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Evidence and receipts

**Requirement APS-06-19.** The implementation SHALL represent **evidence and receipts** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `EVIDENCE_AND_RECEIPTS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict evidence and receipts while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Generated artifacts

**Requirement APS-06-20.** The implementation SHALL represent **generated artifacts** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `GENERATED_ARTIFACTS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict generated artifacts while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Archives and snapshots

**Requirement APS-06-21.** The implementation SHALL represent **archives and snapshots** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `ARCHIVES_AND_SNAPSHOTS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict archives and snapshots while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Subdirectories by Document State and Agile Role

Explains when state and role should be represented through directories versus metadata.

### Role-based ownership surfaces

**Requirement APS-06-22.** The implementation SHALL represent **role-based ownership surfaces** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `ROLE_BASED_OWNERSHIP_SURFACES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict role-based ownership surfaces while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### State-based review queues

**Requirement APS-06-23.** The implementation SHALL represent **state-based review queues** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `STATE_BASED_REVIEW_QUEUES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict state-based review queues while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Avoiding directory explosion

**Requirement APS-06-24.** The implementation SHALL represent **avoiding directory explosion** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `AVOIDING_DIRECTORY_EXPLOSION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict avoiding directory explosion while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Cross-functional work products

**Requirement APS-06-25.** The implementation SHALL represent **cross-functional work products** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `CROSS_FUNCTIONAL_WORK_PRODUCTS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict cross-functional work products while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Access control

**Requirement APS-06-26.** The implementation SHALL represent **access control** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `ACCESS_CONTROL_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict access control while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.

## Managing Archived Versions and Snapshots

This section defines archival, snapshot, and historical replay requirements.

### Immutable snapshots

**Requirement APS-06-27.** The implementation SHALL represent **immutable snapshots** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `IMMUTABLE_SNAPSHOTS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict immutable snapshots while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Retention classes

**Requirement APS-06-28.** The implementation SHALL represent **retention classes** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `RETENTION_CLASSES_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict retention classes while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Snapshot manifests

**Requirement APS-06-29.** The implementation SHALL represent **snapshot manifests** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `SNAPSHOT_MANIFESTS_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict snapshot manifests while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Replayability

**Requirement APS-06-30.** The implementation SHALL represent **replayability** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `REPLAYABILITY_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict replayability while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Legal holds and deletion

**Requirement APS-06-31.** The implementation SHALL represent **legal holds and deletion** as an explicit protocol concern with a stable identifier, authority source, evidence expectation, and failure consequence. It SHALL NOT leave the concern solely in narrative convention or infer it from a tracker status.

**Operational test.** A verifier MUST be able to locate the representation, resolve its dependencies, and produce one of the canonical standing outcomes. Missing representation yields `LEGAL_HOLDS_AND_DELETION_MISSING`; an unavailable checking capability yields `UNSUPPORTED`; contradictory evidence yields a typed refusal rather than a softened success.

**Falsifier.** Conformance is refuted when a same-coordinate candidate can omit or contradict legal holds and deletion while still receiving the standing or lifecycle promotion that the concern was intended to guard.

### Chapter-level minimum conformance

A conforming implementation of this section SHALL make every listed concern machine-readable, SHALL bind evidence to the exact subject coordinate, SHALL preserve the accepted baseline on refusal, and SHALL emit a receipt for successful promotion. The standing ceiling is **PARTIAL_ALIVE | ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED**; no chapter text authorizes a stronger claim than observed evidence.
