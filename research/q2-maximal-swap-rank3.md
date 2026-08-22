# Erdős 892, Question 2: maximal-anchor swap decomposition and the rank-three boundary

**Status (22 August 2026).**  This note does not prove admissibility or
inadmissibility of the logarithmic-barrier profile.  It studies only the true
terminal set after a maximal old anchor has been selected.  In particular, none
of the conclusions below replaces the actual union by the anchorwise sum already
ruled out by Proposition Q2.1 of `research/q2-actual-union.md`.

The main unconditional conclusions are:

1. maximality has an exact *coprime-swap* characterization which includes all
   later divisors, comparable or incomparable with the selected anchor;
2. after the maximal layer is identified, the actual union has an exact
   reciprocal-multiplicity bilinear formula;
3. terminal rank can be truncated once for the whole actual union;
4. selected quotients of any fixed rank $q\le 2$ contribute $o(X_k)$;
5. rank $3$ is the first genuine obstruction: even inside a bounded terminal
   Ω-band, the corresponding unweighted candidate-pair count is
   $\Omega(X_k)$.  Hence maximality or representation multiplicity, rather than
   terminal membership alone, must be used from rank $3$ onward.

All uses of Mertens, the dyadic prime number theorem, fixed-rank
Hardy--Ramanujan bounds, Erdős--Kac, and Turán--Kubilius are explicitly marked.

## 1. Setup and the true maximal-anchor set

Retain

\[
 n_i=\left\lceil i+i(\log(i+1))^2\right\rceil,
 \qquad X_i=2^{n_i},\qquad U_i=\log\log X_i,
\]

\[
 T_i=U_i+A\sqrt{U_i},\qquad
 C_i=\{d\in(X_i/2,X_i]:d\text{ odd},\ \Omega(d)\ge T_i\},
 \tag{1.1}
\]
where $A>0$ is fixed.  For $m\in C_k$ which has an old pool
divisor, define

\[
 \iota_k(m)=\max\{i<k:\text{ some }d\in C_i\text{ divides }m\},
 \qquad
 \nu_i(m)=\#\{d\in C_i:d\mid m\}.
 \tag{1.2}
\]

Thus $\nu_{\iota_k(m)}(m)\ge1$.  For an index set
$I\subseteq\{1,\ldots,k-1\}$, the actual maximal-anchor portion is

\[
 \mathcal M_k(I)=\{m\in C_k:\iota_k(m)\in I\}.
 \tag{1.3}
\]

The critical strip used below is

\[
 I_k=\{i\in\mathbb Z:k/3\le i\le2k/5\}.
 \tag{1.4}
\]

Everything in (1.2)--(1.4) is a terminal statement: an integer $m$ is
charged once, according to the largest layer which actually divides it.

## 2. Exact coprime-swap characterization of maximality

The promotion argument in the stage manuscript tests divisors $da\mid dr$,
and therefore sees only later divisors which are multiples of $d$.  A later
divisor need not be comparable with $d$.  The following elementary lemma gives
the exact missing parametrization.

### Proposition 2.1 (coprime divisor swaps) -- proved

Let $d,r,e$ be positive integers and put $m=dr$.  Then $e\mid m$ if
and only if there are divisors $a\mid r$, $b\mid d$ such that

\[
 (a,b)=1,\qquad e=\frac d b\,a.
 \tag{2.1}
\]

In the forward direction the pair can be chosen canonically as

\[
 g=(d,e),\qquad b=d/g,\qquad a=e/g.
 \tag{2.2}
\]

Consequently, if $d\in C_i$, $d\mid m$, and $r=m/d$, then $i$
is the largest old hit of $m$ if and only if for no $i<j<k$ do there
exist $a\mid r$, $b\mid d$, $(a,b)=1$, with

\[
 \frac d b a\in C_j.
 \tag{2.3}
\]

#### Proof

Suppose first that $e\mid dr$, and define $g,a,b$ by (2.2).  Then
$(a,b)=1$.  Dividing $e\mid dr$ by $g$ gives $a\mid br$, so
Euclid's lemma gives $a\mid r$.  Also $b\mid d$ and
$e=(d/b)a$, proving the forward implication.

Conversely, if $a\mid r$ and $b\mid d$, then
$(d/b)a\mid dr$, prime by prime; the coprimality condition makes (2.1)
the canonical form but is not needed for this last divisibility.  Applying the
equivalence to each divisor $e\in C_j$, $i<j<k$, proves (2.3). □

### The swap spectrum

For $d\mid m=dr$, define the coprime size--rank swap spectrum

\[
 \Sigma(d,r)=
 \left\{
 \left(\log_2\frac ab,\ \Omega(a)-\Omega(b)\right):
 a\mid r,\ b\mid d,\ (a,b)=1
 \right\}\subset\mathbb R\times\mathbb Z.
 \tag{2.4}
\]

Write

\[
 \sigma_i(d)=\log_2(X_i/d)\in[0,1).
\]

In the pool application \(m=dr\) is odd, so \(d,r\), and every divisor
\(e\mid m\) are automatically odd.  Complete additivity of Ω and direct comparison
with the endpoints of $C_j$ then show that (2.3) is equivalent to

\[
 \Sigma(d,r)\cap
 \bigcup_{i<j<k}
 \left(
   (n_j-n_i+\sigma_i(d)-1,n_j-n_i+\sigma_i(d)]
   \times[T_j-\Omega(d),\infty)
 \right)=\varnothing.
 \tag{2.5}
\]

Indeed, for $e=(d/b)a$,

\[
 \log_2 e=n_i-\sigma_i(d)+\log_2(a/b),
 \qquad
 \Omega(e)=\Omega(d)+\Omega(a)-\Omega(b).
\]

The slice $b=1$ of (2.4) is exactly the quotient-divisor spectrum used by
the promotion sets $A_{i,k}(d)$ and $E^\square_{i,k}(d)$.  Thus (2.5),
not the $b=1$ slice, is the exact maximality condition.  If $(d,r)=1$
and

\[
 \Lambda(n)=\{(\log_2 c,\Omega(c)):c\mid n\},
\]

then every divisor pair is automatically coprime and

\[
 \Sigma(d,r)=\Lambda(r)-\Lambda(d)
 \tag{2.6}
\]

as a Minkowski difference.  This gives a precise additive-combinatorial object
for a future container or bilinear argument.

## 3. Exact actual-union bilinear identity

For $m$ with $\iota_k(m)=i$, summing over every maximal-layer divisor with
weight $1/\nu_i(m)$ charges $m$ exactly once.  Therefore

\[
 |\mathcal M_k(I)|=
 \sum_{i\in I}\ \sum_{d\in C_i}\
 \sum_{\substack{r\ge1:\ dr\in C_k\\ \iota_k(dr)=i}}
 \frac1{\nu_i(dr)}.
 \tag{3.1}
\]

This is an identity, not a union bound.  Proposition 2.1 permits the condition
$\iota_k(dr)=i$ in (3.1) to be replaced exactly by the swap-spectrum
avoidance (2.5).

The terminal and anchor intervals force every quotient in the $i$-th summand
to lie in

\[
 \mathcal R_{i,k}=
 \left(\frac{X_k}{2X_i},\frac{2X_k}{X_i}\right).
 \tag{3.2}
\]

For all sufficiently large $i$, $X_{i+1}/X_i>4$.  Hence the intervals
$\mathcal R_{i,k}$ are pairwise disjoint: the upper endpoint for $i+1$
is smaller than the lower endpoint for $i$.  Thus the quotient $r$ itself
determines its possible anchor index $i$.  Formula (3.1) may consequently be
viewed as one terminal bilinear sum over the disjoint union
$\bigcup_{i\in I}\mathcal R_{i,k}$, retaining both the maximality
indicator and the reciprocal multiplicity.  Dropping either of those two
features returns to an overcount which need not be $o(X_k)$; Section 6 makes
this sharp at quotient rank three.

#### Proof of (3.1) and (3.2)

For fixed $m\in\mathcal M_k(I)$, the only nonzero outer index is
$i=\iota_k(m)$.  There are exactly $\nu_i(m)$ eligible divisors $d$, and
each contributes $1/\nu_i(m)$, proving (3.1).  If $m=dr$, then
$m>X_k/2$, $d\le X_i$ imply $r>X_k/(2X_i)$, while $m\le X_k$,
$d>X_i/2$ imply $r<2X_k/X_i$.  Finally,
$X_{i+1}/X_i=2^{n_{i+1}-n_i}>4$ eventually, which proves disjointness. □

## 4. One terminal rank truncation for the whole actual union

### Proposition 4.1 (terminal Ω-lifting) -- proved modulo Turán--Kubilius

For $B>A$, put

\[
 C_k^{\le B}=
 \{m\in C_k:\Omega(m)\le U_k+B\sqrt{U_k}\}.
 \tag{4.1}
\]

There is an absolute $C$ such that, uniformly for all sufficiently large
$k$ and $B>0$,

\[
 |C_k\setminus C_k^{\le B}|\le \frac{C}{B^2}X_k.
 \tag{4.2}
\]

If $m\in C_k^{\le B}$, $d\in C_i$, $d\mid m$, and $r=m/d$, then

\[
 \Omega(r)\le Q_{i,k}(B):=
 U_k+B\sqrt{U_k}-U_i-A\sqrt{U_i}.
 \tag{4.3}
\]

Uniformly for $ak\le i\le bk$, where $0<a<b<1$ are fixed,

\[
 Q_{i,k}(B)
 \le (B-A)\sqrt{U_k}+O_{a,A}(1)
 \tag{4.4}
\]

for each fixed $B$.  In particular,

\[
 |\mathcal M_k(I)|
 \le \frac{C}{B^2}X_k+
 |\mathcal M_k(I)\cap C_k^{\le B}|.
 \tag{4.5}
\]

This pays the upper-rank exceptional set once at the terminal level; there is
no sum over anchors.

#### Proof

The Turán--Kubilius estimate for the additive function Ω gives

\[
 \sum_{n\le x}(\Omega(n)-\log\log x)^2
 \ll x\log\log x.
 \tag{4.6}
\]

Chebyshev's inequality bounds the number of all $n\le X_k$ above the
threshold in (4.2) by $O(X_k/B^2)$; restricting to the odd terminal dyadic
interval only decreases the count.  Since Ω is completely additive,

\[
 \Omega(r)=\Omega(m)-\Omega(d)
 \le U_k+B\sqrt{U_k}-T_i,
\]

which is (4.3).  Regular variation gives, uniformly on a fixed proportional
strip,

\[
 U_k-U_i=\log(n_k/n_i)=O_a(1),\qquad
 \sqrt{U_k}-\sqrt{U_i}=O_a(U_k^{-1/2}).
\]

Substitution proves (4.4), and (4.5) is the terminal partition. □

For a future closure it would be enough to prove, for every fixed $B>A$,

\[
 |\mathcal M_k(I_k)\cap C_k^{\le B}|=o_{A,B}(X_k),
 \tag{4.7}
\]

and then let $B\to\infty$ in (4.5).  Proposition 4.1 does not prove
(4.7); it identifies the exact rank range which a maximal-anchor estimate must
handle.

## 5. Fixed quotient rank: a complete actual-union bound

### Theorem 5.1 (fixed-rank maximal quotients) -- proved modulo the standard fixed-rank bound

Fix $0<a<b<1/2$ and an integer $q\ge1$.  Choose any deterministic
maximal-anchor rule: for each $m\in\mathcal M_k([ak,bk])$, select one
$d_*(m)\in C_{\iota_k(m)}$ dividing $m$, and put
$r_*(m)=m/d_*(m)$.  Then

\[
 \#\{m\in\mathcal M_k([ak,bk]):\Omega(r_*(m))\le q\}
 \ll_{a,b,q} X_k(\log k)^{q-3}.
 \tag{5.1}
\]

In particular,

\[
 \#\{m\in\mathcal M_k([ak,bk]):\Omega(r_*(m))\le2\}
 \ll_{a,b}\frac{X_k}{\log k}=o(X_k).
 \tag{5.2}
\]

The estimate is uniform in the deterministic choice rule.  In fact its proof
does not need maximality after the selected triples have been injected into the
larger set of all pairs; hence it is a genuine upper bound for this part of the
actual terminal union.

#### Proof

The map

\[
 m\longmapsto(\iota_k(m),d_*(m),r_*(m))
\]

is injective.  For a fixed $i\in[ak,bk]$, (3.2) places $r_*(m)$ below

\[
 R_{i,k}=2X_k/X_i.
\]

Uniformly on the strip,

\[
 \log R_{i,k}\asymp_{a,b} k(\log k)^2,
 \qquad \log\log R_{i,k}\asymp\log k.
 \tag{5.3}
\]

The fixed-rank Hardy--Ramanujan estimate gives, for fixed $q$,

\[
 \#\{r\le R:\Omega(r)\le q\}
 \ll_q \frac{R(\log\log R)^{q-1}}{\log R}.
 \tag{5.4}
\]

There are at most $X_i$ choices for $d$.  Equations (5.3)--(5.4)
therefore bound all selected triples with this $i$ by

\[
 X_i\,\frac{(2X_k/X_i)(\log k)^{q-1}}
 {k(\log k)^2}
 \ll_{a,b,q}\frac{X_k}{k}(\log k)^{q-3}.
\]

Summing over fewer than $k$ indices proves (5.1), and $q=2$ gives
(5.2). □

Thus quotient ranks $0,1,2$ are harmless even before the full swap condition
is exploited.  The estimate becomes only $O(X_k)$ at $q=3$, and this loss is
real at the level of candidate pairs.

## 6. A strict rank-three barrier inside the true terminal pool

For $A<B$, define the two-sided band

\[
 C_i^{A,B}=\{d\in(X_i/2,X_i]:d\text{ odd},\
 U_i+A\sqrt{U_i}\le\Omega(d)\le U_i+B\sqrt{U_i}\}.
 \tag{6.1}
\]

By the odd dyadic Erdős--Kac theorem,

\[
 |C_i^{A,B}|\gg_{A,B}X_i.
 \tag{6.2}
\]

### Proposition 6.1 (rank-three terminal pair barrier) -- proved modulo the audited Q2.1 inputs

Fix $B>A$, and let $B_0=(A+B)/2$.  For every sufficiently large $k$,
consider the candidate-pair count

\[
 \begin{split}
 P_{k,3}^{A,B}:=
 \sum_{i\in I_k}\ \sum_{d\in C_i^{A,B_0}}
 \#\{r\in E^\square_{i,k}(d):
       \Omega(r)=3,\ dr\in C_k^{A,B}\}.
 \end{split}
 \tag{6.3}
\]

Then

\[
 P_{k,3}^{A,B}\gg_{A,B}X_k.
 \tag{6.4}
\]

Consequently the proposed relaxation

> "after imposing the genuine terminal Ω-band, sum the rank-three
> avoidance candidates over $(i,d)$ and prove that the pair count is
> $o(X_k)$"

is false.  This is a strict counterexample to that *pair-count route*, not a
lower bound for the actual union and not an inadmissibility result.

#### Proof

The proof of Proposition Q2.1 constructs, uniformly for
$i\in I_k$ and every odd $d\in(X_i/2,X_i]$, a subset

\[
 \mathcal E^{(3)}_{i,k}(d)\subseteq E^\square_{i,k}(d)
\]

consisting of numbers $r=pqs$, with $p,q,s$ distinct odd primes, and

\[
 |\mathcal E^{(3)}_{i,k}(d)|\gg \frac{X_k}{di}.
 \tag{6.5}
\]

Here $p,q$ form the good semiprime $u$, while $s$ is the prime counted
in the moving dyadic interval.  Hence every constructed quotient has exactly
three prime factors with multiplicity.

Uniformly for $i\in I_k$, regular variation gives

\[
 T_k-T_i=\log(k/i)+o_A(1)\le\log3+o_A(1)<3.
 \tag{6.6}
\]

Thus, for $d\in C_i^{A,B_0}$ and
$r\in\mathcal E^{(3)}_{i,k}(d)$,

\[
 \Omega(dr)=\Omega(d)+3>T_k.
\]

The size condition in $E^\square$ gives $dr\in(X_k/2,X_k]$.
For the upper rank bound, again uniformly on the strip,

\[
 U_i+B_0\sqrt{U_i}+3
 <U_k+B\sqrt{U_k}
 \tag{6.7}
\]

for all sufficiently large $k$, because
$(B-B_0)\sqrt{U_k}\to\infty$ while $U_k-U_i=O(1)$.
Therefore every product in (6.5) lies in the genuine terminal band
$C_k^{A,B}$.

Using (6.2), $d\le X_i$, and (6.5), the contribution of one index is

\[
 \sum_{d\in C_i^{A,B_0}}|\mathcal E^{(3)}_{i,k}(d)|
 \gg \frac{X_k}{i}\sum_{d\in C_i^{A,B_0}}\frac1d
 \ge \frac{X_k}{i}\frac{|C_i^{A,B_0}|}{X_i}
 \gg_{A,B}\frac{X_k}{i}.
\]

Finally,

\[
 \sum_{i\in I_k}\frac1i\longrightarrow\log(6/5)>0,
\]

which proves (6.4). □

There are two broad mechanisms by which (6.4) can coexist with a small actual
maximal-anchor union:

1. many candidate pairs produce the same terminal integer, and the factor
   $1/\nu_i(m)$ in (3.1) removes their multiplicity; or
2. a candidate $d$ is not genuinely maximal because of a later divisor omitted
   by the finite $E^\square$ screen.  This includes both a comparable
   $b=1$ promotion in an unscreened far layer $h>H(i,k)$ and an arbitrary
   coprime swap with $b>1$.

The truncated $b=1$ avoidance in $E^\square$ sees neither multiplicity nor the
full second mechanism.

## 7. Two exact rank-three maximality problems

There are two useful rank-three objects, and they must not be identified.

### 7.1 Deterministically selected rank

For fixed $A<B$ and a fixed deterministic maximal-layer divisor rule, define

\[
 \mathcal M_{k,3}^{A,B}(d_*)=
 \{m\in C_k^{A,B}:\iota_k(m)\in I_k,\
   \Omega(m/d_*(m))=3\}.
 \tag{7.1}
\]

Its exact counting identity is

\[
 |\mathcal M_{k,3}^{A,B}(d_*)|
 =
 \sum_{i\in I_k}\sum_{d\in C_i}
 \sum_{\substack{r\in\mathcal R_{i,k},\ \Omega(r)=3\\
                  dr\in C_k^{A,B}\\
                  \Sigma(d,r)\text{ avoids all rectangles in }(2.5)}}
 \mathbf 1_{\{d=d_*(dr)\}}.
 \tag{7.2}
\]

Here the swap condition is exactly equivalent to $\iota_k(dr)=i$.  There is no
$1/\nu_i$ factor: the deterministic selector itself charges every terminal
integer once.  A direct selected-anchor target is to construct a rule $d_*$ for
which

\[
 |\mathcal M_{k,3}^{A,B}(d_*)|=o_{A,B}(X_k).
 \tag{7.3}
\]

### 7.2 Symmetric random-anchor rank

If one instead retains the reciprocal multiplicity from (3.1), the exact object is

\[
 \begin{split}
 W_{k,3}^{A,B}:={}&
 \sum_{i\in I_k}\sum_{d\in C_i}
 \sum_{\substack{r\in\mathcal R_{i,k},\ \Omega(r)=3\\
                  dr\in C_k^{A,B}\\
                  \Sigma(d,r)\text{ avoids all rectangles in }(2.5)}}
 \frac1{\nu_i(dr)}.
 \end{split}
 \tag{7.4}
\]

For a fixed terminal integer $m$, its contribution to (7.4) is

\[
 \frac{\#\{d\in C_{\iota_k(m)}:d\mid m,\
                 \Omega(m/d)=3\}}
      {\nu_{\iota_k(m)}(m)}.
 \tag{7.5}
\]

Thus $W_{k,3}^{A,B}$ is the total probability of rank three when the maximal-layer
divisor is chosen uniformly for each $m$; it is not, in general, the cardinality in
(7.1) for an arbitrary deterministic rule.  Proving

\[
 W_{k,3}^{A,B}=o_{A,B}(X_k)
 \tag{7.6}
\]

would control the terminal integers for which **every** maximal-layer divisor has
rank-three quotient, and would permit a selector to avoid rank three whenever a
non-rank-three maximal divisor exists.  A complete growing-rank argument would still
have to coordinate that choice with all other quotient ranks.

Neither (6.4) nor Theorem 5.1 decides (7.3) or (7.6).  Equations (7.2) and
(7.4) are the two exact maximality-conditioned bilinear divisor-chain sums; all
incomparable later divisors are retained through the swap spectrum.

### Why a deterministic rank-only proof stops

Membership in $C_i$ does not by itself make the divisor logarithms of $d$
a factor-two mesh.  The assertion

> every sufficiently high-Ω integer has a divisor in every ratio-two interval
> between $1$ and itself

is false: $d=3^L$ has arbitrarily large Ω, but
$(3^t,2\cdot3^t]$ contains no divisor of $d$ for $0\le t<L$.

This obstruction also occurs inside the actual source pool.  Put
$L=\lceil T_i\rceil$.  Since $3^L=X_i^{o(1)}$, the prime number theorem
in dyadic intervals supplies, for all large $i$, an odd prime

\[
 q\in\left(\frac{X_i}{2\cdot3^L},\frac{X_i}{3^L}\right].
\]

Then $d=3^Lq\in(X_i/2,X_i]$, $\Omega(d)=L+1\ge T_i$, while the divisors
below $q$ are only $1,3,\ldots,3^L$, still with ratio-three gaps.
Thus no proof of (7.2) or (7.4) can use only the scalar inequality
$\Omega(d)\ge T_i$; it must use distributional thinness of such divisor
spectra, interaction with the three prime factors of $r$, or the multiplicity
weight.

This is a counterexample to the stated deterministic mesh lemma only.  It is
not a counterexample to (7.3) or (7.6): a particular $d$ with a sparse divisor spectrum
has zero-density significance unless it can be amplified.

## 8. Precise next dependencies

The next proof attempt should attack either exact sum (7.2) or (7.4), before
returning to growing quotient rank.  Three non-equivalent sufficient inputs remain
live:

1. **Swap-hitting estimate.**  Show that all but $o(X_k)$ of the rank-three
   candidate mass has a coprime pair $a\mid r,b\mid d$ whose point in
   $\Sigma(d,r)$ hits one of the rectangles (2.5).  This proves that the
   candidate anchor was not maximal.
2. **Multiplicity estimate.**  On the candidates for which the swap spectrum
   avoids every later rectangle, prove that the harmonic weight
   $1/\nu_i(dr)$ saves a factor tending to infinity relative to (6.4), thereby
   proving (7.6).
3. **Counterexample amplification.**  Construct a positive-density or
   non-vanishing terminal family satisfying the full swap avoidance, not merely
   the $b=1$ avoidance.  Only such a family, with the relevant rank and
   multiplicity information, could refute (7.3) or (7.6); isolated sparse divisor
   examples cannot.

If a rank-three target is proved with a selector compatible across ranks, the
hierarchy then asks for fixed $q=4,5,\ldots$, followed by uniformity up to the
terminal truncation range $q\ll_{A,B}\sqrt{\log k}$ in Proposition 4.1.  If
(7.3) is disproved for every selector by an actual terminal family, the resulting
family is a precise obstruction to the logarithmic-barrier construction.  Neither
outcome is established in this note.
