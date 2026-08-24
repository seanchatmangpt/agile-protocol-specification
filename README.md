# Agile Protocol Specification v26.8.24

APS is an executable constitution for **knowledge-work reconstitution and autonomic manufacturing**.

> **Chatman's Law:** historical production cost confers no preservation privilege. Durable value migrates toward the recoverable knowledge, contracts, evidence, and manufacturing capability needed to reproduce or improve useful consequences.

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

The active repository was rebuilt as a successor authority system, not as a documentation book around predecessor machinery.

```text
MANIFEST.json                         authority map
.aps-syntax.md                        compact protocol syntax
ontology/                             RDF/public-ontology profiles + SHACL
tools/requirements-ci.txt             pinned semantic qualification stack
contracts/                            executable contract/evidence JSON Schemas
specification-guide/src/v26_8_24/     normative manuscript
examples/fortune500-fibo/             synthetic enterprise contract/reconstitution case
simulation/                           executable sensitivity scenario
tools/                                semantic/schema court + deterministic model
tests/                                repository/simulation qualification
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

## Rice's Theorem is the epistemic boundary

No general algorithm—including an LLM-based reviewer—can decide every nontrivial semantic property of arbitrary programs under the standard assumptions of Rice's Theorem.

APS therefore does not make “inspect arbitrary source harder” its terminal epistemology. It moves meaning upstream into admitted semantics and executable contracts, constrains manufacturing to qualified patterns, observes real consequence, manufactures adversarial falsifiers, and records bounded standing with residual unknowns.

The goal is not omniscience about arbitrary code. It is a production system whose important semantic commitments do not need to be reverse-engineered from arbitrary code each time.

## Five-level × seven-dimension jig model

```text
L1 Craft -> L2 Template -> L3 Fixture -> L4 Jig -> L5 Closed-Loop Manufacturing System
```

The seven dimensions are product knowledge, work positioning, operation guidance, process sequence, error prevention, measurement & qualification, and adaptation & learning.

Maturity is a vector, not a comforting average. A sophisticated engine can still depend on craft knowledge in one dimension.

The industrial lineage extends through metrology, machine tools, flexible manufacturing, jidoka, poka-yoke, and closed-loop production. The historical pattern is the relocation of production knowledge from worker memory into inspectable, reusable manufacturing capital.

## Reference manufacturing stack

The current ecosystem is treated as a set of replaceable reference roles, not permanent authority:

- `ggen-spec-kit` — intent-to-semantics/admission;
- `ggen-marketplace` — accumulated executable knowledge;
- `ggen` — deterministic manufacturing kernel;
- `ggen-create` — inductive/inverse manufacturing;
- `ggen-legacy` — observation, reconstitution, assurance, sunset;
- `clap-noun-verb` — typed interaction calculus;
- `ggen-mcp` — bounded protocol transport;
- `ash_r2rml` — semantic-operational closure;
- `XaaS` — enterprise platform projection;
- `AutoFDE Lab` — SELECT-side planning/search;
- `GymAct` — governed falsification/world execution;
- `ex4pm` — process execution/evidence reference boundary.

Every named implementation remains sunk when a superior qualified successor can reconstitute its useful truth.

## Synthetic FIBO Fortune-500 experiment

`ontology/fortune500-fibo-profile.ttl` and `examples/fortune500-fibo/` define a **synthetic** financial-enterprise case using FIBO Legal Persons as a public semantic substrate.

The deterministic sensitivity model asks what happens when admitted enterprise capabilities project across many interfaces, environments, and DfCM architecture candidates. Its human comparison includes requirements/architecture, implementation, review/verification, security/compliance, deployment/operations, documentation/audit, and coordination—not code authoring alone.

Board-level governance compression is modeled as validation of bounded source classes—ontology/profile, manufacturing patterns, authority policy, verifier law—rather than manual inspection of every manufactured artifact. “Validate once” always means a versioned scoped admission, never permanent approval.

The model is intentionally not empirical evidence about a real company.

## Full process intelligence

Artifact correctness is insufficient. Consequential activity must emit comparable object-centric and provenance evidence so the enterprise can analyze conformance, variants, bottlenecks, authority exceptions, rework, failure propagation, economic performance, and **process fitness**.

A perfectly conformant unsafe process is still unsafe.

## Software manufacturing as capital

The factory accumulates reusable ontology profiles, contracts, templates, jigs, generator compositions, verifiers, authority policies, process mappings, and reconstitution knowledge.

Code that can be reproduced from those sources increasingly behaves like **inventory**. The durable asset is the knowledge required to remanufacture it.

The target is maximum **qualified manufacture**, not minimum files, minimum commits, or meaningless volume.

## Adversarial pressure is a manufacturing input

Resistance and criticism are not merely adoption friction. A critic with a different loss function can discover failure states the constructor never searched.

```text
objection -> candidate falsifier -> explicit failure state -> evidence -> new requirement or admitted limit
```

Liability, authority attribution, long-horizon reconstruction, unsafe-but-conformant processes, artifact-scale governance, replay, and model/session disappearance become reusable qualification requirements when evidence admits them.

## Executed machine-readable qualification

The repository verifier does more than inspect filenames. It:

- parses every active Turtle graph with RDFLib;
- meta-validates and executes the SHACL profile with pySHACL against the synthetic FIBO graph;
- validates every JSON Schema under Draft 2020-12;
- validates synthetic contract, reconstitution, and process-event instances;
- enforces the exact active source tree and absence of predecessor authority outside `archive/`;
- verifies the exact five-level × seven-dimension jig;
- checks constitutional/ggen/Rice/reference-stack doctrine;
- builds the active mdBook and executes the synthetic sensitivity model in exact-head CI.

Pinned qualification dependencies are in `tools/requirements-ci.txt`.

## Standing and claim discipline

`ALIVE | PARTIAL_ALIVE | BLOCKED | BUILD_BROKEN | UNKNOWN | UNSUPPORTED | REFUSED`

The repository court can earn `ALIVE` for **repository coherence and executable semantic/schema conformance**. That does not prove the long-horizon crown hypothesis that hand-authored enterprise code can cease to be the durable carrier of enterprise knowledge.

The crown remains an explicit falsifiable research program.

## Verify everything

Fresh environment:

```bash
make all
```

Or explicitly:

```bash
python3 -m pip install --disable-pip-version-check -r tools/requirements-ci.txt
python3 tools/verify.py --no-receipt
python3 -m unittest discover -s tests -v
mdbook build -d /tmp/aps-book specification-guide
python3 tools/simulate_fortune500.py examples/fortune500-fibo/enterprise.json
```

Promotion evidence must bind to the exact candidate head.

## Archive law

The predecessor Markdown corpus is preserved under `archive/pre-v26.8.24/`. Other predecessor code, generated artifacts, workflows, and receipts remain exactly recoverable from the immutable predecessor commit recorded in `MANIFEST.json`.

Archive material is evidence, never current authority without explicit re-admission.
