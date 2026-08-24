---
receipt: APS-v26.7.30-mdbook-0.5-repair
date: 2026-07-30
standing: PARTIAL_ALIVE
subject: mdBook 0.5 configuration compatibility
predecessor_run: 30522692446
---

# mdBook 0.5 Configuration Repair

## Observed failure

The Rust-built `mdbook 0.5.4` executable refused `specification-guide/book.toml` before rendering. The parser reported that the legacy `multilingual` field is not part of the mdBook 0.5 book schema.

## Repair

The materialization step removes exactly this obsolete line before source verification and compilation:

```bash
sed -i '/^multilingual = false$/d' specification-guide/book.toml
```

No content, language, navigation, renderer, or protocol semantics are changed. APS v26.7.30 remains an English single-language book through `language = "en"`.

## Standing

`PARTIAL_ALIVE`: the failure and repair are observed and bounded. Promotion to `ALIVE` requires a successful replay through source verification, HTML rendering, PDF rendering, structural PDF checks, rendered-page witnesses, and the generated-output commit.

## Falsifier

This repair is false or insufficient if `mdbook build` still rejects the configuration or fails at a later renderer boundary.
