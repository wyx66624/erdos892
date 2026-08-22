# Independent review record: positive-surplus integrality gap

Date: 22 August 2026  
Reviewed manuscript: `research/general-positive-surplus-gap.md`  
Frozen author SHA-256: `863403229ff9bd7d3a7aacfbef4dce1d021f9f51638beeb6df4a0237a5385106`

## Review 1 — combinatorial and certificate audit

Final grade: **A**.

The reviewer independently checked the two chain decompositions in Lemma 1.1,
the eleven-chain proof of `width(P_21)=11`, the three displayed antichains,
all nine expectation rows, the normalized weighted upper certificate, and an
exhaustive enumeration of all 16,513 antichains of `P_21`.  The enumeration
confirmed integer margin `8/9`, weighted maximum `22`, and width `11`;
it was used only adversarially, not in the proof.

The first review found a missing width certificate and a form-feed corruption
in one TeX command.  The exact frozen manuscript repairs both and received A.

## Review 2 — quantifier, extension, and scope audit

Final grade: **A**.

The reviewer independently checked the definitions of
`rho_N(C;b), rho_N^*(C;b)`, attainment on the finite antichain simplex,
strict growth of `q_t=ceil(22t/21)`, primitivity of all three infinite
samples, exact prime counts at each later deadline, and the bound
`rho_N(1;b)<=8/9` for every `N>=9`.  The PNT/Mertens consequences and
the limitation to fixed dilation `C=1` were also checked.

The first review requested explicit dilation notation and expanded endpoint
and analytic arguments.  The exact frozen manuscript includes these repairs
and received A.

## Admission boundary

Both reviews certify the paper theorem and its stated mechanism barrier.  They
do not certify Erdős 892, any all-dilation counterexample, or a conjecture-level
Lean theorem.  The result only proves that uniform positive first-moment
fractional surplus at a fixed dilation is not sufficient for integer rounding.
