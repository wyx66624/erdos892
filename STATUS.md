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
| B11 | For the logarithmic barrier profile, maximality is exactly equivalent to avoidance by the full coprime size-rank swap spectrum. The actual union has exact deterministic-selector and reciprocal-multiplicity formulas; fixed quotient ranks at most 2 contribute \(o(X_k)\), while unweighted rank-3 candidate pairs remain \(\gg X_k\) even inside two-sided source/terminal \(\Omega\)-bands. | independently proved and twice reviewed modulo named analytic inputs | coprime-swap identity, Turán--Kubilius, fixed-rank Hardy--Ramanujan, odd dyadic Erdős--Kac, audited Q2.1 inputs |
| B12 | Conditional on the hereditary batch condition (HBC), every quasi-primitive input admits an absolute-dilation primitive injection: a sparse two-prime reservoir absorbs all source factors, and a sublinear weighted batch-erasure lemma encodes the remaining binary shadow words. | independently proved and twice reviewed modulo dyadic PNT | absorption divisibility reflection, weighted primitive-batch erasure, binary-word growth bound, order statistics |
| B13 | HBC holds whenever intrinsic-height edges admit prefix-synchronized deleted primes; it also holds for every one-root exact-\(\Omega\)-rank star. A canonical least-root selector triangularizes every core divisibility, and the maximal-node blocker and LLL criteria isolate the remaining exchange/probability estimates. | independently proved and twice reviewed | common-denominator cancellation, audited two-shadow theorem, finite-domain compactness, explicit strict examples |
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

1. **Quasi-primitive embedding.** Prove the universal hereditary batch
   condition (HBC), jointly selecting the immediate-shadow parents and binary types,
   or construct an amplifiable family for which every such selection fails. B8 and
   B12 show that HBC is sufficient and that, once it is available, all arithmetic
   parent/type labels can be erased with one absolute dilation. A fixed selector is
   not enough: the explicit nine-element palette in
   `research/q1-absorbed-hbc.md` defeats all 135 admissible type choices for one
   selector but has a repaired selector satisfying HBC. Likewise, encoding the full
   deleted-prime word within product budget is impossible for the alphabet
   \(\{2,3,5\}\), since \(1/2+1/3+1/5>1\). These close only those stated
   mechanisms. A finite obstruction is not an infinite counterexample unless it is
   amplified without bounded recoding. B13 proves two complementary positive classes—prefix-synchronized intrinsic-height forests and exact-rank one-root stars—and a canonical-root triangularization, but no synchronization, exchange, or local-lemma estimate is yet known for every mixed-rank forest.
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
   B11 reduces the first unsolved quotient layer to rank 3 and separates two exact
   targets: a deterministic selector sum and a symmetric `1/nu` maximal-anchor mass.
   Neither target has yet been shown to be `o(X_k)`.
4. **Formalization.** Do not begin the conjecture-level Lean development until
   the complete written proof has passed two independent reviews. After that gate,
   formalize compactness interfaces first; analytic inputs are admitted only through
   precisely stated Mathlib theorems or proved modules.

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
