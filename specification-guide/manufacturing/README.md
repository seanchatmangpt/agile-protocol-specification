# APS ggen manufacturing consumer

This directory turns the active APS mdBook control surface into a real consumer of the ggen ecosystem.

## Authority

`docs/book.ttl` owns book identity and ordered navigation as RDF using the `mdbook-pattern-language-pack` vocabulary. `ggen.toml` is the thin consumer manifest. `ecosystem.lock.json` pins the exact ggen release, release-asset digest, ggen source commit, ggen-marketplace commit, pack version, and the Git blob identities of the marketplace pack surfaces APS executes.

The committed `../src/SUMMARY.md` is a generated projection. Do not hand-edit it. Change admitted RDF and re-manufacture.

`../book.toml` retains APS-specific presentation policy (theme, print settings). Exact-head qualification separately proves that its semantic book identity agrees with the marketplace-generated `book.toml` projection.

## Exact-head manufacturing court

CI performs the following on the exact candidate head:

1. validates this static consumer contract independently;
2. downloads the pinned ggen release binary and verifies its SHA-256;
3. checks out the exact ggen-marketplace commit;
4. verifies the Git blob SHA of each admitted pack surface;
5. stages the real `mdbook-pattern-language-pack` beside this consumer;
6. runs `ggen sync run`;
7. runs `ggen receipt verify`;
8. runs `ggen sync run` a second time and requires byte-identical output;
9. compares manufactured `docs/SUMMARY.md` byte-for-byte with the committed APS projection;
10. independently compares generated and committed mdBook identity fields.

This makes ggen and ggen-marketplace capital equipment rather than copied source. APS owns its admitted facts; the marketplace owns the reusable pattern; ggen owns deterministic manufacture.

No file here grants consequential production DO authority.
