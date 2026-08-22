# Independent review record: Q2 source-local rank-three blocks

Date: 22 August 2026  
Reviewed manuscript: `research/q2-source-local-block-decomposition.md`  
Frozen author SHA-256: `19aec53d81cfe7a68cc93d51cb2c3a65bacba7b7a1b35695b5f7d013804aaade`

## Review 1 — coprime-swap and endpoint audit

Final grade: **A** after repair.

The reviewer reconstructed the gcd-based swap bijection, including repeated
prime factors and `gcd(d,r)>1`, checked the half-open size window, the excess
rank cutoff, the quotient-rank identity, and the singleton `a=1` block.
The first pass found that Corollary 2.2 used `Q^+,D^+` outside their defined
domain.  The frozen manuscript restricts every occurrence to
`mathcal N_k^{A,B}` and received A.

## Review 2 — multiplicity and quantifier audit

Final grade: **A** after repair.

The reviewer independently checked the exact formulas for `nu_i` and
`f_{i,3}`, Corollary 2.1's exceptional-set sum, the labelled
prime-occurrence upper bound, repeated-prime extreme cases, and the distinction
from the rank-five promotion screen.  The first pass also rejected wording
that suggested surjectivity onto every rank-three divisor; the frozen text
uses only the correct injection and received A.

## Admission boundary

The reviews certify the exact finite-block identities, the strict
`a=1` obstruction to uniform blockwise anti-concentration, and the stated
conditional source-block population criteria.  The exceptional-set estimate,
the rank-three target, ranks four and higher, Q2, Erdős 892, and conjecture-level
Lean remain open.
