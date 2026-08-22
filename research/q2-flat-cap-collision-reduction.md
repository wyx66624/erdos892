# Erdős 892, Q2: flat-cap lower tails and five source-collision shapes

**Reviewed paper status (22 August 2026).**  This note does not prove the
rank-three estimate, Question 2, or Erdős 892.  It gives two deterministic
reductions on the actual maximal, high-excess, rank-five-screen survivors of
`research/q2-aggregate-block-energy.md`:

1. the centered energy in B29 is reduced to three diagonal rank-block
   variances, whose incidence pairs have only five possible gcd-rank shapes;
2. the centered-energy hypothesis may instead be replaced by a pointwise
   upper flatness condition.  An exact one-sided counting lemma then controls
   the low tail without a second-moment estimate.

The reductions are finite and elementary.  They use no probabilistic or
analytic-number-theoretic input.

## 1. Retained domain and notation

Fix real constants `A<B`.  Let `H_k -> infinity` with
`H_k=o(sqrt(log k))`, and retain the sets
\(\mathcal N_k,\mathcal L_k,\mathcal G_k\), the bins
\(\mathcal G_{k,s}\), and the nonempty-bin index set \(\mathcal S_k\) from
`research/q2-aggregate-block-energy.md`.  Thus every
\(m\in\mathcal G_k\) is an actual terminal integer in \(C_k^{A,B}\),
\(i=\iota_k(m)\) is its maximal old layer, and `d(m)` is the least divisor in
\(\mathcal D_i(m)\) whose complementary quotient `r(m)=m/d(m)` has
\(\Omega(r(m))=3\).  In particular, once `H_k>=4`, the selected triple is a
rank-five-screen survivor.

For such an `m`, let \(W(m)\) be the finite witness set

\[
 \left\{(a,b):\begin{array}{l}
 a\mid r(m),\ b\mid d(m),\ (a,b)=1,\\
 d(m)a/X_i\le b<2d(m)a/X_i,\\
 \Omega(b)\le \tau_i(d(m))+\Omega(a)
 \end{array}\right\}.                                      \tag{1.1}
\]

The left endpoint is weak and the right endpoint is strict.  The exact
source-local decomposition gives

\[
 A_m:=|W(m)|=\nu_i(m),\qquad
 B_m:=\#\{(a,b)\in W(m):\Omega(a)=\Omega(b)\}=f_{i,3}(m).
                                                               \tag{1.2}
\]

For a nonempty bin `s`, put

\[
 M_s=|\mathcal G_{k,s}|,\quad I_s=\sum_m A_m,\quad
 E_s=\sum_m A_m^2,\quad \mu_s=I_s/M_s,                       \tag{1.3}
\]

where here and below a sum carrying the subscript `m` is over
\(m\in\mathcal G_{k,s}\).  The bin condition is
\(2^s\le B_m<2^{s+1}\).

## 2. The exact rank-block covariance identity

For `0<=j<=3`, define

\[
 C_{m,j}:=\#\{(a,b)\in W(m):\Omega(a)=j\},                    \tag{2.1}
\]

and for a nonempty bin define

\[
 I_{s,j}:=\sum_m C_{m,j},\qquad
 E_{s;j,\ell}:=\sum_m C_{m,j}C_{m,\ell},\qquad
 \Gamma_{s;j,\ell}:=E_{s;j,\ell}-{I_{s,j}I_{s,\ell}\over M_s}.
                                                               \tag{2.2}
\]

### Lemma 2.1 (the rank-zero block is constant)

For every `m` in the retained domain, \(C_{m,0}=1\).

#### Proof

The only divisor `a|r(m)` with \(\Omega(a)=0\) is `a=1`.  Since
`d(m)` belongs to `C_i`,

\[
 1/2<d(m)/X_i\le1.
\]

Consequently the half-open interval
\([d(m)/X_i,2d(m)/X_i)\) contains exactly one positive integer, namely
`b=1`.  It is a divisor of `d(m)`, is coprime to `a=1`, and obeys the rank
cutoff.  Thus the `j=0` block consists of `(1,1)`.  \(\square\)

### Proposition 2.2 (three-block covariance reduction)

For every nonempty bin,

\[
 E_s-{I_s^2\over M_s}
   =\sum_{j=1}^3\sum_{\ell=1}^3\Gamma_{s;j,\ell}              \tag{2.3}
\]

and

\[
 0\le E_s-{I_s^2\over M_s}
 \le 3\sum_{j=1}^3\Gamma_{s;j,j}.                             \tag{2.4}
\]

Hence B29 hypothesis (1.9) follows from the following stronger but more
explicit diagonal condition:

\[
 \sum_{s\in\mathcal J_k}{1\over\mu_s^2}
       \sum_{j=1}^3\Gamma_{s;j,j}=o_{A,B}(X_k).                \tag{2.5}
\]

#### Proof

Because \(\Omega(r(m))=3\), every divisor `a|r(m)` has rank between zero
and three.  Thus \(A_m=\sum_{j=0}^3C_{m,j}\).  Centering this identity and
using Lemma 2.1 removes the constant rank-zero block and gives (2.3).
Pointwise Cauchy--Schwarz gives

\[
 (A_m-\mu_s)^2
 =\left(\sum_{j=1}^3
    (C_{m,j}-I_{s,j}/M_s)\right)^2
 \le3\sum_{j=1}^3(C_{m,j}-I_{s,j}/M_s)^2.
\]

Summation over the bin proves (2.4), and (2.5) then implies B29 (1.9).
\(\square\)

### Proposition 2.3 (five collision shapes)

For `j=1,2,3` and an integer `c`, let \(F_{s;j,c}\) count ordered quintuples
\((m,a,b,a',b')\) such that `m` lies in the bin, both `(a,b)` and
`(a',b')` lie in `W(m)`,

\[
 \Omega(a)=\Omega(a')=j,\qquad \Omega((a,a'))=c.              \tag{2.6}
\]

Then the three diagonal block energies of (2.2) satisfy

\[
 \begin{aligned}
 E_{s;1,1}&=F_{s;1,0}+F_{s;1,1},\\
 E_{s;2,2}&=F_{s;2,1}+F_{s;2,2},\\
 E_{s;3,3}&=F_{s;3,3}.
 \end{aligned}                                                \tag{2.7}
\]

Thus only the five gcd-rank shapes

\[
 (j,c)=(1,0),(1,1),(2,1),(2,2),(3,3)                         \tag{2.8}
\]

can occur.  Here `block` distinguishes the diagonal block energy
\(\sum_m C_{m,j}^2\) from a single gcd-rank collision count.

#### Proof

The equality between a diagonal block energy and the corresponding tuple
count is just the expansion of \(C_{m,j}^2\).  Since `a,a'|r(m)` and
\(\Omega(r(m))=3\), for `j=1` their gcd has rank zero or one.  For `j=2`,
the identity

\[
 \Omega((a,a'))+\Omega(\operatorname{lcm}(a,a'))=4
\]

and \(\operatorname{lcm}(a,a')\mid r(m)\) show that the gcd rank is at
least one and at most two.  Finally a divisor `a|r(m)` with
\(\Omega(a)=\Omega(r(m))=3\) must equal `r(m)`, so the `j=3` gcd rank is
three.  This reasoning is valuation-theoretic and remains valid when `r(m)`
has repeated prime factors.  \(\square\)

Propositions 2.2--2.3 turn the energy target into estimates for five explicit
ordered collision types.  The subtraction
\(I_{s,j}^2/M_s\) is essential: a bound for the raw collision count alone
does not measure concentration around the bin mean.
Explicitly, the numerator in the sufficient condition (2.5) is

\[
 \begin{aligned}
 \sum_{j=1}^3\Gamma_{s;j,j}
  ={}&F_{s;1,0}+F_{s;1,1}-{I_{s,1}^2\over M_s}\\
    &+F_{s;2,1}+F_{s;2,2}-{I_{s,2}^2\over M_s}\\
    &+F_{s;3,3}-{I_{s,3}^2\over M_s}.
 \end{aligned}                                                \tag{2.9}
\]

## 3. The mean is an off-diagonal-incidence question

Define

\[
 O_m:=\#\{(a,b)\in W(m):\Omega(a)\ne\Omega(b)\}.              \tag{3.1}
\]

Then, exactly,

\[
 A_m=B_m+O_m.                                                  \tag{3.2}
\]

Indeed, (1.2) partitions `W(m)` according as the two ranks agree or do not.
If \(\overline O_s=M_s^{-1}\sum_mO_m\), the bin endpoints give

\[
 \mu_s-2^{s+1}<\overline O_s\le\mu_s-2^s.                    \tag{3.3}
\]

Consequently either of the following is an explicit sufficient mean target:

\[
 \overline O_s\ge4R_k2^s
 \quad\Longrightarrow\quad \mu_s\ge4R_k2^s,                 \tag{3.4}
\]

whereas B29 (1.8) itself implies

\[
 \overline O_s>(4R_k-2)2^s.                                  \tag{3.5}
\]

Thus growth of the diagonal multiplicity `B_m` cannot by itself establish
B29 (1.8); the required mean surplus is, up to the displayed factor-two bin
loss, precisely a population of source-local witnesses with unequal ranks.
These off-diagonal incidences may be split into the countable types

\[
 (j,\ell),\qquad 0\le j\le3,\quad
 0\le\ell\le\tau_i(d(m))+j,\quad \ell\ne j,                  \tag{3.6}
\]

where `j=Omega(a)` and `ell=Omega(b)`.  The upper range is finite for each
terminal but is not uniformly bounded in the high-excess regime.

## 4. A flat-cap replacement for centered energy

### Lemma 4.1 (exact lower-tail bound under an upper cap)

Let \(x_1,\ldots,x_M\ge0\) have positive mean `mu`.  Suppose
\(x_t\le(1+\delta)\mu\) for every `t`, where \(\delta\ge0\).  For
`0<=theta<1`,

\[
 {1\over M}\#\{t:x_t<\theta\mu\}
 \le {\delta\over1+\delta-\theta}.                            \tag{4.1}
\]

#### Proof

Let `pM` be the number of indices in the displayed lower tail.  Bounding
the lower-tail entries by `theta mu` and every other entry by
`(1+delta)mu` gives

\[
 \mu\le p\theta\mu+(1-p)(1+\delta)\mu.
\]

Rearrangement proves (4.1).  Strictness of the lower-tail inequality only
strengthens the estimate.  \(\square\)

The same cap also gives the centered-energy bound

\[
 \sum_t(x_t-\mu)^2
 =\sum_tx_t^2-M\mu^2
 \le\delta M\mu^2,                                             \tag{4.2}
\]

because \(x_t^2\le(1+\delta)\mu x_t\).  Hence the cap is also a
pointwise route to B29 (1.9) whenever the additional summability condition
\(\sum_{s\in\mathcal J_k}\delta_{k,s}M_s=o_{A,B}(X_k)\) holds.  Condition
(4.6) below need not imply this variance summability when some deltas are
large; Lemma 4.1 supplies the needed one-sided estimate directly under
(4.6).

### Theorem 4.2 (flat-cap incidence criterion)

Suppose there are `R_k -> infinity`, sets
\(\mathcal J_k\subseteq\mathcal S_k\), and numbers
\(\delta_{k,s}\ge0\) such that

\[
 \sum_{s\in\mathcal S_k\setminus\mathcal J_k}M_s=o_{A,B}(X_k),
                                                               \tag{4.3}
\]

\[
 \mu_s\ge4R_k2^s\qquad(s\in\mathcal J_k),                    \tag{4.4}
\]

\[
 A_m\le(1+\delta_{k,s})\mu_s
 \quad(m\in\mathcal G_{k,s},\ s\in\mathcal J_k),            \tag{4.5}
\]

and

\[
 \sum_{s\in\mathcal J_k}
 {\delta_{k,s}\over1/2+\delta_{k,s}}M_s=o_{A,B}(X_k).         \tag{4.6}
\]

Then \(W_{k,3}^{A,B}=o_{A,B}(X_k)\).

In particular, (4.6) holds if
\(\sup_{s\in\mathcal J_k}\delta_{k,s}\to0\), because the bins
are disjoint subsets of the positive integers at most `X_k` and hence
\(\sum_sM_s\le X_k\).

#### Proof

Call `m` bad when \(A_m<R_kB_m\).  In bin `s`,

\[
 R_kB_m<R_k2^{s+1}\le\mu_s/2.
\]

Lemma 4.1 with `theta=1/2` therefore bounds the bad proportion by
\(\delta_{k,s}/(1/2+\delta_{k,s})\).  Conditions (4.3) and (4.6) show
that only `o(X_k)` high-excess terminals are bad.  Every other high-excess
terminal contributes

\[
 {B_m\over A_m}\le {1\over R_k}
\]

to the symmetric mass.  Their number is at most `X_k`, so this contribution
is `o(X_k)`.  The low-excess set has size `o(X_k)` by the audited
low-excess erasure theorem, and every one of its summands is at most one.
This proves the claim.  \(\square\)

### Strict boundary of the flat-cap route

The cap (4.5) does not follow from the mean condition (4.4).  In the abstract
array from B29, take `M` even, `B_m=1`, put `A_m=1` on half the indices and
`A_m=2R` on the other half, and take `R_k=R/4`.  Then (4.4) holds for large
`R`, but

\[
 {\max_mA_m\over\mu_s}-1\longrightarrow1,                    \tag{4.7}
\]

so no cap with `delta -> 0` is available.  This closes only the inference
“large bin mean implies flat cap”; it is not claimed that the array is
realized by maximal divisor terminals.

Conversely, the sparse arithmetic family of B29 has
\(\tau_i(d_i)\to\infty\) but \(A_m=\nu_i(m)\le2\).  Hence high source
excess alone does not even imply the mean growth (4.4), and therefore cannot
imply the complete flat-cap criterion.  That family makes no maximal-layer
claim, so it does not refute a theorem using full maximality or the rank-five
screen.

## 5. Dependency and boundary audit

1. **Maximality and screen scope.**  Propositions 2.2--2.3 and Theorem 4.2
   are stated only for the selected representations in `mathcal G_k`.
   Maximality is encoded by `i=iota_k(m)`; high excess then implies survival
   of every audited rank-five promotion block.  No estimate for the number of
   such survivors is proved here.
2. **Endpoints.**  All collision counts use exactly the weak-left,
   strict-right interval in (1.1).  Lemma 2.1 uses
   `X_i/2<d<=X_i`, so `b=1` is included even when `d=X_i` and `b=2` is
   excluded at the only possible upper endpoint.
3. **Repeated primes.**  The variables `a,a'` are integer divisors, not
   labelled prime subsets.  Proposition 2.3 uses gcd and lcm valuations and
   covers `r=p^3` and `r=p^2q` without multiplicity overcounting.
4. **Empty bins.**  Every division by `M_s` is restricted to
   \(s\in\mathcal S_k\), where `M_s>0`.
5. **What remains for rank three.**  One must prove either B29 (1.8)--(1.9),
   the off-diagonal mean target (3.4) together with (2.5), or the flat-cap
   hypotheses (4.4)--(4.6), on the actual screen survivors.  These are
   sufficient conditions, not estimates established here.
6. **Ranks at least four.**  Even a complete proof of any criterion in item
   5 settles only the rank-three symmetric target in the fixed terminal band
   and critical source strip.  Quotient ranks `q>=4`, uniformity over the
   full terminal range, and the remaining Q2 construction are separate gaps.
7. **Formalization.**  The results are paper-level reductions.  They do not
   justify conjecture-level Lean code.
