# Independent review record: stopping-time Laplace debt

Date: 22 August 2026  
Reviewed manuscript: `research/general-stopping-laplace-certificate.md`  
Frozen author SHA-256: `f5beb6c3f4d3278f428ff9b5a606c0ce8cd79df0e9b001111bd87a02e1408458`

## Review 1 — supermartingale, stopping, and compactness audit

Final grade: **A** after repair.

The reviewer checked the conditional filtration, the direction of the
nonnegative supermartingale inequality, bounded optional stopping, the
integer overshoot `d+1`, all prefix debt products, block repayment, and the
finite-prefix-to-Koenig lift.  An initial claim that the concrete `P_40`
blocks extended unchanged to arbitrary length was rejected.  The frozen text
limits that construction to ten shells and supplies a separate fixed
infinite prime-shell construction.

## Review 2 — arithmetic examples and union-bound barrier audit

Final grade: **A** after repair.

The reviewer independently recomputed the positive covariance `21/100`,
the Cramer-root identity `q_i=1`, and the exact ten-deadline sum
`6267056487/5000000000>1`.  The finite upper-half family and the
projection-consistent prime-shell version were checked as genuine divisor
antichains.  The barrier is correctly restricted to direct sums of
per-deadline upper bounds for the same distribution.

## Admission boundary

The reviews certify the stopping-time Laplace-debt theorem, block repayment,
the Koenig lift, and the strict non-NA/union-bound examples.  No arithmetic
argument derives a safe-shell certificate from the hypotheses of Erdős 892;
the general characterization and conjecture-level Lean remain open.
