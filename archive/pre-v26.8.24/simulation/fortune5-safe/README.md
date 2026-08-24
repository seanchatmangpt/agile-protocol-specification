# APS Fortune-5-Scale SAFe Simulation

This package is executable machinery for the APS v26.7.30 MCP/A2A enterprise profile. It simulates a fictional Fortune-5-scale digital delivery system without representing any actual company.

## Architecture

```text
APS work order
    ↓
A2A peer-agent task graph
    ↓ delegation
MCP tools / resources / prompts
    ↓ intent
exclusive actuation broker
    ↓ applied or refused
hash-chained receipt ledger
    ↓
deterministic replay report
```

The admitted topology contains five portfolios, twenty development value streams, forty Solution Trains, eighty Agile Release Trains, eight hundred teams, and 7,200 delivery personnel. The engine materializes the complete 945-object coordination graph with deterministic hierarchical identifiers, then binds its digest into replay evidence.

## Protocol profiles

The MCP profile is pinned to `2025-11-25` and implements initialization plus deterministic tools, resources, and prompts. The A2A profile is pinned to `1.0.0` and implements Agent Card discovery, message submission, task retrieval/listing, cancellation, messages, parts, tasks, and artifacts.

MCP is the capability plane. A2A is the peer-agent collaboration plane. Neither protocol grants business authority. Every simulated mutation crosses the broker, which evaluates role authority, guardrails, preconditions, and human authorization boundaries before emitting an applied or refused receipt.

## Autonomics

The control system follows a bounded MAPE-K loop:

1. **Monitor** flow, dependency, architecture, compliance, and budget metrics.
2. **Analyze** threshold violations at an exact PI and iteration coordinate.
3. **Plan** a typed intent with a named controller and authority token.
4. **Execute** through an MCP tool and the exclusive actuation broker.
5. **Knowledge** is the append-only hash-chained receipt ledger used for replay.

Controllers include a portfolio WIP guard, dependency controller, architecture runway controller, compliance gate, and budget watch. Thresholds and delta ceilings are admitted under the configuration’s `autonomics` object. The budget watch intentionally cannot reallocate funds; it produces `HUMAN_AUTHORIZATION_REQUIRED`.

## Run

```bash
cargo run --manifest-path simulation/fortune5-safe/Cargo.toml -- \
  simulate \
  --config simulation/fortune5-safe/config/fortune5-enterprise.json \
  --scenario simulation/fortune5-safe/config/global-core-modernization.json \
  --out simulation/fortune5-safe/target/aps-safe-sim/simulation-report.json
```

Exercise an MCP fixture:

```bash
cargo run --manifest-path simulation/fortune5-safe/Cargo.toml -- \
  mcp-fixture \
  --config simulation/fortune5-safe/config/fortune5-enterprise.json \
  --scenario simulation/fortune5-safe/config/global-core-modernization.json \
  --request simulation/fortune5-safe/fixtures/mcp_rebalance.json
```

Exercise an A2A fixture:

```bash
cargo run --manifest-path simulation/fortune5-safe/Cargo.toml -- \
  a2a-fixture \
  --config simulation/fortune5-safe/config/fortune5-enterprise.json \
  --scenario simulation/fortune5-safe/config/global-core-modernization.json \
  --request simulation/fortune5-safe/fixtures/a2a_plan_pi.json
```

Run the verifier ladder:

```bash
python3 simulation/fortune5-safe/scripts/verify.py --require-cargo
```

The GitHub workflow also runs `cargo fmt`, `cargo clippy -D warnings`, tests, deterministic replay, negative authority fixtures, and uploads the receipts as an artifact.

## Exclusions

This is not a SAFe certification product. It does not implement MCP or A2A network transports, OAuth, streaming, push notifications, signed Agent Cards, or every optional protocol feature. Those exclusions are deliberate Gall checkpoints rather than implied support.

## Stateful protocol sessions

Run the MCP profile as a real stdio JSON-RPC session. Each input line is one request and each non-notification response is emitted as one JSON line:

```bash
cargo run --manifest-path simulation/fortune5-safe/Cargo.toml -- \
  mcp-stdio \
  --config simulation/fortune5-safe/config/fortune5-enterprise.json \
  --scenario simulation/fortune5-safe/config/global-core-modernization.json
```

A client-command example is provided at `config/mcp-client.example.json`.

Run the persistent A2A simulation harness with:

```bash
cargo run --manifest-path simulation/fortune5-safe/Cargo.toml -- \
  a2a-jsonl \
  --config simulation/fortune5-safe/config/fortune5-enterprise.json \
  --scenario simulation/fortune5-safe/config/global-core-modernization.json
```

The A2A JSONL binding is an executable test harness, not a claim of the production HTTP, REST, gRPC, streaming, or push-notification bindings.
