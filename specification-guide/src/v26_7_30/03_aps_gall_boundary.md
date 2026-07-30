# APS–Gall Boundary and Deterministic Work Orders

This boundary is the operational center of v26.7.30. APS manufactures admitted work orders; Gall executes and observes checkpoints. Preserving that separation prevents plans from impersonating consequences and implementation agents from granting themselves standing.

## Preservation of the boundary

APS and Gall solve adjacent but non-equivalent problems.

```text
APS  : intent → admitted work order
Gall : admitted work order → checkpoint observation → standing → receipt
```

APS specifies what must be attempted and what evidence would count. Gall determines whether the attempt crossed a checkpoint. APS may name a Gall checkpoint, its dependencies, verifier command, expected receipt class, and falsifier. APS MUST NOT predeclare that the checkpoint is `ALIVE`.

## SELECT and DO

The planner owns `SELECT`: choosing a bounded target, resolving dependencies, admitting exclusions, and constructing the work order. The coding or execution agent owns bounded `DO`: applying only the selected delta. Gall owns the checkpoint observation and standing assignment.

```text
SELECT(W) ≠ DO(W) ≠ VERIFY(W) ≠ PROMOTE(W)
```

A single runtime may implement multiple roles, but role transitions SHALL be explicit and receipted. Hidden role collapse is self-certification.

## Work-order normal form

A deterministic APS work order SHALL contain:

1. stable work-order and release identifiers;
2. source and exact base coordinate;
3. target consequence and bounded scope;
4. admitted observations and unresolved prerequisites;
5. required and forbidden deltas;
6. authority and role assignments;
7. acceptance commands and expected observations;
8. same-object falsifiers and negative fixtures;
9. evidence ladder and standing ceiling;
10. rollback, quarantine, or repair behavior;
11. Gall checkpoint identifiers and predecessor relations;
12. expected receipt and replay requirements;
13. explicit exclusions and nonclaims.

A ticket that says “implement feature X” is not in normal form. It lacks enough law to distinguish successful implementation, adjacent implementation, partial completion, unsupported verification, and scope drift.

## Determinism criterion

A ticket is deterministic when two competent executors, starting from the same admitted coordinate, can identify the same permitted change set and the same acceptance boundary without negotiating hidden requirements.

This does not require a single implementation. APS permits reversible construction and multiple lawful candidates. It requires that candidate diversity remain inside declared constraints and that every candidate face the same falsifiers.

## Gall checkpoint binding

```toml
[[gall.checkpoints]]
id = "APS-GALL-004"
predecessors = ["APS-GALL-003"]
claim = "work-order schema rejects unbounded scope"
standing_ceiling = "ALIVE"

[[gall.checkpoints.verification]]
kind = "unit"
command = "python3 specification-guide/scripts/verify_v26_7_30.py"
expected = "ALIVE"

[[gall.checkpoints.falsifiers]]
id = "unbounded-scope-accepted"
fixture = "fixtures/work_order_unbounded.json"
expected_refusal = "SCOPE_BOUNDARY_MISSING"
```

The checkpoint binding is a declaration. The resulting receipt belongs to Gall or the executing verifier. APS stores the expected shape and later links the observed receipt.

## Repair packets

A failed checkpoint SHALL produce a repair packet that preserves the original work order and identifies the smallest typed delta:

```yaml
work_order: aps-v26.7.30-book
checkpoint: APS-GALL-004
standing: BLOCKED
observed_delta: REQUIRED_FALSIFIER_MISSING
expected: every normative claim has a same-object falsifier
observed: claim aps.ticket.authority has no falsifier
required_repair: add a negative fixture and bind it to the claim
nonclaims:
  - no assertion that other checkpoints failed
```

Repair is a successor transformation. It does not rewrite the failed receipt or erase the candidate that produced it.

## Jira and GitHub projections

APS work orders MAY project into Jira, GitHub Issues, Linear, or another tracker. The tracker object is a view. Canonical fields SHOULD be preserved in structured metadata, issue forms, front matter, or linked artifacts. Tracker status labels such as “Done” SHALL NOT override APS lifecycle or Gall standing.

## Work-order falsifiers

A work order is refused when any of the following holds:

- the base coordinate cannot be resolved;
- scope contains open-ended verbs without a closure condition;
- acceptance references commands that do not exist and no unsupported path is declared;
- the same actor is producer and sole final verifier;
- a required Gall predecessor is absent;
- rollback or refusal behavior is missing for consequential actuation;
- exclusions are implicit;
- success can be claimed without a receipt.
