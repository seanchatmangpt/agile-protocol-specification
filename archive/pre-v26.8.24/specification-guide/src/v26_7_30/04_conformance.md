# Conformance, Verification, Receipts, and Replay

Conformance is a repeatable decision over named objects, not a stylistic judgment. This chapter defines how validators, evidence ladders, negative fixtures, receipts, and replay constrain what may be reported as ALIVE.

## Conformance is executable

A specification that cannot distinguish conforming from nonconforming artifacts is explanatory literature, not an operational standard. APS therefore requires every claimed profile to expose a deterministic validator and a finite set of positive and negative fixtures.

## Validator contract

A validator SHALL:

- identify the exact APS profile and schema versions;
- validate syntax before semantics;
- resolve referenced identifiers and dependencies;
- emit typed diagnostics with object paths;
- preserve all failures rather than stop at the first convenient error unless configured for fail-fast operation;
- distinguish `UNKNOWN` from `UNSUPPORTED`;
- produce a machine-readable report and a human-readable summary;
- hash the validated inputs and report content;
- exit nonzero for refused conformance.

## Receipt model

A receipt binds a consequence cell:

```text
Γ = ⟨attempt, authority, admittedInput, operation, output,
     evidence, standing, lineage, replayContract⟩
```

At minimum, a receipt contains:

```json
{
  "schema": "aps.receipt.v26.7.30",
  "operation_id": "aps-book-verify",
  "subject": "sha256:...",
  "coordinate": {"revision": "...", "command": "..."},
  "standing": "ALIVE",
  "evidence": [{"kind": "structure", "digest": "sha256:..."}],
  "nonclaims": ["mdBook rendering not observed when mdbook is unavailable"]
}
```

A conventional log line cannot substitute because it usually lacks subject identity, authority, policy, standing, and replay obligations.

## Replay

Replay answers whether the recorded operation still produces the recorded observation under the same or an explicitly translated coordinate.

```text
replay(R, κ2) → {MATCH, DIVERGED, UNSUPPORTED, UNKNOWN}
```

A divergence does not automatically prove the original receipt fraudulent. The toolchain, source tree, dependency graph, clock, random seed, external service, or policy may have changed. The replay report SHALL identify the first divergent coordinate component it can observe.

## Mutation and negative fixtures

Positive tests demonstrate that an admitted path can succeed. Negative fixtures demonstrate that forbidden paths are refused. Mutation adequacy challenges whether the verifier would detect a meaningful corruption.

For a claim set `Q` and mutant set `M`:

```text
mutation_score = killed(M) / |M|
```

The score is interpretable only when mutants correspond to declared laws. Thousands of trivial mutants do not compensate for leaving the authority bypass, receipt omission, or scope widening mutant alive.

## Book verifier profile

The v26.7.30 book validator checks:

- every SUMMARY link resolves;
- every chapter has substantive body and one top-level title;
- required constitutional distinctions occur in the admitted corpus;
- JSON schemas parse;
- duplicate boilerplate stays below a bounded threshold;
- no generated `book/` output appears in the source manifest;
- a deterministic receipt records chapter count, word count, file digests, and standing.

Because `mdbook` is not guaranteed to be installed in every verifier environment, rendering is a separate capability. Lack of `mdbook` SHALL be reported as `UNSUPPORTED`, never silently counted as a successful build.

## Independent review consequence

A verifier report SHALL name both the claims it supports and the questions it did not test. Review completion is not universal endorsement. Where reviewers disagree, APS preserves the competing observations, identifies the shared object coordinate, and routes the unresolved difference into a repair or authority decision rather than averaging incompatible conclusions.

## Release gate

The release gate is conjunctive:

```text
ReleaseReady ⇔ StructureAlive ∧ SchemaAlive ∧ InvariantsAlive
               ∧ ReceiptAlive ∧ noBlockingRefusal
```

Rendering and link crawling MAY be additional required conjuncts in CI. A local release can be `PARTIAL_ALIVE` when structural verification succeeds but the rendering tool is unavailable. It becomes `ALIVE` for the full release profile only after the declared full verifier ladder closes.
