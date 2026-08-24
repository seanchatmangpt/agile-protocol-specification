# Contract First, ggen First

APS does not treat code as the primary design object. It treats admitted semantic and behavioral contract as the design object from which implementations, tests, tool invocations, documentation, and evidence surfaces can be manufactured.

## The Chatman Equation

```text
A = mu(O*)
```

`O*` is admitted knowledge, `mu` is lawful manufacture, and `A` is a consequence with only the standing justified by evidence.

For design by contract:

```text
Intent
  -> public semantics + enterprise facts
  -> executable contract
  -> manufacturing graph
  -> candidate implementation(s)
  -> independent verifier(s)
```

Implementation and verification are siblings derived from common authority. Tests do not silently become the sole specification, and implementation does not get to define its own correctness after the fact.

## Contract before implementation

The contract graph should express, where relevant:

- semantic subjects and identity;
- preconditions;
- postconditions;
- invariants;
- refusals;
- authority requirements;
- cardinality and data constraints;
- idempotency and replay law;
- evidence obligations;
- resource bounds;
- compatibility;
- standing transitions.

Different implementations can compete while satisfying the same admitted contract. That preserves DfCM option space.

## ggen first

The decision is not `generated versus handwritten`.

The decision law is:

**Known pattern? Compose it.**

**Known tool? Generate its invocation.**

**Novel mechanism? Discover it once, then teach the factory.**

More completely:

1. if an admitted reusable manufacturing pattern exists, compose it;
2. if a specialized generator/tool is superior, manufacture its declarations, configuration, inputs, and invocation;
3. if the solution is a known sequence of tools, manufacture the script/workflow;
4. if the difference is repository-specific, express it as facts, constraints, or parameters;
5. only then author genuinely irreducible new runtime mechanism;
6. after successful qualification, extract generalizable novelty into reusable manufacturing knowledge.

## Downstream generators are capital equipment

A native generator is not an alternative to the upstream manufacturing layer.

```text
ontology / admitted knowledge
        -> ggen-like manufacture
        -> generator declarations + invocation
        -> specialized generator
        -> artifact
```

This applies to framework generators, database migration tools, compilers, package managers, infrastructure engines, deployment systems, CLIs, and external executables.

The upstream factory need not reimplement every machine tool. It must know how to configure, constrain, invoke, and qualify it.

## CLI invocations and scripts are manufactured software

A command line is an executable projection of manufacturing intent:

```text
CLI Invocation = mu(O*)
```

So are scripts, workflow files, migration plans, build manifests, test plans, queries, deployment commands, and receipt policies. Treating those as handwritten glue preserves artisan work unnecessarily.

## Applications and libraries

Applications contain large amounts of composition and projection:

```text
Application = mu(O*, reusable capabilities)
```

Their architecture, resource declarations, policies, interfaces, persistence projections, integrations, deployment topology, tests, observability, documentation, and evidence surfaces should therefore carry a strong presumption of manufacture.

Libraries contain more irreducible mechanism but still decompose:

```text
Library = Generated Surface + Irreducible Mechanism
```

Public API, types, feature declarations, adapters, schemas, errors, tests, docs, examples, packaging, bindings, and conformance surfaces may remain manufacturable even when the core algorithm is novel.

## One-off is a decomposition failure until proven otherwise

A unique business requirement often decomposes into known primitives:

- state machine;
- policy;
- authorization;
- transaction;
- receipt;
- idempotency;
- retry;
- circuit breaker;
- event/outbox;
- workflow;
- schema mapping;
- external binding.

Uniqueness frequently lies in composition and parameters, not mechanism.

## Marketplace as accumulated executable knowledge

The reusable knowledge base should accumulate at multiple scales:

- primitive manufacturing capabilities;
- technology patterns;
- architectural patterns;
- qualified solution compositions;
- independent verifier patterns;
- adversarial falsifier packs.

The compounding law is:

```text
Novel_t
  -> observed success/failure
  -> extracted contract
  -> independent qualification
  -> reusable pattern admission
  -> KnownPattern_(t+1)
```

Today's one-off becomes tomorrow's manufacturing primitive.

## Burden of proof for manual authorship

Hand authorship is the residual category. It should be justified by one or more of:

- no admitted known pattern exists;
- no composition of known patterns closes the contract;
- no existing specialized tool can perform the transformation;
- the factory cannot yet manufacture the tool's lawful input/invocation;
- genuinely novel runtime semantics or algorithmic mechanism is required.

Even then, the exceptional mechanism should be surrounded by manufactured contracts, tests, evidence, integration, and documentation and should become a candidate reusable pattern after qualification.
