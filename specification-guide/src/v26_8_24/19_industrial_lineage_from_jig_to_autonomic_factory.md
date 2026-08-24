# Industrial Lineage: From Jig to Autonomic Factory

APS is intentionally derived from manufacturing history rather than from software-generation fashion. The central historical pattern is the progressive movement of production knowledge out of individual craft judgment and into capital equipment, process law, metrology, and feedback.

## Craft

In craft production the worker carries much of the coordinate system:

```text
inspect -> measure -> mark -> position -> choose operation -> transform -> compare -> correct
```

The product may be excellent, but repeatability depends on tacit skill and repeated local decisions.

## Template

Templates externalize desired geometry or form. They reduce interpretation, but the worker still locates the work, chooses much of the operation, and judges conformance.

The template is an early form of industrial memory: product knowledge survives beyond the individual craftsperson.

## Fixture

Fixtures externalize datum and positioning knowledge. The workpiece is held in a predictable relationship to the operation. Variation caused by locating the work falls dramatically.

The worker no longer needs to reconstruct the coordinate system for every unit.

## Jig

A jig couples work positioning with operation guidance. It can embody hole location, tool entry, angle, legal motion, and sometimes sequence.

The crucial transition is:

```text
worker chooses geometry each time
  -> tooling embodies geometry once
  -> worker or machine replays the admitted operation
```

A jig is therefore **industrial memory plus constraint**.

## Gauge and metrology

Repeatable production creates a second-order problem: the thing that makes products repeatable can itself wear, drift, or be wrong.

Industrial systems therefore qualify the jig, datum, gauge, and process—not only the final product.

That yields a general law:

> Inspect and calibrate the system that manufactures repeatability.

APS applies the same law to templates, ontologies, generators, policy, verifier logic, and the manufacturing kernel itself.

## Machine tools and transfer systems

Machine tools move transformation energy and motion into capital equipment. Special-purpose machinery and transfer lines then encode larger sequences of work.

The key economic shift is not merely faster motion. A larger fraction of production knowledge becomes reusable across units.

## CNC and flexible manufacturing

CNC absorbs much of the tool-guidance function into programmable coordinates and paths. Yet the underlying jig problem remains: datum, workholding, legal operation, sequence, tool selection, calibration, and qualification still must be embodied somewhere.

Flexible manufacturing increases the number of product families that common capital equipment can lawfully produce.

This is the industrial analogue of DfCM: not one rigid production line, but a qualified production system capable of realizing a broad family of admissible designs.

## Jidoka and poka-yoke

Jidoka moves abnormal-condition detection into the production system so defects do not silently propagate. Poka-yoke makes classes of invalid operation difficult or impossible.

APS equivalents include:

- typed `REFUSED`;
- fail-closed authority;
- semantic/contract gates;
- bounded filesystem/network actuation;
- invariant checks before consequence;
- exact-head promotion law;
- independent verification after consequence.

The goal is not to document that an operator should avoid a bad state. It is to design the manufacturing system so the bad transition cannot acquire standing.

## Andon as capability discovery

A recurring manual exception is not merely labor to optimize. It is a signal that the factory lacks an embodied capability or that its current law is wrong.

```text
manual exception
  -> observe
  -> classify
  -> candidate missing contract/pattern/jig
  -> falsify
  -> admit reusable capability
```

Thus exception handling can become capital formation.

## Semiconductor analogy

Modern semiconductor production provides an extreme example of design separated from direct manual fabrication. High-level design intent is transformed through many machine-readable representations, rule decks, synthesis/place-and-route flows, process constraints, masks, equipment programs, metrology, and qualification stages.

The durable leverage lies heavily in design rules, process knowledge, tooling, and verified transformations—not in a human manually reproducing each transistor.

APS seeks an analogous relationship between enterprise intent/semantics and replaceable software realizations.

## Automated craftsmanship versus manufacture

An LLM that writes source code dramatically faster can still preserve the artisanal topology:

```text
request -> intelligent craftsperson -> code -> review -> deploy
```

The worker changed; the production system did not.

Manufacturing changes the topology:

```text
admitted product definition
  -> embodied contract + jig + process law
  -> capital equipment
  -> independent metrology
  -> repeatable qualified consequence
  -> feedback into reusable manufacturing knowledge
```

This distinction explains why raw model capability is not the terminal competitive object. The factory—its contracts, orchestration, jigs, authority, metrology, and learning law—determines production reliability and compounding capacity.

## The historical direction

```text
Craft
  -> Template
  -> Fixture
  -> Jig
  -> Jig + Gauge
  -> Machine Tool
  -> Transfer / Special-Purpose System
  -> CNC / Flexible Manufacturing
  -> Closed-Loop Qualified Cell
  -> Autonomic Reconstitutable Factory
```

The final step is an APS research target, not a historical claim. Its defining property would be a factory that can manufacture broad knowledge-work product families, qualify their consequences, learn reusable patterns from evidence, and reconstitute its own production machinery when superior capital becomes available.
