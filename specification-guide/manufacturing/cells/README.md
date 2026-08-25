# APS ggen manufacturing cells

APS uses the ggen ecosystem as a set of specialized manufacturing cells rather than as one monolithic generator.

Each cell has one bounded responsibility, one APS-owned admitted graph, and one marketplace-owned manufacturing law. Exact-head qualification stages the exact marketplace commit, executes the pinned ggen runtime, verifies receipts, and requires deterministic replay.

## Cells

| Cell | Marketplace capital equipment | APS-owned authority | Qualified consequence |
|---|---|---|---|
| `mdbook` | `mdbook-pattern-language-pack` | `../docs/book.ttl` | mdBook identity and navigation projections |
| `consequence` | `consequence-ir-pack` | `consequence/ontology.ttl` | admitted bounded consequence/authority/receipt/replay graph plus admission marker |
| `standing` | `standing-ladder-pack` | `standing/ontology.ttl` | evidentiary promotion audit trail for an APS fact |
| `dfcm` | `dfcm-maximalist-court-pack` | `dfcm/ontology.ttl` | reversible candidate/qualification/SELECT projections |

The cells do not share mutable generated state. Their common datum is the exact ggen release plus exact ggen-marketplace commit recorded in `../ecosystem.lock.json`.

## Semantic fences

APS operational repository standing (`UNKNOWN`, `PARTIAL_ALIVE`, `ALIVE`, `BLOCKED`, `BUILD_BROKEN`, `UNSUPPORTED`) remains distinct from the `standing-ladder-pack` evidentiary ladder (`UNKNOWN` through `VERIFIED`). The latter qualifies the standing of a fact or claim; it does not replace repository-operational state.

A consequence-IR `DO` instance in the qualification cell represents only bounded CI-local filesystem manufacture under explicit authority. It grants no production actuation authority.

The DfCM cell manufactures a candidate court. Its SELECT projection is evidence for a selection opportunity, not an authorization to actuate a selected option.

## Manufacturing law

```text
APS admitted facts
      ↓
exact marketplace pack
      ↓
pinned ggen runtime
      ↓
generated projection
      ↓
ggen receipt verification
      ↓
second manufacture
      ↓
byte-identical fixed point
      ↓
independent APS court
```

This is a deeper form of ggen-first: reusable law stays in the marketplace, APS carries only its domain facts and the thin binding needed to place them in a manufacturing cell.
