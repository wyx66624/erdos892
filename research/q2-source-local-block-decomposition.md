# Erdős 892, Q2: source-local block decomposition of the rank-three multiplicity

**Reviewed paper status.** This note does not prove the rank-three estimate
\(W_{k,3}^{A,B}=o(X_k)\), and therefore does not decide Q2.  It proves an
exact finite-block formula for its summand.  The formula localizes the
size-conditioned rank problem from all divisors of the terminal integer to at
most eight explicit divisor windows of one selected source anchor.  It also
isolates an unranked block-population estimate which is sufficient for the
rank-three target and is logically weaker than the previously proposed
maximum-atom statement (AC).

Retain all notation of `research/q2-maximal-swap-rank3.md` and
`research/q2-rank3-excess-screen.md`.  In particular,

\[
 L_i=\lceil T_i\rceil,\qquad
 \mathcal D_i(m)=\{e\in C_i:e\mid m\},\qquad
 \nu_i(m)=|\mathcal D_i(m)|,
\]

and \(f_{i,3}(m)\) is the number of \(e\in\mathcal D_i(m)\) for which
\(\Omega(m/e)=3\).

## 1. The source-local blocks

Fix integers \(i<k\), an odd integer \(m\), and a representation

\[
 m=dr,\qquad d\in C_i,\qquad \Omega(r)=3.
 \tag{1.1}
\]

Put

\[
 \tau=\tau_i(d):=\Omega(d)-L_i\ge0.
\]

For every divisor \(a\mid r\) and integer \(h\ge0\), define

\[
 \begin{split}
 N_{i,d,a}(h):=\#\bigg\{b\mid d:\;&(a,b)=1,\quad
       \frac{da}{X_i}\le b<\frac{2da}{X_i},\\
     &\Omega(b)=h\bigg\}.
 \end{split}
 \tag{1.2}
\]

Also put

\[
 Q_{i,d,a}:=\sum_{0\le h\le \tau+\Omega(a)}N_{i,d,a}(h),
 \qquad
 D_{i,d,a}:=N_{i,d,a}(\Omega(a)).
 \tag{1.3}
\]

These are finite sets.  No distributional hypothesis is included in the
definition.  The interval in (1.2) is half-open because the pool interval is
\((X_i/2,X_i]\).

### Proposition 1.1 (exact same-layer block decomposition)

Under (1.1),

\[
 \boxed{\displaystyle
 \nu_i(m)=\sum_{a\mid r}Q_{i,d,a}}
 \tag{1.4}
\]

and

\[
 \boxed{\displaystyle
 f_{i,3}(m)=\sum_{a\mid r}D_{i,d,a}}.
 \tag{1.5}
\]

In particular,

\[
 \frac{f_{i,3}(m)}{\nu_i(m)}
 =\frac{\sum_{a\mid r}D_{i,d,a}}
        {\sum_{a\mid r}Q_{i,d,a}}.
 \tag{1.6}
\]

The formula is valid with repeated prime factors in \(r\).  The index set is
the set of integer divisors of \(r\), so it has at most eight members because
\(\Omega(r)=3\).

#### Proof

For \(e\in\mathcal D_i(m)\), use the canonical coprime-swap decomposition

\[
 g=(d,e),\qquad b=d/g,qquad a=e/g.
 \tag{1.7}
\]

Since \(e\mid dr\), Euclid's lemma gives \(a\mid r\); clearly \(b\mid d\),
\((a,b)=1\), and

\[
 e=\frac d b a.
 \tag{1.8}
\]

Conversely, every pair \((a,b)\) with \(a\mid r\), \(b\mid d\), and
\((a,b)=1\) defines through (1.8) a divisor of \(m\).  It is important that
this correspondence is bijective, not merely surjective: from (1.8) and
\((a,b)=1\),

\[
 (d,e)=d/b,
\]

so (1.7) recovers \((a,b)\) uniquely.

The size condition \(e\in(X_i/2,X_i]\) is exactly

\[
 \frac{da}{X_i}\le b<\frac{2da}{X_i}.
 \tag{1.9}
\]

Complete additivity of \(\Omega\) and \(\Omega(d)=L_i+\tau\) show that the
pool-rank condition is

\[
 \Omega(e)=L_i+\tau+\Omega(a)-\Omega(b)\ge L_i
 \quad\Longleftrightarrow\quad
 \Omega(b)\le\tau+\Omega(a).
 \tag{1.10}
\]

Equations (1.7)--(1.10) partition \(\mathcal D_i(m)\) into the blocks counted
by (1.3), proving (1.4).

Finally,

\[
 \Omega(m/e)=\Omega(br/a)=\Omega(b)+3-\Omega(a).
 \tag{1.11}
\]

Thus the complementary quotient has rank three exactly when
\(\Omega(b)=\Omega(a)\).  This proves (1.5) and (1.6). \(\square\)

### Boundary check 1.2 (the unavoidable singleton block)

For \(a=1\), one has

\[
 Q_{i,d,1}=D_{i,d,1}=1.
 \tag{1.12}
\]

Indeed \(d/X_i\in(1/2,1)\), because \(d\) is odd while \(X_i\) is a power
of two, so the half-open interval
\([d/X_i,2d/X_i)\subset(1/2,2)\) contains exactly the positive odd divisor
\(b=1\) of \(d\).  This pair recovers the originally selected divisor \(d\).

Consequently a proposed estimate of the form

\[
 \max_{a\mid r}\frac{D_{i,d,a}}{Q_{i,d,a}}=o(1)
\]

is impossible for every rank-three representation: its \(a=1\) term is
identically one.  This is a strict logical obstruction only to *uniform
blockwise* anti-concentration.  It does not obstruct aggregate domination by
the nontrivial blocks.

Writing

\[
 Q^+_{i,d,r}:=\sum_{\substack{a\mid r\\a>1}}Q_{i,d,a},
 \qquad
 D^+_{i,d,r}:=\sum_{\substack{a\mid r\\a>1}}D_{i,d,a},
 \tag{1.13}
\]

the exact ratio becomes

\[
 \frac{f_{i,3}(m)}{\nu_i(m)}
 =\frac{1+D^+_{i,d,r}}{1+Q^+_{i,d,r}}.
 \tag{1.14}
\]

This is the useful aggregate form.

### Basic and extreme cases

For every block, \(0\le D_{i,d,a}\le Q_{i,d,a}\).  If
\(r=p^3\), the decomposition has the four blocks
\(a=1,p,p^2,p^3\); if \(r=pqs\) with three distinct primes, it has the
maximal eight blocks.  When \(\tau=0\), the \(a\)-block admits only
\(\Omega(b)\le\Omega(a)\), so its diagonal is its top allowed rank.  At the
opposite extreme, increasing \(\tau\) enlarges every denominator block but
does not change its diagonal rank.  This monotonicity in the rank cutoff is
one reason (1.14) can be more accessible than a maximum-atom local limit
statement.  A block may nevertheless be empty because its size window lies
outside the divisor range of \(d\); no non-emptiness is assumed.

## 2. A weaker sufficient condition than maximum-atom (AC)

For fixed \(A<B\), let \(\mathcal N_k^{A,B}\) be the set of terminal
integers \(m\in C_k^{A,B}\) such that

\[
 i=\iota_k(m)\in I_k,
 \qquad f_{i,3}(m)>0.
\]

For each such \(m\), select deterministically one representation

\[
 m=d(m)r(m),\qquad d(m)\in\mathcal D_i(m),\qquad \Omega(r(m))=3;
 \tag{2.1}
\]

for example choose the least eligible \(d(m)\).  Define \(Q^+(m)\) and
\(D^+(m)\) by (1.13) for this selected representation.

### Corollary 2.1 (source-local domination criterion)

Suppose there is a sequence \(R_k\to\infty\) for which

\[
 \#\left\{m\in\mathcal N_k^{A,B}:
 1+Q^+(m)<R_k\bigl(1+D^+(m)\bigr)\right\}=o_{A,B}(X_k).
 \tag{2.2}
\]

Then

\[
 W_{k,3}^{A,B}=o_{A,B}(X_k).
 \tag{2.3}
\]

#### Proof

Every \(m\in\mathcal N_k^{A,B}\) contributes
\(f_{i,3}(m)/\nu_i(m)\) to \(W_{k,3}^{A,B}\).  This statement is
independent of which rank-three representation was selected.  Proposition
1.1 computes that contribution using the selected representation as
\((1+D^+(m))/(1+Q^+(m))\).

On the complement of the exceptional set in (2.2), the ratio is at most
\(1/R_k\).  On the exceptional set it is at most one.  Since
\(|\mathcal N_k^{A,B}|\le X_k\), summing gives

\[
 W_{k,3}^{A,B}
 \le X_k/R_k+o_{A,B}(X_k)=o_{A,B}(X_k).
 \]

\(\square\)

This criterion asks only that, for almost all relevant maximal terminal
integers, the cumulative population of the allowed source-divisor blocks
dominates their fixed-rank diagonal population.  It does **not** ask for a
bound on the maximum atom over every rank, as (AC) does.

At the level of finite probability laws this distinction is strict: a target
atom may tend to zero while a different atom remains, say, \(1/2\).  Thus
control of the particular diagonal in (1.14) does not logically imply the
maximum-atom bound used in (AC).  No assertion is made here that every such
abstract law is realized by divisor blocks.

### Corollary 2.2 (an unranked block-population target)

Uniformly for \(m\in\mathcal N_k^{A,B}\),

\[
 1+D^+(m)=f_{i,3}(m)
 \le \binom{\Omega(m)}3
 \ll_{A,B}(\log k)^3.
 \tag{2.4}
\]

Consequently, (2.3) follows if there is \(R_k\to\infty\) such that, outside
an \(o_{A,B}(X_k)\) subset of \(\mathcal N_k^{A,B}\),

\[
 Q^+(m)\ge R_k(\log k)^3.
 \tag{2.5}
\]

#### Proof

A divisor of \(m\) having \(\Omega=3\) is obtained by choosing three prime
occurrences from a labelled list of the \(\Omega(m)\) prime occurrences.
The map from such triples to divisors may fail to be injective when primes
repeat, but it is surjective.  Hence their number is at most
\(\binom{\Omega(m)}3\).  The map \(e\mapsto m/e\) injects the complements
counted by \(f_{i,3}(m)\) into the divisors of \(m\) having \(\Omega=3\), so
the first inequality follows.  Surjectivity is neither asserted nor needed,
because an arbitrary rank-three divisor need not have its complementary
factor in the pool \(C_i\).

The terminal upper band gives

\[
 \Omega(m)\le U_k+B\sqrt{U_k}=O_B(\log k),
\]

which proves (2.4).  Condition (2.5) then implies (2.2), after changing the
implicit constant in \(R_k\), and Corollary 2.1 applies. \(\square\)

Condition (2.5) is deliberately coarse.  Its possible value is that it
removes the rank coordinate entirely from the desired *denominator* estimate:
one may count every divisor \(b\) in the seven or fewer explicit windows
(1.2), up to the excess budget, rather than prove a two-dimensional local
limit theorem.  It is an alternative sufficient mechanism, not an established
estimate.

## 3. Relation to the rank-five screen

The blocks above are a same-layer multiplicity mechanism.  They use

\[
 b\in[da/X_i,2da/X_i)
\]

and produce another divisor \(da/b\in C_i\).  The rank-five promotion screen
uses

\[
 b\in[dp/X_j,2dp/X_j),\qquad j>i,
\]

and produces a later divisor in \(C_j\), contradicting maximality.  Therefore
the two estimates are not substitutes:

* many same-layer blocks make the reciprocal multiplicity small;
* a later-layer block removes the candidate altogether.

Both mechanisms remain live, and they can be combined by applying the
rank-five screen first and (1.14) only to its survivors.

## 4. Quantifier and dependency audit

1. **Exact identities.** Proposition 1.1 holds for every finite
   \(i<k\), every odd \(m\), and every representation (1.1).  It uses no
   maximality, no asymptotic theorem, and no unproved distributional input.
2. **Maximality.** Maximality enters Corollary 2.1 only through the definition
   of the terminal family and its layer \(i=\iota_k(m)\).
3. **Repeated primes.** Divisors \(a\mid r\) are integer divisors, not labelled
   prime subsets.  The canonical gcd pair makes (1.4)--(1.5) bijective even
   when \(r=p^3\) or shares primes with \(d\).
4. **Endpoints.** The weak lower and strict upper bounds in (1.2) are exactly
   equivalent to \(X_i/2<da/b\le X_i\); no endpoint is discarded.
5. **External inputs.** None are used in Proposition 1.1 or Corollary 2.1.
   Corollary 2.2 uses only the already defined terminal upper band and an
   elementary labelled-prime-occurrence upper bound.
6. **Remaining gap.** Neither (2.2) nor (2.5) is proved.  A valid next theorem
   must show that the low-aggregate-block survivors of the full maximality
   condition form \(o(X_k)\); pointwise high excess is insufficient, as the
   family in Section 6 of `research/q2-rank3-excess-screen.md` has
   \(\nu_i(m)\le8\).
7. **Claim boundary.** Even proving Corollary 2.1's hypothesis settles only
   the rank-three symmetric target.  Ranks \(q\ge4\), uniformity up to the
   terminal \(O(\sqrt{\log k})\) range, and the full Q2 construction remain
   separate dependencies.  No Lean formalization is justified at this stage.

## 5. Next minimal analytic target

After applying the low-excess erasure and the rank-five screen, select one
rank-three maximal representation for every surviving terminal integer.  The
closest new target is to prove, for some \(R_k\to\infty\),

\[
 \#\{m\in\mathcal N_k^{A,B}:\ Q^+(m)<R_k(1+D^+(m))\}=o(X_k).
 \tag{5.1}
\]

This is a seven-window, source-local divisor-population statement.  It retains
all common-prime dependencies through \((a,b)=1\), but it only compares the
fixed ranks \(\Omega(b)=\Omega(a)\le3\) against the cumulative allowed ranks
\(\Omega(b)\le\tau+\Omega(a)\).  Thus it is strictly more targeted than a
full maximum-atom local limit theorem and mathematically distinct from the
later-layer rank-five screen.
