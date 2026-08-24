# MCP and A2A Autonomics for a Fortune-5-Scale SAFe Enterprise

This chapter defines the executable enterprise simulation profile shipped with APS v26.7.30. The profile converts the book’s protocol law into a deterministic Rust system that models a fictional Fortune-5-scale digital delivery organization. It is intentionally not a digital twin of any real company. Its purpose is to make the APS claims falsifiable at enterprise cardinality while preserving the boundary between declared work, agent collaboration, tool invocation, authorized actuation, evidence, and replay.

The central composition is:

```text
APS work order
  → A2A task graph
  → MCP capability invocation
  → exclusive actuation broker
  → applied or refused receipt
  → replayable enterprise event ledger
```

A2A and MCP are adjacent but non-equivalent. A2A represents independent agents collaborating through discoverable capabilities, messages, stateful tasks, parts, and artifacts. MCP represents a host or agent using tools, resources, and prompts through negotiated capabilities. The simulator therefore refuses the common architectural collapse in which every agent is treated as a tool or every tool call is treated as an autonomous agent. Peer delegation occurs on the A2A plane. Context access and executable capabilities occur on the MCP plane. Business authority belongs to neither plane; authority is evaluated by the APS actuation broker.

## Preserve: SAFe as the enterprise coordination fence

The simulation preserves the useful organizational distinctions of SAFe. A portfolio groups value streams under a common funding and governance model. Development value streams contain solutions and delivery organizations. Solution Trains coordinate multiple Agile Release Trains and suppliers for large integrated solutions. ARTs coordinate teams around a common cadence. Backlogs preserve the decomposition from portfolio epics to capabilities, features, enablers, and stories. PI planning, iteration execution, system-level evaluation, and inspect-and-adapt form synchronization points.

These distinctions are retained because removing them would destroy the very coordination problem the simulation is meant to test. However, APS does not accept schedule, ceremony completion, role prestige, or tracker status as proof that value was produced. SAFe provides a coordination grammar; APS supplies admission, authority, falsifiers, receipts, and replay.

The fictional `Apex Meridian Group` profile contains:

| Object | Count |
|---|---:|
| Portfolios | 5 |
| Development value streams | 20 |
| Solution Trains | 40 |
| Agile Release Trains | 80 |
| Teams | 800 |
| Delivery personnel represented by team cardinality | 7,200 |

The simulator deterministically materializes the complete 945-object coordination graph: 5 portfolios, 20 value streams, 40 Solution Trains, 80 ARTs, and 800 teams. Every object receives a stable hierarchical identifier and parent closure. The graph is still a bounded model rather than a claim of empirical realism. It represents the digital delivery system, not the company’s entire workforce, balance sheet, physical operations, customers, or legal entities.

## Fence: what the simulation may and may not establish

The simulation can establish that the checked-in machinery compiles, that the admitted scenario executes, that A2A and MCP requests route through their declared boundaries, that autonomic proposals are bounded, that unauthorized actions are refused, and that identical coordinates replay to the same receipt head. It cannot establish that a real enterprise will behave like the model. It cannot establish full MCP or A2A transport conformance because the v26.7.30 profile is deliberately in-process and excludes production authentication, network transport, streaming, push notifications, and optional protocol features.

The standing ceiling is therefore narrow:

```text
ALIVE(simulation coordinate)
≠ ALIVE(real corporation)
≠ certified MCP implementation
≠ certified A2A implementation
≠ certified SAFe implementation
```

The use of SAFe terminology is descriptive and interoperable. No affiliation with or certification by Scaled Agile is claimed.

## Calculus: from admitted observation to receipted consequence

The simulation instantiates the Chatman equation at an enterprise control boundary:

```text
O  = configuration, scenario, protocol request, and current metrics
O* = validated configuration + exact seed + protocol versions + authority token
A  = μ(O*) = task, artifact, applied action, or typed refusal
R  = hash-chained receipt proving the observed consequence
```

The lawful path is:

```text
parse
→ route
→ admit or refuse
→ diagnose and plan
→ request actuation
→ broker authorization
→ mutate or preserve baseline
→ receipt
→ replay
```

No A2A agent may mutate enterprise state directly. No MCP tool definition grants authority merely because the tool is discoverable. The broker is the only control path permitted to change policy-governed metrics. Environmental simulation transitions, such as market demand or a production incident, are observations rather than control actuations; they are still recorded in the ledger, but they do not claim an authorized management decision.

**Requirement APS-15-01.** Every policy-governed state mutation SHALL cross the exclusive actuation broker and SHALL produce either an applied receipt or a refused receipt.

**Operational test.** The report invariants `zero_unreceipted_actuation` and `topology_cardinality_exact` MUST equal true. The number of `actuation.applied` and `actuation.refused` ledger events MUST match the broker counters, and the materialized topology MUST close to the configured enterprise scale.

**Falsifier.** Any code path that changes intake state, capacity allocation, architecture enabler allocation, release readiness, or budget allocation without a broker receipt refutes conformance.

## MCP capability plane

The MCP profile is pinned to specification version `2025-11-25`. It implements the base JSON-RPC semantic shape and the following methods:

- `initialize`
- `notifications/initialized`
- `tools/list`
- `tools/call`
- `resources/list`
- `resources/read`
- `prompts/list`
- `prompts/get`

Initialization requires an exact protocol version and returns deterministic server capabilities. Tool listings use a stable order to make discovery and replay insensitive to hash-map iteration. Input definitions use JSON Schema-shaped objects. Results contain text plus `structuredContent`; refused tool execution sets `isError` without collapsing the refusal into a transport failure.

The server exposes read-only resources for enterprise topology, current SAFe flow metrics, A2A Agent Cards, and the receipt-chain head. Prompts encode bounded PI planning, inspect-and-adapt, and release-governance questions. The tool surface includes enterprise inspection, portfolio intake control, bounded capacity rebalance, architecture runway allocation, release evaluation, budget-reallocation requests, and receipt-head inspection.

The critical distinction is discoverability versus authority. `tools/list` answers what can be requested. The broker answers whether a specific caller at a specific coordinate may cause the requested consequence.

**Requirement APS-15-02.** MCP tool discovery SHALL NOT be interpreted as authorization, and each actuating tool call SHALL carry an explicit authority token evaluated by the broker.

**Falsifier.** A tool call with an absent or invalid authority token that mutates enterprise state refutes conformance.

The profile includes a stateful stdio binding. `mcp-stdio` reads one JSON-RPC request per line, preserves the admitted enterprise engine across the session, suppresses notification responses, and emits one JSON response line for each request. This makes the capability plane directly connectable to MCP hosts without converting the simulation into a network service.

The profile excludes HTTP transport, OAuth, sampling, elicitation, and experimental MCP tasks. Those are later Gall checkpoints. They are not inferred from the presence of the stdio semantic profile.

## A2A peer-agent plane

The A2A profile is pinned to released version `1.0.0`. It models Agent Cards, Messages, Tasks, Parts, and Artifacts, plus bounded operations for card discovery, message submission, task retrieval, task listing, and cancellation.

The simulated agent system contains five discoverable roles:

1. **Lean Portfolio Management Agent** — creates a PI plan artifact from admitted topology and guardrails.
2. **Solution Train Coordination Agent** — resolves cross-ART dependency pressure by requesting a bounded MCP capacity tool.
3. **Enterprise Architecture Agent** — produces architecture runway observations without direct actuation.
4. **Release Governance Agent** — invokes the MCP release gate and returns the receipt as an A2A artifact.
5. **Investment Committee Liaison Agent** — can collect and route budget evidence but transitions to `input-required` rather than impersonating human investment authority.

Messages carry interaction turns. Artifacts carry task outputs. The simulator does not hide output inside status prose because critical results must remain retrievable and typed. Tasks use server-generated deterministic identifiers and terminal states. Once completed, rejected, failed, or canceled, a task cannot be restarted or canceled as though it were still mutable. The `a2a-jsonl` harness preserves the task store across requests so `message/send`, `tasks/get`, `tasks/list`, and `tasks/cancel` exercise a stateful peer-agent lifecycle rather than isolated function calls.

**Requirement APS-15-03.** A2A task outputs SHALL be represented as artifacts, and terminal tasks SHALL reject subsequent cancellation or restart attempts.

**Falsifier.** Returning the PI plan only as an ephemeral status message, or mutating a completed task back to working, refutes conformance.

A2A delegation does not expose agent chain-of-thought, hidden memory, or internal prompts. The contract is capability, task state, exchanged message, artifact, and receipt. Opaque internal execution is compatible with APS only when external consequences remain bounded and independently observable.

## MCP and A2A composition

The release-governance path demonstrates the intended composition:

```text
A2A message/send
  → release-governance-agent task
  → MCP tools/call safe.release.evaluate
  → broker evaluates release-governance authority
  → compliance and flow preconditions
  → APPLIED or REFUSED receipt
  → A2A release-evaluation artifact
```

The dependency-resolution path follows the same law:

```text
A2A dependency task
  → MCP safe.capacity.rebalance
  → delta guardrail ≤ 5 percent
  → broker decision
  → capacity and blocked-feature consequence
  → receipt artifact
```

This composition prevents two dangerous substitutions. First, the A2A agent cannot claim that delegation itself caused the business consequence. Second, the MCP tool cannot claim that successful execution means the broader A2A task or PI succeeded. Each layer receives only the standing earned at its own boundary.

**Requirement APS-15-04.** The A2A task receipt SHALL preserve the underlying MCP actuation decision and SHALL NOT upgrade a refused tool call into a completed business outcome.

## Autonomics: bounded MAPE-K rather than unconstrained agency

All autonomic thresholds and delta ceilings are admitted in the enterprise configuration under `autonomics`; they are not hidden constants. Configuration validation refuses incoherent policy, such as a requested capacity movement above its maximum or an architecture floor above its ceiling.

The simulation includes autonomic control loops organized as Monitor–Analyze–Plan–Execute over Knowledge. The knowledge base is the event and receipt ledger. Monitoring reads current metrics. Analysis compares observations with admitted thresholds. Planning manufactures typed intents. Execution invokes the MCP capability plane and broker. The controller never receives a hidden bypass around authorization.

The controllers are:

- **Portfolio WIP guard.** Freezes intake when active features exceed the portfolio WIP limit. It may unfreeze only after WIP falls below a stricter release threshold, preventing oscillation at the boundary.
- **Dependency controller.** Requests a three-percent capacity rebalance when blocked-feature ratio exceeds twelve percent. The broker refuses any delta above five percent.
- **Architecture runway controller.** Raises enabler allocation to the admitted floor when architecture risk is elevated. It cannot allocate more than twenty-five percent.
- **Compliance gate.** Refuses release readiness when compliance risk exceeds tolerance.
- **Budget watch.** Observes budget pressure and requests intervention, but its autonomous authority is intentionally insufficient. The result is `HUMAN_AUTHORIZATION_REQUIRED`.

The autonomics therefore implement homeostasis, not sovereignty. They may keep the system inside predefined guardrails. They may not invent strategy, broaden their authority, change the guardrails that constrain them, or convert an advisory observation into a funded decision.

**Requirement APS-15-05.** Autonomic controllers SHALL operate within explicit delta ceilings and SHALL escalate decisions reserved for human authority instead of fabricating authorization.

**Falsifier.** An autonomic budget controller that successfully reallocates lean budget is a same-object refutation, not a convenient demonstration.

## Deterministic enterprise cadence

The scenario `global-core-modernization` runs two PIs with five iterations each. Its seed is `26730`. Initial conditions deliberately begin under pressure: portfolio WIP exceeds the guardrail, architecture risk exceeds the threshold while enabler capacity is below its floor, blocked work is material, and budget consumption is elevated. Scheduled shocks introduce regulatory demand, a dependency wave, a market surge, a production incident, and supplier delay.

Each iteration records completion, intake, blocked work, risk changes, and budget consumption. Autonomic plans are then derived from the resulting coordinate. Cross-ART dependency pressure may create an A2A task. At PI closure, the release-governance agent evaluates the integrated candidate through the MCP release tool. The result can be admitted or refused; the cadence ends either way because completion of a calendar interval does not imply release standing.

The pseudo-random generator is local, deterministic, and seeded. It does not use system time, network calls, global randomness, or unordered collections in receipt material. The event ledger is a SHA-256 hash chain:

```text
H₀ = 64 zeroes
Hₙ = SHA-256(Hₙ₋₁ || canonical_json(eventₙ))
```

The final report binds configuration, scenario, metrics, and receipt head into a replay key. Two executions at the same coordinate must produce identical standing, metrics, event count, receipt head, and replay key.

**Requirement APS-15-06.** Same-coordinate replay SHALL be deterministic.

**Falsifier.** A second run with identical source, config, scenario, seed, protocol versions, and toolchain that produces a different receipt head yields `DETERMINISTIC_REPLAY_MISMATCH`.

## Failure taxonomy

The simulation preserves the APS standing lattice and typed refusals:

- `ALIVE` — observed compile, execution, invariant, and replay checks succeeded.
- `PARTIAL_ALIVE` — a bounded subset executed, but the complete verifier ladder did not.
- `BLOCKED` — an admitted dependency or authority prerequisite prevented the requested consequence.
- `BUILD_BROKEN` — the Rust or integration verifier executed and failed.
- `UNKNOWN` — observation is insufficient to classify the coordinate.
- `UNSUPPORTED` — the requested protocol method or action is outside the implemented profile.

Representative refusal codes include `AUTHORITY_REFUSED`, `BOUNDED_DELTA_REFUSED`, `HUMAN_AUTHORIZATION_REQUIRED`, `COMPLIANCE_GATE_REFUSED`, `FLOW_GATE_REFUSED`, `MCP_METHOD_NOT_FOUND`, `MCP_TOOL_UNSUPPORTED`, `A2A_AGENT_CARD_NOT_FOUND`, `A2A_SKILL_UNSUPPORTED`, and `A2A_TERMINAL_TASK_IMMUTABLE`.

A protocol error and a tool refusal are not interchangeable. An unknown JSON-RPC method is a protocol-level method error. A valid `tools/call` request that lacks business authority is a structured tool result with refusal standing. This distinction lets callers repair their request without mistaking a lawful refusal for infrastructure failure.

## Verifier ladder

The repository workflow executes the following ladder:

```text
static JSON and source admission
→ cargo fmt
→ cargo clippy -D warnings
→ unit tests
→ protocol integration fixtures
→ negative authority and bounded-delta fixtures
→ end-to-end Fortune-5-scale scenario
→ deterministic replay
→ verifier receipt artifact
```

The canonical replay commands are:

```bash
cargo test --manifest-path simulation/fortune5-safe/Cargo.toml --all-targets
python3 simulation/fortune5-safe/scripts/verify.py --require-cargo
```

The verifier inspects the scale floor, exact MCP and A2A versions, required method profile, source invariants, runtime report, receipt chain, negative fixtures, and replay identity. Its output is `simulation/fortune5-safe/target/aps-safe-sim/verification-receipt.json`, uploaded by GitHub Actions rather than treated as hand-authored source.

## Exclusions and extension path

The current checkpoint intentionally excludes production network servers, OAuth, enterprise identity, remote MCP authorization, A2A streaming, push notifications, signed Agent Cards, gRPC and REST bindings, persistent databases, real portfolio adapters, real financial systems, and private employee or customer data.

A lawful extension proceeds by Gall checkpoints:

1. preserve the deterministic kernel and the v26.7.30 MCP stdio binding;
2. add MCP Streamable HTTP with authentication and trace propagation;
3. add an A2A HTTP binding with well-known Agent Cards;
4. add persistence and crash replay;
5. add chaos testing for duplicate delivery, reordering, timeout, cancellation, and split-brain authority;
6. add performance benchmarks at increasing portfolio and task cardinality;
7. publish independent conformance reports without upgrading unsupported features by implication.

The v26.7.30 machinery is therefore a living checkpoint. It demonstrates the complete constitutional path from enterprise intent to agent delegation, tool use, bounded autonomics, receipt, and replay. It does not pretend that a simulated corporation is a real one or that protocol-shaped JSON is sufficient for production standing.

## Sources

- Model Context Protocol Specification, version 2025-11-25: `https://modelcontextprotocol.io/specification/2025-11-25`
- Agent2Agent Protocol Specification, released version 1.0.0: `https://a2a-protocol.org/latest/specification`
- Scaled Agile Framework knowledge base entries for portfolios, ART and Solution Train backlogs, Solution Trains, flow, and PI roadmaps: `https://framework.scaledagile.com/`
