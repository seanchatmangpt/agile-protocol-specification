# Source Admission and Edition Scope

**Edition:** APS v26.7.30  
**Release coordinate:** 2026-07-30  
**Status:** normative candidate  
**Primary author:** Sean Chatman

APS v26.7.30 begins by refusing a common failure in AI-assisted specification work: treating every available sentence as if it had equal authority. The repository contains a table of contents, generated HTML, AI-assistant doctrine, historical conversations, enterprise-architecture notes, an empty syntax file, and a prior complete manuscript. Those objects are evidence of different kinds. They cannot lawfully be merged until their provenance, purpose, and authority are classified.

## The admitted corpus

The edition admits five source classes:

1. **Repository doctrine.** `CLAUDE.md`, the root README, module context files, and build instructions define the current repository fence. They control file placement, mutable versus immutable states, generated-output boundaries, and the mdBook build path.
2. **Current structural truth.** `specification-guide/src/SUMMARY.md` defines the inherited topic taxonomy. The generated search index and print edition demonstrate that the prior source chapters had headings but no body. The taxonomy is preserved; the emptiness is not.
3. **Historical design record.** `.service-colony.md`, `CUSTOM-GPT-CONTEXT.md`, planning conversations, and related archives preserve the evolution of APS from a Gherkin-like process notation toward a machine-readable operating constitution. They are informative evidence, not self-executing law.
4. **Prior complete manuscript.** `APS_2030_Complete_Manuscript.md` contributes the constitutional distinctions among intent, implementation, evidence, standing, falsifiers, receipts, and independent verification. Its repeated boilerplate is not imported as depth. Its propositions are normalized into this edition.
5. **External standards.** BCP 14 terminology, PROV-O, DCAT, SHACL, ODRL, BPMN, C4, OCEL 2.0, SLSA, and TOGAF are referenced only for the concerns they actually standardize. Reference does not imply equivalence or certification.

## Admission function

Let the observed corpus be `O`. APS does not manufacture the edition directly from `O`; it first constructs an admitted observation `O*`.

```text
O* = admit(O, authority, provenance, relevance, consistency, boundary)
A  = μ(O*)
R  = receipt(A)
```

`admit` is not summarization. It is a typed partition:

```text
admit(x) ∈ {NORMATIVE, INFORMATIVE, HISTORICAL, GENERATED, REFUSED, UNKNOWN}
```

A source is **NORMATIVE** only when it has explicit authority for the current coordinate. An **INFORMATIVE** source may explain a decision without authorizing it. A **HISTORICAL** source preserves lineage. A **GENERATED** source is a projection and must not be hand-edited as canonical input. A **REFUSED** source contradicts an admitted invariant or falls outside scope. **UNKNOWN** means authority or meaning has not been established; it is not permission to use the source silently.

## What APS is

APS is a protocol for turning human and machine intent into bounded, reviewable, machine-readable work orders. It defines the declarations that must exist before downstream work receives standing: scope, owner, target state, admitted inputs, exclusions, acceptance checks, falsifiers, evidence requirements, authority, and expected receipts.

APS is not another sprint ceremony. It can be projected into Scrum, Kanban, SAFe, Jira, GitHub Issues, BPMN, Gantt, C4, PDDL, or other planning and representation systems. None of those projections exhausts the APS object. The same admitted work order may produce many views; no single view becomes the canonical law unless explicitly designated.

## What APS is not

APS does not execute Gall checkpoints. It does not prove that implementation happened. It does not convert an author’s confidence into standing. It does not grant an AI agent unrestricted authority. It does not treat a commit, test, review, or receipt as universal proof.

APS owns the **input model** and the **declaration boundary**. Gall owns checkpoint execution and the observation of whether the declared consequence became real. This distinction is constitutional and is formalized later in this book.

## Normative language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are interpreted as BCP 14 terms only when written in uppercase. A requirement without an object, boundary, verifier, or failure consequence is not enforceable enough to receive normative standing.

## Edition falsifier

The claim that v26.7.30 completes the APS book is falsified by any of the following at the release coordinate:

- a linked chapter is missing or heading-only;
- the APS/Gall ownership boundary is ambiguous;
- no machine-readable work-order schema exists;
- acceptance can be asserted without a falsifier or evidence coordinate;
- a failed or unsupported verifier is reported as success;
- generated mdBook output is treated as the source of truth;
- the book cannot be deterministically checked for structure and required invariants.

This edition therefore ships with schemas, a verifier, and a verifier receipt. The book is an admitted candidate only at the exact content digests recorded by that receipt.
