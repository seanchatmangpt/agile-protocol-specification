# Rice's Theorem and Epistemic Boundaries

APS treats Rice's Theorem as a foundational warning for the LLM and agentic-software era.

Under the standard computability assumptions, no general algorithm can decide every nontrivial semantic property of arbitrary programs. The theorem does **not** say useful program properties can never be established. It says the universal problem is not solvable merely by adding a smarter reviewer, a larger model, or a more elaborate static analyzer.

## Why this matters to machine manufacture

A production system that accepts arbitrary source and asks an intelligence to determine every consequential semantic property is built on the wrong epistemic object.

```text
arbitrary implementation
  -> inspect harder
  -> infer intended semantics
  -> decide whether every important behavior is safe/correct
```

cannot become a universal proof method.

APS shifts the problem upstream:

```text
admitted semantics + executable contract
  -> bounded manufacturing law
  -> constrained realization
  -> independent observation/falsification
  -> bounded standing
```

The objective is not omniscience about arbitrary code. It is to manufacture within domains where the relevant claims are explicit enough to constrain, measure, falsify, and replay.

## LLM reasoning does not repeal undecidability

A model may infer intent, discover bugs, synthesize proofs for bounded cases, construct tests, and produce strong probabilistic judgments. None of that grants a general decision procedure for arbitrary nontrivial program semantics.

Therefore:

- model confidence is not standing;
- code inspection is not equivalent to execution evidence;
- persuasive explanation is not proof;
- passing tests do not establish every semantic property;
- a generated artifact cannot certify itself merely because the generator understands its own construction story.

## Manufacture changes the epistemic geometry

Generation is valuable not only because it reduces labor. It can restrict the implementation space.

If a qualified manufacturing pattern has known contracts, permitted transformations, typed refusals, authority law, evidence obligations, and independent falsifiers, then each manufactured artifact begins inside a narrower semantic envelope than arbitrary handwritten source.

This is the same industrial move made by a jig: remove degrees of freedom that need not remain free.

```text
more unconstrained implementation freedom
  -> harder semantic inference problem

more admitted contract + qualified manufacturing constraint
  -> smaller lawful behavior space
  -> stronger bounded verification
```

DfCM still maximizes **candidate designs**, but each candidate must remain inside admitted law. Combinatorial breadth and behavioral law are compatible.

## Reconstitution does not require total understanding

A successor does not need a magical proof that it has understood every property of a predecessor. It needs a bounded claim about the properties that matter to the intended transition.

Reconstitution therefore records:

- observed behavior;
- known obligations;
- recovered contracts;
- explicit unknowns;
- unsupported properties;
- adversarial falsifiers;
- prospective sunset risk.

If a required semantic property cannot be recovered or independently qualified, the correct standing remains `UNKNOWN`, `UNSUPPORTED`, `PARTIAL_ALIVE`, or `REFUSED` depending on the boundary.

## Public semantics reduce reverse inference

When enterprise meaning is encoded only in implementation, each new tool must infer meaning from accidental code structure. Public ontologies and explicit enterprise profiles move more of that meaning into a durable, inspectable layer before implementation.

The advantage is not that RDF or OWL makes arbitrary software decidable. The advantage is that important semantic commitments stop needing to be rediscovered from arbitrary software at all.

## The epistemic law

APS therefore adopts:

> **Do not attempt to solve arbitrary program meaning after implementation when the relevant meaning can be admitted before manufacture.**

This is why contract-first, ggen-first manufacture, typed refusal, bounded authority, independent verification, process evidence, and explicit residual unknowns are one system rather than unrelated practices.
