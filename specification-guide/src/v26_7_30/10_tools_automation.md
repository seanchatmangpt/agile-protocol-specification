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

## MCP, A2A, and Enterprise Autonomics

APS v26.7.30 includes an executable reference profile at `simulation/fortune5-safe/` and a normative analysis in [MCP and A2A Autonomics for a Fortune-5-Scale SAFe Enterprise](15_mcp_a2a_safe_simulation.md). The profile preserves three independent planes: A2A peer collaboration, MCP capability access, and APS business authority. It refuses any architecture in which discoverable tools silently become authority or agent delegation silently becomes actuation.

### MCP capability boundary

**Requirement APS-10-17.** MCP servers SHALL expose tools, resources, and prompts as capabilities, while all policy-governed state changes SHALL remain subject to the APS actuation broker.

**Operational test.** `tools/list` MUST be deterministic. An actuating `tools/call` without an admitted authority token MUST produce a structured refusal result rather than mutate state or return a protocol success that implies application success.

**Falsifier.** Conformance is refuted if tool discoverability is sufficient to change portfolio WIP, capacity, architecture allocation, release readiness, or lean budget.

### A2A collaboration boundary

**Requirement APS-10-18.** A2A Agent Cards and tasks SHALL describe peer capabilities and collaboration state without exposing or acquiring direct control authority.

**Operational test.** A2A outputs MUST be persisted as task artifacts. A task that needs an enterprise consequence MUST invoke an MCP capability and preserve the underlying broker receipt.

**Falsifier.** Conformance is refuted if an A2A agent mutates enterprise state without an MCP tool call and broker receipt.

### Autonomic control law

**Requirement APS-10-19.** MAPE-K controllers SHALL manufacture bounded intents from admitted metrics and SHALL NOT modify the guardrails or authority lattice that constrain them.

**Operational test.** Portfolio intake, dependency, and architecture controllers MUST remain within their configured delta ceilings. A budget controller MUST escalate to human authority and produce `HUMAN_AUTHORIZATION_REQUIRED`.

**Falsifier.** An autonomous lean-budget reallocation or an unbounded capacity movement refutes conformance at the same simulation coordinate.

### Deterministic enterprise replay

**Requirement APS-10-20.** The enterprise simulation SHALL bind configuration, scenario, seed, protocol versions, source revision, and toolchain into its evidence coordinate and SHALL produce identical receipt heads for identical coordinates.

**Operational test.** The self-test MUST execute the complete scenario twice and compare standing, metrics, event count, receipt head, and replay key.

**Falsifier.** Same-coordinate receipt drift yields `DETERMINISTIC_REPLAY_MISMATCH` and prevents ALIVE standing.

### Fortune-5-scale nonclaim

**Requirement APS-10-21.** The simulation SHALL identify its enterprise as fictional and SHALL distinguish cardinality testing from empirical claims about a real corporation.

**Operational test.** Configuration and verifier receipts MUST contain the scale counts and explicit nonclaims. No real company name, employee data, customer data, financial record, or operational endpoint may be required.

**Falsifier.** Claiming that the simulated results establish performance or governance properties of an actual Fortune 5 company refutes the profile’s admission boundary.
