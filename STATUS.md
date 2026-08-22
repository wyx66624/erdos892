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
| B14 | HBC can be strictly relaxed for fixed shadow data: split each same-word core preorder into terminal-rank layers and pay layer \(j\) the deadline \(Wj^{1/s}\). If every terminal rank is bounded by the corresponding unused deletion slack, the refined batches still admit one absolute-dilation primitive injection. | independently proved and twice reviewed | rank-layer antichains, sublinear refined-deadline count, B12 weighted erasure |
| B15 | For incomparable quotients \(e,f\), an immediate shadow \(e/p\) can divide \(f/q\) exactly when \(p\) is the unique one-unit exponent surplus of \(e\) over \(f\) and \(q\) is a surplus of \(f\). Hence any primitive star palette in which every member has a safe deletion prime has a one-type primitive shadow batch. | independently proved and twice reviewed | valuation-by-valuation criterion, safe-prime selection, exact conflict probability formula |
| B16 | For fixed selectors, HBC is exactly avoidance of finite-support pair events in a product of local shadow states. For fixed prime deletions it is exactly coherent binary proper colouring of the depthwise core-comparability graphs, with an exact forced-0 bipartite extension test; union-bound and local-lemma criteria follow from post-LCA collision entropy. | independently proved and twice reviewed | cylinder-event support reduction, coherent colouring equivalence, LLL/compactness, explicit private-prime chain barrier |
| B17 | The finite universal-HBC problem is an exact CSP. Every quasi-primitive set with at most four elements admits HBC, while the numerical-minimum-cover selector already fails on `{2,3,4,12}` and is repaired by another selector. Exhaustive and deterministic sampled searches found no universal obstruction in the archived ranges. | small-cardinality theorem independently proved and twice reviewed; computations reproduced | four-element forest classification, exact DFS, deterministic enumeration, independent Cartesian cross-check |
| B18 | Every quasi-primitive set with at most five elements admits HBC; more strongly, every intrinsic-height lower-cover selector on such a set can be completed by weighted shadow/type choices. Hence every finite universal-HBC counterexample has at least six elements. | independently proved and twice reviewed | four-child star lemma, common-denominator cancellation, mixed-root `2+1` lemma, exhaustive height-profile classification |
| B19 | In the Q2 critical strip, maximality has an exact cofactor/excess-budget form with at most two threshold jumps. Modulo central-range Sathe--Selberg and fixed-rank Hardy--Ramanujan, all rank-three triples with source excess `<=H_k=o(sqrt(log k))` have total mass `o(X_k)`. Every remaining maximal triple must survive an explicit fixed rank-five moving-block screen; an `o(X_k)` survivor bound would imply both the symmetric `1/nu` target and a deterministic rank-three-avoiding selector. | independently proved and twice reviewed modulo named standard analytic inputs | cofactor identity, threshold calculation, Sathe--Selberg/Hardy--Ramanujan, rank-five promotion, exact energy and anti-concentration interfaces |
| B20 | Every primitive pairwise non-coprime quotient palette `E subset Z_{>=2}` with at most five members admits weighted immediate-shadow choices whose two type classes are injective and primitive. More generally this holds at arbitrary cardinality when one member uses at most two distinct primes. Hence every one-root star with at most five children satisfies HBC, and any one-root-star HBC obstruction has at least six children. | independently proved and twice reviewed | common-prime partition, fragile-surplus valuation lemma, minimum-`Omega` blocker count, B18 four-child star lemma |
| B21 | Every primitive pairwise non-coprime quotient palette `E subset Z_{>=2}` with at most six members admits weighted immediate-shadow choices whose two type classes are injective and primitive. In the unique five-option tie, full blocker saturation forces a `{2,p}` prime cover and hence a global two-batch repair. Thus every one-root star with at most six children satisfies HBC. | independently proved and twice reviewed | B20 five-child theorem, minimum-`Omega` blocker orientation, saturated blocker bijection, two-prime common-denominator repair |
| B22 | Every primitive pairwise non-coprime quotient palette `E subset Z_{>=2}` with at most eight members admits weighted immediate-shadow choices whose two type classes are injective and primitive. After one blocker is selected per saturated option, any two support primes cover all blockers; at most two extras have a two-point support transversal. A nine-member family strictly defeats this two-prime-cover repair but has an explicit one-change HBC repair. | independently proved and twice reviewed | strong induction from B20/B21, support-transversal saturation lemma, two-prime common-denominator repair, symbolic nine-member certificate |
| B23 | A finite fractional deadline-antichain witness rounds to an integer antichain under an exact rational Laplace budget; separate width-saturation, Cantelli, and negative-association surplus criteria follow. Uniform NA surplus plus a finite early-safe window lifts by König to infinite domination. Directly summing the width-saturation bounds for all prefixes would force `b_i` to be linear and violate the classical reciprocal-log necessary condition. | independently proved and twice reviewed | Markov/Cantelli inequalities, exact divisor-poset width, negative association, geometric tail bound, König compactness, B10 deadline model |
| B24 | Any nine-member one-root palette obstruction must have every minimum-`Omega` member supported on `{2,p,q}`. For every successful assignment on its eight-member deletion and every blocker-representative choice, all five options are saturated and the three extras have exactly the singleton signatures `{2}`, `{p}`, `{q}`. This is a necessary-structure theorem, not a nine-member solution. | independently proved and twice reviewed | B22 eight-member theorem, blocker orientation, saturated support-transversal repair, exact three-subset transversal lemma |
| B25 | In the true divisor poset with deadlines `(3,9,10,13,14,15,19,20,21)`, the integer margin is `8/9` while the fractional margin is `22/21`. The same projection-consistent three-point distribution extends along prime deadlines with `rho_N^*>=22/21` for every `N`, while `rho_N<=8/9` for every `N>=9`. Thus uniform positive first-moment surplus at a fixed dilation is strictly insufficient for integer rounding. | independently proved and twice reviewed | explicit chain covers, three-antichain witness, weighted dual certificate, prime extension |
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
   B14 gives a separate non-HBC route: it suffices to bound every same-word core-chain rank by a fixed power of the unused deletion slack. No universal selector satisfying that rank--slack inequality is known.
   B15 reduces the one-root arbitrary-rank star problem to a directed fragile-surplus graph and solves every palette with one safe deletion prime per member. B20 solves every palette of size at most five and every palette containing a member supported on at most two primes. B21 closes six members, and B22 extends the saturation-transversal repair through eight members. B24 now proves the exact necessary form of a nine-member obstruction: every minimum-rank support is `{2,p,q}`, every eight-member deletion solution saturates all five options, and its three extras have the singleton signatures `{2}`, `{p}`, `{q}`. The archived nine-member certificate realizes these signatures but is repaired by one changed deletion, so the exchange problem remains open. The arbitrary-cardinality star statement remains open; a strict counterexample would refute universal HBC, though not the original domination conjecture.
   B16 gives exact probabilistic and graph-colouring formulations. The unresolved estimates are a universal product-state LLL distribution, a coherent prefix colouring for every selected forest, or a strict obstruction defeating all shadow/selector choices; the private-prime chain rejects only type-only repair after its displayed bad deletions.
   B17 proves the non-computational boundary `|B|<=4` and supplies an exact finite decision procedure. The archived exhaustive searches cover 567,646 globally distinct nonempty sets across the three exact universes and find no counterexample, but finite search is not a theorem and does not establish universal HBC. The smallest failing fixed-selector pair refutes only the numerical-minimum-cover rule.
   B18 raises the paper boundary to `|B|<=5`, uniformly over every intrinsic-height selector. B20 removes the five-child star from the six-point obstruction list, B21 closes six-child stars, and B22 proves that a one-root-star obstruction needs at least nine children. The remaining six-point shapes include three same-word nodes split among three parents and two consecutive non-singleton levels with unequal inherited deletion products. None is known to be an obstruction; universal HBC even for all six-point sets remains open.
2. **General domination.** Identify a cross-scale condition beyond the two classical
   scalar restrictions and consecutive dyadic load packing, then prove both
   directions.
   B10 closes only the claim that the complete chain polytope remains integral after
   direct intersection with nested deadline lower bounds; extended formulations and
   all-constant obstructions remain open. B23 supplies four rigorous surplus-rounding interfaces (rational Laplace budgets,
   width saturation, Cantelli variance control, and negative association) and a König
   lift. B25 now proves that even a projection-consistent uniform positive fractional
   surplus is insufficient at a fixed dilation: an explicit true-divisor-poset family
   has `rho_N^*>=22/21` for every prefix but `rho_N<=8/9` from depth nine onward.
   Therefore the remaining rounding target must derive structured surplus—NA,
   Laplace-controlled, stopping-time, block-correlated, or another condition excluding
   the certified phase split—and a compatible finite early-safe window. B23 separately
   rules out only summing width-saturation failures over every prefix; enlarged
   dilation, block, stopping-time, and correlated approaches remain open.
3. **Prescribed density scales.** Either control the actual terminal union of the
   middle-anchor low-multiplier events in the unresolved logarithmic profile, or
   exhibit a scale sequence satisfying all known local restrictions that is
   nevertheless inadmissible. B9 rigorously rules out replacing this actual union by
   an unconditioned anchorwise supremum or average.
   B11 reduces the first unsolved quotient layer to rank 3 and separates two exact
   targets: a deterministic selector sum and a symmetric `1/nu` maximal-anchor mass.
   Neither target has yet been shown to be `o(X_k)`.
   B19 removes the entire source-excess range `tau<=H_k=o(sqrt(log k))` and proves that every high-excess maximal rank-three triple avoids a fixed rank-five screen. The closest remaining estimate is `|S_k(H_k)|=o(X_k)` for the screen survivors, or the stated size-conditioned rank anti-concentration condition (AC). A divergent first moment, variance growth alone, and pointwise high excess are each strictly insufficient by explicit counterexamples.
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
