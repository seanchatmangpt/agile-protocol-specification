# Security and Consequential Authority

APS security begins by refusing ambient authority.

## Reportable classes

Security-relevant findings include:

- a path that can cause consequential `DO` without explicit authority;
- missing or forgeable evidence for consequential action;
- replay/idempotency defects that can duplicate consequence;
- semantic ambiguity that can manufacture a materially different action than the admitted contract;
- verifier self-attestation that can hide meaningful corruption;
- process evidence that cannot attribute object, activity, authority, and receipt;
- archive/predecessor material accidentally treated as active authority;
- governance compression that permits unqualified generator or policy changes to bypass admission.

## Safety law

Typed refusal is preferable to ambiguous execution. When required authority, semantics, bounds, or evidence are absent, the lawful result is `REFUSED`, `UNKNOWN`, or another bounded standing—not optimistic continuation.

This repository currently contains a specification and synthetic sensitivity experiment. It does not grant production deployment or operational authority.
