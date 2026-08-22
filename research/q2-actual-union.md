# Erdős 892, Question 2: actual-union notes at the logarithmic barrier

**Status (22 August 2026).** This is a research note, not a solution of Question 2.  Every
statement below is marked either **proved**, **conditional**, **computational evidence**, or
**open**.  The note isolates a strict obstruction to the anchorwise finite-saturation route and
records a period-free finite certificate that still leaves an actual-union route open.

## 1. The exact remaining object

Use the logarithmic barrier profile from Section 8 of the stage manuscript:

\[
 n_i=\left\lceil i+i(\log(i+1))^2\right\rceil,\qquad
 X_i=2^{n_i},\qquad U_i=\log\log X_i,
\]

and, for fixed \(A>0\),

\[
 T_i=U_i+A\sqrt{U_i},\qquad
 C_i=\{d\in(X_i/2,X_i]:d\text{ odd},\ \Omega(d)\ge T_i\}.
\]

For \(i<k\), \(d\in(X_i/2,X_i]\), put

\[
 H(i,k)=\min(i,k-i-1),\qquad Y_{i,k,d}=X_k/d,
\]

\[
 D_{i,h}(d)=\left(X_{i+h}/(2d),X_{i+h}/d\right]\cap\mathbb N_{\rm odd}
 \quad(1\le h\le H(i,k)),
\]

and define the finite shifted-block avoidance set

\[
 E^{\square}_{i,k}(d)=\left\{r:\frac{Y_{i,k,d}}2<r\le Y_{i,k,d},\ r\text{ odd},\
 a\nmid r\ \text{for all }a\in\bigcup_{h\le H(i,k)}D_{i,h}(d)\right\}. \tag{Q2.1}
\]

If \(m\in C_k\) has maximal old pool divisor \(d\in C_i\), then \(m/d\) belongs to
\(E^{\square}_{i,k}(d)\).  This is because \(T_{i+h}-T_i<1\) for \(h\le i\), so every
nontrivial quotient divisor in \(D_{i,h}(d)\) would promote \(d\) to a later pool divisor.

The stage manuscript proves all of the following:

- adjacent-layer pollution is \(o(X_k)\);
- the last \(H_k\) anchors are harmless for the polylogarithmic range in Proposition 8.27;
- all small-prime-radical exceptions can be combined over all anchors into one actual union;
- complete-period transfer and a raw second-moment/Chebyshev estimate cannot close the
  remaining estimate.

Thus the unresolved region contains \(\Theta(k)\) middle anchors, for example
\(k/3\le i\le 2k/5\).  In this strip \(H(i,k)=i\).  The missing estimate must use the actual
union over these anchors or the dependence created by maximality.  The next theorem shows
that an anchorwise saturation estimate is not merely unavailable: it is false at the strength
needed for summation.

## 2. A semiprime floor for finite-block avoidance

### Proposition Q2.1 (moving-endpoint semiprime floor) — **proved**

Fix \(0<a<b<1/2\).  There is \(c_{a,b}>0\) such that, for every sufficiently large \(k\),
every integer \(i\) with \(ak\le i\le bk\), and every odd
\(d\in(X_i/2,X_i]\),

\[
 |E^{\square}_{i,k}(d)|\ge c_{a,b}\frac{Y_{i,k,d}}{i}. \tag{Q2.2}
\]

Consequently, with the notation of (355) in the stage manuscript,

\[
 \varepsilon^{\square}_{i,k}\ge \frac{c_{a,b}}i,
 \qquad
 \sum_{ak\le i\le bk}\varepsilon^{\square}_{i,k}\gg_{a,b}1. \tag{Q2.3}
\]

In particular, the anchorwise hypotheses (356) and (397) cannot hold for this profile.
This does **not** show that the profile is inadmissible; it shows that the unconditioned
avoidance sets in (Q2.1) are too large to be summed one anchor at a time.

#### Proof

Write

\[
 Y=X_k/d,\qquad Z=X_{2i}/d,\qquad
 \mathcal D=\bigcup_{1\le h\le i}D_{i,h}(d).
\]

Uniformly for \(1\le h\le i\), Lemma 8.37 of the stage manuscript gives

\[
 \log \Theta_h\asymp h(\log i)^2,
 \qquad \Theta_h:=X_{i+h}/(2d), \tag{Q2.4}
\]

and \(D_{i,h}(d)=(\Theta_h,2\Theta_h]\cap\mathbb N_{\rm odd}\).  Also
\(\mathcal D\subset(1,Z]\).

Choose small \(\eta>0\), depending only on \(a,b\), and put \(P=Z^{\eta/2}\).
Let \(\mathcal U\) be the set of products \(u=pq\) of two distinct odd primes at most \(P\)
such that none of \(p,q,pq\) lies in \(\mathcal D\).  Mertens' theorem gives

\[
 \sum_{\substack{p\le P\\p\text{ odd prime}}}\frac1p\asymp\log\log P\asymp\log i.
\]

For one ratio-two interval, the standard prime reciprocal estimate and the fixed-semiprime
upper bound give

\[
 \sum_{\Theta_h<p\le2\Theta_h}\frac1p\ll\frac1{\log(2\Theta_h)},
\]

\[
 \sum_{\substack{\Theta_h<u\le2\Theta_h\\\Omega(u)=2}}\frac1u
 \ll\frac{\log\log(3\Theta_h)}{\log(2\Theta_h)}.
\]

Using (Q2.4),

\[
 \sum_{h\le i}\sum_{\Theta_h<p\le2\Theta_h}\frac1p
 \ll\frac1{\log i}, \tag{Q2.5}
\]

while

\[
 \sum_{h\le i}\sum_{\substack{\Theta_h<u\le2\Theta_h\\\Omega(u)=2}}\frac1u
 \ll \frac1{(\log i)^2}\sum_{h\le i}\frac{\log(3h(\log i)^2)}h
 \ll1. \tag{Q2.6}
\]

The reciprocal weight of all products of two distinct primes at most \(P\) is
\(\asymp(\log i)^2\).  Products for which one prime lies in \(\mathcal D\) have reciprocal
weight \(O((\log i)(\log i)^{-1})=O(1)\) by (Q2.5), and products which themselves lie in
\(\mathcal D\) have weight \(O(1)\) by (Q2.6).  Hence

\[
 \sum_{u\in\mathcal U}\frac1u\gg(\log i)^2. \tag{Q2.7}
\]

Regular variation of \(j(\log j)^2\), uniformly for \(ak\le i\le bk\), gives

\[
 \frac{\log Y}{\log Z}
 =\frac{n_k-n_i+O(1)}{n_{2i}-n_i+O(1)}
 \ge 1+\delta_{a,b} \tag{Q2.8}
\]

for some \(\delta_{a,b}>0\).  Choose \(\eta<\delta_{a,b}/2\).  Then, for every
\(u\in\mathcal U\), \(Y/u\ge Z^{1+\delta_{a,b}/2}\).  The standard uniform Buchstab
lower bound for rough integers therefore yields

\[
 \#\left\{s:\frac{Y}{2u}<s\le\frac Yu,\ P^-(s)>Z\right\}
 \gg_{a,b}\frac{Y}{u\log Z}. \tag{Q2.9}
\]

The representations \(r=us\) in (Q2.9) are distinct because \(u\) is exactly the part of
\(r\) supported on primes at most \(Z\).  They are odd.  Moreover every divisor of \(r\)
which is at most \(Z\) divides \(u\), and the only divisors of \(u=pq\) are
\(1,p,q,pq\).  By the definition of \(\mathcal U\), none lies in \(\mathcal D\).  Thus all
these \(r\) belong to \(E^{\square}_{i,k}(d)\).  Summing (Q2.9), using (Q2.7), and noting
\(\log Z\asymp i(\log i)^2\), gives

\[
 |E^{\square}_{i,k}(d)|
 \gg \frac{Y}{\log Z}\sum_{u\in\mathcal U}\frac1u
 \gg \frac Yi.
\]

This proves (Q2.2) and (Q2.3).  \(\square\)

### Corollary Q2.2 (mean-anchor summation also fails) — **proved**

Define the averaged pair-count proxy

\[
 \bar\varepsilon_{i,k}:=\frac1{X_k}\sum_{d\in C_i}|E^{\square}_{i,k}(d)|. \tag{Q2.10}
\]

Since \(|C_i|\gg_A X_i\) and every \(d\le X_i\), Proposition Q2.1 gives, in the same
middle strip,

\[
 \bar\varepsilon_{i,k}\gg_A\frac1i,
 \qquad \sum_{ak\le i\le bk}\bar\varepsilon_{i,k}\gg_{A,a,b}1. \tag{Q2.11}
\]

Thus replacing the supremum over \(d\) by an average over \(d\) does not by itself repair
the anchorwise sum.  A successful proof must combine the images \(dE^{\square}_{i,k}(d)\)
as an actual union, or impose information omitted by (Q2.1), such as maximal-anchor survival
and terminal-rank compatibility.

## 3. Period-free finite Bonferroni certificates

Whole-period transfer incurs an error involving the least common multiple of every generator.
The following elementary lemma transfers a *truncated* inclusion-exclusion certificate directly
to the specified terminal interval and has no period term.

For real \(Y\ge3\), let

\[
 I_Y=(Y/2,Y]\cap\mathbb N_{\rm odd},\qquad N_Y=|I_Y|.
\]

For a finite set \(F\) of odd integers greater than one and \(s\ge1\), define

\[
 \mathcal B_{2s}(F)
 =1+\sum_{\substack{\varnothing\ne S\subseteq F\\|S|\le2s}}
 (-1)^{|S|}\frac1{\operatorname{lcm}(S)}. \tag{Q2.12}
\]

### Lemma Q2.3 (short-interval Bonferroni transfer) — **proved**

Uniformly in \(Y,F,s\),

\[
 \frac1{N_Y}\#\{r\in I_Y:f\nmid r\text{ for every }f\in F\}
 \le \mathcal B_{2s}(F)
 +O\left(\frac1Y\sum_{j=0}^{2s}\binom{|F|}{j}\right). \tag{Q2.13}
\]

If \(2s\ge|F|\), the untruncated expression with the exact finite-interval counts is an
identity.

#### Proof

For every odd \(q\ge1\), direct counting in the dyadic interval gives

\[
 \frac1{N_Y}\#\{r\in I_Y:q\mid r\}=\frac1q+O(1/Y), \tag{Q2.14}
\]

uniformly even when \(q>Y\).  Apply the even Bonferroni upper bound to the complement of
the union of the events \(\{f\mid r\}\).  An intersection indexed by
\(S\subseteq F\) is the event \(\operatorname{lcm}(S)\mid r\).  Substitute (Q2.14) term by
term.  There are \(\sum_{j\le2s}\binom{|F|}{j}\) retained terms.  \(\square\)

This lemma evades the density-period uncertainty in Corollary 8.31: large
\(\operatorname{lcm}(F)\) is harmless provided the number of retained Bonferroni terms is
small compared with \(Y\).  For a middle anchor, \(\log Y\asymp k(\log k)^2\), so even
certificates with \(|F|=k^{O(1)}\) and \(s=O(\log k)\) have a potentially negligible floor
error.  The unresolved problem is to make the model quantity \(\mathcal B_{2s}(F)\) small
after the maximal-anchor/actual-union conditioning.

### Corollary Q2.4 (finite certificate sufficient condition) — **conditional**

Suppose that for every relevant \((i,k,d)\) one chooses

\[
 F_{i,k,d}\subseteq\bigcup_{h\le H(i,k)}D_{i,h}(d)
\]

and an integer \(s_{i,k,d}\ge1\).  Put

\[
 \eta_{i,k,d}=\mathcal B_{2s_{i,k,d}}(F_{i,k,d})
 +C Y_{i,k,d}^{-1}
 \sum_{j\le2s_{i,k,d}}\binom{|F_{i,k,d}|}{j}. \tag{Q2.15}
\]

If the adjacent and terminal-strip errors are \(o(X_k)\), and the actual maximal-anchor
images admit the bound

\[
 \lim_{J\to\infty}\sup_{k>J}\frac1{X_k}
 \left|\bigcup_{J\le i\le k-H_k-1}\ 
       \bigcup_{d\in C_i} d\bigl(I_{Y_{i,k,d}}\cap E(F_{i,k,d})\bigr)\right|=0, \tag{Q2.16}
\]

then the barrier profile is admissible.  A stronger, easier-to-check but now known to be
unattainable in unconditioned form is obtained by replacing the union cardinality in (Q2.16)
by \(\sum_{i,d}Y_{i,k,d}\eta_{i,k,d}\).  Proposition Q2.1 explains why the actual union in
(Q2.16) is essential.

## 4. Three independent live routes

### 4.1 Truncated inclusion-exclusion / Janson / Brun route — **open**

For a squarefree certificate \(F\), in the independent prime-divisibility model define

\[
 D_F=\sum_{f\in F}\prod_{p\mid f}\xi_p,\qquad
 \mu_F=\sum_{f\in F}\frac1f,
\]

\[
 \Delta_F=\sum_{\substack{f\ne g\in F\\(f,g)>1}}
 \frac1{\operatorname{lcm}(f,g)}.
\]

A robust Janson bound has exponent of the scale

\[
 \frac{\mu_F^2}{\mu_F+\Delta_F}. \tag{Q2.17}
\]

The target is not an abstract natural-density bound.  One needs a pruned family
\(F_{i,k,d}\), or preferably a family chosen after maximal-anchor conditioning, for which:

1. the exponent in (Q2.17) is at least \((1+\epsilon)\log k\);
2. a Brun/Janson expansion can be truncated at \(2s=O(\log k)\);
3. the Bonferroni floor error in (Q2.13) is negligible;
4. the resulting exceptional images overlap across \(i\) strongly enough to satisfy
   (Q2.16), rather than an anchorwise sum contradicted by Proposition Q2.1.

**Strict counterexample to a naive version.**  Large \(\mu_F\) alone gives no saturation.
For

\[
 F_z=\{3p:p\le z,\ p\text{ odd prime},\ p\ne3\},
\]

one has \(\mu_{F_z}\sim(1/3)\log\log z\to\infty\), but every odd integer not divisible by
3 avoids every member of \(F_z\); its avoidance density is at least \(2/3\).  The common
factor makes \(\Delta_F\) large.  This rules out only a first-moment claim, not a pruned Janson
or cluster-expansion argument.

### 4.2 Analytic divisor-window / bilinear actual-union route — **open**

The natural quantity is the image union

\[
 \mathcal U_k=
 \bigcup_{i\in[k/3,2k/5]}\ \bigcup_{d\in C_i}
 dE^{\square}_{i,k}(d), \tag{Q2.18}
\]

intersected with \(C_k\) and with the condition that \(d\) is a maximal old pool divisor.
Proposition Q2.1 shows that the pair count
\(\sum_{i,d}|E^{\square}_{i,k}(d)|\) is necessarily \(\gg X_k\), so the desired
\(|\mathcal U_k|=o(X_k)\) can only come from overlap or maximality.

A viable analytic lemma would be a bilinear or dispersion estimate of the form

\[
 \#\{m\in C_k:\text{the selected maximal anchor lies in }[k/3,2k/5]}=o(X_k), \tag{Q2.19}
\]

where the anchor is selected by a deterministic rule and all quotient windows are retained
inside the same count.  Swapping the order of summation turns promotion into chains
\(d\mid da\mid m\), suggesting a large-sieve/dispersion estimate for divisor chains rather
than separate Ford estimates.

**Useful proved reduction using a two-sided rank band.**  If the pools are replaced by

\[
 C_i^{A,B}=\{d\in(X_i/2,X_i]:d\text{ odd},\
 U_i+A\sqrt{U_i}\le\Omega(d)\le U_i+B\sqrt{U_i}\},\quad A<B,
\]

then they still have fixed positive density by Erdős--Kac, and every relation
\(d\mid m\), \(d\in C_i^{A,B}\), \(m\in C_k^{A,B}\), forces

\[
 \Omega(m/d)\le U_k-U_i+B\sqrt{U_k}-A\sqrt{U_i}. \tag{Q2.20}
\]

The Hardy--Ramanujan upper bound for integers with at most \(Q\) prime factors therefore
gives a completely explicit low-rank contamination criterion.  In the middle strip of the
barrier profile, however, (Q2.20) permits \(Q\asymp(B-A)\sqrt{\log k}\); its layerwise bound
is \(k^{-1+o(1)}\), not summable over \(\Theta(k)\) anchors.  The band is therefore useful
only if combined with (Q2.18), not as another anchorwise union bound.

The existing strict barriers remain applicable: complete-period averaging gives total error
\(\gg k/\log k\), unrestricted scale-free radical maxima fail by the CRT construction, and
the displayed Tenenbaum residual bounds cannot be summed even with heterogeneous cutoffs.
None of these refutes (Q2.19).

### 4.3 Boolean divisor-spectrum / container route — **open**

Define the logarithmic divisor spectrum

\[
 \mathscr L(r)=\{\log_2 a:a\mid r\}.
\]

For \(d\in(X_i/2,X_i]\), put \(\sigma_i(d)=\log_2(X_i/d)\in[0,1)\).  Then (Q2.1) is exactly

\[
 \mathscr L(r)\cap
 \bigcup_{h\le H(i,k)}
 (n_{i+h}-n_i+\sigma_i(d)-1,
  n_{i+h}-n_i+\sigma_i(d)]=\varnothing. \tag{Q2.21}
\]

This gives a clean additive-combinatorial object.  If \((r_1,r_2)=1\), then

\[
 \mathscr L(r_1r_2)=\mathscr L(r_1)+\mathscr L(r_2)
\]

(Minkowski sum).  For squarefree \(r=p_1\cdots p_q\), \(\mathscr L(r)\) is the Boolean
subset-sum set of the weights \(\log_2p_j\).  The desired input is an inverse theorem:
if this subset-sum set misses all the shifted intervals in (Q2.21), then the prime-log
multiset lies in a small family of structured containers; a sieve estimate must then show
that the corresponding integers have small *actual-union* mass.

**Strict deterministic counterexamples to naive mesh claims.**

- Large \(\Omega(r)\) alone does not imply a dense divisor spectrum: \(r=p^q\) has only
  \(q+1\) divisor logarithms, all in one arithmetic progression.
- Even for squarefree \(r\), superincreasing weights
  \(\log p_{j+1}>2\sum_{\ell\le j}\log p_\ell\) leave macroscopic subset-sum gaps.

Thus a deterministic statement based only on rank is false.  These exceptional structures
are arithmetically thin, so a container-plus-sieve theorem remains plausible and is not
excluded.

## 5. Finite optimization and computations

The exact compactness number \(\Gamma_r(E)\) can be computed as a mixed-integer program:
binary variables \(x_m\) for \(1\le m\le2^{n_r}\), constraints
\(x_a+x_b\le1\) whenever \(a\mid b\), and prefix constraints

\[
 \sum_{m\le2^{n_i}}x_m\ge t\,2^{n_i}\qquad(1\le i\le r),
\]

with objective maximize \(t\).  The supplied script also enumerates the shifted-block toy
model and finite Bonferroni sums.

### Computational evidence (not proofs)

HiGHS reported optimal MILP solutions for the following small instances:

| Exponents | computed \(\Gamma_r\) | counts of one optimizer at the cutoffs |
|---|---:|---|
| \([2]\) | \(0.5\) | \([2]\) |
| \([2,5]\) | \(0.375\) | \([2,12]\) |
| \([2,5,9]\) | \(147/512=0.287109375\) | \([2,10,147]\) |
| \([2,5,9,12]\) | \(33/128=0.2578125\) | \([2,9,132,1057]\) |
| \([2,4,7,10]\) | \(0.2724609375\) | \([2,5,35,279]\) |

The first four entries use the beginning/truncations of the logarithmic-barrier profile, except
that \(12\) is used instead of the next true exponent \(15\) to keep the optimization small.
The interior cutoff, not always the terminal cutoff, can be binding.

For the toy grid with logarithmic window positions \(2h\), phase zero, and terminal endpoint
\(Y=2^{2(H+2)}\), direct enumeration gave avoidance fractions

| \(H\) | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|
| avoidance | 0.625000 | 0.546875 | 0.472656 | 0.402344 | 0.355469 |

For \(H=3\), \(Y=2048\), and the 21 odd generators in the three windows, the exact
avoidance fraction was \(0.4609375\).  The model/actual even Bonferroni upper bounds at
orders \(2,4,6,8\) were respectively

\[
\begin{array}{c|cccc}
2s&2&4&6&8\\ \hline
\text{model}&0.852427&0.632784&0.502604&0.465030\\
\text{actual finite interval}&0.857422&0.544922&0.462891&0.460938.
\end{array}
\]

These values support the use of moderately deep Bonferroni truncation, but are far too small
to predict the asymptotic middle-anchor union.

At cutoff \(2^{20}\), a separate toy calculation compared one-sided high-\(\Omega\) pools
with a central two-sided \(\Omega\) band at source exponents \(8,12,16\).  The fraction of the
terminal pool hit by at least one source was approximately \(0.4118\) for the half-space and
\(0.2965\) for the band.  This is evidence that (Q2.20) removes some pollution, not evidence
of asymptotic admissibility.

Reproduction:

```bash
python research/experiments/q2_finite_checks.py
```

The captured output is in `research/experiments/q2_finite_checks.txt`.

## 6. Precise remaining gap after this note

Proposition Q2.1 rules out the following hoped-for closure:

\[
 \sum_{i\asymp k}\sup_{d\in C_i}
 \frac{|E^{\square}_{i,k}(d)|}{Y_{i,k,d}}=o(1),
\]

and even its version with the supremum replaced by an average over \(d\).  Therefore the
remaining target is strictly an actual-union/maximality statement such as (Q2.19), or an
equivalent terminal statement that charges a terminal integer only once.

The period-free Lemma Q2.3 removes one technical obstruction to such a proof: a finite
Janson/Brun certificate can be transferred directly to the moving dyadic quotient interval
without requiring that the interval contain a full lcm period.  What is still missing is either:

1. a cluster expansion after maximal-anchor conditioning whose truncated lcm sums satisfy
   (Q2.16); or
2. a bilinear divisor-chain estimate proving (Q2.19); or
3. a Boolean subset-sum inverse theorem plus a sieve bound for all exceptional containers.

No counterexample to any of these three statements is known here.  No admissibility or
inadmissibility claim for the logarithmic-barrier profile, and no solution of Erdős 892, is made.
