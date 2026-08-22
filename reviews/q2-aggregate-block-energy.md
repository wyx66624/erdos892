# Independent review record: Q2 aggregate-block incidence energy

Date: 22 August 2026  
Reviewed manuscript: `research/q2-aggregate-block-energy.md`  
Frozen author SHA-256: `c75fbf6e7b61421d277fa68dab89f4eb891c4b33fe9d70962346e0e715dd8792`

## Review 1 — domains, bins, and arithmetic boundary audit

Final grade: **A** after repair.

The first pass found inconsistent low/high-set notation, an undefined bin
summation domain, and an off-by-one excess count in the sparse source.  The
frozen manuscript defines `mathcal N_k, mathcal L_k, mathcal G_k,
mathcal S_k` and `mathcal J_k` explicitly, covers the empty-band and
`K_k=1` cases, requires integral `H_i`, and uses
`tau_i(d_i)=H_i+1`.  The reviewer then checked the Chebyshev count, the
exceptional contribution, all four integer-divisor blocks, and the three
scale separations and gave A.

## Review 2 — maximality scope and second-moment audit

Final grade: **A** after repair.

The reviewer independently verified the low-excess injection, rank-five-screen
scope, incidence interpretation, and the sparse family's
`Q^+<=1, nu_i<=2` conclusion.  A scope sentence was restricted to the
arithmetic objects entering Theorem 1.1.  The finite-array barrier now takes
`R_k=R/4`, so the mean hypothesis holds while half the indices remain bad;
bounded relative second moment alone is therefore rigorously insufficient.
The final frozen text received A with no A/B/C blocker.

## Admission boundary

The reviews certify the deterministic binned incidence-energy implication and
the stated pointwise sparse-source obstruction.  Hypotheses (1.8)--(1.9), the
rank-three survivor estimate, ranks at least four, Q2, Erdős 892, and
conjecture-level Lean remain open.
