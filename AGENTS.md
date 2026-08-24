# AGENTS.md — APS v26.8.24

This repository is an executable specification of knowledge-work reconstitution and autonomic manufacturing. Read `MANIFEST.json`, `.aps-syntax.md`, and the active mdBook before changing anything.

## Operating doctrine

Treat every existing implementation as sunk at a new decision boundary. Existing behavior, contracts, safety properties, and evidence are observations to recover; existing structure receives no continuation privilege.

Use this order:

```text
observe -> admit knowledge -> contract -> DfCM -> construct -> authorize -> do -> evidence -> verify -> standing -> reconstitute
```

### ggen-first

Before handwriting a repeatable surface, ask:

1. Is there an admitted known manufacturing pattern? Compose it.
2. Is there a specialized generator/tool? Manufacture its declarations, configuration, and invocation.
3. Is there a known tool sequence? Manufacture the script/workflow.
4. Is the difference only parameters/facts? Encode them as authority.
5. Only then author irreducible novel mechanism.
6. After qualification, promote reusable novelty into manufacturing knowledge.

Do not confuse a native generator with an alternative to upstream manufacture.

### Contract first

Design semantic subjects, preconditions, postconditions, invariants, refusals, authority, idempotency, resource bounds, evidence, compatibility, and standing before choosing implementation. Implementation and verifier should be sibling consequences of authority whenever feasible.

### Evidence law

Inspection is not execution. Verify state at the claimed boundary. Prefer real subprocesses/services/databases when the claim concerns them, negative fixtures, sabotage/mutation, exact-head CI, replay, and independently observable state.

No narrative may upgrade `UNKNOWN`, `BLOCKED`, or `PARTIAL_ALIVE` to `ALIVE`.

## Repository boundaries

`archive/` is predecessor evidence only. Never repair archived material or use it as current authority.

Active source must contain no predecessor-version authority surfaces. `tools/verify.py` enforces this structurally.

Generated book output belongs outside the repository. Current CI builds to `/tmp` and publishes receipts as workflow artifacts.

## Required validation

Run all of:

```bash
python3 tools/verify.py --no-receipt
python3 -m unittest discover -s tests -v
mdbook build -d /tmp/aps-book specification-guide
python3 tools/simulate_fortune500.py examples/fortune500-fibo/enterprise.json
```

Before promotion, require exact-head CI for the candidate being promoted.
