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
| B8 | Every finite or countable pairwise non-coprime palette admits an immediate-shadow map with fibres of size at most two; every quasi-primitive Hasse palette therefore has a half-size code with one abstract bit. | independently proved and reviewed | Katona's shadow theorem, Hall, and K\u00f6nig |
| B9 | For the logarithmic barrier profile, every middle anchor has shifted-block avoidance mass \(\gg 1/i\); hence unconditioned supremum and mean anchorwise summation cannot close the construction. | independently proved modulo named standard analytic inputs | Mertens, dyadic semiprime bounds, dyadic PNT |
| B10 | Fixed-dilation deadline feasibility is exactly measured by an integer antichain margin; its one-point random relaxation has a weighted maximum-antichain dual. Prefix width is strictly weaker, and in the actual divisor poset \(P_{15}\) the random relaxation has value 1 while the integer margin is \(6/7\). | independently proved and twice reviewed | convex separation, Stanley chain polytope, explicit two-antichain and nine-chain certificates |
| L1 | `Primitive.image_of_reflects_dvd` in Lean. | formally checked | Lean CI run 16 |
| L2 | Finite canonical top-half saturation for a fixed lower kernel. | formally checked and independently reviewed | PR 1; Lean CI run 16 |

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
   dilation constants diverge. B8 reduces every Hasse edge to a half-size shadow plus
   one bit, but the parent/type labels and cross-rank divisibility still need a
   globally primitive arithmetic encoding with one uniform constant. A finite obstruction alone is not
   an infinite counterexample unless it is amplified without bounded recoding.
2. **General domination.** Identify a cross-scale condition beyond the two classical
   scalar restrictions and consecutive dyadic load packing, then prove both
   directions.
   B10 closes only the claim that the complete chain polytope remains integral after
   direct intersection with nested deadline lower bounds; extended formulations,
   valid inequalities, surplus rounding, and all-constant obstructions remain open.
3. **Prescribed density scales.** Either control the actual terminal union of the
   middle-anchor low-multiplier events in the unresolved logarithmic profile, or
   exhibit a scale sequence satisfying all known local restrictions that is
   nevertheless inadmissible. B9 rigorously rules out replacing this actual union by
   an unconditioned anchorwise supremum or average.
4. **Formalization.** Formalize the compactness interfaces first; analytic inputs are
   admitted only through precisely stated Mathlib theorems or proved modules.

## Branch policy

- `main`: audited text, deterministic certificates, and compiling Lean only.
- `research/q1-*`: quasi-primitive embeddings, finite factor-two searches, and
  counterexample amplification attempts.
- `research/q2-*`: prescribed-scale constructions and actual-union estimates.
- `research/general-*`: finite deadline invariants, rounding, and obstruction certificates.
- `research/formal-*`: experimental Lean statements that may temporarily fail CI;
  no unproved declaration is merged.

No route is closed because it is unfashionable or temporarily stuck. A route is
marked closed only by an explicit counterexample, contradiction, or theorem proving
that its stated mechanism cannot supply the missing implication.
