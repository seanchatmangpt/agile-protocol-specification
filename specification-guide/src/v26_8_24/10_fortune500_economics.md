# Fortune-500 Economics and the End of Enterprise Code as Capital

The economic comparison is not human lines-of-code per day versus machine lines-of-code per day. It is human enterprise-change lifecycle cost versus machine-manufactured qualified enterprise state.

## Human lifecycle cost

Humans do not merely author implementation. A conventional enterprise change can require separate effort for:

- requirements translation;
- architecture;
- implementation;
- peer review;
- data/schema work;
- integration;
- testing;
- security/compliance;
- deployment;
- change management;
- observability;
- documentation;
- audit evidence;
- rollback planning;
- coordination and queue time.

The cost grows approximately with the number of concepts, projections, target systems, environments, and candidate architectures that humans must independently translate and reconcile.

```text
human_cost ~ concepts * projections * variants * candidates * lifecycle_work
```

Humans therefore prune design space early. Sunk cost begins determining architecture because exploring another complete candidate is expensive.

## DfCM moves combinatorics into compute

Machine manufacture changes the cost structure:

```text
human effort ~ novel knowledge + exceptions + governance
machine effort ~ manufactured consequences + qualification compute
```

This is the economic precondition for DfCM. Candidate breadth can increase dramatically without multiplying human teams at the same rate.

## FIBO-based enterprise example

Consider a financial Fortune-500 enterprise using FIBO plus enterprise-specific facts, operational profiles, mappings, and policy as semantic authority.

One admitted concept family may lawfully project into many surfaces:

- Ash resources/actions/policies;
- relational tables, constraints, and migration inputs;
- R2RML semantic mappings;
- JSON/GraphQL/API schemas;
- CLI/MCP capability schemas;
- SaaS and internal-system bindings;
- deployment and environment manifests;
- tests and falsifiers;
- OCEL/provenance instrumentation;
- documentation and catalog entries.

The relevant metric is the **manufacturing multiplier**:

```text
M = lawful qualified downstream consequences / admitted upstream knowledge
```

Large code volume may be a side effect of high `M`; it is not itself the objective.

## Enterprise code becomes inventory

Most enterprise source code is translation among representations rather than novel computation.

When those translations are projections from common authority:

```text
semantic contract -> resource -> persistence -> API -> policy -> deployment -> evidence
```

hand-authored enterprise code loses its role as the durable carrier of enterprise knowledge.

Executable instructions do not disappear. Their accounting status changes:

```text
enterprise code = current inventory / materialization
semantic + manufacturing knowledge = durable capital
```

## Three future classes of code

APS distinguishes:

1. **Irreducible mechanism** — genuinely novel algorithms, runtimes, drivers, cryptography, schedulers, protocol machinery, and similar reusable mechanism.
2. **Generated projection** — anything lawfully derivable from admitted contracts and known manufacturing patterns.
3. **Legacy executable awaiting absorption** — an incumbent whose observable contract can be wrapped, measured, reconstituted, and eventually replaced if a successor earns standing.

## Daily-build enterprise

The asymptotic target is an enterprise whose software estate can be treated as a reproducible build of current admitted knowledge:

```text
O*_t -> mu_t -> A_t -> qualification -> execution evidence
O*_(t+1) -> mu_(t+1) -> A_(t+1) -> qualification -> execution evidence
```

Yesterday's estate becomes sunk at the next decision boundary. What persists is semantic authority, contracts, evidence, and reusable manufacturing capability.

## Knowledge leverage metric

A primary productivity measure becomes:

```text
Knowledge Leverage = qualified consequences produced / novel human decisions required
```

A related enterprise remanufacture metric is:

```text
Enterprise Remanufacture Ratio = qualified enterprise surface manufactured per period / novel knowledge admitted per period
```

These metrics better describe the phase change than commits, LOC, or developer velocity.

## Why incumbent adoption is structurally difficult

The people most qualified by the incumbent production system to evaluate the successor may also possess human and organizational capital whose value the successor depreciates.

The system therefore should not depend on persuasion. It must make adoption increasingly an evidence question:

```text
does the qualified successor dominate the incumbent process on admitted objectives and constraints?
```

The old system's resistance becomes evolutionary pressure on the successor's safety, accountability, evidence, and fitness.
