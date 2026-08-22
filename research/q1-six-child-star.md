# Six-child stars: saturation forces a two-prime repair

Date: 22 August 2026  
Scope: the tight minimum-rank insertion case for one-root HBC stars  
Status: **complete paper proof proposed for independent review; universal HBC remains open**

This note closes the six-child one-root star case left by the audited five-child
theorem.  Let $E\subseteq\mathbb Z_{\ge2}$ be primitive and pairwise non-coprime.
For each $x\in E$, an admissible weighted shadow choice consists of a prime
$d_x\mid x$ and a type $t_x\in\{0,1\}$, where type $1$ is allowed only when
$d_x$ is odd.  The choice is successful when, for each type, the selected shadows
$x/d_x$ are distinct and primitive.

The only insertion-count tie for six children occurs when a minimum-$\Omega$ member
$e$ has

\[
 \operatorname{supp}(e)=\{2,p,q\},
 \qquad p,q\text{ distinct odd primes}.
\tag{0.1}
\]

It then has exactly five options

\[
 (2,0),(p,0),(p,1),(q,0),(q,1).
\tag{0.2}
\]

Five old members really can block these five options without any blocker overlap; an
explicit example is given in Section 4.  The positive mechanism is different.  Exact
saturation forces every old member to contain either $2$ or $p$.  Discarding the
old assignment and deleting $2$ on the even class and $p$ on the remaining class
then solves the entire six-member palette.

This proves HBC for every one-root star with at most six children.  It does not prove
the arbitrary-star case, universal HBC for general Hasse forests, or Erdős Problem 892.

## 1. Two elementary interfaces

### Lemma 1.1 (two-prime cover)

Let $A\subseteq\mathbb Z_{\ge2}$ be primitive, let $u$ be a prime, and let $v$
be an odd prime.  Suppose

\[
 \forall a\in A,\qquad u\mid a\quad\text{or}\quad v\mid a.
\tag{1.1}
\]

Then $A$ admits successful weighted two-type shadow choices.

#### Proof

Put

\[
 A_0=\{a\in A:u\mid a\},
 \qquad A_1=A\setminus A_0.
\tag{1.2}
\]

Delete $u$ on $A_0$ and use type $0$.  By (1.1), every member of $A_1$ is
divisible by $v$; delete $v$ there and use type $1$.  Both choices are weighted
admissible because type $0$ accepts every prime and $v\ge3$.

Within either class the deleted prime is common.  Hence

\[
 a/u\mid b/u\iff a\mid b,
 \qquad
 a/v\mid b/v\iff a\mid b.
\tag{1.3}
\]

Primitivity of $A$ proves injectivity and primitivity in both type classes.  Empty
classes cause no problem.  ∎

### Lemma 1.2 (one old member blocks at most one option)

Let $A\subseteq\mathbb Z_{\ge2}$ be primitive, choose $e\in A$ with minimum
$\Omega(e)$, and put $F=A\setminus\{e\}$.  Fix any successful weighted shadow
choice on $F$.  Write the choice on $f\in F$ as deletion $d_f$, type $t_f$,
and shadow $s_f=f/d_f$.

For a prime $r\mid e$ and a type $t$ admissible for $r$, say that $f$
**blocks** $(r,t)$ if $t=t_f$ and $e/r$ is equal or comparable to $s_f$.
Then every $f\in F$ blocks at most one pair $(r,t)$.  Moreover, whenever $f$
blocks $(r,t)$,

\[
 \frac e r\mid\frac f{d_f}.
\tag{1.4}
\]

#### Proof

Minimum rank gives

\[
 \Omega(e/r)=\Omega(e)-1
 \le \Omega(f)-1=\Omega(f/d_f).
\tag{1.5}
\]

If $f/d_f\mid e/r$, divisibility gives the reverse inequality in (1.5), so the
two ranks are equal.  The quotient then has $\Omega$-rank zero and is $1$; hence
the shadows are equal.  Thus every comparability conflict has the orientation (1.4).

Since $A$ is primitive, $e$ and $f$ are incomparable.  Comparing valuations in
(1.4), first note that $r=d_f$ would give $e\mid f$ after multiplication by
$r$, which is impossible.  For every prime $\ell\ne r$ one then has

\[
 v_\ell(e)\le v_\ell(f)-\mathbf1_{\ell=d_f}\le v_\ell(f),
\]

while $v_r(e)-1\le v_r(f)$.  Since $e\nmid f$, the required valuation surplus
must occur at $r$ and nowhere else, and its size is exactly one:

\[
 v_r(e)=v_r(f)+1.
\tag{1.6}
\]

Therefore $r$ is uniquely determined by $f$.  The type is also uniquely determined,
because a conflict requires $t=t_f$.  Thus $f$ blocks at most one option.  ∎

## 2. The saturated tie

The following is the new step.  It does not assert that saturation is impossible; it
turns a saturated old assignment into a different global assignment.

### Lemma 2.1 (saturated five-blocker repair)

Let $A\subseteq\mathbb Z_{\ge2}$ be primitive with $|A|=6$.  Let
$e\in A$ have minimum $\Omega$-rank and satisfy (0.1).  Put
$F=A\setminus\{e\}$, and fix a successful weighted shadow choice on $F$.

If all five options in (0.2) are blocked, then $A$ admits a successful weighted
two-type shadow choice.  More precisely, the repair may be chosen by deleting $2$
from every even member in type $0$, and deleting $p$ from every remaining member
in type $1$.

#### Proof

There are five options and five old members.  Lemma 1.2 says that an old member blocks
at most one option.  If every option is blocked, the blocker incidence is therefore a
bijection: every $f\in F$ blocks exactly one option, and every option has exactly one
blocker.

Let $f_2$ be the blocker of $(2,0)$.  Equation (1.4) gives

\[
 e/2\mid f_2/d_{f_2}\mid f_2.
\tag{2.1}
\]

Since $p\mid e/2$, this implies $p\mid f_2$.

Every other old member blocks an option whose deleted prime is $p$ or $q$.  If
$f$ blocks such an option, (1.4) gives $e/p\mid f$ or $e/q\mid f$.  Both
$e/p$ and $e/q$ are even, so

\[
 2\mid f.
\tag{2.2}
\]

The distinguished member $e$ itself is even.  Consequently every member of $A$
is divisible by $2$ or by $p$.  Lemma 1.1 with $u=2$ and $v=p$ supplies the
claimed repair.  Notice that the type-$1$ class has at most the single member
$f_2$; it is empty if $f_2$ is also even.  ∎

### Remark 2.2 (what saturation proves and does not prove)

The proof uses the equality between the number of old members and the number of
options.  It does not show that two old blockers coincide, nor that the original
five-member assignment extends.  It proves that saturation exposes a two-prime cover,
after which the old assignment can be discarded.  This distinction is necessary: the
strict example in Section 4 has five distinct blockers and no free insertion option.

## 3. Six-child theorem

### Theorem 3.1 (weighted primitive shadows through six members)

Every finite primitive pairwise non-coprime family

\[
 E\subseteq\mathbb Z_{\ge2},\qquad |E|\le6,
\tag{3.1}
\]

admits admissible weighted immediate-shadow choices whose type-$0$ and type-$1$
images are injective and primitive.

#### Proof

The audited five-child theorem settles $|E|\le5$, so suppose $|E|=6$.  Choose
$e\in E$ with minimum $\Omega(e)$.

If $\omega(e)\le2$, the audited support-at-most-two proposition partitions the whole
family into two common-prime batches and proves the conclusion.  Hence assume
$\omega(e)=r\ge3$.

Apply the five-child theorem to $F=E\setminus\{e\}$.  For each distinct prime
dividing $e$, type $0$ is available, and for each odd distinct prime, type $1$
is also available.  Thus $e$ has

\[
 N(e)=2r-\mathbf1_{2\mid e}
\tag{3.2}
\]

admissible insertion options.  By Lemma 1.2, the five old members block at most five
of them.

If $N(e)\ge6$, an unblocked option exists and may be inserted into the old choice.
The only remaining case is

\[
 r=3,\qquad 2\mid e,\qquad N(e)=5,
\tag{3.3}
\]

because $r=3$ with $e$ odd gives six options, while $r\ge4$ gives at least
seven.  Write the other two support primes as $p,q$.  If one of the five options
is unblocked, insert it.  If all five are blocked, Lemma 2.1 discards the saturated
old choice and supplies a successful two-prime-cover choice on the whole of $E$.
All cases are exhausted.  ∎

### Corollary 3.2 (six-child one-root HBC)

Let $r_0\ge1$, let $E$ satisfy Theorem 3.1, and put

\[
 B=\{r_0\}\cup\{r_0e:e\in E\}.
\tag{3.4}
\]

Then $B$ is quasi-primitive and admits HBC with $r_0$ as the parent of every
nonroot.

#### Proof

Primitivity of $E$ makes the displayed edges lower covers and makes distinct top
elements incomparable.  For distinct $e,f\in E$,

\[
 \gcd(r_0e,r_0f)=r_0\gcd(e,f)>r_0.
\tag{3.5}
\]

If this gcd were another member $r_0e'$, then $e'\mid e,f$, contradicting
primitivity.  Thus the gcd of incomparable members is not in $B$, so $B$ is
quasi-primitive.

Apply Theorem 3.1 to the quotient palette.  Multiplication by the common root $r_0$
preserves equality and divisibility, so the two type-shadow images become the two
primitive injective length-one core batches.  The empty-word batch is the singleton
$\{r_0\}$.  This is HBC.  ∎

## 4. Strict saturation without blocker overlap

The assertion “five blocked options must have a repeated blocker” is false, even when
the tight member is the unique minimum-$\Omega$ element.  Let

\[
 e=30=2\cdot3\cdot5
\]

and put

\[
 E=\{30,1155,2210,4370,5394,9102\},
\tag{4.1}
\]

where

\[
\begin{aligned}
1155&=3\cdot5\cdot7\cdot11,&
2210&=2\cdot5\cdot13\cdot17,\\
4370&=2\cdot5\cdot19\cdot23,&
5394&=2\cdot3\cdot29\cdot31,\\
9102&=2\cdot3\cdot37\cdot41.
\end{aligned}
\tag{4.2}
\]

The five old members have the following successful assignment.

| blocked option for $e$ | old member $f$ | deleted prime $d_f$ | old shadow $f/d_f$ | type |
|---|---:|---:|---:|---:|
| $(2,0)$ | $1155$ | $7$ | $165=15\cdot11$ | $0$ |
| $(3,0)$ | $2210$ | $13$ | $170=10\cdot17$ | $0$ |
| $(3,1)$ | $4370$ | $19$ | $230=10\cdot23$ | $1$ |
| $(5,0)$ | $5394$ | $29$ | $186=6\cdot31$ | $0$ |
| $(5,1)$ | $9102$ | $37$ | $246=6\cdot41$ | $1$ |

The family $E$ is primitive.  The element $30$ has $\Omega=3$, while every old
member has $\Omega=4$ and misses one of the primes $2,3,5$, so neither direction
of divisibility between $30$ and an old member is possible.  Distinct old members
all have the same $\Omega$-rank and hence cannot divide one another.  The family is
pairwise non-coprime: the first old member shares $5$ with the next two and $3$
with the last two; the two $2\cdot5$-members share $10$, the two
$2\cdot3$-members share $6$, and a member of either latter pair shares $2$ with
a member of the other pair.  Every old member also shares $3$ or $5$ with $30$.

The type-$0$ old shadows are $165,170,186$, and the type-$1$ shadows are
$230,246$.  Within each type they are distinct and all have $\Omega=3$, so they
form primitive images.  Thus the displayed old assignment is valid.  Nevertheless,

\[
 15\mid165,\qquad10\mid170,230,\qquad6\mid186,246,
\tag{4.3}
\]

so the five distinct old members block the five options of $30$ bijectively.  This
strictly refutes blocker-overlap and fixed-assignment-extension subclaims; it also
shows that merely choosing a different minimum-rank member is unavailable, because
$30$ is the unique minimum-rank member.

Lemma 2.1 repairs the same set.  The even class

\[
 \{30,2210,4370,5394,9102\}
\]

deletes $2$ in type $0$, with shadows

\[
 15,1105,2185,2697,4551.
\tag{4.4}
\]

The remaining singleton $1155$ deletes $3$ in type $1$, with shadow $385$.
Common-prime cancellation proves the type-$0$ image primitive, and the type-$1$
image is a singleton.  Hence saturation is genuine but always repairable at six
members.

## 5. Exact open boundary

There is no remaining gap for a one-root star with at most six children.  The next
unclosed star interface starts at seven children.  In the tight support pattern (0.1),
one may solve six old members using Theorem 3.1, but the five options of $e$ can be
blocked by five of those six members.  The sixth member need not be captured by the
two-prime cover in Lemma 2.1.  Thus the saturation-bijection proof does not by itself
extend to seven children.  This is a precise failure of the counting mechanism, not a
counterexample to seven-child HBC, and that route remains open.

General quasi-primitive Hasse forests also retain mixed-parent and consecutive-
branching configurations not represented by one-root stars.  The arbitrary-star
problem, universal HBC, the historical domination question, and Erdős Problem 892
all remain open.  Accordingly, no conjecture-level Lean formalization is justified by
this partial theorem alone.
