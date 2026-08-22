# Five-child stars: minimum-rank insertion and a two-prime partition

Date: 22 August 2026  
Scope: the arbitrary-rank one-root star interface for universal HBC  
Status: **paper proof proposed for independent review; universal HBC remains open**

This note proves that every primitive pairwise non-coprime quotient palette of
cardinality at most five admits two weighted primitive immediate-shadow
classes.  Consequently every quasi-primitive one-root star with at most five
children satisfies HBC.  It also proves an arbitrary-cardinality theorem when
one palette member uses at most two distinct primes.

The result removes the five-child star from the list of possible six-point HBC
obstructions.  It does not handle general six-point forests, prove universal
HBC, or solve Erdős Problem 892.

Write $\omega(n)$ for the number of distinct prime divisors and $\Omega(n)$
for the number counted with multiplicity.  Type $0$ may delete any prime and
type $1$ may delete only an odd prime.

Throughout this note, every quotient palette is a subset of
$\mathbb Z_{\ge2}$; in particular, each palette member has a prime divisor.

## 1. Common-prime batches

### Lemma 1.1

Let $F$ be primitive and suppose one prime $p$ divides every member of $F$.
Then

\[
 f\longmapsto f/p\qquad(f\in F)
\]

is injective and has primitive image.

#### Proof

The relation $f/p\mid g/p$ is equivalent to $f\mid g$.  ∎

### Proposition 1.2 (a member on at most two primes)

Let $E\subseteq\mathbb Z_{\ge2}$ be a finite or countable primitive pairwise
non-coprime family.  If some $e_0\in E$ satisfies $\omega(e_0)\le2$, then $E$ admits weighted
immediate-shadow choices whose type-$0$ and type-$1$ images are primitive and
injective.

#### Proof

If $e_0$ is a power of one prime $p$, every member of $E$ is divisible by
$p$, since it must be non-coprime to $e_0$.  Delete $p$ everywhere and use
type $0$; Lemma 1.1 applies.

Otherwise the distinct prime support of $e_0$ is $\{p,q\}$.  Choose an odd
member $o$ of this pair and call the other prime $u$.  Put

\[
 E_1=\{f\in E:o\mid f\},\qquad E_0=E\setminus E_1.
\]

Every $f\in E_0$ is non-coprime to $e_0$ but is not divisible by $o$, so
$u\mid f$.  Delete $o$ on $E_1$ and give that class type $1$; delete $u$ on
$E_0$ and give it type $0$.  Both classes have a common deleted prime, so
Lemma 1.1 proves the required injectivity and primitivity.  The type-$1$
weight is admissible because $o$ is odd.  ∎

## 2. The exact one-blocker valuation lemma

### Lemma 2.1 (fragile surplus)

Let $e,f$ be incomparable positive integers, and let primes $p\mid e$ and
$q\mid f$ be deleted once.  If

\[
 e/p\mid f/q,
\tag{2.1}
\]

then $p\ne q$, and $p$ is the unique prime at which $e$ has larger valuation
than $f$; moreover

\[
 v_p(e)=v_p(f)+1,
 \qquad v_q(f)>v_q(e).
\tag{2.2}
\]

In particular, for fixed $f$ and its fixed deleted prime $q$, at most one
prime deletion $p$ from $e$ can make (2.1) hold.

#### Proof

If $p=q$, multiplying (2.1) by $p$ gives $e\mid f$, impossible.  For every
prime $\ell\ne p$, comparison of valuations in (2.1) gives

\[
 v_\ell(e)\le v_\ell(f)-\mathbf1_{\ell=q}\le v_\ell(f).
\]

At $p$ it gives $v_p(e)-1\le v_p(f)$.  Since $e\nmid f$, there must be a
valuation surplus, and the preceding inequalities show that its only possible
location is $p$.  The surplus is therefore exactly one.  The inequality at
$q$ is strict because the right-hand side of (2.1) deleted one copy of $q$.
This proves (2.2) and uniqueness.  ∎

### Lemma 2.2 (minimum-rank insertion count)

Let $E\subseteq\mathbb Z_{\ge2}$ be primitive, choose $e\in E$ with minimum $\Omega(e)$, and suppose
weighted two-type primitive shadow choices have already been fixed on
$E\setminus\{e\}$.  If $\omega(e)=r$, then $e$ has

\[
 2r-\mathbf1_{2\mid e}
\tag{2.3}
\]

admissible pairs $(p,t)$, where $p\mid e$ is prime, $t=0$ is always allowed,
and $t=1$ is allowed exactly when $p$ is odd.  Each old member blocks at most
one of these pairs by equality or comparability in the same type.

#### Proof

Formula (2.3) just counts one type-$0$ option for every distinct prime and one
additional type-$1$ option for every odd distinct prime.

Let an old member $f$ delete $q_f$ and have type $t_f$, with shadow
$s_f=f/q_f$.  A conflict can occur only for an option of type $t_f$.  Since
$e$ has minimum total rank,

\[
 \Omega(e/p)\le\Omega(f/q_f).
\]

If $s_f\mid e/p$, divisibility forces equality of these two ranks and then
equality of the two integers.  Thus every equality or comparability conflict
implies

\[
 e/p\mid f/q_f.
\]

By Lemma 2.1, the fixed old member $f$ can satisfy this relation for at most
one prime $p$.  Its fixed type then blocks at most the single option
$(p,t_f)$.  ∎

## 3. The five-child theorem

### Theorem 3.1

Every finite primitive pairwise non-coprime family
$E\subseteq\mathbb Z_{\ge2}$ with $|E|\le5$ admits
weighted immediate-shadow choices such that, for each type, the chosen
shadows are distinct and primitive.

#### Proof

For $|E|\le4$, use the four-child star lemma: for three members, put a
common-prime pair in type $0$ and the remaining non-power-of-$2$ member in
type $1$ (pairing the unique possible power of $2$ first when necessary).  For
four members, if some pair shares an odd prime, put that pair in type $1$ and
put the remaining non-coprime pair in type $0$; if no pair shares an odd
prime, all four members are even, so deleting $2$ from all of them in type
$0$ works by Lemma 1.1.  The cases of one or two members are immediate.

It remains that $|E|=5$.  Choose $e\in E$ with minimum $\Omega(e)$.  If
$\omega(e)\le2$, Proposition 1.2 proves the conclusion for the whole family.
Otherwise $\omega(e)\ge3$.  Apply the four-child result to
$E\setminus\{e\}$.  Lemma 2.2 gives at least

\[
 2\omega(e)-\mathbf1_{2\mid e}\ge5
\]

admissible insertion pairs, while the four old members block at most four of
them.  Choose an unblocked pair.  Its shadow is neither equal nor comparable
to an old shadow of the same type, and its labelled shadow differs locally
from all old labelled shadows.  Adding it therefore preserves both primitive
type batches and labelled injectivity.  ∎

### Corollary 3.2 (five-child one-root HBC)

Let $r\ge1$, and let $E$ satisfy Theorem 3.1.  Then

\[
 B=\{r\}\cup\{re:e\in E\}
\]

is quasi-primitive and admits HBC with $r$ as the parent of every nonroot.

#### Proof

Primitivity of $E$ makes all displayed edges lower covers.  Two distinct top
elements are incomparable.  Their gcd is not $r$, because their quotients are
non-coprime, and it cannot equal another member $re'$, since then
$e'=\gcd(e,f)$ would divide two members of the primitive family.  Thus $B$ is
quasi-primitive.

Use Theorem 3.1 on the edge quotients.  Within a fixed type, multiplying the
primitive shadow image by the common root $r$ preserves primitivity and
injectivity.  The two one-letter words separate the types, and the empty-word
batch is the singleton $\{r\}$.  Hence HBC holds.  ∎

## 4. A strict barrier to a simpler subroute

One type does not always suffice even for three children.  Take

\[
 E_\triangle=\{6,15,100\}.
\]

The possible immediate shadows are

\[
 \partial 6=\{2,3\},\qquad
 \partial15=\{3,5\},\qquad
 \partial100=\{20,50\}.
\]

If the shadows of $6$ and $15$ are distinct, they are either $2$ with $3$
or $5$, or $3$ with $5$.  In every case at least one divides both possible
shadows $20,50$ of $100$.  Thus no one-type primitive injective shadow choice
exists.  Two types repair the same family, for example

\[
 6\mapsto(3,0),\qquad15\mapsto(5,0),\qquad100\mapsto(20,1),
\]

where the type-$1$ choice deletes the odd prime $5$.  This strict example
rejects only the one-type shortcut; it supports rather than contradicts the
two-type theorem.

## 5. Exact remaining gap

For a minimum-rank member with $r$ distinct primes, the insertion argument
works whenever the already solved palette has fewer than
$2r-\mathbf1_{2\mid e}$ members.  At six children the first unresolved
case has $r=3$, includes the prime $2$, and may have five old blockers for
exactly five options.  A proof must exploit blocker overlap or change the old
four/five-member assignment; a strict counterexample must realize all option
blocks simultaneously while retaining primitivity and pairwise
non-coprimality.

For general six-point quasi-primitive sets, Theorem 3.1 removes the five-child
star but leaves mixed-parent and two-consecutive-branching configurations.
None is declared impossible.  No conjecture-level Lean formalization should
begin before a complete universal embedding or a sufficient replacement for
the original domination problem is proved and independently reviewed twice.
