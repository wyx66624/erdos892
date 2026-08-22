# Eight-child stars: saturation transversals and a sharp repair boundary

Date: 22 August 2026  
Scope: the arbitrary-rank one-root star interface for universal HBC  
Status: **complete paper proof proposed for independent review; universal HBC remains open**

This note strengthens the six-child saturation argument.  It proves that every
primitive pairwise non-coprime quotient palette of cardinality at most eight
admits two weighted primitive immediate-shadow classes.  Hence every one-root
Hasse star with at most eight children satisfies HBC.

The proof introduces the **extra-signature transversal** left after selecting
one blocker for every option of a minimum-rank member.  Every pair of primes in
that member's support covers all selected blockers.  At cardinality at most
eight there are at most two extra old members, so their nonempty support
signatures have a transversal of size at most two.  A common-prime partition
then repairs the entire palette.

A nine-member parametric family shows that this particular two-prime-cover
repair is sharp: three extras can require three different support primes and
the full family can have no two-prime cover.  An explicit one-change shadow
repair shows that this is not a nine-child HBC counterexample.

Throughout, a palette is a finite primitive pairwise non-coprime family
$E\subseteq\mathbb Z_{\ge2}$.  Type $0$ may delete any prime, while type $1$
may delete only an odd prime.

## 1. Saturation and support transversals

We use two audited interfaces.

1. If every member of a primitive family is divisible by one of two distinct
   primes $u,v$, with $v$ odd, then delete $u$ in type $0$ on the $u$-class
   and delete $v$ in type $1$ on the remaining class.  Common-denominator
   cancellation makes both shadow images injective and primitive.
2. Let $e$ have minimum $\Omega$-rank, and fix a successful assignment on
   $F=E\setminus\{e\}$.  Each old member blocks at most one admissible
   prime/type option $(s,t)$ of $e$.  If it blocks that option, then

   \[
    e/s\mid f/d_f,
   \tag{1.1}
   \]

   where $d_f$ is its fixed deleted prime.

For completeness, the second fact follows because minimum rank orients every
shadow comparability as (1.1), and valuation comparison makes $s$ the unique
one-unit surplus prime of $e$ over $f$.

### Lemma 1.1 (saturated support-transversal repair)

Let $e\in E$ have minimum $\Omega$-rank and support

\[
 S=\operatorname{supp}(e),\qquad |S|\ge3.
\]

Fix a successful weighted shadow assignment on $F=E\setminus\{e\}$, and
suppose every admissible option of $e$ is blocked.  Select one blocker for
each option, and call the resulting set of old members $H$.  Put
$G=F\setminus H$.

If the nonempty signature family

\[
 \bigl\{S\cap\operatorname{supp}(g):g\in G\bigr\}
\tag{1.2}
\]

has a transversal of cardinality at most two, then the whole palette $E$
admits a successful weighted two-type shadow assignment.

#### Proof

Because one old member blocks at most one option, blockers selected for
distinct options are distinct.  Let $h\in H$ block an option whose deleted
source prime is $s\in S$.  Equation (1.1) gives

\[
 e/s\mid h/d_h\mid h.
\tag{1.3}
\]

Fix any two distinct primes $u,v\in S$.  At least one of $u,v$ differs from
$s$, and every support prime of $e$ other than $s$ divides $e/s$.  Hence

\[
 u\mid h\quad\text{or}\quad v\mid h.
\tag{1.4}
\]

Thus every pair of support primes covers $H$, as well as $e$ itself.

Every signature in (1.2) is nonempty: pairwise non-coprimality gives
$\gcd(e,g)>1$.  Let $T\subseteq S$, $|T|\le2$, meet all the signatures.
If necessary, enlarge $T$ to a two-element subset $\{u,v\}$ of $S$; this is
possible because $|S|\ge3$.  At least one of $u,v$ is odd, since only one
prime is even.  Name an odd member $v$.

The extras $G$ are covered by $\{u,v\}$ because $T\subseteq\{u,v\}$ meets
their signatures.  Equation (1.4) covers $H$, and $e$ contains both primes.
Hence every member of $E$ is divisible by $u$ or $v$.  The two-common-prime
construction stated above supplies the required assignment.  ∎

### Corollary 1.2 (at most two extras)

Under the hypotheses of Lemma 1.1, if $|G|\le2$, then the whole palette is
solvable.

#### Proof

Choose one prime from each nonempty signature in (1.2).  The chosen set is a
transversal of cardinality at most two.  ∎

## 2. The eight-child theorem

### Theorem 2.1

Every primitive pairwise non-coprime family

\[
 E\subseteq\mathbb Z_{\ge2},\qquad |E|\le8,
\tag{2.1}
\]

admits admissible weighted immediate-shadow choices whose type-$0$ and
type-$1$ images are injective and primitive.

#### Proof

Use strong induction on $n=|E|$.  The audited five-child theorem supplies the
base $n\le5$.  Let $6\le n\le8$, assume the result below $n$, and choose
$e\in E$ with minimum $\Omega(e)$.

If $\omega(e)\le2$, the audited support-at-most-two theorem solves the whole
palette at arbitrary cardinality.  Assume $r=\omega(e)\ge3$.  By induction,
the old palette $F=E\setminus\{e\}$ has a successful assignment.

The member $e$ has

\[
 L(e)=2r-\mathbf1_{2\mid e}
\tag{2.2}
\]

admissible prime/type options.  Each old member blocks at most one.  If some
option is unblocked, insert it into the old assignment.

It remains that all $L(e)$ options are blocked.  Select one distinct blocker
per option, forming $H$.  The number of extras is

\[
 |G|=n-1-L(e)\le 8-1-5=2,
\tag{2.3}
\]

because $r\ge3$ gives $L(e)\ge5$.  Corollary 1.2 discards the old assignment
and supplies a successful assignment on all of $E$.  This exhausts the
induction.  ∎

### Corollary 2.2 (eight-child one-root HBC)

Let $r_0\ge1$, let $E$ satisfy Theorem 2.1, and put

\[
 B=\{r_0\}\cup\{r_0e:e\in E\}.
\tag{2.4}
\]

Then $B$ is quasi-primitive and admits HBC with $r_0$ as the parent of every
nonroot.

#### Proof

Primitivity of $E$ makes all displayed edges lower covers.  Pairwise
non-coprimality gives

\[
 \gcd(r_0e,r_0f)=r_0\gcd(e,f)>r_0
\]

for distinct top elements.  This gcd cannot be another member $r_0e'$,
because then $e'\mid e,f$, contradicting primitivity.  Thus $B$ is
quasi-primitive.  Theorem 2.1 gives the two length-one primitive core batches
after multiplication by the common root, while the empty-word batch is the
singleton $\{r_0\}$.  Hence HBC holds.  ∎

## 3. A strict nine-member boundary for the repair mechanism

We now construct a saturated palette for which the signature family needs
three support primes and, more strongly, the entire palette has no cover by
two primes.  This refutes only the two-prime-cover repair at the next
cardinality.

Let

\[
 a=2,\quad b,c,\quad
 x_{ab},x_{ac},x_{bc},\quad
 h_a,h_b,h_c,\quad
 d_a,d_{b0},d_{b1},d_{c0},d_{c1}
\tag{3.1}
\]

be pairwise distinct primes, except for the displayed equality $a=2$.  Put

\[
\begin{aligned}
 e&=abc,\\
 A&=bc\,h_a d_a,\\
 B_0&=ac\,h_b d_{b0},&
 B_1&=ac\,h_b d_{b1},\\
 C_0&=ab\,h_c d_{c0},&
 C_1&=ab\,h_c d_{c1},\\
 G_a&=a\,x_{ab}x_{ac}h_a,\\
 G_b&=b\,x_{ab}x_{bc}h_b,\\
 G_c&=c\,x_{ac}x_{bc}h_c.
\end{aligned}
\tag{3.2}
\]

Let $\mathcal E$ be the family of these nine integers.

### Proposition 3.1

The family $\mathcal E$ is primitive and pairwise non-coprime.  The following
is a successful assignment on $\mathcal E\setminus\{e\}$:

\[
\begin{array}{c|cccccccc}
 f&A&B_0&B_1&C_0&C_1&G_a&G_b&G_c\\ \hline
 d_f&d_a&d_{b0}&d_{b1}&d_{c0}&d_{c1}
     &x_{ab}&x_{ab}&x_{ac}\\
 t_f&0&0&1&0&1&0&0&0 .
\end{array}
\tag{3.3}
\]

Its first five members block all five options of $e$ bijectively.  The full
family has no two-prime cover.  Nevertheless, changing only the deletion on
$A$ and then inserting $e$ gives a successful assignment on all nine members.

#### Proof

The member $e$ has total rank $3$ and every old member has total rank $4$.
Each old support omits at least one of $a,b,c$, so $e$ divides none of them;
rank excludes the reverse direction.  Distinct old members have equal rank
and different supports, hence are incomparable.  Thus $\mathcal E$ is
primitive.

The blocker members are pairwise non-coprime: $A$ shares $c$ with
$B_0,B_1$ and $b$ with $C_0,C_1$, while every $B_i$ shares $a$ with every
$C_j$.  The extras share $x_{ab},x_{ac},x_{bc}$ pairwise.  The extra $G_a$
shares $h_a$ with $A$ and $a$ with all $B_i,C_j$; symmetrically, $G_b$
shares $h_b$ with the $B_i$ and $b$ with the other blocker classes, while
$G_c$ shares $h_c$ with the $C_i$ and $c$ with the other blocker classes.
Every old member also shares a support prime with $e$.  This exhausts all
pairs and proves pairwise non-coprimality.

Under (3.3), the type-$0$ shadows are

\[
 bc\,h_a,\quad ac\,h_b,\quad ab\,h_c,\quad
 a\,x_{ac}h_a,\quad b\,x_{bc}h_b,\quad c\,x_{bc}h_c,
\tag{3.4}
\]

and the type-$1$ shadows are

\[
 ac\,h_b,\qquad ab\,h_c.
\tag{3.5}
\]

Within each type these are distinct squarefree products of total rank $3$,
so the old assignment is successful.  Its blockers satisfy

\[
 e/a=bc\mid bc\,h_a,\quad
 e/b=ac\mid ac\,h_b,\quad
 e/c=ab\mid ab\,h_c
\tag{3.6}
\]

in both available types where appropriate.  Hence $A,B_0,B_1,C_0,C_1$
block $(a,0),(b,0),(b,1),(c,0),(c,1)$ respectively.

We next rule out a two-prime cover.  Any covering pair must contain at least
one of $a,b,c$ in order to cover $e$.  If it contains two of them, it misses
the extra whose support meets $\{a,b,c\}$ only in the third.  If it contains
exactly one, say $a$, then its other prime must cover both $G_b$ and $G_c$;
their unique common prime is $x_{bc}$.  But neither $a$ nor $x_{bc}$ divides
$A$, so this pair fails.  The cases with unique support prime $b$ or $c$ are
symmetric, using respectively the blocker classes $B_i$ or $C_i$.  A pair
containing none of $a,b,c$ misses $e$.  Thus no two primes cover
$\mathcal E$.

Finally, keep (3.3) except that $A$ now deletes $b$ in type $0$, and insert
$e$ by deleting $a=2$ in type $0$.  The type-$0$ shadows become

\[
 bc,\quad c\,h_a d_a,\quad ac\,h_b,\quad ab\,h_c,\quad
 a\,x_{ac}h_a,\quad b\,x_{bc}h_b,\quad c\,x_{bc}h_c.
\tag{3.7}
\]

The last six are distinct squarefree products of rank $3$.  The rank-$2$
shadow $bc$ divides none of them: each displayed rank-$3$ shadow omits $b$
or omits $c$.  Hence the type-$0$ image is primitive and injective.  The
unchanged type-$1$ image (3.5) is primitive and injective.  This is the
claimed global repair.  ∎

### Corollary 3.2 (sharpness of the present mechanism)

At nine palette members, full saturation can leave three extra signatures

\[
 \{a\},\qquad\{b\},\qquad\{c\}
\]

with transversal number $3$, and the palette need not have any two-prime
cover.  Therefore Lemma 1.1 and the counting bound (2.3) cannot by themselves
prove the nine-child theorem.  Proposition 3.1 simultaneously proves that
this failure is not an HBC obstruction: a one-change repair exists.

## 4. Exact remaining gap

There is no remaining one-root-star gap through eight children.  The next
unclosed case is a nine-member quotient palette.  Proposition 3.1 rejects
only the automatic two-prime-cover repair; it does not reject exchange,
three-signature structure, probabilistic selection, or a different arithmetic
encoding.

General quasi-primitive Hasse forests still have mixed-parent and consecutive-
branching configurations not represented by one-root stars.  Universal HBC,
the historical domination implication, both characterizations in Erdős
Problem 892, and their conjecture-level Lean formalization all remain open.
