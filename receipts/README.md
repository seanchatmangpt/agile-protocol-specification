# Receipts

APS receipts are exact-coordinate evidence, not evergreen authority.

Current verification writes receipts outside the repository during CI and uploads them as immutable workflow artifacts. This directory intentionally contains no committed success receipt for the current candidate, because committing a receipt produced before its own commit would create coordinate ambiguity.

A receipt must identify the source coordinate, contract or policy coordinate, requested/observed consequence, integrity digests, verifier identity, and bounded standing appropriate to the claim.

Historical receipt evidence is preserved through the predecessor archive/commit. It must not be read as standing for the active candidate.
