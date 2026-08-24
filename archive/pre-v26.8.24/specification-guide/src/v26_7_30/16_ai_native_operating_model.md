# AI-Native Fortune-5 Operating Model

An AI-Native operating model is not an organization with more copilots. It is an organization whose strategy, portfolio, value-stream, train, team, protocol, control, and evidence surfaces are designed so that bounded machine participants can contribute without silently acquiring authority. At Fortune-5 scale, this distinction is constitutional. A model may generate an analysis, propose a portfolio allocation, draft a feature, detect a control excursion, or prepare an execution plan. None of those acts is equivalent to admitting a business commitment, authorizing a consequential change, or proving that the change occurred lawfully.

APS therefore treats AI-Native SAFe as a layered operating system. SAFe supplies the organizational topology and economic cadence. APS supplies admitted observations, deterministic work orders, typed authority, and exclusions. Gall supplies observed standing at checkpoints. BRCE owns consequential DO. MCP exposes bounded context and tools to agent hosts. A2A coordinates peer agents and long-running tasks. MAPE-K autonomic controllers maintain bounded operating conditions. Receipts and replay close the system.

## 1. Preserve the SAFe organizational fence

The implementation preserves the useful organizational objects that already coordinate a large enterprise:

- portfolios allocate strategic themes, guardrails, and investment horizons;
- development and operational value streams define persistent flows of value;
- Agile Release Trains coordinate products and solutions across teams;
- Solution Trains coordinate multiple ARTs where a single train is insufficient;
- Lean Portfolio Management governs strategy, funding, portfolio operations, and governance;
- System Teams, Shared Services, Communities of Practice, and enabling functions provide cross-cutting capabilities;
- PI Planning establishes a synchronized planning boundary;
- Inspect and Adapt establishes a recurring learning boundary.

AI-Native transformation does not erase these objects. It changes their information density, cycle time, and executable precision. The fence is preserved because it carries accountability, funding, architecture, compliance, and human coordination that cannot be reconstructed from a collection of autonomous agents after the fact.

## 2. Formal enterprise state

Let the enterprise operating state be

\[
E = (S, V, T, W, P, A, C, K, R)
\]

where:

- \(S\) is the set of strategic themes and economic constraints;
- \(V\) is the set of portfolios, value streams, solutions, ARTs, and teams;
- \(T\) is the temporal structure of portfolio horizons, PIs, iterations, and control intervals;
- \(W\) is the admitted work graph;
- \(P\) is the policy set;
- \(A\) is the authority graph;
- \(C\) is the controller set;
- \(K\) is the shared knowledge and evidence base;
- \(R\) is the receipt and replay ledger.

An agent may propose a transition \(\Delta E\). A transition has standing only when its source observations are admitted, its authority path is resolved, its preconditions and exclusions are satisfied, its actuation passes through the exclusive broker, and its consequences produce receipts that can be independently replayed.

The effective authority for any consequential action is:

\[
A_{effective} = \min(A_{policy}, A_{identity}, A_{environment}, A_{human}, A_{budget}, A_{risk})
\]

The minimum operator is intentional. Additional agent capability cannot increase authority beyond the narrowest applicable constraint. Missing evidence does not become permission. UNKNOWN does not become ADMITTED. A successful proposal does not become successful execution.

## 3. Four-plane architecture

### 3.1 Strategy and value plane

This plane contains enterprise strategy, strategic themes, portfolio guardrails, value-stream economics, architecture runway, regulatory obligations, and customer outcomes. AI participants may synthesize signals, generate scenarios, estimate delays, identify option value, or challenge portfolio assumptions. Human fiduciaries retain accountability for strategy, capital allocation, material risk acceptance, and organizational commitments.

### 3.2 Coordination plane

This plane contains portfolio Kanban, solution and ART backlogs, PI objectives, dependencies, risks, capacity allocation, and team work. APS converts these coordination objects into typed, deterministic work orders. A work order names the admitted source, target, authority, acceptance tests, exclusions, budget, rollback path, expected receipt, and replay hook. Ambiguous tickets may remain useful discussion artifacts, but they do not have executable standing.

### 3.3 Protocol plane

MCP and A2A occupy different positions in this plane.

MCP is the host-to-server context and tool protocol. It exposes bounded resources, prompts, and tools to an agent host. The Fortune-5 profile pins MCP revision `2025-11-25`, requires capability negotiation, treats tool annotations as untrusted metadata, and forbids tool discovery from implying actuation authority. MCP servers may expose enterprise topology, current admitted state, schemas, policy decisions, simulation results, and work-order preparation. They must not bypass the broker.

A2A is the peer-agent task and artifact protocol. It publishes Agent Cards, negotiates skills, creates task identities, tracks task lifecycle, carries messages and artifacts, and supports long-running coordination. The profile pins A2A protocol version `1.0`. An A2A task may manufacture analysis, plans, evidence bundles, or candidate work orders. It cannot elevate its own authority or declare its own evidence sufficient.

MCP answers: “What bounded context and tools can this host use?” A2A answers: “Which peer agent can perform this task, and what artifacts did it return?” APS answers: “What has authority and standing?” BRCE answers: “What may execute?” Gall answers: “What was observed at the checkpoint?”

### 3.4 Actuation and evidence plane

All consequential DO passes through the exclusive broker. The broker resolves policy, identity, environment, approval, budget, risk, and idempotency constraints before actuation. Every accepted actuation produces a receipt containing at least the admitted input digest, work-order identity, policy decision, executor identity, environment identity, result digest, timestamps or logical clock, and replay coordinate.

The invariant is:

\[
\forall a \in Actuation,\; \exists r \in Receipt : binds(r, a)
\]

or operationally: zero unreceipted actuation.

## 4. Fortune-5 topology

A Fortune-5 topology is expected to contain multiple portfolios, many value streams, hundreds of ARTs, thousands of teams, and tens of thousands of people and agents. Scale is represented explicitly rather than inferred from a demo-scale graph. The deterministic simulator in `simulation/fortune5-safe/` models:

- 10 portfolios;
- 100 value streams;
- 500 ARTs;
- 5,000 teams;
- 50,000 people;
- 60,000 agents;
- portfolio, PI, iteration, and control-loop clocks;
- MCP and A2A protocol surfaces;
- MAPE-K autonomic controllers;
- brokered actuation and receipts;
- deterministic replay from a seed.

These numbers are not a production capacity claim. They establish that the object model, algorithms, invariants, and evidence pipeline can be exercised at the intended topology rather than only at a toy scale.

## 5. Automation versus autonomics

Automation executes a predetermined transition when its trigger and preconditions are satisfied. Autonomics continuously observes the operating state and selects among bounded responses. APS uses the MAPE-K model:

1. **Monitor** collects admitted telemetry and evidence.
2. **Analyze** evaluates thresholds, trends, constraints, and causal hypotheses.
3. **Plan** manufactures one or more candidate interventions.
4. **Execute** submits the selected work order to the broker.
5. **Knowledge** retains topology, policy, receipts, replay results, and learned control parameters.

The controller state is

\[
C_i = (scope_i, signals_i, policy_i, envelope_i, standing_i, history_i)
\]

Each controller has an explicit scope and actuation envelope. Controllers may be arranged at team, ART, value-stream, portfolio, platform, security, reliability, cost, and compliance levels. Higher-level controllers do not silently overwrite lower-level commitments. Conflicts are resolved through declared precedence and policy, then receipted.

Examples include:

- WIP and flow controllers that reduce admission when queues exceed guardrails;
- dependency controllers that surface cross-ART critical paths;
- reliability controllers that freeze promotion when error budgets are exhausted;
- security controllers that revoke credentials or quarantine artifacts under predefined policy;
- cost controllers that propose capacity shifts when unit economics drift;
- compliance controllers that require additional evidence before regulated transitions;
- portfolio controllers that recommend—not self-authorize—funding reallocation.

## 6. PI Planning as an admitted graph transformation

PI Planning is represented as a bounded graph transformation rather than a meeting transcript. Inputs include strategic themes, portfolio constraints, architecture runway, feature candidates, capacity, dependencies, risks, prior receipts, and current telemetry. The planning process produces a candidate graph of PI objectives, feature allocations, dependency commitments, risk dispositions, and evidence obligations.

The graph is admitted only when:

- every objective has a responsible train or solution context;
- every dependency has both producer and consumer coordinates;
- capacity does not exceed admitted envelopes;
- architecture and compliance obligations have owners and tests;
- risks have explicit dispositions;
- unresolved assumptions remain typed as assumptions;
- the plan has a revision identity and replayable derivation.

Agents can explore many plans combinatorially. They cannot erase the distinction between a candidate plan and an accepted commitment.

## 7. Evidence-driven ceremonies

SAFe ceremonies become evidence boundaries:

- portfolio sync examines strategy execution, economics, policy exceptions, and receipt aggregates;
- ART sync examines flow, dependency, and impediment evidence;
- System Demo binds integrated behavior to a specific build and environment;
- Inspect and Adapt binds problem-solving claims to observed outcomes;
- iteration review binds accepted stories to executable tests and artifacts;
- release governance binds promotion to policy decisions, attestations, and rollback coordinates.

A ceremony may still include discussion and judgment. The AI-Native addition is that its inputs, decisions, exclusions, and consequences can be represented as inspectable objects instead of disappearing into slides and memory.

## 8. Failure semantics

The operating model distinguishes:

- **PARTIAL_ALIVE**: a bounded checkpoint executes, while broader closure remains open;
- **ALIVE**: the claimed scope has observed executable proof;
- **BLOCKED**: an external prerequisite or authority edge prevents execution;
- **BUILD_BROKEN**: the admitted source fails compilation or construction;
- **UNKNOWN**: evidence has not been observed;
- **UNSUPPORTED**: the requested capability is outside the implemented boundary.

These states must not collapse. A queue delay is UNKNOWN, not failure. A schema-valid work order is PARTIAL_ALIVE, not executed. A simulation is ALIVE for simulation claims, not for production deployment. A refused action is evidence that the authority system is operating, not evidence that the requested effect occurred.

## 9. Verification ladder

The Fortune-5 machinery advances through:

1. unit tests for state, policy, protocol, and controller primitives;
2. integration tests for MCP, A2A, broker, ledger, and control loops;
3. end-to-end seeded simulation;
4. failure and chaos fixtures;
5. full-scale topology execution;
6. performance benchmarks;
7. an independent verifier report;
8. book and PDF publication receipts.

The independent verifier reconstructs the expected topology and invariants from the seed. It does not accept the simulator’s self-description as proof. Deterministic run receipts must compare byte-for-byte where the law declares determinism.

## 10. Exclusions and nonclaims

This repository establishes an executable reference implementation and conformance surface. It does not claim that a Fortune-5 company has been reorganized, that production systems have been connected, that MCP or A2A endpoints are publicly deployed, or that regulated authority has been delegated to agents. Production admission requires organization-specific identity, policy, data classification, risk, environment, and legal controls.

The reference architecture deliberately excludes direct model-to-production actuation, authority inferred from model confidence, self-approval by the proposing agent, mutable receipts, unbounded controller scope, and promotion based only on narrative review.

## 11. Operational coordinate

The canonical executable machinery is `simulation/fortune5-safe/`. Its Rust workspace contains domain, APS control, MCP server, A2A bus, MAPE-K autonomics, deterministic simulator, telemetry, and verifier crates. The required local ladder is:

```bash
cargo fmt --manifest-path simulation/fortune5-safe/Cargo.toml --all -- --check
cargo test --manifest-path simulation/fortune5-safe/Cargo.toml --all-targets
cargo clippy --manifest-path simulation/fortune5-safe/Cargo.toml --all-targets -- -D warnings
cargo run --release --manifest-path simulation/fortune5-safe/Cargo.toml -- simulate
cargo run --release --manifest-path simulation/fortune5-safe/Cargo.toml -- verify
python3 specification-guide/scripts/verify_v26_7_30.py
mdbook build specification-guide
```

The generated receipts, verifier report, HTML book, and PDF are consequences of these coordinates. They are not substitutes for them.
