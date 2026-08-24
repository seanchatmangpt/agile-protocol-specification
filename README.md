# Agile Protocol Specification v26.8.24

APS is an executable constitution for **knowledge-work reconstitution and autonomic manufacturing**.

It starts from a simple law:

> **Chatman's Law:** historical production cost confers no preservation privilege. Durable value migrates toward the recoverable knowledge, contracts, evidence, and manufacturing capability needed to reproduce or improve useful consequences.

Compactly:

```text
everything is sunk
-> preserve truth, not implementations
-> contract before implementation
-> manufacture the largest lawful candidate space
-> authorize consequence explicitly
-> independently qualify
-> turn evidence into reusable manufacturing knowledge
-> reconstitute again
```

## This repository is the specification

The active repository is deliberately small enough to identify its authority surfaces and broad enough to exercise them. It is no longer a documentation book wrapped around predecessor work-order machinery.

```text
MANIFEST.json                         authority map
.aps-syntax.md                        compact protocol syntax
ontology/                             public-ontology-aligned semantic profiles
contracts/                            executable contract/evidence envelopes
specification-guide/src/v26_8_24/     normative manuscript
examples/fortune500-fibo/             synthetic enterprise contract/reconstitution case
simulation/                           executable sensitivity scenario
 tools/                               whole-repository verifier + deterministic model
 tests/                               state/structure qualification
 .github/workflows/                    exact-head qualification court
 archive/                              predecessor evidence only
```

## Governing architecture

```text
reality / predecessor
  -> observation
  -> admitted knowledge O*
  -> executable contract
  -> DfCM candidate manufacturing space
  -> SELECT
  -> CONSTRUCT
  -> explicit authority / refusal
  -> DO
  -> object-centric process evidence + receipts
  -> independent verification
  -> standing
  -> reusable knowledge
  -> next reconstitution
```

The manufacturing equation is:

```text
A = mu(O*)
```

Generated artifacts are consequences; they do not become independent semantic authority merely because they execute.

## Contract-first, ggen-first law

**Known pattern? Compose it.**

**Known tool? Generate its invocation.**

**Novel mechanism? Discover it once, then teach the factory.**

A specialized framework generator, compiler, migration tool, package manager, infrastructure engine, or external executable is capital equipment. Upstream manufacturing should produce its declarations, configuration, scripts, and invocations whenever those are derivable.

Applications therefore carry a strong presumption of manufacture. Libraries retain genuinely irreducible mechanism while their surrounding APIs, types, adapters, tests, docs, packaging, and bindings remain candidates for manufacture.

## Five-level × seven-dimension jig model

APS uses the industrial progression:

```text
L1 Craft -> L2 Template -> L3 Fixture -> L4 Jig -> L5 Closed-Loop Manufacturing System
```

across seven dimensions:

1. product knowledge;
2. work positioning;
3. operation guidance;
4. process sequence;
5. error prevention;
6. measurement & qualification;
7. adaptation & learning.

This is a maturity vector, not a comforting average. A sophisticated engine can still depend on craft knowledge in one dimension.

## Synthetic FIBO Fortune-500 experiment

`ontology/fortune500-fibo-profile.ttl` and `examples/fortune500-fibo/` define a **synthetic** financial-enterprise case using FIBO Legal Persons as a public semantic substrate.

The deterministic sensitivity model asks what happens to manufacturing volume and full human lifecycle-equivalent effort when admitted enterprise capabilities project across many interfaces, environments, and DfCM architecture candidates. It also models board-level governance compression by validating source classes—ontology/profile, manufacturing patterns, authority policy, verifier law—instead of manually inspecting every manufactured artifact.

It is intentionally not empirical evidence about a real company.

Run it:

```bash
python3 tools/simulate_fortune500.py examples/fortune500-fibo/enterprise.json
```

## Full process intelligence

Artifact correctness is insufficient. Consequential activity must emit comparable object-centric and provenance evidence so the enterprise can analyze conformance, variants, bottlenecks, authority exceptions, rework, failure propagation, economic performance, and **process fitness**.

A perfectly conformant unsafe process is still unsafe.

## Governance compression

“Validate once” means **admit a bounded, versioned law once**, not approve it forever.

A board or delegated authority can validate classes of semantic source, contract law, manufacturing patterns, authority policy, verifier/metrology law, and risk bounds. Each manufactured consequence still proves derivation and is automatically qualified. A material source-law change creates a new decision boundary and requires new admission.

Governance therefore moves upstream without disappearing.

## Software manufacturing as capital

The factory accumulates reusable capability: ontology profiles, contracts, templates, jigs, generator compositions, verifiers, authority policies, process mappings, and reconstitution knowledge.

Code that can be reproduced from those sources increasingly behaves like **inventory**. The durable asset is the knowledge required to remanufacture it.

The goal is maximum **qualified manufacture**, not minimum files, minimum commits, or meaningless volume.

## Adversarial pressure is part of the design method

Resistance and criticism are not merely adoption friction. A critic with a different loss function can discover failure states the constructor never searched.

```text
objection -> candidate falsifier -> explicit failure state -> evidence -> new requirement or admitted limit
```

Liability, authority attribution, long-horizon reconstruction, unsafe-but-conformant processes, artifact-scale governance, replay, and model/session disappearance are architecture requirements once evidence admits them.

## Standing and claim discipline

APS uses:

`ALIVE | PARTIAL_ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED | REFUSED`

The repository verifier can earn `ALIVE` for **repository coherence**. That does not prove the long-horizon crown hypothesis that hand-authored enterprise code can cease to be the durable carrier of enterprise knowledge.

The crown remains an explicit falsifiable research program.

## Verify everything

```bash
make all
```

or individually:

```bash
python3 tools/verify.py --no-receipt
python3 -m unittest discover -s tests -v
mdbook build -d /tmp/aps-book specification-guide
python3 tools/simulate_fortune500.py examples/fortune500-fibo/enterprise.json
```

Promotion evidence must bind to the exact candidate head.

## Archive law

The predecessor Markdown corpus is preserved under `archive/pre-v26.8.24/`. Other predecessor code, generated artifacts, workflows, and receipts remain exactly recoverable from the immutable predecessor commit recorded in `MANIFEST.json`.

Archive material is evidence, never current authority without explicit re-admission.
