# CLAUDE.md — APS v26.8.24

`AGENTS.md` is the general repository constitution. This file adds Claude-specific execution guidance.

## Start here

1. Read `MANIFEST.json`.
2. Read `.aps-syntax.md`.
3. Read `specification-guide/src/SUMMARY.md` and relevant active chapters.
4. Treat `archive/` as evidence only.
5. Run `python3 tools/verify.py --no-receipt` before and after structural changes.

## Do not preserve sunk structure by default

The correct question is not “how do I modify this file?” but “what truth does this file carry, and what should the successor manufacturing system look like if the incumbent implementation has no preservation privilege?”

Recover required truth before removing an incumbent. Reconstitute rather than cosmetically modernize when the object model has changed.

## Manufacturing behavior

Prefer public ontology + bounded local profile + executable contract + generated/manufactured consequence. Prefer reusable manufacturing patterns and generated tool invocations over handwritten glue. Use handwritten code only for irreducible mechanism or bootstrap boundaries that cannot yet be lawfully manufactured, and make the reason explicit.

Maximize lawful reversible candidate space with DfCM. Do not interpret “good engineering” as automatically minimizing files, commits, variants, or candidate implementations.

## Claim discipline

A passing structural verifier proves only structural conformance. The synthetic Fortune-500 model proves only deterministic arithmetic over declared assumptions. Neither proves the long-horizon enterprise crown hypothesis.

Use the narrowest evidence-earned standing.
