# Claim ledger — 22 August 2026

## Global status

**Neither characterization in Erdős Problem 892 is proved here. The historical
quasi-primitive implication is also open.**

The supplied stage manuscript contains extensive partial results, but it explicitly
disclaims a full solution. It is treated as a source of candidate lemmas until each
dependency is independently audited.

## Audited baseline

| ID | Statement | Status | Dependency |
|---|---|---|---|
| B1 | Pointwise domination is equivalent to the corresponding counting-function deadlines. | proved | elementary order statistics |
| B2 | Fixed-constant domination is equivalent to feasibility of every finite prefix. | proved | König's infinity lemma |
| B3 | Domination implies \(\sum_n 1/(b_n\log b_n)<\infty\). | proved modulo source | Erdős (1935) |
| B4 | Domination implies the classical reciprocal-sum little-o bound. | proved modulo source | Erdős–Sárközy–Szemerédi (1967) |
| B5 | Positive density at every scale \(2^{n_i}\) implies \(\sum_i1/n_i<\infty\). | proved | B3 plus disjoint shells |
| B6 | The intended gcd-free condition means incomparable input pairs. | source-verified | Erdős–Sárközy–Szemerédi (1970), pp. 41–42 |
| B7 | If \(\sum_n1/b_n<\infty\), then \((b_n)\) has a primitive dominator with an explicit constant. | independently proved and reviewed | elementary dyadic greedy construction |
| L1 | `Primitive.image_of_reflects_dvd` in Lean. | formally checked when CI is green | Mathlib only |

## Candidate results from the supplied manuscript

These are **not automatically admitted** merely because they are labelled theorem in
the PDF.

| Candidate | Claimed role | Current gate |
|---|---|---|
| C2 | Every arbitrary-height two-adic tower over an odd primitive skeleton is dominated. | analytic reservoir proof and Lean abstraction under audit |
| C3 | Every quasi-primitive set obeys a consecutive-density local packing law. | published combinatorial input and reduction under audit |
| C4 | Polynomial density scales \(n_i=\lceil i^p\rceil\) are admissible iff \(p>1\). | Ford/Tenenbaum dependencies and maximal-overlap proof under audit |
| C5 | Exact finite factor-two reductions and exhaustive searches through the reported bounds. | source code/reproduction certificate missing from upload |

## Exact unresolved interfaces

1. **Quasi-primitive embedding.** Prove a uniform finite-prefix dilation bound for
   every historically quasi-primitive tuple, or construct a family whose required
   dilation constants diverge. A finite obstruction alone is not an infinite
   counterexample unless it is amplified without bounded recoding.
2. **General domination.** Identify a cross-scale condition beyond the two classical
   scalar restrictions and consecutive dyadic load packing, then prove both
   directions.
3. **Prescribed density scales.** Either control the actual terminal union of the
   middle-anchor low-multiplier events in the unresolved logarithmic profile, or
   exhibit a scale sequence satisfying all known local restrictions that is
   nevertheless inadmissible.
4. **Formalization.** Formalize the compactness interfaces first; analytic inputs are
   admitted only through precisely stated Mathlib theorems or proved modules.

## Branch policy

- `main`: audited text, deterministic certificates, and compiling Lean only.
- `research/q1-*`: quasi-primitive embeddings, finite factor-two searches, and
  counterexample amplification attempts.
- `research/q2-*`: prescribed-scale constructions and actual-union estimates.
- `research/formal-*`: experimental Lean statements that may temporarily fail CI;
  no unproved declaration is merged.

No route is closed because it is unfashionable or temporarily stuck. A route is
marked closed only by an explicit counterexample, contradiction, or theorem proving
that its stated mechanism cannot supply the missing implication.
