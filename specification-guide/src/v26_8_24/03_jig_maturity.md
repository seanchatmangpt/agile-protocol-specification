# Five-Level × Seven-Dimension Jig Maturity

The historical jig matters because it moved manufacturing knowledge out of the craftsperson and into repeatable production equipment. APS uses that industrial progression before applying it to software.

The model is exactly **five levels by seven dimensions**. There is no Level 0 baseline in the maturity ladder.

## The five levels

### L1 — Craft

The worker carries the coordinate system, sequence, technique, inspection knowledge, and correction method. Quality depends heavily on tacit expertise. The product can be excellent, but production knowledge is not embodied in a reusable manufacturing system.

### L2 — Template

The desired form or specification is externalized. A template reduces interpretation but normally does not locate the workpiece, constrain the operation, enforce sequence, or independently qualify the result.

### L3 — Fixture

The workpiece is located and held against explicit datums. Variation due to positioning falls sharply. The fixture stabilizes the operation but does not necessarily guide the transforming tool or encode the complete process.

### L4 — Jig

The tooling embodies both location and operation guidance. It constrains what operation can occur, where it occurs, and often in what sequence. Poka-yoke and interlocks can make invalid transformations difficult or impossible. Manufacturing knowledge has migrated materially from worker judgment into the production system.

### L5 — Closed-Loop Manufacturing System

The system combines jig-like constraint with independent metrology, process evidence, feedback, reconfiguration, and controlled learning. It can qualify both product and process and can turn observed exceptions or successful novelty into candidate improvements to reusable manufacturing capability.

## The seven dimensions

| Dimension | L1 — Craft | L2 — Template | L3 — Fixture | L4 — Jig | L5 — Closed-Loop Manufacturing System |
|---|---|---|---|---|---|
| Product knowledge | Desired result mainly in craft knowledge | Shape/specification externalized | Product references tied to repeatable datums | Product requirements embodied in tooling | Machine-readable product definition drives and constrains production |
| Work positioning | Worker manually locates work | Template provides reference | Fixture deterministically locates and holds work | Jig couples work position to operation | System selects/configures positioning and verifies datum state |
| Operation guidance | Worker decides how to transform | Pattern/instruction suggests operation | Work is stabilized but transformation remains operator-directed | Tool/action/path is constrained by the jig | Operation is configured from admitted manufacturing knowledge and live state |
| Process sequence | Sequence depends on worker judgment | Recommended sequence documented | Repeatable setup supports standard sequence | Tooling constrains or enforces legal sequence | Multi-stage process is orchestrated, state-aware, and evidence-bound |
| Error prevention | Skill and rework catch errors | Visual reference reduces error | Incorrect positioning becomes harder | Poka-yoke/interlocks prevent many invalid operations | Invalid transitions are refused before consequence and abnormal states trigger controlled response |
| Measurement & qualification | Worker judges quality | Compare with template/master | Repeatability and datum conformance can be measured | Independent gauges/tolerances qualify output | Inline metrology qualifies product and process with replayable evidence |
| Adaptation & learning | Improvement remains tacit with craftsperson | Better templates are manually created | Fixtures are redesigned from observed variation | Jigs improve from defect/process evidence | Successful learning becomes candidate reusable manufacturing knowledge after independent qualification |

## Do not average away bottlenecks

Represent maturity as a vector:

```text
J = <product, positioning, guidance, sequence, prevention, metrology, learning>
```

with each dimension in `L1..L5`.

A single scalar can hide the exact weakness that keeps a factory dependent on expert reconstruction. A system may have L5 measurement and only L2 operation guidance. The profile is more informative than the mean.

## What the phase changes mean

```text
Craft -> Template
```

externalizes product knowledge.

```text
Template -> Fixture
```

externalizes datum and positioning knowledge.

```text
Fixture -> Jig
```

externalizes operation knowledge.

```text
Jig -> Closed Loop
```

externalizes qualification, feedback, and reusable learning.

The central industrial lesson is not automation for its own sake. It is the relocation of production knowledge from individual memory into inspectable, reusable, qualified manufacturing capital.

## Applying the matrix later

When APS applies this model to a software factory, sophistication inside the engine does not automatically earn a higher level. The question remains whether a new operator can discover the workpiece, locate authority, perform the legal operation, prevent invalid consequence, qualify the result, and improve the factory without reconstructing private inventor knowledge.
