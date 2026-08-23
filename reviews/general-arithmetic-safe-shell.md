# Independent review record: arithmetic safe shells

Date: 22 August 2026  
Reviewed manuscript: `research/general-arithmetic-safe-shell.md`  
Frozen author SHA-256: `619eb8cc71b1fbf72f742c1ce66e68d1c09fce73d5ff507d0e60561eb47b2b16`

## Review 1 — capacity, endpoints, and projection audit

Final grade: **A**.

The reviewer checked first-shell and odd/even endpoints, same-shell and
cross-shell incomparability, the exact coefficient two in the finite
multiple increment, deterministic tie-breaking, projection consistency, and
the conditional Laplace identity `q_i=1`.

## Review 2 — constants and mechanism-boundary audit

Final grade: **A**.

The reviewer independently checked all floor bounds in the uniform relative
gap corollary, the composite example `b_i=3^i,m=6,C=36`, and the exact
scope of the reciprocal-load barrier.  The witness `b_i=i^2` correctly
shows that the corollary is a strict subclass of B7 without making a claim
about the full TSC(2) class.

## Admission boundary

The reviews certify TSC(2), its adaptive true-divisor safe-shell kernel, the
explicit relative-gap positive class, and the coarse reciprocal-load
barrier.  This class is already covered abstractly by B7; no safe-shell
certificate is derived in the unresolved divergent reciprocal-sum region.
Erdős 892 and conjecture-level Lean remain open.
