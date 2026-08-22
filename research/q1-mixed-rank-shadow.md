# Q1 research note: mixed-rank shadows and the remaining label-erasure problem

Date: 22 August 2026  
Scope: the quasi-primitive special case of Erdős Problem 892  
Global status: **OPEN**. Nothing below proves that every quasi-primitive sequence has a primitive dominator.

## 1. Claim labels and dependency policy

- **THEOREM**: an elementary proof is included below.
- **CONDITIONAL**: the deduction is complete once the explicitly named external/manuscript input is admitted.
- **CONJECTURE**: precise but unproved.
- **BARRIER**: a precise proposed mechanism is refuted; this is not a counterexample to the Erdős problem.
- **COMPUTATION**: finite sanity evidence only.

The supplied 169-page manuscript is not treated as audited merely because it labels a statement a theorem. In particular, its Theorems 5.56 and 5.82 remain manuscript inputs until their external dependencies and proofs pass the repository review protocol.

## 2. Exact setting

For an integer \(n\ge 1\), let

\[
  \Omega(n)=\sum_p v_p(n),\qquad \Omega(1)=0,
\]

and let \(\operatorname{supp}(n)=\{p:p\mid n\}\). For \(E\subseteq\{2,3,\ldots\}\), define the immediate multiplicative shadow

\[
  \partial E=\{e/p:e\in E,\ p\text{ prime},\ p\mid e\}.
\]

A family is *pairwise non-coprime* if \(\gcd(e,f)>1\) whenever \(e\ne f\).

An increasing set \(B\subseteq\mathbb N\) is quasi-primitive in the historical sense if no two incomparable members \(x,y\in B\) have \(\gcd(x,y)\in B\). Equivalently, for every \(d\in B\),

\[
  Q_d(B)=\{b/d:b\in B,\ d\mid b,\ b>d\}
\]

is pairwise non-coprime. Indeed, two strict multiples \(du,dv\) have gcd exactly \(d\) if and only if \(\gcd(u,v)=1\); in that case neither quotient can divide the other. The stronger Hasse formulation used below is proved in Section 4.

## 3. Mixed-rank two-shadow theorem

### 3.1 The only non-elementary input

**KATONA-SHADOW input.** If \(\mathcal A\) is a finite intersecting family of \(s\)-subsets of a finite set, then every subfamily \(\mathcal G\subseteq\mathcal A\) satisfies

\[
  |\partial_{\rm set}\mathcal G|\ge |\mathcal G|,
\]

where \(\partial_{\rm set}\mathcal G\) is the family of all \((s-1)\)-subsets contained in members of \(\mathcal G\).

This is the form attributed in the supplied manuscript to G. O. H. Katona, *Intersection theorems for systems of finite sets*, Acta Math. Acad. Sci. Hungar. 15 (1964), 329-337. The exact source statement must still be checked independently before admission to `main`.

### 3.2 Exact-rank lemma, with the exponent-vector step audited

**CONDITIONAL LEMMA 3.1 (exact-rank two-shadow map).** Assume KATONA-SHADOW. Let \(F\) be a finite pairwise non-coprime family with \(\Omega(e)=k\ge 1\) for all \(e\in F\). Then there is a map

\[
  \psi:F\longrightarrow \partial F,
  \qquad \psi(e)\mid e,
  \qquad \Omega(\psi(e))=k-1,
\]

such that every fibre has size at most two.

**Proof.** For each support cardinality \(s\), let

\[
  \mathcal A_s=\{\operatorname{supp}(e):e\in F,
                     |\operatorname{supp}(e)|=s\}.
\]

Because \(F\) is pairwise non-coprime, \(\mathcal A_s\) is intersecting. Every subfamily remains intersecting, so KATONA-SHADOW and Hall's theorem give an injection

\[
  T_s:\mathcal A_s\longrightarrow \partial_{\rm set}\mathcal A_s,
  \qquad T_s(S)\subset S,
  \qquad |S\setminus T_s(S)|=1.
\]

Write \(q_s(S)\) for the unique prime in \(S\setminus T_s(S)\). For \(e\in F\) with support \(S\) of size \(s\), set

\[
  \psi_s(e)=e/q_s(S).
\]

We verify that \(\psi_s\) is injective on the whole support-size-\(s\) slice, including distinct exponent vectors with the same support.

1. If \(v_{q_s(S)}(e)\ge2\), then \(\operatorname{supp}(\psi_s(e))=S\). Equality of two such images forces equality of their supports, hence the same deleted prime, and then equality of the original integers.
2. If \(v_{q_s(S)}(e)=1\), then \(\operatorname{supp}(\psi_s(e))=T_s(S)\). Equality of two such images and injectivity of \(T_s\) again force the same support, the same deleted prime, and the same original integer.
3. The two cases cannot collide, since their image support sizes are respectively \(s\) and \(s-1\).

Now combine the maps over \(s\). If an integer \(d\) has support size \(r\), a preimage of \(d\) can arise only from the support-size \(r\) slice (the deleted prime had exponent at least two) or the support-size \(r+1\) slice (the deleted prime had exponent one). Each slice contributes at most one preimage. Hence \(|\psi^{-1}(d)|\le2\). Dividing by one prime gives \(\Omega(\psi(e))=k-1\). ∎

### 3.3 New mixed-rank extension

**CONDITIONAL THEOREM 3.2 (mixed-rank two-shadow theorem).** Assume KATONA-SHADOW. Let \(E\subseteq\{2,3,\ldots\}\) be finite or countable and pairwise non-coprime. No common value of \(\Omega\) is assumed. There are maps

\[
  \psi:E\to\mathbb N,
  \qquad \tau:E\to\{0,1\},
\]

such that

\[
  \psi(e)\mid e,
  \qquad e/\psi(e)\text{ is prime},
  \qquad e\longmapsto(\psi(e),\tau(e))\text{ is injective}.
  \tag{MS}
\]

Equivalently, \(|\psi^{-1}(d)|\le2\) for every \(d\). In particular, for every finite \(G\subseteq E\),

\[
  |G|\le2|\partial G|.
  \tag{1}
\]

The integer fibre cap (equivalently, the number of types) two is best possible.
This does not assert that the real coefficient (2) in (1) is optimal.

**Proof, finite case.** Partition

\[
  E=\bigsqcup_{k\ge1}E_k,
  \qquad E_k=\{e\in E:\Omega(e)=k\}.
\]

Apply Lemma 3.1 separately to every nonempty \(E_k\). Its shadow lies entirely in the layer \(\Omega=k-1\). Shadows belonging to different \(k\)'s are therefore disjoint, so combining the maps does not increase the fibre bound. Colour the at most two members in each fibre by \(0,1\); this gives (MS). Restricting the map to \(G\) gives (1).

**Proof, countable case.** Form a bipartite graph with left side \(E\), right side \(\mathbb N\times\{0,1\}\), and

\[
  e\sim(d,t)\quad\Longleftrightarrow\quad e/d\text{ is prime}.
\]

Every left degree is \(2\omega(e)<\infty\). For every finite \(G\subseteq E\), the finite case gives

\[
  |G|\le2|\partial G|=|N(G)|.
\]

Thus every finite left subset satisfies Hall's condition. Enumerate \(E\), take a matching of each finite initial segment, and apply Koenig's infinity lemma to the finitely branching tree of such matchings. The resulting infinite matching is exactly (MS). ∎

**Sharpness.** For distinct primes \(p,q,r\), let

\[
 E^\star=\{qr^2,q^2r,pr^2,pqr,pq^2,p^2r,p^2q\}.
\]

This is pairwise non-coprime, every member has \(\Omega=3\), and

\[
  \partial E^\star=\{p^2,q^2,r^2,pq,pr,qr\}.
\]

Hence \(|E^\star|=7>|\partial E^\star|=6\), so a one-type injective shadow map is impossible. Theorem 3.2 supplies two types, and therefore the minimum *integer fibre cap* is two.  The example supplies only the real ratio (7/6), not a proof that the coefficient (2) in (1) is optimal. If pairwise non-coprimality is removed, an arbitrarily large family of distinct primes has shadow \(\{1\}\), so no uniform fibre bound is possible.

**COMPUTATION (sanity check only).** With \((p,q,r)=(2,3,5)\), a direct bipartite matching gives, among others,

\[
  12\mapsto(6,0),\ 18\mapsto(9,0),\ 20\mapsto(10,0),\
  30\mapsto(15,0),\ 45\mapsto(15,1),\ 50\mapsto(25,0),\ 75\mapsto(25,1).
\]

This merely checks the sharp example; it is not used in the proof.

## 4. Universal Hasse consequence for quasi-primitive sets

For \(b\in B\), let \(L_B(b)\) be the set of lower covers of \(b\) in the divisibility poset induced by \(B\). Every nonminimal \(b\) has a lower cover because an integer has finitely many divisors. Choose

\[
  \sigma(b)\in L_B(b)
\]

for every nonminimal member, and put

\[
  E_d=\{b/d:\sigma(b)=d\}.
\]

**THEOREM 4.1 (elementary Hasse palette lemma).** If \(B\) is quasi-primitive, then every \(E_d\) is primitive and pairwise non-coprime.

**Proof.** If distinct \(e_1,e_2\in E_d\) satisfied \(e_1\mid e_2\), then

\[
  d<de_1<de_2,
  \qquad d\mid de_1\mid de_2,
\]

contradicting that \(d=\sigma(de_2)\) is a lower cover. Thus \(E_d\) is primitive. If \(\gcd(e_1,e_2)=1\), then \(de_1,de_2\) are incomparable by the first part and

\[
  \gcd(de_1,de_2)=d\in B,
\]

contradicting quasi-primitivity. ∎

**CONDITIONAL COROLLARY 4.2 (universal abstract half-size code).** Assume KATONA-SHADOW. For every finite or countable quasi-primitive \(B\), every lower-cover selector admits maps

\[
  b\longmapsto\bigl(\sigma(b),s(b),t(b)\bigr)
  \qquad (b\in B\setminus R),
\]

where \(R\) is the set of divisibility-minimal members, such that

\[
  \sigma(b)s(b)=b/p_b\le b/2
\]

for a prime \(p_b\), and the labelled triples are injective. More strongly, for each fixed parent \(d\), the pairs \((s(b),t(b))\) are injective among children assigned to \(d\).

**Proof.** Apply Theorem 3.2 to every \(E_d\) and set \(s(de)=\psi_d(e)\), \(t(de)=\tau_d(e)\). The parent label separates different palettes. Since \(e/s(e)\) is a prime at least two, the half-size inequality follows. ∎

This is the main new reduction: arbitrary mixed local ranks do **not** create a shadow-capacity loss larger than one bit. The unresolved issue is erasing the abstract parent/type labels arithmetically with one uniform multiplicative constant.

## 5. What the theorem does not prove

### 5.1 Shadow values need not be primitive

**BARRIER 5.1 (numeric projection is unsafe).** The conclusion of Theorem 3.2 does not say that \(\psi(E)\) is primitive. For the primitive pairwise non-coprime palette \(E=\{6,20\}\), the valid choices

\[
  6\mapsto2,\qquad20\mapsto4
\]

give \(2\mid4\). This refutes the rule "choose arbitrary immediate shadows and forget the labels." It does not refute the possibility of a more coherent choice; for this two-element example, other choices work.

The exact-rank case avoids comparability once injectivity is arithmetized, because all coded values can be kept in one \(\Omega\)-layer. In the mixed-rank case, different shadow ranks can divide one another.

### 5.2 One type is rigorously impossible

The family \(E^\star\) above is a strict cardinal obstruction to every one-type immediate-shadow injection. Thus the bit in Corollary 4.2 is genuine and cannot simply be deleted.

### 5.3 A distinct bounded marker for every labelled slot is not universal

**BARRIER 5.2 (small-budget slot explosion).** Consider

\[
  B=\{p,2p:p\text{ an odd prime}\}.
\]

Every child quotient is \(2\), so the abstract compression produces one slot of deleted-prime budget \(2\) for each root. Any scheme demanding a distinct positive-integer or prime marker \(q_p\le 2C\) for every such slot has only finitely many possible markers and therefore fails. Nevertheless

\[
  p\mapsto2p,\qquad2p\mapsto3p
\]

is a pointwise factor-two primitive recoding. Hence universal label erasure must sometimes reuse a marker across a primitive family of parents; one-marker-per-parent is disproved as a universal mechanism.

### 5.4 Iteration loses path boundaries

Iterating Corollary 4.2 along a Hasse path deletes one prime per edge and creates one bit per edge. The product of deleted primes supplies at least one bit of multiplicative budget per edge. However, the surviving factors multiply commutatively, so the integer product does not remember their edge boundaries or order. Existing separated-support word-tree constructions avoid this ambiguity by hypothesis; arbitrary quasi-primitive Hasse diagrams do not provide such separation.

Repeated quotient \(2\) is the critical equality case: the deleted-prime budget is exactly one bit per level. The supplied manuscript claims to solve all unary two-adic towers by a self-absorbing reservoir, but that does not automatically handle a path alternating unary stretches with genuinely branching mixed-rank palettes.

## 6. Independent prime-transversal route

This route should remain separate from the shadow route because each has examples where the other is more efficient.

For a pairwise non-coprime palette \(E\), a *prime transversal* is a finite set of primes \(T\) such that every \(e\in E\) is divisible by some \(p\in T\). Such a transversal always exists: the support of any fixed pivot \(e_0\in E\) meets every member of \(E\).

**THEOREM 6.1 (elementary transversal channel decomposition).** In the setting of Theorem 4.1, choose a prime transversal \(T_d\) of every \(E_d\), and assign each \(e\in E_d\) to one prime \(\chi_d(e)\in T_d\cap\operatorname{supp}(e)\). Then

\[
  B=R\ \sqcup\!\!\bigsqcup_{d,p} B_{d,p},
  \qquad
  B_{d,p}=\{de:\chi_d(e)=p\},
\]

and every nonempty channel has anchor \(dp\), while

\[
  B_{d,p}/(dp)=\{e/p:\chi_d(e)=p\}
\]

is primitive.

**Proof.** The displayed sets form a partition. Division by the same prime preserves divisibility: \(e/p\mid f/p\) if and only if \(e\mid f\). The latter is impossible for distinct members because \(E_d\) is primitive. ∎

**CONDITIONAL COROLLARY 6.2.** If the near-critical primitive-channel gluing theorem claimed as Theorem 5.82 of the supplied manuscript is independently admitted, Theorem 6.1 proves domination whenever the multiset of used anchors

\[
  \{1\}\sqcup\{dp:B_{d,p}\ne\varnothing\}
\]

has counting function

\[
  O_\eta\!\left(\frac{x}{\log(2x)(\log\log(4x))^{1+\eta}}\right)
\]

for some \(\eta>0\). This is a new sufficient interface, not a universal decomposition theorem.

**BARRIER 6.3 (unbounded transversal cost despite pairwise intersection).** There is no universal bound on either the cardinality or reciprocal-prime weight of a transversal, even for primitive exact-rank palettes.

For a cardinality example, take \(2k-1\) primes and all products indexed by \(k\)-subsets. The supports are pairwise intersecting, all integers have exact \(\Omega=k\), and a transversal requires exactly \(k\) primes.

For the stronger reciprocal-weight version, let \(P\) be a finite prime set with

\[
  W=\sum_{p\in P}\frac1p>2A,
\]

and let

\[
  \mathcal F=\left\{S\subseteq P:\sum_{p\in S}\frac1p>W/2\right\}.
\]

Two members of \(\mathcal F\) cannot be disjoint. Put \(N=|P|\), choose \(p_S\in S\), and encode

\[
  e_S=\left(\prod_{p\in S}p\right)p_S^{N-|S|}.
\]

Then \(\Omega(e_S)=N\), so \(E=\{e_S:S\in\mathcal F\}\) is primitive, and it is pairwise non-coprime. If \(T\) hits all supports and \(\sum_{p\in T}1/p<W/2\), then \(P\setminus T\in\mathcal F\) is disjoint from \(T\), a contradiction. Thus every transversal has reciprocal weight at least \(W/2>A\). The divergence of \(\sum_p1/p\) makes \(A\) arbitrary.

This closes only the proposed universal bounded-transversal/Kraft route. It does not close adaptive shadow coding, root-dependent composite markers, or batching across parents.

## 7. Logic/topology route for a negative result

The following lemma isolates what finite counterexamples would have to do in order to produce an infinite counterexample.

Fix an envelope \(f:\mathbb N\to\mathbb N\), and let \(X_f\) be the space of all infinite increasing quasi-primitive sequences \(b=(b_n)\) with \(b_n\le f(n)\), viewed as a closed subspace of

\[
  \prod_{n\ge1}\{1,\ldots,f(n)\}.
\]

For an integer \(C\ge1\), let \(D_C\subseteq X_f\) consist of sequences having a primitive dominator with constant \(C\).

**THEOREM 7.1 (Baire finite-obstruction dichotomy).** Assume (X_f\ne\varnothing). The space \(X_f\) is compact metrizable. Each \(D_C\) is closed. Consequently:

1. If every member of \(X_f\) has some finite domination constant, then there are a finite admissible prefix \(Q\) and a constant \(C\) such that every member of \(X_f\) extending \(Q\) belongs to \(D_C\).
2. If, for every nonempty prefix cylinder \([Q]\subseteq X_f\) and every \(C\), there is a longer extendible prefix \(Q'\) with no primitive \(C\)-witness, then the sequences in \(X_f\) having no primitive dominator form a comeagre, in particular nonempty, subset.

**Proof.** The product of finite discrete spaces is compact metrizable. Strict increase and quasi-primitivity are each determined by finitely many coordinates at a time, so \(X_f\) is closed. Finite antichain compactness says \(b\in D_C\) if and only if every finite prefix has a primitive \(C\)-witness. Thus the complement of \(D_C\) is a union of cylinders based on finite \(C\)-hard prefixes, so \(D_C\) is closed.

If \(X_f=\bigcup_C D_C\), the Baire category theorem gives some \(D_C\) nonempty interior, which contains a prefix cylinder. This proves (1). Under the hypothesis of (2), every cylinder contains a smaller cylinder disjoint from \(D_C\), so every \(D_C\) is nowhere dense. Baire then shows that \(X_f\setminus\bigcup_C D_C\) is comeagre. ∎

**BARRIER 7.2 (remote scaling destroys finite hardness).** Let \(B=(b_1<\cdots<b_N)\) be fixed, and define the untruncated real distortion

\[
 \widetilde c(B)=\inf\{C>0:\text{there is a primitive increasing }(a_i)_{i\le N}
                    \text{ with }a_i\le Cb_i\}.
\]

If \(p_N\) is the \(N\)-th prime, then

\[
  \widetilde c(LB)\le \max_i\frac{p_i}{Lb_i}
          \le\frac{p_N}{Lb_1}\longrightarrow0.
\]

Thus placing isolated copies of a fixed finite certificate at remote scales cannot preserve, let alone amplify, its lower bound. A negative construction needs nested or density-preserving hard extensions of the kind appearing in Theorem 7.1. This explains rigorously why a finite certificate alone is not an infinite counterexample.
Under the normalized convention (C\ge1), the corresponding quantity is
\(\max\{1,\widetilde c(LB)\}\), which tends to (1), so the same construction still
cannot amplify any obstruction above the trivial normalized floor.

## 8. Current bottleneck and proof-dependency chain

The closest clean dependency chain is now

\[
\begin{array}{c}
\text{quasi-primitivity}\\
\Downarrow\ \text{(Theorem 4.1)}\\
\text{primitive, pairwise non-coprime Hasse quotient palettes}\\
\Downarrow\ \text{(Katona + Hall + rank separation)}\\
\text{one deleted prime and one abstract bit per edge, at half-size cost}\\
\Downarrow\ \textbf{OPEN}\\
\text{bounded arithmetic erasure of parent/rank/type labels across all paths}\\
\Downarrow\\
\text{primitive dominator.}
\end{array}
\]

The open arrow must simultaneously handle:

1. divisibility among shadows from different \(\Omega\)-layers;
2. collisions between numerically equal slots belonging to different parents;
3. infinitely many small deleted primes, where distinct bounded markers are impossible;
4. commutative loss of edge order under path iteration;
5. reuse of markers across compatible primitive parent batches, as forced by \(\{p,2p\}\).

### Next minimal lemmas (all open)

**CONJECTURE A (hybrid shadow-batching lemma).** Hasse shadow slots can be partitioned into primitive batches so that the binary type and batch marker cost are bounded by the product of deleted primes along every source path.

**CONJECTURE B (critical-small-prime reduction).** After batching all channels sharing a fixed small deleted prime, the residual unbatched slots have enough multiplicative contraction to satisfy a near-critical channel deadline condition.

**CONJECTURE C (finite factor-two form).** Every finite quasi-primitive tuple has an ordered factor-two primitive witness. Together with finite antichain compactness, a uniform proof would settle the infinite implication with constant two. The supplied manuscript gives exact finite reductions and searches only; no proof or counterexample is presently admitted.

These conjectures are intentionally kept separate. Failure of one does not close the others without a strict counterexample to its exact statement.

## 9. Counterexample report

- **No counterexample was found to the quasi-primitive implication.**
- **No counterexample was found to Theorem 3.2.** Its derivation is complete modulo the explicitly stated Katona shadow theorem.
- Strict counterexamples were found or verified only for stronger mechanisms:
  - one shadow type: \(E^\star\);
  - forgetting the labels after an arbitrary shadow choice: \(\{6,20\}\) with shadows \(2,4\);
  - one distinct bounded marker per small-budget slot: \(\{p,2p\}\);
  - a universal bounded prime-transversal/Kraft cost: the weighted support construction in Barrier 6.3;
  - amplification by remote dilation of a fixed finite certificate: Barrier 7.2.

None of these barriers is a counterexample to Erdős Problem 892.
