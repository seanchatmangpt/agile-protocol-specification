# Formal Semantics and Conformance Calculus

This chapter supplies the mathematical objects and decision functions needed to make APS falsifiable. The notation is intentionally bounded: it states exactly what a receipt or verifier establishes and prevents local evidence from being inflated into universal proof.

## State model

Let an APS world be a labeled directed multigraph:

```text
G = (V, E, τV, τE, α)
```

`V` contains protocol objects. `E` contains typed relations such as `declares`, `supersedes`, `implements`, `verifies`, `refuses`, `authorizes`, `dependsOn`, and `receipts`. `τV` and `τE` assign object and relation types. `α` assigns attributes including content digests, versions, times, authorities, and coordinates.

A work order is not valid merely because its JSON parses. It is admitted when it satisfies structural, semantic, authority, and closure predicates:

```text
Admitted(W) ⇔ Schema(W) ∧ Bounded(W) ∧ Authorized(W)
              ∧ Falsifiable(W) ∧ Verifiable(W) ∧ Closed(W)
```

`Closed(W)` means every identifier required to interpret or execute the work order resolves within the admitted dependency boundary or is explicitly classified as an external prerequisite.

## Observation closure

`O` is necessarily partial. APS therefore makes the admission boundary explicit:

```text
O* = {x ∈ O | admissible(x, policy, coordinate)}
```

The manufacturing function `μ` is lawful only over `O*`:

```text
A = μ(O*)
```

The result `A` is not authoritative until a receipt binds the operation and its consequence:

```text
R ⊢ A = μ(O*)
```

The turnstile is intentionally bounded. `R` does not prove every possible property of `A`; it proves that the recorded operation produced the recorded consequence from the recorded admitted input under the recorded coordinate.

## Delta calculus

Given intended graph `Gi` and observed implementation graph `Go`, APS computes a typed delta:

```text
Δ(Gi, Go) = (M, X, C, U)
```

where:

- `M` is the set of missing required objects or edges;
- `X` is the set of extra forbidden objects or edges;
- `C` is the set of contradictory attributes or relations;
- `U` is the set of unevidenced claims.

The empty delta is necessary but not sufficient for `ALIVE`. Runtime evidence may still be absent. The standing function therefore considers both delta and evidence:

```text
stand(Δ, E, Π) → Standing
```

`Π` is the policy profile. A documentation-only profile may accept structural evidence. A production-actuation profile may require unit, integration, end-to-end, chaos, stress, benchmark, and independent verifier evidence.

## Falsifier semantics

Every normative claim `q` SHALL expose at least one falsifier `f(q)` that operates on the same object and boundary:

```text
f(q) : Observation → {supports, refutes, unknown, unsupported}
```

Adjacency is not refutation. A failing test of a neighboring function does not refute `q`. A successful demonstration of a similar workflow does not support `q`. Same-object verification requires alignment of object identity, input domain, authority, closure, actuation path, and claimed consequence.

## Evidence coordinates

Evidence is a tuple, not an adjective:

```text
κ = ⟨source, revision, tree, toolchain, target, features,
     environment, command, inputDigest, outputDigest, time⟩
```

Every evidence item SHALL bind to `κ`. Evidence without a source revision or input digest is vulnerable to drift. Evidence without a toolchain or target is not portable. Evidence without command and output is difficult to replay. Evidence without a claim identifier cannot be attributed to the object it supports.

## Evidence ladder

APS defines an ordered verification program, not an automatic proof hierarchy:

```text
unit → integration → e2e → chaos → stress → benchmark → verifier report
```

Each rung answers a different question. Unit tests isolate local laws. Integration tests establish composition. End-to-end tests exercise the selected path. Chaos tests challenge fault assumptions. Stress tests locate resource boundaries. Benchmarks characterize cost and latency. An independent verifier report audits the relationship among all prior evidence and the claim.

A policy MAY omit rungs for low-consequence artifacts, but the omission SHALL be explicit. A skipped rung is not a passed rung.

## Transition calculus

Let `L` be lifecycle state and `p` a promotion request. Promotion is lawful only if:

```text
promote(x, L1, L2) ⇔ allowed(L1, L2)
                       ∧ criteria(x, L2)
                       ∧ authority(p, L2)
                       ∧ noBlockingRefusal(x)
```

Allowed transitions are:

```text
Draft       → Provisional | Refused
Provisional → Draft | InReview | Refused
InReview    → Provisional | Accepted | Refused
Accepted    → Final | Superseded
Final       → Superseded
Refused     → Draft(successor only)
```

Direct `Draft → Final` promotion is refused. Reopening an accepted artifact edits a successor, not the accepted object. Content identity changes imply a new digest and therefore a new candidate coordinate.

## Conformance profiles

- **APS-Core:** object identity, lifecycle, work-order schema, falsifier, typed outcome.
- **APS-Evidence:** Core plus evidence coordinates, independent verification, and receipts.
- **APS-Gall-Input:** Evidence plus deterministic checkpoint bindings and repair packet semantics.
- **APS-Actuation-Boundary:** Gall-Input plus broker authority, rollback, replay, and zero-unreceipted-actuation enforcement.

An implementation SHALL state the profile it claims. Claiming “APS compliant” without a profile is incomplete.
