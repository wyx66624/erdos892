# Universal HBC selection: positive round via divisibility height and synchronized deletion

Date: 22 August 2026  
Scope: the OPEN interface in `q1_next_round.md`, Conjecture 6.2  
Status: **two new sufficient theorems and exact barriers; universal HBC remains open**

This note follows a positive route.  It does not assume that a failed greedy choice is a
counterexample to HBC.  Instead it isolates a global grading which makes the commutative
path product harmless, proves a flexible synchronized-prime certificate, and records a
second theorem for exact-rank stars.  It then gives strict quasi-primitive counterexamples
to three tempting strengthenings.  None of those counterexamples refutes universal HBC.

Throughout, $q_0=2,q_1=3$.  A type-$t$ deletion of a prime $p$ is weighted-admissible
when $q_t\le p$.

## 1. The intrinsic divisibility height

Let $B\subseteq\mathbb N$ be finite or countable.  For $b\in B$, define

\[
 h_B(b)=\max\{m:\ b_0\mid b_1\mid\cdots\mid b_m=b,
                 \ b_i\in B,\ b_i<b_{i+1}\}.
\tag{1.1}
\]

The maximum is finite because $b$ has only finitely many divisors.  Write
$B_j=\{b:h_B(b)=j\}$.

### Lemma 1.1 (height is a strict poset rank)

If $x,y\in B$ and $x\mid y,\ x<y$, then

\[
 h_B(x)<h_B(y).
\tag{1.2}
\]

Consequently every $B_j$ is primitive.

**Proof.**  Append $y$ to a longest chain ending at $x$.  This gives
$h_B(y)\ge h_B(x)+1$.  Thus two distinct elements of the same height cannot be
comparable.  ∎

### Lemma 1.2 (maximal-chain lower covers)

If $h_B(b)=j\ge1$, there is a lower cover $d\in L_B(b)$ with

\[
 h_B(d)=j-1.
\tag{1.3}
\]

**Proof.**  Take a chain of length $j$ ending at $b$, and let $d$ be its
penultimate member.  An element strictly between $d$ and $b$ would lengthen the
chain.  Hence $d$ is a lower cover.  Its displayed prefix proves
$h_B(d)\ge j-1$; a longer chain to $d$, followed by $b$, would contradict the
definition of $j$.  ∎

Thus a parent selector can always be chosen so that every selected edge raises height
by exactly one.  This is substantially different from maximizing $\Omega$ of the
parent; Section 5.1 gives a strict counterexample to that proposed substitute.

## 2. A prefix-synchronized prime certificate

The main new object is a binary prime automaton on type words.

### Definition 2.1 (PSPC)

A **prefix-synchronized prime certificate** (PSPC) on $B$ consists of:

1. for each binary word $u$ and $t\in\{0,1\}$, a prime
   $\pi_{u,t}\ge q_t$;
2. for every nonminimal $b\in B$, a parent $\sigma(b)\in L_B(b)$ and a type
   $t(b)\in\{0,1\}$;
3. recursively defined words $\epsilon(r)=\varnothing$ on roots and
   $\epsilon(b)=\epsilon(\sigma(b))t(b)$ elsewhere;

such that, if $h_B(b)=j\ge1$, then

\[
 h_B(\sigma(b))=j-1,
 \qquad
 \pi_{\epsilon(\sigma(b)),t(b)}\mid \frac b{\sigma(b)}.
\tag{2.1}
\]

For an edge with quotient $e=b/\sigma(b)$, set

\[
 p_b=\pi_{\epsilon(\sigma(b)),t(b)},
 \qquad \psi_{\sigma(b)}(e)=e/p_b.
\tag{2.2}
\]

The primes are synchronized only among edges with the same word-prefix and next type.
They may vary with the complete prefix, may occur in the roots, and may be reused at
arbitrarily many parents and heights.  There is no support-disjointness assumption.

### Theorem 2.2 (PSPC implies HBC)

Every finite or countable $B$ carrying a PSPC satisfies HBC for the choices in
(2.2).  In particular, this conclusion holds for every quasi-primitive $B$ carrying
a PSPC.

**Proof.**  First check the local labelled-shadow condition.  Fix a parent $d$ and
two selected children $de_1,de_2$ of the same type $t$.  The parent word is the
same, so both edges delete the same prime $p=\pi_{\epsilon(d),t}$.  If
$e_1/p=e_2/p$, then $e_1=e_2$, hence the children are equal.  Children of different
types have different labels.  Thus $e\mapsto(\psi_d(e),t)$ is injective.  The
weight condition holds because $p\ge q_t$.

Now let $b$ have height $j$ and word
$\epsilon=t_1\cdots t_j$.  Every selected path visits heights
$0,1,\ldots,j$.  Define the word-dependent integer

\[
 L(\epsilon)=\prod_{i=1}^j
 \pi_{t_1\cdots t_{i-1},t_i},
 \qquad L(\varnothing)=1.
\tag{2.3}
\]

Multiplying the edge identities gives the exact core formula

\[
 c(b)=\frac b{L(\epsilon)}.
\tag{2.4}
\]

Suppose $b,b'$ have the same word and $c(b)\mid c(b')$.  They have the same
height $j$ and the same denominator $L(\epsilon)$; multiplying the divisibility
by this denominator gives $b\mid b'$.  Lemma 1.1 forces $b=b'$.  Hence every
fixed-word core batch is injective and primitive, which is precisely HBC.  ∎

The proof exposes the useful invariant: **the deleted product is a function of the
type word alone**.  Once parents follow the intrinsic height, equal words put the
sources in one primitive height level, and common-denominator cancellation proves HBC.

### Corollary 2.3 (binary level-prime criterion)

Suppose that for every $j\ge1$ there are primes

\[
 \lambda_{j,0}\ge2,\qquad \lambda_{j,1}\ge3,
\tag{2.5}
\]

such that every $b\in B_j$ has a lower cover $d\in B_{j-1}$ and a type
$t\in\{0,1\}$ satisfying

\[
 \lambda_{j,t}\mid b/d.
\tag{2.6}
\]

Then $B$ admits HBC.

**Proof.**  Make one such choice for each $b$, and put
$\pi_{u,t}=\lambda_{|u|+1,t}$.  This is a PSPC, so Theorem 2.2 applies.  ∎

### Corollary 2.4 (one synchronized prime per height)

It is enough that for every $j\ge1$ there is a prime $\lambda_j$ such that every
$b\in B_j$ has some lower cover $d\in B_{j-1}$ with $\lambda_j\mid b/d$.
One deletes $\lambda_j$ and uses type $0$ on every height-$j$ edge.

This criterion allows composite and mixed-$\Omega$ quotients, branching, infinitely
many parents, repeated primes, and arbitrary overlaps between shadow supports.  Its
only global synchronization is by intrinsic height.

## 3. Overlapping certificates and strict separation

### 3.1 A displayed PSPC certificate with overlapping supports

Put

\[
 B_\dagger=\{1,6,10,14,990,1950,3570\}.
\tag{3.1}
\]

Its height levels are

\[
 B_0=\{1\},\qquad B_1=\{6,10,14\},\qquad
 B_2=\{990,1950,3570\}.
\tag{3.2}
\]

Select

\[
 1\to6,10,14,\qquad
 6\to990,\quad10\to1950,\quad14\to3570.
\tag{3.3}
\]

All displayed edges are lower-cover edges.  Their quotient palettes are

\[
 \{6,10,14\},\qquad \{165\},\qquad\{195\},\qquad\{255\}.
\tag{3.4}
\]

Delete $2$ at height one and $3$ at height two, always with type $0$.  The
word-$0$ cores are $3,5,7$, and the word-$00$ cores are

\[
 990/6=165,\qquad1950/6=325,\qquad3570/6=595,
\tag{3.5}
\]

two primitive batches.

This example is quasi-primitive.  Indeed, the gcds of incomparable pairs belong to
$\{2,30\}$, disjoint from $B_\dagger$.  The displayed fixed selector and shadow
choices do not meet the separated-support hypotheses: the height-one shadows have support union
$\{3,5,7\}$, while the shadows at parents $6,10,14$ are respectively
$55,65,85$; all three later parent blocks share $5$, and they also overlap the
height-one block.  Thus the displayed PSPC certificate itself does not satisfy the
separated-support hypotheses.  No conclusion about different choices for
$B_\dagger$ is drawn; the strict separation is supplied by the next example.

### 3.2 A strict example beyond every separated-support choice

Let

\[
 B_{\mathrm{strict}}=\{2,24,80\}.
\tag{3.6}
\]

The unique root is \(2\), and \(24,80\) are incomparable with

\[
 \gcd(24,80)=8\notin B_{\mathrm{strict}}.
\tag{3.7}
\]

Hence \(B_{\mathrm{strict}}\) is quasi-primitive.  Both top elements have intrinsic
height one, their forced parent is \(2\), and their edge quotients are

\[
 24/2=12,\qquad 80/2=40.
\tag{3.8}
\]

Delete the common prime \(2\) and give both edges type \(0\).  The labelled local
shadows are \(6,20\), which are distinct and incomparable.  The word-\(0\) cores are

\[
 2\cdot6=12,\qquad 2\cdot20=40,
\tag{3.9}
\]

also distinct and incomparable.  Equivalently, Corollary 2.4 applies with
\(\lambda_1=2\), so this is a complete PSPC and HBC certificate.

On the other hand, no separated-support shadow choice exists.  The parent selector is
forced.  The complete lists of immediate shadows are

\[
 \partial\{12\}=\{6,4\},\qquad
 \partial\{40\}=\{20,8\}.
\tag{3.10}
\]

Every integer in these two sets is even.  Thus every possible chosen shadow contains
the root prime \(2\), whereas the separated-support verifier requires the union of all
shadow supports to be disjoint from the root support \(\{2\}\).  Types cannot repair a
support intersection.  Therefore **every** parent/shadow/type choice fails that
verifier, while the displayed PSPC satisfies HBC.  The example branches, has mixed
quotient ranks \(\Omega(12)=3\) and \(\Omega(40)=4\), and is not a repeated-\(2\)
path family.  This proves a strict extension beyond the separated-support criterion.

## 4. A second positive theorem: exact-rank one-root stars

The synchronized-prime condition is not the only positive mechanism.  Exact
$\Omega$-rank makes divisibility disappear after an injective two-shadow coding.

### Theorem 4.1 (exact-rank star HBC)

Let $r\ge1$, and let $E\subseteq\{2,3,\ldots\}$ be finite or countable,
primitive, pairwise non-coprime, and satisfy

\[
 \Omega(e)=k\ge1\qquad(e\in E).
\tag{4.1}
\]

Then

\[
 B=\{r\}\cup\{re:e\in E\}
\tag{4.2}
\]

is quasi-primitive and admits HBC with $r$ as the parent of every nonroot member.

**Proof.**  Primitivity of $E$ makes every $r\to re$ a lower-cover edge.  The
only incomparable pairs in $B$ are two top elements.  Their gcd is
$r\gcd(e,f)$.  It is not $r$, because $E$ is pairwise non-coprime, and it cannot
be $re'\in B$: in that case $e'=\gcd(e,f)$ divides both $e$ and $f$.
Primitivity of $E$ first forces $e'=e$ and then $e'=f$, contradicting that the
two top elements are distinct.  Thus $B$ is quasi-primitive.

Apply the audited exact-rank/mixed-rank shadow theorem to obtain an immediate-shadow
map $e\mapsto\psi(e)$ with fibres of size at most two.  In a two-element fibre,
the two deleted primes are distinct; give the member deleting the smaller prime type
$0$, and the other type $1$.  The latter prime is at least $3$, so the weighting
is admissible.  Give a singleton fibre type $0$.  For each type, the shadows are
distinct, and all have $\Omega=k-1$; hence each type-shadow image is primitive.
Multiplication by the common root $r$ preserves equality and divisibility.  The two
length-one core batches are therefore primitive and injective.  The empty batch is
$\{r\}$, proving HBC.  ∎

This theorem genuinely uses both types.  With $(p,q,s)=(2,3,5)$, take

\[
 E^\star=\{75,45,50,30,18,20,12\}.
\tag{4.3}
\]

It has seven members but only six immediate-shadow values, so no one-type injective
shadow map exists.  One valid two-type map is

\[
\begin{array}{c|ccccccc}
e&12&18&20&30&45&50&75\\ \hline
\psi(e)&6&9&10&15&15&25&25\\
t(e)&0&0&0&0&1&0&1.
\end{array}
\tag{4.4}
\]

The type-$1$ members delete $3$, so the weights are admissible.  Taking $r=2$
also violates separated support: the root prime $2$ occurs in several displayed
shadows.  Nevertheless Theorem 4.1 proves HBC.

## 5. Strict barriers to natural strengthenings

These examples eliminate only the stated lemmas.  They do not eliminate the positive
routes above or universal HBC.

### 5.1 Maximizing $\Omega$ of the lower cover does not grade the forest

Let

\[
 B_\Omega=\{2,6,30,243,2430\}.
\tag{5.1}
\]

This set is quasi-primitive: its incomparable gcds are $1$ or $3$, neither in
$B_\Omega$.  The lower covers of $2430$ are $30$ and $243$.  Since
$\Omega(30)=3<5=\Omega(243)$, a maximal-$\Omega$ selector chooses $243$.
It also selects $2\to6\to30$.  Hence the selected forest depth of $2430$ is one,
while that of its divisor $30$ is two.  Thus the proposed lemma

> maximal-$\Omega$ lower covers make selected depth strictly increase under divisibility

is false.  Intrinsic longest-chain height, not $\Omega$-greed, repairs it.

### 5.2 A common deleted prime is insufficient without height-compatible parents

Let

\[
 B_c=\{2,3,20,60\},
\tag{5.2}
\]

which is quasi-primitive.  Select $2\to20$ and $3\to60$.  Both are lower-cover
edges, and their quotients $10,20$ are divisible by $2$.  Deleting $2$ with
type $0$ gives cores

\[
 2(10/2)=10,\qquad3(20/2)=30.
\tag{5.3}
\]

They lie in the same word-$0$ batch and $10\mid30$.  The failed selector puts
the comparable elements $20\mid60$ at the same selected depth.  This strictly
refutes the rule “one common edge prime automatically gives HBC.”  It does not refute
Corollary 2.4, which requires parents in the preceding intrinsic-height level.

### 5.3 Two synchronized level primes are sufficient, not necessary

Assign the primes $2,3,5,7,11,13,17$ to the seven points of the Fano plane and take
the seven line-products

\[
 E_F=\{30,154,442,273,561,595,715\}.
\tag{5.4}
\]

Distinct Fano lines meet in exactly one point.  Thus $E_F$ is an exact-rank
primitive pairwise non-coprime family, and

\[
 B_F=\{1\}\cup E_F
\tag{5.5}
\]

is quasi-primitive.  No two primes meet every quotient support: in the Fano plane the
union of the three lines through either of two points contains only five of the seven
lines, so two lines avoid both points.  Therefore no two primes
$\lambda_{1,0},\lambda_{1,1}$ can satisfy the level-one coverage hypothesis of
Corollary 2.3 (and no PSPC can do so at the empty prefix).

Yet HBC holds.  Delete respectively $2,2,2,3,3,5,5$, obtaining

\[
 15,77,221,91,187,119,143.
\tag{5.6}
\]

These are distinct and all have $\Omega=2$, hence form a primitive type-$0$
batch.  This is a strict counterexample to **necessity** of the synchronized-prime
certificate, not to HBC.  It shows that the height-synchronization and exact-rank
routes are complementary and should both remain active.

## 6. Minimal-counterexample insertion and exact blockers

The following elementary lemma is the correct induction interface.  It avoids the false
assumption that any maximal element can be inserted by an arbitrary shadow.

### Lemma 6.1 (maximal-node repair criterion)

Let $B$ be finite, let $x\in B$ be maximal and nonminimal, and suppose an HBC
choice has been fixed on $B\setminus\{x\}$.  For $d\in L_B(x)$, put $e=x/d$.
An **available option** is a triple $(d,p,t)$ such that

1. $p\mid e$ is prime and $p\ge q_t$;
2. the labelled shadow $(e/p,t)$ is not already used by a child selecting parent $d$.

Let $u=\epsilon(d)$, $C=c(d)e/p$, and $w=ut$.  If some available option has
$C$ incomparable with every existing core in the word-$w$ batch, then the fixed
HBC choice extends to $B$.

Conversely, if $B$ is a cardinality-minimal finite **quasi-primitive**
counterexample to universal HBC, then, for every maximal nonminimal $x$ and every
fixed HBC choice on $B\setminus\{x\}$, every available option is blocked by an
existing $y\ne x$ with

\[
 \epsilon(y)=w,
 \qquad c(y)\mid C\ \text{or}\ C\mid c(y).
\tag{6.1}
\]

**Proof.**  The first assertion checks exactly the local labelled-map condition and the
only global batch affected by inserting $x$.  For the converse, deleting a maximal
element changes no lower-cover relation among the remaining elements.  Minimality gives
HBC on $B\setminus\{x\}$; an unblocked available option would extend it by the first
assertion, a contradiction.  ∎

For an option $a$, write $F_y$ for the set of options blocked by $y$.  The exact
finite induction target is now

\[
 \left|\bigcup_y F_y\right|<|A_x|,
\tag{6.2}
\]

where $A_x$ is the set of available options.  A useful next arithmetic lemma would
bound the multiplicity with which one old core can block the prime deletions of $e$.
The obstruction is asymmetric: the condition $e/p\mid z$ usually singles out at
most one deficient prime, whereas $z\mid e/p$ can hold for many $p$.  Any valid
discharging proof must treat these two orientations separately.

### Lemma 6.2 (canonical-root triangularization)

Let \(R\) be the primitive set of divisibility-minimal members of \(B\), and fix a
total well-order \(\prec\) of \(R\).  Define

\[
 \rho(b)=\min_{\prec}\{r\in R:r\mid b\}.
\tag{6.3}
\]

There is a lower-cover selector whose selected root at every \(b\) is exactly
\(\rho(b)\).  For any shadow choices on such a selector,

\[
 c(x)\mid c(y)\quad\Longrightarrow\quad \rho(y)\preceq\rho(x).
\tag{6.4}
\]

**Proof.**  Put \(r=\rho(b)\).  Take any saturated \(B\)-chain from \(r\) to \(b\)
and let \(d\) be the penultimate member.  Then \(d\in L_B(b)\) and \(r\mid d\).
If a root \(s\prec r\) divided \(d\), it would divide \(b\), contradicting the
definition of \(r\).  Hence \(\rho(d)=r\).  Selecting such a parent recursively
preserves \(\rho\) all the way to the selected root.

The selected root \(\rho(x)\) is a factor of \(c(x)\).  Thus
\(c(x)\mid c(y)\) gives \(\rho(x)\mid c(y)\mid y\), so \(\rho(x)\) is one of the
roots below \(y\).  Minimality in (6.3) gives \(\rho(y)\preceq\rho(x)\).  ∎

This proves a useful triangular form for the proposed reparenting route.  When roots
are processed increasingly, an earlier-root core can never divide a later-root core;
the only possible new cross-root obstruction is a later-root core dividing an
earlier-root core.  The equal-root blocks remain and must be solved internally.

The strict conclusion does **not** extend from the root to every selected ancestor.
For example, in the quasi-primitive chain \(p\to2p\to4p\), deleting \(2\) on both
edges gives \(c(4p)=p\), so the selected ancestor \(2p\) does not divide the core.
What is always true is only

\[
 \rho(x)\mid c(x)\mid c(y)\mid y,
\tag{6.5}
\]

which supplies an alternative saturated chain from \(\rho(x)\) to \(y\).
Reparenting \(y\) along that chain can change the words and cores of an entire
descendant subtree, so (6.4) alone is not yet a conflict-removal theorem.  A valid
exchange lemma must show that an order-decreasing reparenting removes at least one
obstruction without creating an earlier one.  No counterexample to that carefully
stated exchange target is claimed here.

## 7. A rigorous LLL/compactness criterion

The probabilistic route can be stated without pretending that the needed universal
probability estimate is already known.

For finite $B$, give every nonroot $b$ an independent random variable whose finite
domain consists of all weighted-admissible triples

\[
 (d,e/p,t),\qquad d\in L_B(b),\quad e=b/d,\quad
 p\mid e\text{ prime},\quad p\ge q_t.
\tag{7.1}
\]

For each pair of distinct nodes, use two classes of bad events:

- $L_{b,b'}$: two nodes select the same parent and the same labelled shadow;
- $G_{b,b'}$: their recursively computed words agree and their cores are equal or
  comparable.

Each event depends only on variables in the finite divisor closures of its named nodes.
No bad event occurs exactly when the sampled choice satisfies HBC.

### Proposition 7.1 (checkable LLL certificate)

Suppose a product distribution on (7.1) has the following properties:

1. every bad event has probability at most $p$;
2. in the variable-overlap dependency graph, every bad event has degree at most $D$;
3. $e p(D+1)\le1$.

Then $B$ admits HBC.

**Proof.**  The symmetric Lovasz local lemma gives positive probability that no bad
event occurs.  Such an outcome is an HBC choice.  ∎

The same uniform $p,D$ criterion implies HBC for a countable $B$: apply the finite
local lemma to every finite set of atomic constraints and then use the finite-domain
compactness lemma from `q1_next_round.md`, Section 6.  More generally, for a
**finite event family**, the usual asymmetric criterion with \(0<x_E<1\),

\[
 \Pr(E)\le x_E\prod_{F\sim E}(1-x_F)
\tag{7.2}
\]

is available.  In the countable case this statement is used only on finite atomic-event
families and then transferred by compactness; no claim about positivity of an infinite
product is needed.

This keeps the LLL route alive, but identifies its exact missing arithmetic input: a
uniform estimate for $\Pr(G_{b,b'})$ after conditioning on the two finite ancestor
closures.  Proposition 7.1 alone is not a proof of universal HBC.

## 8. Current dependency chain and next targets

The proved positive chain is

\[
\begin{aligned}
&\text{intrinsic divisibility height}
 +\text{ prefix-synchronized deleted primes}\\
&\qquad\Longrightarrow c(b)=b/L(\epsilon(b))
 \Longrightarrow\text{ HBC (Theorem 2.2)},\\[2mm]
&\text{one-root exact-rank palette}
 +\text{ two-shadow fibre cap}\\
&\qquad\Longrightarrow\text{two primitive shadow batches}
 \Longrightarrow\text{ HBC (Theorem 4.1)}.
\end{aligned}
\tag{8.1}
\]

Together with the absorbed arithmetic erasure theorem in `q1_next_round.md`, each
line gives a bounded primitive dominator for its stated class.

The closest OPEN tasks are now sharper:

1. **Blocker multiplicity.**  Prove a discharging inequality for (6.2), separately for
   the two divisibility orientations, or exhibit a strict quasi-primitive family
   refuting the proposed inequality.
2. **Hybrid decomposition.**  Find a coherent height-graded decomposition in which
   some prefixes use synchronized primes and the remaining one-root palettes use the
   exact-rank theorem.  Cross-parent comparability is the only point not already proved.
3. **LLL estimate.**  Bound the probability of a global event $G_{b,b'}$ by local
   arithmetic data and compare it with divisor-closure overlap degree.
4. **Universal selector.**  Neither Theorem 2.2 nor Theorem 4.1 covers arbitrary mixed
   quotient palettes.  Universal HBC, the historical quasi-primitive implication, and
   Erdős Problem 892 therefore remain open.

No Lean formalization is appropriate yet for the universal claim.  The theorems above
are paper-level intermediate results; they should be independently reviewed before any
repository or formalization step.
