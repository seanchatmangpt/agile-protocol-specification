# Chatman's Law

## Law

**Chatman's Law:** In knowledge work, historical production cost confers no preservation privilege. As remanufacturing capability improves, durable value migrates from incumbent artifacts and production skills toward the recoverable knowledge, contracts, evidence, and manufacturing capability required to reproduce or improve their useful consequences.

A compact form is:

```text
preserve truth, not implementations
```

A stronger operational form is:

```text
everything is sunk
-> recover what must survive
-> manufacture from current knowledge
-> independently qualify
```

## Formal statement

Let:

- `A_t` be an incumbent knowledge-work artifact or estate at time `t`;
- `K_t` be admitted reusable knowledge recovered from reality and prior artifacts;
- `M_t` be available manufacturing capability;
- `C_R(A_t | K_t, M_t)` be prospective remanufacture cost;
- `I(A_t | K_t)` be the value of required information still irrecoverably trapped only in `A_t`.

As remanufacture cost falls:

```text
C_R -> 0  =>  preservation privilege(A_t) -> I(A_t | K_t)
```

When all required truth has been externalized so that `I = 0`, the artifact may retain current utility but has **zero preservation privilege**.

Utility is not privilege. A working incumbent may continue to run because it is currently useful, contractual, safer, or cheaper prospectively. It does not survive because of the money, labor, or identity already invested in it.

## Human capital is included

Chatman's Law applies not only to code but to the human production method that code historically required.

Examples include:

- language-specific authoring skill;
- hand-maintained framework conventions;
- bespoke integration knowledge;
- manual QA and release ceremony;
- architecture translation roles;
- deployment runbooks;
- audit reconstruction practices.

When those activities become lawful consequences of admitted manufacturing knowledge, prior investment in performing them manually creates no continuation privilege.

## Technology choice under the law

A technology is not preserved because humans already know it, like it, or built around it. Nor is a new technology chosen because it is fashionable. The relevant question is whether it is useful capital equipment for the current manufacturing system.

A programming language may therefore become primarily a **manufacturing target** rather than a human authoring preference. Frameworks may become intermediate representations or downstream generators. They remain replaceable if their semantics are represented above them.

## Artifact depreciation and knowledge appreciation

Traditional software practice frequently treats the repository as accumulated capital. Chatman's Law reverses that accounting model:

```text
implementation = depreciating inventory
reusable semantic/manufacturing knowledge = compounding capital
```

The desired direction is:

```text
artifact -> observation -> reusable knowledge
```

not:

```text
artifact -> permanent preservation obligation
```

## Technical debt corollary

When lawful remanufacture becomes cheaper than understanding and repairing an incumbent, technical debt becomes closer to obsolete inventory than financial debt.

The rational response may be:

```text
observe -> recover contract -> remanufacture -> qualify -> sunset
```

rather than indefinitely repairing the incumbent.

## Enterprise corollary

An enterprise application is not necessarily durable architecture. Under semantic manufacture it can become a current materialization:

```text
A_t = mu_t(O*_t)
```

where `O*_t` is admitted enterprise knowledge and `mu_t` is the current lawful manufacturing function.

Tomorrow's estate can be:

```text
A_(t+1) = mu_(t+1)(O*_(t+1))
```

The enterprise preserves the knowledge required for continuity, not yesterday's realization merely because yesterday was expensive.
