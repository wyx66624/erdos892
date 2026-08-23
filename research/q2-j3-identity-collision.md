# Erdős 892, Q2: identity-window formulas and the rank-three single-window collision

**Reviewed paper status.**  This note does not prove
the B29 centered-energy hypothesis, the rank-three estimate, Question 2, or
Erdős 892.  It sharpens the five collision shapes of
`research/q2-flat-cap-collision-reduction.md`.  Three of those shapes are
exactly within-one-window identity collisions, and the `j=3` shape is a
single half-open divisor-window problem.  The remaining two shapes are the
only genuinely cross-window collisions.

All statements below are made on the retained domain of B29: actual maximal,
high-excess terminals that survive the audited rank-five screen.  The proofs
are deterministic and do not use maximality to infer an unproved divisor
estimate.

## 1. Retained notation and window populations

Fix real `A<B`, a sufficiently large `k`, and a nonempty B29 bin
\(s\in\mathcal S_k\).  For every \(m\in\mathcal G_{k,s}\), write

\[
 i=\iota_k(m),\qquad d=d(m),\qquad r=r(m)=m/d,
 \qquad \Omega(r)=3,
\]

where `d(m)` is the least selected maximal-layer divisor.  Put
\(\tau=\tau_i(d)\).  Thus `m` is an actual maximal terminal, and the
selected triple survives every rank-five promotion block once `H_k>=4`.

For each integer divisor `a|r`, define the exact window population

\[
 Q_m(a):=\#\left\{b\mid d:\begin{array}{l}
 (a,b)=1,\\
 da/X_i\le b<2da/X_i,\\
 \Omega(b)\le\tau+\Omega(a)
 \end{array}\right\}.                                      \tag{1.1}
\]

The lower endpoint is weak and the upper endpoint is strict.  This is the
quantity denoted \(Q_{i,d,a}\) in B27.  In the notation of PR #36,

\[
 C_{m,j}=\sum_{\substack{a\mid r\\\Omega(a)=j}}Q_m(a)
 \qquad(0\le j\le3).                                        \tag{1.2}
\]

The sum is over integer divisors, not labelled prime occurrences.  Hence
(1.1)--(1.2) retain repeated factors in `r` and common factors of `d,r`
without overcounting.

## 2. The three identity shapes and the two cross shapes

Recall that \(F_{s;j,c}\) counts ordered pairs of witnesses with common
terminal, both `a`-coordinates of rank `j`, and gcd of those coordinates of
rank `c`.

### Theorem 2.1 (exact identity-window formulas) — THEOREM

For `j=1,2,3`,

\[
 \boxed{F_{s;j,j}=
 \sum_{m\in\mathcal G_{k,s}}
 \sum_{\substack{a\mid r(m)\\\Omega(a)=j}}Q_m(a)^2.}          \tag{2.1}
\]

Moreover,

\[
\begin{aligned}
 F_{s;1,0}
 &=\sum_m\left[
   \left(\sum_{\substack{a\mid r(m)\\\Omega(a)=1}}Q_m(a)\right)^2
       -\sum_{\substack{a\mid r(m)\\\Omega(a)=1}}Q_m(a)^2\right],\\
 F_{s;2,1}
 &=\sum_m\left[
   \left(\sum_{\substack{a\mid r(m)\\\Omega(a)=2}}Q_m(a)\right)^2
       -\sum_{\substack{a\mid r(m)\\\Omega(a)=2}}Q_m(a)^2\right]. \tag{2.2}
\end{aligned}
\]

Thus `(1,1)`, `(2,2)`, and `(3,3)` are precisely identity shapes
`a=a'`.  The only shapes with \(a\ne a'\) are `(1,0)` and `(2,1)`.

#### Proof

Let `a,a'` have rank `j` and suppose
\(\Omega((a,a'))=j\).  Since `(a,a')|a`, complete additivity gives

\[
 \Omega\bigl(a/(a,a')\bigr)=0,
\]

so `a=(a,a')`; the same argument gives `a'=(a,a')`.  Hence `a=a'`.
Conversely `a=a'` plainly has gcd rank `j`.  For a fixed `m,a`, the two
`b`-coordinates can therefore be chosen independently in exactly
\(Q_m(a)^2\) ordered ways.  Summing proves (2.1).

For rank one, distinct integer divisors are distinct primes, hence have gcd
one.  Expanding the square in (1.2) separates the equal and unequal
`a`-coordinates and gives the first line of (2.2).  For distinct rank-two
divisors `a,a'`,

\[
 \Omega((a,a'))+\Omega(\operatorname{lcm}(a,a'))=4.
\]

The lcm divides `r`, so its rank is at most three and the gcd rank is at
least one.  The gcd rank cannot be two, since the first paragraph would then
give `a=a'`.  It is therefore one, and the same square expansion gives the
second line.  This valuation argument includes `r=p^3`, `r=p^2q`, and
`r=pqr`. \(\square\)

### Corollary 2.2 (sharp domination of cross shapes) — THEOREM

For every nonempty bin,

\[
 F_{s;1,0}\le2F_{s;1,1},\qquad
 F_{s;2,1}\le2F_{s;2,2}.                                    \tag{2.3}
\]

The coefficient `2` is best possible for arbitrary nonnegative window
populations on the maximal eight-block factorization shape `r=pqr`.

#### Proof

The number of rank-one divisors of `r` is
\(t=\omega(r)\le\Omega(r)=3\).  Complementation `a -> r/a` bijects the
rank-one and rank-two integer divisors, even when primes repeat, so both
families have `t` members.  For nonnegative \(x_1,\ldots,x_t\),

\[
 \left(\sum_hx_h\right)^2-\sum_hx_h^2
 \le(t-1)\sum_hx_h^2\le2\sum_hx_h^2                         \tag{2.4}
\]

by Cauchy--Schwarz.  Apply (2.4) terminal by terminal to (2.2), first with
\(x_h=Q_m(a_h)\), then with \(x_h=Q_m(r/a_h)\), and sum over `m`.
For `t=3` and equal positive `x_h`, equality holds in (2.4), which proves
sharpness for the stated nonnegative-vector class.  No realization of that
equality case by maximal arithmetic terminals is asserted. \(\square\)

This reduces the five raw collision counts to the three identity-window
energies.  It does **not** by itself prove a centered estimate: raw identity
energy still contains the bin mean.

### Corollary 2.3 (three raw identity energies suffice) — CONDITIONAL

PR #36 condition (2.5), and hence B29 (1.9), follows from

\[
 \sum_{s\in\mathcal J_k}{
  3F_{s;1,1}+3F_{s;2,2}+F_{s;3,3}\over\mu_s^2}
 =o_{A,B}(X_k).                                               \tag{2.5}
\]

Indeed, PR #36 gives
\(\Gamma_{s;j,j}\le E_{s;j,j}\).  Its five-shape identity, followed by
(2.3), gives

\[
 E_{s;1,1}\le3F_{s;1,1},\qquad
 E_{s;2,2}\le3F_{s;2,2},\qquad
 E_{s;3,3}=F_{s;3,3}.
\]

This criterion is deliberately stronger than the centered target and is not
claimed to hold.  Its value is that every remaining raw count now fixes one
source window `a` instead of coupling two different windows.

### Basic factorisation instances

The formulas have the following complete index-level specialisations.

* If `r=p^3`, the rank-one/rank-two window pairs are `(p,p^2)`; both cross
  shapes vanish identically.
* If \(r=p^2q\) with \(p\ne q\), the rank-one windows are `p,q` and their
  complementary rank-two windows are `pq,p^2`.  Each cross shape has the two
  possible ordered unequal index pairs.
* If `r=pqr` with three distinct primes, there are three windows at each of
  ranks one and two, and each cross shape has six possible ordered unequal
  index pairs.

These are statements about possible `a`-indices.  A listed window may have
population zero because of the size, coprimality, or rank cutoff in (1.1).

## 3. The `j=3` block is one explicit divisor window

For an integer pair `d,r`, define the coprime core of `d` relative to `r` by

\[
 d_{\perp r}:=\prod_{p\nmid r}p^{v_p(d)}.                    \tag{3.1}
\]

This is the largest divisor of `d` coprime to `r`.  Put
\(Y_m=m/X_i=dr/X_i\).

### Theorem 3.1 (single-window identity and ratio-collision formula) — THEOREM

For every retained terminal,

\[
 C_{m,3}=Q_m(r)
 =\#\{b\mid d_{\perp r}:Y_m\le b<2Y_m,
                    \ \Omega(b)\le\tau+3\}.                 \tag{3.2}
\]

Consequently

\[
 F_{s;3,3}=\sum_m Q_m(r)^2.                                  \tag{3.3}
\]

If \(T_m:=Q_m(r)(Q_m(r)-1)\), then `T_m` is exactly the number of ordered
triples `(g,u,v)` of positive integers satisfying

\[
\begin{gathered}
 u\ne v,\qquad (u,v)=1,qquad guv\mid d_{\perp r},\\
 Y_m\le gu<2Y_m,\qquad Y_m\le gv<2Y_m,                       \tag{3.4}\\
 \Omega(gu)\le\tau+3,qquad \Omega(gv)\le\tau+3.
\end{gathered}
\]

In every such triple,

\[
 {1\over2}<{u\over v}<2,qquad u,v\ge2.                     \tag{3.5}
\]

Thus

\[
 F_{s;3,3}=I_{s,3}+\sum_mT_m.                                \tag{3.6}
\]

#### Proof

A divisor `a|r` with \(\Omega(a)=3=\Omega(r)\) must equal `r`.
Substituting `a=r` in (1.1) changes the size window to

\[
 dr/X_i\le b<2dr/X_i,
\]

and `(r,b)=1`, `b|d` are together equivalent to
\(b\mid d_{\perp r}\).  This proves (3.2), while (3.3) is Theorem 2.1.

For an ordered pair of distinct eligible divisors `(b,b')`, put

\[
 g=(b,b'),\qquad u=b/g,\qquad v=b'/g.
\]

Then `(u,v)=1`, \(u\ne v\), and
\(guv=\operatorname{lcm}(b,b')\mid d_{\perp r}\).  All remaining
conditions in (3.4) are exactly the two original window and rank conditions.
Conversely, (3.4) gives the distinct eligible ordered pair `(gu,gv)`, and
its gcd is `g`; hence the two constructions are inverse.  Dividing the two
half-open window inequalities gives the strict ratio bounds in (3.5).  If,
say, `u=1`, then `v` is a positive integer with `1<v<2`, impossible; the
same holds with `u,v` interchanged.  Finally `Q^2=Q+Q(Q-1)` gives (3.6).
\(\square\)

The formula retains every endpoint: equality at `Y_m` is allowed, equality
at `2Y_m` is not.  It also retains repeated primes through the exact gcd
parameter `g`; no squarefreeness is used.

## 4. A proved uniqueness boundary and an exceptional-core reduction

Call a positive integer `D` **dyadically divisor-separated** if any two
distinct divisors `x,y|D` satisfy

\[
 \max(x,y)\ge2\min(x,y).                                     \tag{4.1}
\]

The integer `1` and every prime power are dyadically divisor-separated.
The definition is tailored to the half-open window: equality in (4.1) still
prevents two divisors from lying together in `[Y,2Y)`.

### Proposition 4.1 (narrow-window uniqueness) — THEOREM

If \(d_{\perp r}\) is dyadically divisor-separated, then
\(C_{m,3}\in\{0,1\}\), so `T_m=0`.  In particular this holds whenever
\(d_{\perp r}=1\) or \(d_{\perp r}\) is a prime power.

Conversely, if \(C_{m,3}\ge2\), then \(d_{\perp r}\) has at least two distinct
prime divisors.

#### Proof

Two members of `[Y_m,2Y_m)` have ratio strictly between `1/2` and `2`, so
(4.1) permits at most one eligible divisor.  Distinct divisors of a prime
power have ratio at least its prime base (and the factor-two boundary is
excluded by half-openness), proving the stated example.

For the converse, Theorem 3.1 supplies coprime integers \(u,v\ge2\) with
\(uv\mid d_{\perp r}\).  A prime divisor of `u` and a prime divisor of `v` are
distinct, so the coprime core has at least two distinct prime divisors.
\(\square\)

Let

\[
 \mathcal E_{k,s}^{(3)}:=
 \{m\in\mathcal G_{k,s}:d(m)_{\perp r(m)}
       \text{ is not dyadically divisor-separated}\}.        \tag{4.2}
\]

### Corollary 4.2 (exact sufficient reduction for the `j=3` variance)
— CONDITIONAL

The following deterministic bound holds:

\[
 \Gamma_{s;3,3}
 \le M_s+
 \sum_{m\in\mathcal E_{k,s}^{(3)}} C_{m,3}^2.                 \tag{4.3}
\]

Therefore, under the B29 mean hypothesis
\(\mu_s\ge4R_k2^s\) on \(\mathcal J_k\), the `j=3` contribution to PR
#36 condition (2.5) is `o(X_k)` if

\[
 \sum_{s\in\mathcal J_k}{1\over\mu_s^2}
 \sum_{m\in\mathcal E_{k,s}^{(3)}}C_{m,3}^2=o_{A,B}(X_k).     \tag{4.4}
\]

#### Proof

Since \(\Gamma_{s;3,3}=\sum_m(C_{m,3}-I_{s,3}/M_s)^2\),

\[
 \Gamma_{s;3,3}\le\sum_mC_{m,3}^2.
\]

Proposition 4.1 bounds each summand outside the exceptional set by one,
which proves (4.3).  Also `s>=0`, so `mu_s>=4R_k` and

\[
 \sum_{s\in\mathcal J_k}{M_s\over\mu_s^2}
 \le {1\over16R_k^2}\sum_sM_s
 \le {X_k\over16R_k^2}=o(X_k).                               \tag{4.5}
\]

Combining (4.3)--(4.5) proves the conditional assertion. \(\square\)

Condition (4.4) is not proved here.  It is a smaller target supported only
on terminals whose coprime source core has two divisors less than a factor
two apart; it still retains full maximality and rank-five-screen survival.

## 5. Centered fixed-slot reduction

For each `m`, order the distinct primes dividing `r(m)` as
\(p_{m,1}<\cdots<p_{m,t_m}\), where
\(t_m=\omega(r(m))\le3\), and pad with
zeros through slot three.  Define

\[
 x_{m,h}=Q_m(p_{m,h}),\qquad
 y_{m,h}=Q_m(r(m)/p_{m,h}),\qquad z_m=Q_m(r(m)),               \tag{5.1}
\]

with `x_{m,h}=y_{m,h}=0` for `h>t_m`.  Let `V_s(x_h)`, `V_s(y_h)`, and
`V_s(z)` denote the unnormalised centered sums over the bin; explicitly, for
any terminal statistic `w_m`,

\[
 V_s(w):=\sum_{m\in\mathcal G_{k,s}}
 \left(w_m-{1\over M_s}\sum_{m'\in\mathcal G_{k,s}}w_{m'}\right)^2.
                                                                    \tag{5.2}
\]

### Proposition 5.1 (seven single-window variances suffice) — CONDITIONAL

For every nonempty bin,

\[
 \Gamma_{s;1,1}\le3\sum_{h=1}^3V_s(x_h),\qquad
 \Gamma_{s;2,2}\le3\sum_{h=1}^3V_s(y_h),\qquad
 \Gamma_{s;3,3}=V_s(z).                                      \tag{5.3}
\]

Consequently PR #36 condition (2.5), and hence B29 (1.9), follows from

\[
 \sum_{s\in\mathcal J_k}{1\over\mu_s^2}
 \left(3\sum_{h=1}^3[V_s(x_h)+V_s(y_h)]+V_s(z)\right)
 =o_{A,B}(X_k).                                               \tag{5.4}
\]

#### Proof

The complement map gives
\(C_{m,1}=\sum_hx_{m,h}\), \(C_{m,2}=\sum_hy_{m,h}\), and Theorem
3.1 gives \(C_{m,3}=z_m\).  Center each identity over the bin and apply

\[
 (w_1+w_2+w_3)^2\le3(w_1^2+w_2^2+w_3^2)
\]

terminal by terminal.  This proves (5.3).  Summing and invoking PR #36
Proposition 2.2 proves (5.4). \(\square\)

The ordering by numerical prime size is deterministic.  It introduces no
labelled-prime multiplicity and remains valid for `p^3` and `p^2q`.

## 6. Strict boundary of coarse divisor-count information

The total number of divisors of the coprime core does not determine its
single-window collision behaviour.  The prime powers `D=3^N` have
\(N+1\to\infty\) divisors, but every half-open factor-two interval contains at
most one divisor of `D`.  Conversely `D=15` has only four divisors, while
the window `[3,6)` contains the two divisors `3,5` and hence one obtains two
ordered off-diagonal pairs.

This is a **BARRIER** only to a route using the scalar divisor count (or
the total divisor count) without the logarithmic positions of the divisors.
The two displayed cores are local window examples; they are not asserted to
be actual maximal rank-five-screen survivors and therefore do not refute
(4.4), B29, the rank-three estimate, or Q2.

## 7. Dependency and boundary audit

1. **Maximality.**  Every summation theorem is stated on
   \(m\in\mathcal G_{k,s}\).  Maximality fixes \(i=\iota_k(m)\) and high excess
   supplies rank-five-screen survival.  No proof above converts those facts
   into the missing analytic estimate (4.4) or (5.4).
2. **Endpoints.**  All windows are weak on the left and strict on the right.
   The strict ratio in (3.5) and the factor-two equality case in Proposition
   4.1 both use this convention.
3. **Repeated primes.**  `a` ranges over integer divisors.  Complementation
   bijects rank-one and rank-two divisors even for `r=p^3` and `r=p^2q`.
   The core (3.1) removes whole prime-power components sharing a prime with
   `r`, exactly as required by `(b,r)=1`.
4. **Empty bins.**  Division by `M_s` occurs only for
   \(s\in\mathcal S_k\), so \(M_s>0\).
5. **Exact advance.**  The five raw shapes reduce to three identity-window
   energies; `j=3` reduces to one divisor window and an exact coprime
   ratio-collision count.  Its variance is automatic away from (4.2), under
   the retained B29 mean hypothesis.
6. **Open gap.**  One must estimate the exceptional-core energy (4.4), the
   seven fixed-slot variances (5.4), or another B29/PR #36 sufficient
   condition on the actual survivors.  Ranks at least four and the full Q2
   construction remain separate.
7. **Lean.**  This is a paper-level partial result.  It does not justify
   conjecture-level Lean formalisation.
