# Independent review record: conditional-NA phase rounding

Date: 22 August 2026  
Reviewed manuscript: `research/general-conditional-na-rounding.md`  
Frozen author SHA-256: `1c89186e14ed496f74ecc6b7244f45eec8cb161ad3485174b6f5aac11a653154`

## Review 1 — finite budgets and phase-mixture audit

Final grade: **A** after repair.

The reviewer reconstructed the conditional negative-association Laplace
estimate phase by phase, the exact early-failure budget, and the bounded-drift
geometric tail.  The review checked that no global negative association is
used after mixing, recomputed the P30 positive covariance and budget, and
recomputed the B25 three-phase failure budget `33/21>1`.  Minor finite-case
wording was repaired; the frozen manuscript received A.

## Review 2 — infinite lift and quantifier audit

Final grade: **A** after repair.

The reviewer independently checked Theorem C.  For `N<=r`, Theorem A is
applied with `r'=N`, so the late tail is empty and `E_N<=E<1`; only
`N>r` invokes the bounded-drift theorem.  The feasible-prefix tree is
nonempty at every level, prefix closed, and finitely branching, so Koenig's
lemma applies even though the random witnesses for different `N` need not
be projectively consistent.  All constants and phase quantifiers were
rechecked and the frozen manuscript received A.

## Admission boundary

The reviews certify the finite conditional-phase rounding theorem, its
bounded-drift corollary, and the uniform Koenig lift.  No arithmetic argument
yet derives these hypotheses from Erdős 892; uniform dilation, the original
conjecture, and conjecture-level Lean remain open.
