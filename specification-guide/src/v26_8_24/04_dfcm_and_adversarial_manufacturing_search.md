# DfCM and Adversarial Manufacturing Search

Design for Combinatorial Maximalism (DfCM) treats early commitment as a cost. The manufacturing system should preserve and construct the largest lawful candidate space that can be qualified economically before irreversible selection.

## Design the contract, not the code

The primary design object is an executable contract graph describing:

- semantics;
- preconditions;
- postconditions;
- invariants;
- refusals;
- authority requirements;
- identity;
- cardinality;
- idempotency;
- evidence requirements;
- resource bounds;
- compatibility;
- standing rules.

Implementation and verification are sibling consequences of authority:

```text
admitted contract
  -> candidate implementation(s)
  -> independent falsifier(s)
  -> qualification evidence
```

Tests must not silently become the sole specification merely because they execute.

## Known pattern before novel mechanism

The default manufacturing search order is:

1. existing reusable manufacturing pattern;
2. composition of known patterns;
3. existing specialized generator or tool, driven by generated inputs/invocation;
4. generated script/workflow that composes known tools;
5. repo-specific parameterization of known law;
6. only then a genuinely novel mechanism.

A unique requirement does not imply unique implementation. Many 'one-offs' decompose into known state, policy, transaction, authority, identity, retry, workflow, receipt, or integration patterns.

## Novelty becomes tomorrow's capital

A novel mechanism is not granted permanent exceptional status.

```text
Novel_t
  -> successful observation
  -> extracted contract/pattern
  -> independent qualification
  -> marketplace/capability admission
  -> KnownPattern_(t+1)
```

The ecosystem should pay the cost of discovering a generalizable solution once and then manufacture it repeatedly.

## Adversarial DfCM

DfCM must search not only implementations but failure space.

Let:

```text
M = {mu_1, mu_2, ..., mu_n}       candidate manufacturing strategies
F = {f_1, f_2, ..., f_m}          candidate adversarial failure conditions
```

Qualification asks whether candidate strategies survive the admitted falsifier set rather than whether the constructor can tell a persuasive success story.

An adversary wins by discovering a plausible state in which the system's claimed standing is false.

```text
claim C + failure condition f -> not(C)
```

A discovered adversarial win condition becomes a candidate requirement only after it is made explicit and tested. Criticism is not automatically truth; it is a source of unexplored state space.

## Adversarial requirements generation

A high-value adversary often has a different objective function than the constructor. This makes the adversary useful precisely when they do not share the constructor's decomposition.

Examples of adversarial questions that change architecture rather than implementation include:

- What if the system causes catastrophic harm?
- Who possessed authority for the consequence?
- Can the decision be reconstructed years later?
- What if the process conformed exactly but the process itself was unsafe?
- What if artifact volume exceeds any human review capacity?
- What if the model/session disappears?
- What if the same input is replayed and produces materially different consequence?

These questions imply requirements such as attributable authority, independent evidence, process fitness, governance compression, replay, refusal, and liability-defensible provenance.

## Red Queen discipline

The architecture should expect criticism to migrate as lower-level objections are solved:

```text
can it generate?
 -> is it correct?
 -> is verification independent?
 -> who authorized execution?
 -> is the authorized process fit?
 -> who is accountable?
 -> can the evidence survive litigation/regulation/time?
```

The goal is not to silence adversaries. It is to convert plausible attacks into falsifiers until novel attack classes become increasingly expensive to discover.

## Governance cost must not scale with artifact count

Machine manufacture can produce artifact volume beyond human inspection capacity. Therefore:

```text
governance_cost !~ artifact_count
```

Governance must increasingly qualify source, contracts, manufacturing law, policy, and verifier law, then require each consequence to prove derivation from the admitted chain.
