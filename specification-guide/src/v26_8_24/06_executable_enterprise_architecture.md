# Executable Enterprise Architecture

APS v26.8.24 treats enterprise architecture as potentially executable manufacturing authority rather than a descriptive layer that humans manually translate into applications.

## Historical split

Traditional enterprise architecture commonly separates:

```text
enterprise meaning
  -> architecture models
  -> application models
  -> database schemas
  -> integration models
  -> API contracts
  -> deployment models
  -> observability models
```

Each translation creates drift, coordination cost, and another source of truth.

The target architecture collapses those layers toward:

```text
public semantics + enterprise facts + operational closure
  -> lawful projections
```

## Public semantics as durable authority

Public ontologies provide generalized domain meaning. Enterprise-specific ABox facts and application profiles provide bounded local commitments. SHACL or equivalent operational contracts close choices that open-world semantics alone do not settle.

For a financial enterprise, FIBO is a canonical example of the kind of public semantic substrate APS expects to exploit. The durable enterprise model should not be trapped inside one vendor schema, database, framework, or programming language.

## AshR2RML as a phase-change example

The architectural significance of `ash_r2rml` is not merely RDF support for an Elixir framework.

The intended closure is:

```text
RDF/OWL + SHACL
      -> ggen
      -> generated Ash.Resource
      -> Ash application behavior
      -> relational operational state
      -> R2RML virtual RDF view
      -> the same admitted semantic subject
```

The important property is **semantic-operational closure**:

- public/application semantics can drive executable application structure upstream;
- relational persistence remains operationally efficient;
- standards-valid R2RML can expose the live relational subject semantically downstream;
- no second graph database or dual-write synchronization is required by the architecture;
- unsupported or ambiguous mappings should fail closed rather than invent semantics.

This can move enterprise meaning above both framework and database schema.

## Ash as capital equipment, not permanent authority

Under Chatman's Law, Ash, Elixir, PostgreSQL, R2RML engines, and ggen itself remain replaceable.

Ash is attractive when its typed, introspectable resource/action model and extension ecosystem provide a high manufacturing multiplier:

```text
upstream semantic contract
  -> compact Ash application model
  -> persistence / actions / policy / API / workflow / jobs / generated surfaces
```

A human does not need to prefer authoring Elixir for Elixir/Ash to be rational capital equipment for the factory.

## Manufacture and bind

The enterprise contains both systems it owns and systems it cannot recompile.

APS therefore distinguishes:

```text
manufacture: admitted semantics -> new operational realization
bind:        admitted semantics -> external/incumbent observable contract
```

SaaS, vendor platforms, mainframes, existing services, and arbitrary executables can be bindings to the same enterprise semantic subjects without becoming enterprise semantic authority.

## Applications become projections

The unit of enterprise architecture shifts from the durable 'application' toward admitted capability and semantic contract.

```text
application_t = mu_t(enterprise_knowledge_t)
```

Application portfolios can therefore become inventories of current realizations rather than the canonical description of the enterprise itself.

## Enterprise architecture consequence

If generalized and qualified, enterprise architecture stops primarily documenting how applications are integrated after implementation. It becomes the upstream authority from which replaceable applications, integrations, interfaces, tests, deployment, and semantic views can be continuously manufactured.
