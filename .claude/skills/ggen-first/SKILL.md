# ggen-first Manufacturing

Assume ggen-like deterministic manufacture unless a downstream generator is being driven by something the manufacturing layer itself can generate.

Decision law:

1. known marketplace pattern -> compose it;
2. known tool/generator -> manufacture its inputs, configuration, and invocation;
3. known tool sequence -> manufacture the script/workflow;
4. repo-specific variation -> encode facts/parameters;
5. genuinely novel mechanism -> author the irreducible mechanism, then extract and qualify the reusable pattern.

Applications should be overwhelmingly projections/compositions. Libraries retain only the irreducible mechanism that cannot yet be lawfully derived.
