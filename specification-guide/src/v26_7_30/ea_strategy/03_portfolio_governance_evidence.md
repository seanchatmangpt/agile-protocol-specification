## Portfolio, capacity, and leverage

Enterprise Architecture as Strategy governs repeated value creation, not only technical conformance. The architecture repository SHALL connect investment to capabilities, reusable platform services, consumers, outcomes, and evidence.

Portfolio measures include:

- reuse and adoption of platform modules;
- duplicate capability and application cost;
- consumer onboarding time;
- change lead time and failure rate;
- migration and retirement progress;
- cost, capacity, reliability, security, and proof burden;
- semantic drift and exception volume;
- realized operating-model outcomes.

Little’s Law provides a portfolio fence:

```text
WorkInProgress = Throughput × LeadTime
```

Adding work without increasing throughput or accepting longer lead time is not strategy. Architecture work orders must expose dependency closure, constrained capacity, and the cost of proof. Reusable modules should reduce repeated local translation while preserving lawful variation.

Conway’s Law is also operational. The communication structure and decision rights of the enterprise influence the systems it produces. The graph SHALL either align ownership boundaries with desired modularity or make the mismatch explicit as transition debt. A core platform owned by a fragmented committee with no decisive product authority is an architectural contradiction, not merely a staffing issue.


## Executable TOGAF interpretation

TOGAF supplies the architecture-development and governance frame. ggen does not collapse the ADM phases into one generator command because the phases represent different decisions and different authority.

- **Preliminary** defines the enterprise boundary, architecture roles, metamodel, standing vocabulary, standards, exception policy, evidence policy, lifecycle law, repository ownership, and actuation boundary.
- **Phase A** authorizes the architecture initiative, target outcomes, scope, stakeholders, claim ceiling, risks, required decisions, and initial burden of proof.
- **Phase B** declares the operating model, value streams, capabilities, actors, decision rights, process variation, integration needs, standardization needs, and performance outcomes.
- **Phase C** defines information authority, application services, interfaces, product boundaries, stewardship, compatibility, and consumer contracts.
- **Phase D** defines platforms, runtimes, protocols, deployments, security boundaries, suppliers, and operating envelopes.
- **Phase E** constructs candidate GBB/SBB/pack combinations and evaluates viability.
- **Phase F** selects transition architectures, partial-order work, migration, rollback, resource, and evidence plans.
- **Phase G** checks implementation conformance against the admitted architecture contract.
- **Phase H** admits operational evidence, incidents, changing constraints, and new strategy as architecture-change inputs.

The executable ADM is a controlled feedback loop rather than a document waterfall:

```text
vision
-> architecture
-> candidate solutions
-> transition
-> implementation
-> operation
-> observed evidence
-> revised architecture
```

Human judgment remains explicit. Vision approval, risk acceptance, organizational design, supplier choice, exception approval, and irreversible transition may remain human authorities. ggen manufactures the evidence and consequence surface on which those decisions operate. A missing decision is `UNKNOWN`; it is not a failed computation and must not be auto-filled by a planner.

## Public ontology and federated law

The architecture graph is not one universal enterprise ontology. It composes foundation, common, industry, organization, product, and consumer ontologies through explicit imports, profiles, shapes, contracts, and precedence. Public vocabularies are preferred when they preserve the required meaning. Local extensions must declare why the public model is insufficient, which boundary they add, who owns the extension, and how it can later migrate or converge.

PROV-O, DCAT, DCTERMS, SKOS, SHACL, ODRL, FOAF, OCEL, FIBO, QUDT, and SOSA may provide reusable semantic rails. Their presence does not establish conformance. Shapes, rules, fixtures, consumer execution, and evidence determine standing.

Federation preserves source authority. A repository adapter may observe GitHub, cloud inventories, service catalogs, policy systems, telemetry, finance, or ticketing systems, but observation does not automatically admit those records as architecture truth. The route is:

```text
external observation
-> source-bound provenance
-> identity resolution
-> admission or refusal
-> canonical graph
-> projection and evidence
```

One failed source edge does not prove the enterprise graph is unavailable. The repository reports bounded gaps and continues with the admitted dependency-closed state. Missing or stale observations remain visible.

## Architecture views and stakeholder consequence

Executives, architects, developers, operators, auditors, finance, security, suppliers, and consumers need different projections. ggen may manufacture core diagrams, capability maps, value-stream views, ArchiMate exchanges, ownership matrices, interface catalogs, technology landscapes, risk views, roadmaps, cost maps, compliance packets, and evidence graphs.

All views share canonical identities. No stakeholder projection may invent a relationship absent from the admitted graph. A view may intentionally omit detail, but the omission must be declared by profile. Lossy projections are bounded views, not replacement authorities.

The test of a view is not whether it looks complete. It is whether a stakeholder can traverse from the presented decision to the underlying architecture object, owner, evidence, exceptions, and next transition. The view layer therefore becomes explainable access to architecture law rather than a parallel diagram repository.


## Fortune-5 control plane obligations

A Fortune-5-scale execution foundation requires more than repository generation. The architecture profile includes:

- operating-model contracts;
- explicit decision rights;
- policy and exception governance;
- append-only evidence ledger;
- SLO and resilience envelopes;
- segregation of duties;
- supplier and third-party controls;
- data classification and retention;
- recovery objectives and tested rollback;
- proof-bearing promotion gates;
- exact-head release law;
- process evidence and replay.

These obligations must be visible in machine-readable metadata, policy, evidence, or typed refusal. Convention and institutional memory are insufficient.

## Autonomics without hidden power

The autonomic loop is bounded:

```text
observe -> diagnose -> plan -> emit intent
```

It does not directly execute. Monitor, Analyze, and Plan may operate over the architecture graph and evidence ledger. Execute belongs to BRCE or another admitted broker with explicit authority. The loop may recommend repair, rollback, deprecation, scaling, migration, or architecture revision, but the output is an `ArchitectureIntent`.

The lawful continuation is:

```text
stimulus
-> diagnosis
-> candidate repair
-> architecture intent
-> independent admission
-> BRCE execution grant
-> actuator
-> observed result
-> evidence admission
-> receipt
-> replay
```

Zero unreceipted actuation remains a hard invariant. Hooks do not inherit DO authority. A knowledge hook may manufacture an intent or route evidence but cannot mutate filesystem, process, network, deployment, or external state.

## Evidence, standing, and replay

The evidence ladder is:

```text
unit -> integration -> e2e -> chaos -> stress -> benchmark -> verifier report
```

The ladder is not an automatic proof hierarchy. Each claim declares the level required for its own boundary. Evidence binds the same object, authority, operation, revision, toolchain, inputs, outputs, environment, and consequence.

Standing uses the precise vocabulary:

- `ALIVE` — execution was observed and the bounded acceptance contract passed.
- `PARTIAL_ALIVE` — a proper subset executed or the requested crown remains open.
- `BLOCKED` — a known prerequisite prevents lawful completion.
- `BUILD_BROKEN` — the admitted tree does not build under the declared command.
- `UNKNOWN` — required observation has not been made or interpreted.
- `UNSUPPORTED` — the available substrate cannot perform the operation.
- `REFUSED` — an explicit law rejected a transition while preserving state.

No checkpoint receives `ALIVE` from documentation, metadata, generated tests alone, or a neighboring demonstration. Formal proof and runtime correspondence retain separate standing. A successful deployment with missing required evidence remains `UNKNOWN` for the unsupported claim.

Receipts bind authority, admitted inputs, ordered outputs, operation, standing, lineage, and replay contract. ggen execution identities use BLAKE3. APS publication receipts may retain their declared SHA-256 schema without weakening the ggen execution law. Duplicate replay is detected before chain-position error, and refusal preserves verifier state.

OCEL events use admitted logical time for causal replay. Wall-clock timestamps may remain observations but cannot be the sole ordering authority. Events link initiative, work order, actor, capability, artifact, grant, refusal, verifier, receipt, and prior event.
