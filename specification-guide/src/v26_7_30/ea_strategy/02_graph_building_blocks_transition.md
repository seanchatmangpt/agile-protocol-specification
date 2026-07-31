## Canonical enterprise architecture graph

The canonical graph is the machine-readable operating constitution. Its minimum metamodel includes the following classes.

**Strategy:** Enterprise, Boundary, Principle, Driver, Outcome, Requirement, Constraint, Risk, Exception, OperatingModel, ArchitectureInitiative.

**Business:** Capability, ValueStream, Process, Actor, Role, Product, Service, Consumer, DecisionRight.

**Information:** InformationConcept, Ontology, OntologyVersion, OntologyProfile, DataProduct, Policy, Shape, Rule, Classification, RetentionRule.

**Application and technology:** ApplicationService, Component, Repository, Interface, TechnologyStandard, Runtime, Environment, Deployment, Supplier, OperatingEnvelope.

**Manufacturing:** GBB, ArchitectureBuildingBlock, SolutionBuildingBlock, Pack, ConstituentPack, DistributionPack, Query, Template, Projection, Artifact, Validator.

**Transition:** ArchitectureState, BaselineArchitecture, TargetArchitecture, TransitionArchitecture, WorkPackage, Plan, PlanCertificate, Migration, Rollback.

**Governance and evidence:** Claim, Checkpoint, Standing, Evidence, Receipt, ExecutionGrant, Observation, Event, ExceptionDecision, Deprecation, Retirement.

Key relations include `realizes`, `requires`, `constrains`, `owns`, `consumes`, `imports`, `projects`, `produces`, `validates`, `authorizes`, `evidences`, `replaces`, and `transitionsTo`. Every material relation SHALL carry provenance and effective lifecycle.

The graph SHALL detect orphan states:

- a capability with no realization is aspirational;
- an application with no capability relationship may be accidental complexity;
- shared information with no steward is ungoverned;
- a platform with no consumers is inventory, not leverage;
- a generated artifact with no authority coordinate is unsupported;
- a deployed component with no operating evidence remains `UNKNOWN`;
- a retirement plan with no consumer-impact closure is unsafe.

## GBB calculus: ABB, SBB, packs, and profiles

The canonical ggen Building Block kernel preserves the TOGAF distinction between architecture and solution building blocks.

An **Architecture Building Block** states a capability, constraint, interface, quality, or policy that must exist without prematurely selecting an implementation.

A **Solution Building Block** is a concrete realization with technology, deployment, lifecycle, supplier, cost, capacity, and evidence coordinates.

A **GBB** binds the architecture requirement to candidate and admitted realizations:

```text
GBB =
  <identity,
   requirement,
   interfaces,
   constraints,
   realizations,
   manufacturing_law,
   transition_law,
   authority,
   evidence,
   receipt,
   replay>
```

A **bblock** is a versioned, governed group of packs realizing one capability. Packs may contain provider-neutral contracts and provider-specific realizations. Azure, AWS, and GCP—including `gpc` as an accepted GCP alias at the CLI boundary—must remain profiles over one kernel rather than competing architecture truths.

Provider support receives standing independently. A shared capability contract may be `ALIVE` while one cloud realization is `BLOCKED` or `UNKNOWN`. A pack may be active while its production evidence is incomplete. Lifecycle and evidentiary standing remain separate dimensions.

Composition is deterministic and dependency-closed. Conflicting profile claims are refused rather than resolved by input order. Hidden dependencies, hand-patched consumer outputs, and unreceipted promotion are explicit failure modes.

## Architecture repository and `ggen architecture doctor`

The first useful product is not broad autonomic execution. It is a lifecycle-aware federated architecture repository plus an honest diagnostic command.

The repository joins strategy, capabilities, products, repositories, ontologies, packs, receipts, work orders, runtime observations, and transition states without erasing source identity. It SHALL preserve:

- canonical identity and aliases;
- source and revision;
- provenance and effective lifecycle;
- owner, steward, consumer, reviewer, and promotion authority;
- requirements and constraints;
- imports, dependencies, and replacement relations;
- generated surfaces and protected paths;
- standing, evidence, nonclaims, and next transition;
- snapshots and replay coordinates.

`ggen architecture doctor` SHALL answer:

- what the architecture believes;
- why an ontology, pack, capability, or component is present;
- which dependency introduced it;
- who owns and consumes it;
- what it will manufacture;
- what it may read, write, or request;
- what capacity, reliability, security, and cost obligations follow;
- what is deprecated, blocked, unsupported, or unknown;
- what changed since the last admitted state;
- which evidence is missing;
- what the dominant cause is;
- what remediation and next lawful transition are available.

Every command SHALL support machine-readable output and typed refusal. Human output SHALL identify identity, source, standing, dominant cause, and remediation. Dry-run planning is the default for consequential commands. Actuation requires an explicit broker path and execution grant.

The proposed command surface includes:

```text
ggen architecture init|inspect|doctor|graph|impact
ggen architecture baseline|target|transition|comply|explain
ggen architecture export archimate
ggen ontology discover|register|inspect|graph|validate|compose
ggen ontology diff|impact|benchmark|profile|deprecate|retire|replay
ggen pack inspect|graph|compose|verify|benchmark|promote
ggen pack deprecate|retire|replay
ggen plan candidates|transition|verify|explain|receipt
ggen evidence inspect|verify|graph|replay
ggen bblock inspect|compose|verify|promote|deprecate|retire|replay
```

## Architecture contracts

An architecture contract is a machine-readable agreement between authority, provider, consumer, verifier, and operator. It binds:

- capability and operating-model intent;
- required and forbidden behavior;
- semantic inputs and outputs;
- SLO, resilience, capacity, security, and cost envelopes;
- ownership and decision rights;
- accepted variation and extension points;
- build, test, proof, and runtime evidence;
- exception and waiver lifecycle;
- migration, rollback, deprecation, and retirement;
- receipt and replay obligations.

Contracts SHALL generate consumer conformance tests and provider proof obligations together. A provider cannot self-certify solely through tests generated from its own implementation. Independent validation and real consumer execution are required where the claim depends on them.

## Baseline, target, and transition architectures

The architecture is not only a target state. It is a lawful transition system:

```text
BaselineArchitecture
-> CandidateConstruction
-> AdmissibilityGates
-> TransitionArchitecture
-> WorkOrderDAG
-> BoundedIntent
-> ExecutionGrant
-> ObservedConsequence
-> Receipt
-> RevisedArchitecture
```

A baseline must identify observed state, uncertainty, debt, ownership gaps, capacity, incidents, and evidence quality. A target must identify outcomes and claim ceilings without pretending implementation. A transition architecture must preserve dependencies, parallelism, resources, risk, rollback, data migration, consumer compatibility, and proof obligations.

MFW, POWL, and PDDL may project transition plans. CMD may explore candidate combinations. BCINR and CMCA may rank candidates by cost, risk, latency, capability fit, and proof burden. The selected plan remains declarative. A plan is not an execution grant.

No valid plan under current constraints is a legitimate result. The planner SHALL expose conflicting requirements or minimal unresolved obligations rather than silently relax policy.
