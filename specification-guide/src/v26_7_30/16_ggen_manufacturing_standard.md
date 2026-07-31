# ggen Manufacturing, Building Blocks, and Release Law

This chapter admits the reusable manufacturing standards developed in the ggen program during the bounded observation window from 2026-07-23 through 2026-07-30 Pacific time. It does not import the whole ggen implementation into APS. It establishes the APS profile that downstream Gall checkpoints, work-order generators, architecture registries, and release verifiers SHALL use when a repository claims ggen-aligned manufacturing.

The source coordinate is `seanchatmangpt/ggen` release `26.7.62` at revision `68952593c40214ac1a681073d65f3902a9cdfce4`. The consolidated architecture program was merged by `faa52dac474d456ae00105869770161d666ba31f`, which records exact aggregate head `036ab703e885aff90a79536a5db5b24608e8a32f`. These coordinates bound provenance. They do not grant APS permission to claim every ggen capability as locally executed.

## Preserve the authority boundary

ggen is an ontology-to-artifact manufacturing system. The ontology, admitted graph, public namespace, and explicit policy are authority. Templates, source files, command surfaces, documentation, tests, reports, and receipts are projections or evidence surfaces. A projection MAY be committed when repository doctrine requires it, but a committed projection MUST NOT silently become a second authority.

The canonical direction is:

```text
admitted ontology and policy
-> deterministic query and rule closure
-> typed construction plan
-> bounded actuation request
-> generated artifact set
-> independent verification
-> receipt
-> replay
```

A human or agent SHALL repair the authority source or generator when a generated projection is wrong. Hand-editing a generated output to create apparent conformance is refused as `HAND_CODED_GENERATED_OUTPUT`. A second synchronization over unchanged admitted inputs SHALL produce byte-identical outputs or a typed drift report. “Close enough” output is not replay.

**Requirement GGEN-AUTH-001.** Every ggen-aligned work order SHALL name the canonical authority, generated surfaces, protected generated paths, generator coordinate, and replay command.

**Falsifier.** Change a generated file without changing ontology, policy, template, or admitted input. The verifier must report drift rather than accept the changed projection as a new source of truth.

## Law-state manufacturing calculus

The reusable control flow is:

```text
parse -> route -> admit/refuse -> diagnose/repair
      -> construct -> actuate -> receipt -> replay/hook
```

Parsing produces observations, not standing. Routing identifies the law and capability boundary. Admission decides whether the observation may enter the manufacturing world. Diagnosis can explain a refusal or construct a repair plan but cannot mutate the world. Construction creates reversible plans and artifacts in the graph domain. Actuation crosses into filesystem, process, network, deployment, or external state only through the admitted broker. Receipts bind consequences. Replay tests whether the same admitted coordinate still yields the same observation. Hooks may route evidence or new work, but hooks do not inherit actuation authority.

For APS, this expands the Chatman equation without replacing it:

```text
O --admission--> O*
A = μ(O*)
R ⊢ A = μ(O*)
```

The manufacturing function `μ` is not one opaque call. A conforming implementation exposes the lawful morphisms used to parse, query, construct, project, actuate, verify, receipt, and replay. A missing morphism is not repaired by prose.

**Requirement GGEN-CALC-001.** Each work item SHALL declare the stage it changes and SHALL NOT blur construction, admission, actuation, verification, or standing assignment.

## Maximal frontmatter as admitted observation

ggen maximal frontmatter treats metadata as an executable admission carrier rather than decorative prose. APS adopts the principle, not a fixed serialization monopoly. TOML, YAML, JSON, RDF, or another declared syntax MAY carry the observation, but the carrier SHALL be complete enough to route, constrain, verify, and replay the work.

A maximal work-order frontmatter record SHALL include:

- stable identity, namespace, schema version, and source coordinate;
- authority and admission basis;
- lifecycle state separate from evidentiary standing;
- MUST and MUST NOT obligations;
- allowed and forbidden paths;
- inputs, outputs, dependencies, and replacement relations;
- required capabilities and actuation authority;
- acceptance commands and expected evidence;
- positive witnesses, negative fixtures, and same-object falsifiers;
- receipt algorithm, lineage, replay command, and nonclaims;
- owner, assignee, reviewer, and promotion authority;
- logical time or deterministic ordering fields where sequence matters.

Metadata does not imply standing. `UNKNOWN` remains `UNKNOWN` until the declared verifier runs. A populated frontmatter block is not proof that its consequence occurred.

**Requirement GGEN-FM-001.** APS serializers SHALL preserve semantically meaningful frontmatter fields across round trips. A lossy projection SHALL be typed as a refusal or an explicitly bounded partial projection.

## Typed refusal and refusal precedence

A refusal is a first-class result. It preserves the law that prevented mutation and the observation that triggered it. Refusals SHALL be typed, externally visible, and state-preserving. Dry-run mode SHALL perform no mutation. Unknown capability SHALL not be coerced into success. Unsupported substrate SHALL not be reported as policy refusal.

Replay introduces precedence requirements. The ggen CertificationAssist repair established that verified receipt identity is checked before chain position. A duplicate replay therefore returns `DuplicateReplay` even when the duplicate is presented out of order. The verifier state remains unchanged on refusal. This prevents a rejected replay attempt from corrupting the state used to judge later receipts.

A conforming refusal result binds:

```text
refusal = <code, object, law, observed, expected, state_before,
           state_after, repair, evidence>
```

For a refused mutation, `state_after` SHALL equal `state_before`.

**Requirement GGEN-REFUSE-001.** Refusal precedence SHALL be deterministic and testable with overlapping negative fixtures.

**Falsifier.** Submit a verified receipt twice, with the second copy at a position that would also violate chain order. The result must be `DuplicateReplay`, and the chain state must remain byte-identical to its pre-attempt state.

## Zero direct actuation and BRCE continuation

ggen architecture autonomics implement Monitor, Analyze, and Plan but intentionally omit direct Execute. The generated output is an `ArchitectureIntent`, not a side effect. `direct_actuation_allowed` SHALL remain `false` in the APS ggen profile.

The lawful continuation is:

```text
stimulus
-> diagnosis
-> architecture intent
-> independent admission
-> BRCE execution grant
-> actuator
-> observed result
-> evidence admission
-> receipt
```

This preserves the APS–Gall–BRCE separation. APS defines the work and evidence contract. Gall observes checkpoint execution and assigns bounded standing. BRCE owns the exclusive DO path. ggen manufactures projections and intents. No layer may infer another layer’s authority from adjacency.

**Requirement GGEN-ACT-001.** Every filesystem, process, network, deployment, or external API mutation SHALL name the broker capability and produce an externalizable receipt. Zero unreceipted actuation is a hard invariant.

## ggen Building Block kernel

The ggen Building Block, or GBB, standard establishes one canonical architecture kernel. Domain profiles compose the kernel; they do not fork it into competing architecture packages. A CLI may be a facade over the kernel, but the facade SHALL NOT duplicate architecture truth.

A Building Block has stable identity, kind, version, lifecycle state, evidentiary standing, dependencies, required controls, obligations, profile membership, and composition receipt. Lifecycle and standing are separate dimensions. An object may be active yet `UNKNOWN`, deprecated yet `ALIVE` for a historical replay claim, or admitted but `PARTIAL_ALIVE` for an incomplete crown.

Profiles SHALL compose deterministically. Conflicting profile claims are refused with a typed conflict rather than resolved by input order. Composition receipts use BLAKE3 identities over ordered inputs. Public collections SHALL use deterministic ordering.

**Requirement GGEN-GBB-001.** A repository SHALL expose one architecture kernel, profile composition rules, conflict refusals, and composition replay. A second kernel is an architectural fork and requires an explicit migration decision.

## Combinatorial maximalism

Combinatorial maximalism maximizes reversible graph-domain construction before machine-state actuation. It does not mean unbounded execution. The ggen pack pattern combines public ontology, fail-closed SPARQL gates, generated verifier and CLI surfaces, an atomic filesystem broker, BLAKE3 receipt-chain identities, exact-output replay, typed refusals, and sabotage fixtures.

APS adopts these obligations:

1. Generate candidate combinations in the reversible construction domain.
2. Bound exhaustive or pairwise coverage by declared cardinality and resource policy.
3. Admit only combinations that pass all fail-closed semantic gates.
4. Route mutation through one atomic broker.
5. Receipt the exact admitted input set and exact output inventory.
6. Re-run synchronization to prove byte identity.
7. Sabotage authority, closure, ordering, actuation, and replay paths with negative fixtures.

A large generated set without gates is not maximalism. It is uncontrolled expansion. A gate set without negative fixtures is not evidence that refusal works.

**Requirement GGEN-CMD-001.** The conformance report SHALL state explored combinations, admitted combinations, refused combinations, gate count, negative-fixture count, and replay result.

## Deterministic non-LLM self-play

Self-play is a verification substrate, not an invitation to hide nondeterminism behind an agent label. The admitted ggen self-play model uses ontology-authored scenario games, a ggen-manufactured Rust runner and verifier, deterministic actor policies, real filesystem, process, and state transitions, BLAKE3 receipts, and replay. Actors are explicit state machines. No LLM call is required or permitted for the deterministic crown.

The self-play loop is:

```text
scenario graph
-> actor state machines
-> bounded actions
-> real boundary transitions
-> observed events
-> verifier
-> receipt chain
-> replay
```

**Requirement GGEN-PLAY-001.** A self-play claim SHALL publish scenario identity, actor transition tables, seeds or deterministic ordering, capability bounds, boundary evidence, and replay result. A transcript alone is insufficient.

## Multi-surface capability standing

ggen’s current verification constitution requires real boundary crossing, causality, and corroboration across multiple evidence surfaces. APS admits the general law: no status claim without receipts, and no ALIVE crown from a single convenient assertion.

A capability claim SHOULD be corroborated across at least three relevant surfaces selected from:

- execution;
- telemetry;
- persistent state;
- process or operating-system consequence;
- causality;
- generated artifact inventory;
- receipt verification;
- replay.

The surfaces must concern the same object and operation coordinate. Three adjacent demonstrations do not corroborate one missing consequence.

**Requirement GGEN-STAND-001.** Every capability report SHALL name its capability count, proof-surface count, exact command, revision, inputs, outputs, failures, nonclaims, and standing.

## Gall-grade work orders

The ggen-aligned APS projection for Gall is a deterministic work-order DAG. Each checkpoint manufactures a ticket or agent work order with:

- a stable checkpoint and ticket identifier;
- MUST and MUST NOT clauses;
- allowed and forbidden paths;
- context and explicit out-of-scope boundaries;
- dependencies and topological order;
- acceptance criteria and executable verification commands;
- expected evidence and receipt paths;
- assignee, reviewer, and authority;
- lifecycle state and expected Gall standing;
- adversarial questions and same-object falsifier.

Orphan tickets, duplicate identifiers, dependency cycles, ownership disagreement, unsafe local paths, and cross-checkpoint work that bypasses the DAG are refused. Absence of dependencies is represented as an empty set, not an invented dependency.

**Requirement GGEN-GALL-001.** An APS-to-Gall projection SHALL be deterministic, dependency-closed, and replayable from the admitted checkpoint graph.

## Logical time and OCEL evidence

Where ordering matters, generated OCEL events SHALL use admitted logical time or another deterministic clock contract. Wall-clock timestamps MAY be included as observations but SHALL NOT be the sole ordering authority for replay. Every actuation, refusal, verification, and broker decision SHOULD be representable as an OCEL event linked to the work order, capability, actor, artifact, receipt, and prior event.

**Requirement GGEN-OCEL-001.** Replaying the same admitted scenario SHALL preserve event identity and causal order even when wall-clock execution time changes.

## ggen-first proof projection

The ggen-first Lean 4 to Rust pattern separates rendering, admission, and certification:

```text
ggen renders
-> Lean admits
-> Rust projection compiles and executes
-> verifier correlates theorem, artifact, and receipt
```

Generated Rust is not a proof merely because it originated near Lean. Lean kernel admission applies to the theorem object at its exact coordinate. Rust execution applies to the projection. The receipt must correlate both without collapsing their standing.

**Requirement GGEN-PROOF-001.** Proof-backed generation SHALL identify the theorem, kernel result, projection digest, compiler coordinate, runtime verifier, and exclusions.

## Exact-head release law

CI evidence SHALL bind to the exact candidate head. A workflow that verifies an older merge queue head, stale branch, or unrelated artifact cannot promote the current candidate. Checkout steps SHALL pin immutable action revisions and explicitly select the pull-request head or current commit. Exact-head finalizers SHALL be replay-safe and SHALL avoid hidden queue coupling.

The release ladder remains:

```text
unit -> integration -> e2e -> chaos -> stress -> benchmark -> verifier report
```

A repository MAY stop at a lower checkpoint, but it must report `PARTIAL_ALIVE`, `BLOCKED`, `BUILD_BROKEN`, `UNKNOWN`, or `UNSUPPORTED` as appropriate. The word “finalizer” does not manufacture crown completeness.

**Requirement GGEN-REL-001.** Promotion SHALL require an exact-head verifier report whose receipt subject equals the candidate commit and whose required checks correspond to that same commit.

## Public namespace and identity

The admitted namespace origin is `https://chatmangpt.com`. Repository identity, public object identity, and canonical URL are distinct. Metadata does not imply standing. A namespace registry MAY admit an object while its capability standing remains `UNKNOWN`.

**Requirement GGEN-ID-001.** Public identifiers SHALL be stable, dereferenceable where practical, and separated from mutable repository location. Repository transfer or rename SHALL NOT silently change object identity.

## Conformance profile

The machine-readable profile is `specification-guide/standards/ggen-v26.7.62.json`. The focused verifier is:

```bash
python3 specification-guide/scripts/verify_ggen_v26_7_31.py
```

The verifier checks the exact source coordinate, observation window, required standards, state vocabulary, evidence ladder, ontology authority, direct-actuation refusal, BLAKE3 obligation, replay precedence, chapter closure, and same-object exclusions. It emits `receipts/APS-v26.7.31-ggen-standard.json`.

The existing APS book verifier remains the crown entry point. The ggen verifier is a subordinate profile check executed in the same workflow. Neither local verification nor CI may claim that the ggen implementation itself executed inside APS. The admitted consequence is narrower: APS contains a complete, machine-readable, falsifiable, and replayable ggen manufacturing standard.
