# APS ggen manufacturing factory

This directory makes APS a real multi-cell consumer of the ggen ecosystem. APS owns admitted domain facts; ggen-marketplace owns reusable manufacturing law; ggen owns deterministic execution and receipts.

## Common datum

`ecosystem.lock.json` pins one exact ggen release and one exact ggen-marketplace commit. It additionally records the Git blob identities of the critical manifests, ontologies, gates, queries, and templates executed by APS.

The current cells are:

1. **mdBook control surface** — `mdbook-pattern-language-pack` consumes `docs/book.ttl` and manufactures book identity/navigation projections.
2. **Consequence IR** — `consequence-ir-pack` consumes `cells/consequence/ontology.ttl` and applies fail-closed consequence, authority, receipt, replay, and promotion laws.
3. **Evidentiary standing** — `standing-ladder-pack` consumes `cells/standing/ontology.ttl` and refuses skipped or unevidenced promotion rungs.
4. **DfCM option court** — `dfcm-maximalist-court-pack` consumes `cells/dfcm/ontology.ttl` and manufactures candidate, qualification, and SELECT projections while preserving non-selected options.

`cells/README.md` defines their semantic fences. In particular, APS repository-operational standing is not the standing-ladder evidentiary state machine; a CI-local consequence is not production authority; and SELECT is not DO.

## Generated inventory

The committed `../src/SUMMARY.md` is a generated mdBook projection. Do not hand-edit it. Change admitted RDF and re-manufacture.

The consequence, standing, and DfCM projections are qualification evidence rather than committed authority. Exact-head CI archives them with the ggen receipt-verification results. Their source facts remain under `cells/`.

`../book.toml` retains APS-specific presentation policy. Qualification proves that its semantic book identity agrees with the marketplace-generated core projection.

## Exact-head manufacturing court

For every candidate and every merge to `main`, CI:

1. validates APS-owned graphs and cell boundaries independently of ggen;
2. downloads the exact ggen release binary and verifies its SHA-256;
3. checks out the exact marketplace commit;
4. verifies every locked critical pack surface by Git blob identity and pack version;
5. executes the mdBook cell with the real marketplace pack;
6. executes the consequence-IR cell with the real marketplace gates and template;
7. executes the standing-ladder cell with its real no-skipped-states court;
8. executes the DfCM maximalist court with marketplace queries/templates/gates and APS candidate facts;
9. runs `ggen receipt verify` after manufacture;
10. repeats every manufacture and requires byte-identical qualified projections;
11. runs the independent APS RDF/SHACL/JSON-schema courts, unit tests, mdBook build, sensitivity model, and repository-cleanliness gate;
12. uploads exact-head evidence.

This is not complete APS self-hosting. It is stronger: multiple independent portions of APS now use distinct existing marketplace manufacturing laws rather than one bespoke local generator or one demonstration template.

No file here grants consequential production DO authority.
