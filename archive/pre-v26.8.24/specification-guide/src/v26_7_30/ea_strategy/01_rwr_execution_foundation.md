
This chapter applies the complete Enterprise Architecture as Strategy context to the ggen manufacturing standard. It preserves the Ross–Weill–Robertson operating-model and foundation-for-execution frame, TOGAF architecture-development and governance discipline, the ArchiMate stakeholder-view role, and the Chatman Ecosystem’s admitted-knowledge, manufacturing, evidence, actuation, receipt, and replay laws.

The governing thesis is:

> Enterprise architecture becomes strategy when admitted architectural knowledge governs the complete family of operational consequences required to realize the operating model.

ggen changes the unit of architecture from a collection of independently maintained documents to a governed body of admitted semantic knowledge. Strategy, operating model, capabilities, value streams, products, services, information concepts, ontologies, applications, technologies, policies, requirements, transition states, authority, evidence, and standing are represented in one canonical architecture graph. ggen projects that graph into the artifact families required to build, govern, operate, verify, migrate, and retire digital systems.

This is not a claim that templates replace judgment. Human authorities still choose outcomes, operating models, risk posture, boundaries, exceptions, target states, and organizational design. The claim is narrower and stronger: once an architectural judgment is admitted, the enterprise should not restate it manually across code, infrastructure, policy, tests, proofs, observability, portfolio plans, migration plans, compliance packets, and runbooks.

## Preserve the RWR fence

Ross, Weill, and Robertson define an operating model through the required degrees of business-process integration and standardization. APS preserves the four canonical choices:

| Operating model | Integration | Standardization | Architectural consequence |
|---|---:|---:|---|
| Diversification | Low | Low | Autonomous business units, limited shared process and data law |
| Coordination | High | Low | Shared data and customer/process coordination with local process variation |
| Replication | Low | High | Standardized reusable processes with limited cross-unit data integration |
| Unification | High | High | Shared data, standardized core processes, and an enterprise-wide execution foundation |

The architecture SHALL NOT silently assume Unification. A low-integration, low-standardization enterprise must not be forced into a universal platform merely because central architecture prefers uniformity. The graph must encode both common law and permitted local variation. Each initiative SHALL identify the chosen operating model, the integration and standardization claims it changes, the affected business units, and the evidence that would falsify the choice.

RWR’s maturity path is also preserved:

1. **Business Silos** — local applications optimize local needs.
2. **Standardized Technology** — technology platforms and infrastructure are rationalized.
3. **Optimized Core** — shared data and standardized processes realize the operating model.
4. **Business Modularity** — reusable business components support rapid recombination.

ggen adds a clearly fenced extension:

5. **Evidence-Bearing Self-Governance** — the enterprise can explain, manufacture, govern, observe, receipt, replay, and revise its own change from admitted architecture.

Stage 5 is a ggen extension, not a claim that the original RWR framework contains a fifth stage. It is conjunctive. A repository does not reach it by possessing one autonomic loop, one knowledge graph, one generated core diagram, or one successful deployment. All 21 declared dimensions and all 63 proof obligations must close at the same exact coordinate.

## Strategy must survive translation

The central enterprise failure mode is semantic attenuation:

```text
strategic choice
-> operating-model principle
-> architecture standard
-> platform backlog
-> repository change
-> deployment
-> runtime behavior
```

At every boundary, meaning can weaken. Traditional governance uses review to detect drift, but review cannot be the primary carrier of meaning when local decisions grow faster than architecture-board capacity.

ggen makes admitted meaning the carrier. A strategic assertion becomes a stable graph object with provenance, owner, effective lifecycle, authority, constraints, measures, exclusions, and falsifier. Its lawful consequence family can include:

- capability and value-stream maps;
- shared information definitions and stewardship;
- APIs, events, schemas, and compatibility contracts;
- application and technology building blocks;
- provider-specific Azure, AWS, and GCP packs;
- access, classification, retention, and recovery policy;
- tests, negative fixtures, proof obligations, and verifier reports;
- telemetry, SLOs, resilience envelopes, and process evidence;
- portfolio work orders, migration plans, rollback plans, and retirement conditions;
- receipts binding source, transformation, artifact, verification, authorization, and observed consequence.

The strategy-standing law is:

```text
StrategyStanding =
    Intent
  ∧ ArchitectureTraceability
  ∧ ImplementedConsequence
  ∧ OperationalEvidence
```

An executive statement has intent but not standing. A generated architecture has traceability but not implemented consequence. A deployed system may have consequence without embodying the authorized intent. A theorem may prove a model without proving runtime correspondence. The strategy claim receives standing only when the entire same-object chain is explicit and evidenced.

## Foundation for execution

RWR’s foundation for execution combines a chosen operating model with an enterprise architecture that supplies the required integration and standardization. ggen operationalizes that foundation as:

```text
FoundationForExecution =
    OperatingModel
  × DigitizedPlatform
  × EngagementModel
  × EvidenceAndReplay
```

The **digitized platform** is the integrated set of shared data, infrastructure, applications, services, and reusable modules that implements the operating model. It is not one monolithic runtime. It may contain centralized, federated, replicated, or local components as permitted by the operating model. Every reusable platform service SHALL identify its consumers, authority, lifecycle, operating envelope, replacement constraints, and evidence.

The **engagement model** defines how projects, products, platforms, architecture authorities, security, operations, finance, compliance, suppliers, and delivery teams make and enforce decisions. It includes decision rights, exception paths, segregation of duties, promotion authority, and local adaptation rules. An engagement model that exists only as prose is `PARTIAL_ALIVE` at best. Its material decisions must appear in work-order authority, policy gates, review roles, execution grants, and receipts.

The **evidence-and-replay layer** prevents a foundation from becoming a historical diagram. It binds the exact architecture state to generated artifacts, build results, deployment grants, runtime observations, process conformance, incidents, and revisions. Observed consequence returns as new observation and may invalidate or evolve the architecture.

## Core diagram as a projection, not authority

The core diagram is a compact expression of how the enterprise will operate. It identifies the essential customers or constituencies, core processes, shared information, reusable services, and key integration or automation mechanisms that implement the operating model.

In APS, the core diagram SHALL be generated from the canonical architecture graph. It is a stakeholder projection, not a second authority. The graph must preserve the identities and relations required to regenerate the view:

```text
OperatingModel
-> CoreProcess
-> SharedInformation
-> ReusablePlatformService
-> IntegrationMechanism
-> CustomerOrConsumer
-> Measure
-> Evidence
```

A core diagram that cannot be traced to capabilities, application services, solution building blocks, owners, consumers, and operating evidence is descriptive only. A diagram that differs from the graph is drift. An ArchiMate export is governed by the same rule: useful as a view and exchange projection, never an independent source of truth.

The core diagram SHALL expose what is intentionally shared and what remains local. It SHALL identify the smallest reusable execution foundation that supports the selected operating model. It SHALL not become an inventory poster containing every application or technology.
