# Universal HBC on five-point quasi-primitive sets

Date: 22 August 2026  
Scope: the finite boundary for Conjecture 6.2 in `q1_next_round.md`  
Status: **paper proof proposed for independent review; universal HBC remains open**

This note proves that every quasi-primitive set of at most five integers admits
the hybrid primitive-batch condition (HBC).  The proof is non-computational.  In
fact, every lower-cover selector which follows intrinsic divisibility height can
be completed by admissible prime deletions and binary types.  Thus a finite
counterexample to universal HBC, if one exists, has at least six elements.

Nothing here proves universal HBC, the historical quasi-primitive implication,
or Erdős Problem 892.  A finite HBC obstruction would in any case refute only
this sufficient mechanism unless separately amplified to primitive domination.

Throughout, `type 0` may delete any prime, while `type 1` may delete only an odd
prime.  The weight requirements are therefore $q_0=2$ and $q_1=3$.

## 1. Height selectors and two cancellation lemmas

Let $B\subseteq\mathbb N$ be finite and quasi-primitive in the historical
sense: if $x,y\in B$ are incomparable under divisibility, then
$\gcd(x,y)\notin B$.  Define

\[
 h(b)=\max\{m:b_0\mid b_1\mid\cdots\mid b_m=b,
                   \ b_i\in B, b_i<b_{i+1}\}.
\tag{1.1}
\]

If $x\mid y$ and $x<y$, then $h(x)<h(y)$.  Hence every height level
$B_j=\{b:h(b)=j\}$ is primitive.  Every nonminimal $b\in B_j$ has a
lower cover in $B_{j-1}$: take the penultimate element of a longest chain
ending at $b$.  Fix any selector $\sigma$ choosing such a cover.  The
selected forest depth of $b$ is then exactly $h(b)$.

For a selected edge $d\to b=de$, deleting a prime $p\mid e$ replaces the
edge quotient by the immediate shadow $e/p$.  Appending its type to the
parent word gives the complete word of $b$, and multiplying all shadows
along the path gives its core $c(b)$.

### Lemma 1.1 (Hasse palettes)

For a fixed parent $d$, the quotient palette

\[
 E_d=\{e:de\in B, \sigma(de)=d\}
\]

is primitive and pairwise non-coprime.

#### Proof

If $e\mid f$ for distinct palette members, then
$d<de<df$, contradicting that $d$ is a lower cover of $df$.
Thus the palette is primitive.  Its corresponding children are therefore
incomparable.  If $(e,f)=1$, then
$\gcd(de,df)=d\in B$, contradicting quasi-primitivity.  Hence
$(e,f)>1$.  ∎

### Lemma 1.2 (common-denominator cancellation)

Let $X\subseteq\mathbb N$ be primitive, and let $D$ divide every member of
$X$.  Then $\{x/D:x\in X\}$ is injective and primitive.

#### Proof

The relation $x/D\mid y/D$ is equivalent to $x\mid y$.  ∎

## 2. Small one-parent palettes

The following local statement is the only new star input needed in the
five-point classification.

### Lemma 2.1 (four-child star lemma)

Let $E$ be a primitive pairwise non-coprime family with
$1\le |E|\le4$.  For each $e\in E$, one can choose a prime $p(e)\mid e$
and a type $t(e)\in\{0,1\}$ such that

1. $p(e)\ge q_{t(e)}$;
2. for each fixed type $t$, the shadows $e/p(e)$ of that type are distinct
   and primitive.

Consequently, if $E$ is the quotient palette of children of one parent,
those children can be added to a common parent word without creating a local
label collision or a same-word core comparability.

#### Proof

For one member, delete any prime and use type $0$.  For two members, delete
one common prime from both and use type $0$.  Common-denominator
cancellation preserves primitivity.

Suppose $|E|=3$.  If no member is a power of $2$, choose any two members,
delete a common prime from that pair, and give them type $0$.  The remaining
member has an odd prime; delete one and give it type $1$.  If one member is
a power of $2$, it is the only such member because $E$ is primitive.  Pair
it with any second member.  Their common prime must be $2$; delete $2$
from the pair and use type $0$.  The third member is not a power of $2$,
so it supplies an odd prime for type $1$.

Now suppose $|E|=4$.  If some pair shares an odd prime $q$, delete $q$
from that pair and give it type $1$.  The remaining pair is non-coprime;
delete any common prime from it and give it type $0$.  If no pair shares an
odd prime, pairwise non-coprimality forces every pair, and hence every member,
to be even.  Delete $2$ from all four members and give all of them type
$0$.  In every displayed type class a common denominator was deleted, so
Lemma 1.2 gives distinctness and primitivity.  The two types are separate
labels, completing the proof.  ∎

### Lemma 2.2 (two-node word separation)

Suppose $B_j=\{x,y\}$ and the two nodes have distinct selected parents
$d_x,d_y$.  If the parent words differ, then $x,y$ can never enter the same
complete-word batch, regardless of their new edge choices.  Since these are
the only nodes at height $j$, each parent has only one selected child at this
height, so the choices below create no local labelled-shadow collision.

If their parent words agree and one incoming quotient has an odd prime, the
two nodes can be separated by giving that edge type $1$ and the other edge
type $0$.  If both incoming quotients are powers of $2$, both types are
forced to $0$; whenever the already-deleted parent-path products agree,
deleting $2$ on both new edges gives a common complete denominator and hence
primitive cores by Lemma 1.2.

#### Proof

The first two assertions are immediate from concatenation of complete words.
For the last assertion, if the common parent-path deleted product is $D$,
the two new cores are $x/(2D)$ and $y/(2D)$.  The height level $B_j$ is
primitive, so Lemma 1.2 applies.  ∎

## 3. The only mixed-root three-node configuration

The next lemma handles the one case in which three nodes at height one are
split between two roots.

### Lemma 3.1 (a $2+1$ root split)

Let $r,s$ be roots.  Suppose $x=re$ and $y=rf$ select $r$, while
$z=sg$ selects $s$, and all three nodes have height one.  Then their
three cores admit admissible types whose two same-type batches are primitive.

#### Proof

By Lemma 1.1, $e,f$ are primitive and non-coprime.

If $g$ has an odd prime, put $x,y$ in type $0$, deleting one common
prime of $e,f$, and put $z$ alone in type $1$, deleting an odd prime of
$g$.  If $g$ is a power of $2$ but $e,f$ share an odd prime, put
$x,y$ in type $1$ using that prime and put $z$ alone in type $0$.

It remains that $g$ is a power of $2$ and $(e,f)$ has no odd prime.
Since it is nontrivial, both $e$ and $f$ are even.  At least one of them
has an odd prime, because two distinct powers of $2$ cannot form a primitive
pair.  Leave a member having an odd prime as the singleton type-$1$ node.
Pair the other member with $z$, delete $2$ from both sources, and give both
type $0$.  Their cores are respectively $x/2$ (or $y/2$) and $z/2$.
The two sources lie in the primitive height-one level, so Lemma 1.2 makes this
type-$0$ pair primitive.  Each construction also respects the local labelled
shadow condition at $r$, because the two siblings either use a common-prime
primitive pair in one type or receive different types.  ∎

## 4. The five-point theorem

### Theorem 4.1

Every finite quasi-primitive set $B\subseteq\mathbb N$ with $|B|\le5$
admits HBC.  More strongly, every lower-cover selector satisfying

\[
 h(\sigma(b))=h(b)-1
\tag{4.1}
\]

can be completed by weighted-admissible immediate shadows and binary types
to satisfy HBC.

#### Proof

We first close the stronger selector quantifier for $|B|\le4$.  With one root
and at most three nonroots, every non-singleton positive level is either an
at-most-three-child palette of the root or an at-most-two-child palette of the
unique node at the preceding level; Lemma 2.1 handles it for every height
selector.  With two roots and two nonroots, comparable nonroots have different
heights.  If they are incomparable, both have height one: a common selected
parent gives a two-child palette; different parents are handled by type
separation when an odd incoming prime exists, and otherwise both quotients are
powers of $2$, so division of the two primitive height-one sources by the
common denominator $2$ applies.  Three or more roots leave at most one
nonroot.  The cases of at most three total elements are contained in the same
argument.  Thus the claimed arbitrary-height-selector conclusion is already
valid below five points.

The empty-word cores are the roots, which form a primitive set.  We classify
the selected forest by its number $R$ of roots and by the profile
$(n_1,n_2,\ldots)$, where $n_j=|B_j|$.  Only non-singleton positive
levels require choices; at a singleton level, delete any prime on its incoming
edge and use type $0$.  Intrinsic height has no gaps: a longest chain to a
height-$j$ node contains nodes of heights $0,1,\ldots,j$, since a larger
height at an intermediate node would splice to a longer chain.  Consequently
the profiles displayed below exhaust all compositions of the nonroot count.

**One root.**  There are at most four nonroots.  The possible nonzero height
profiles are

\[
 (4),\ (3,1),\ (2,2),\ (2,1,1),\ (1,3),\
 (1,2,1),\ (1,1,2),\ (1,1,1,1).
\tag{4.2}
\]

For $(4)$, apply Lemma 2.1 to the four children of the root.  For
$(3,1)$, apply it to the three height-one children; the height-two level is
a singleton.  In $(2,1,1)$, only the two height-one siblings can conflict.
In $(1,3)$, the three height-two nodes are siblings of the unique
height-one node.  The profiles $(1,2,1)$ and $(1,1,2)$ likewise have one
two-sibling level.  Lemma 2.1 handles all these cases.

For $(2,2)$, first give the two height-one siblings a common-prime type-$0$
deletion.  Their words and complete deleted products therefore agree, and
their cores are primitive.  If the two height-two nodes share a parent, apply
the two-member case of Lemma 2.1.  If their parents differ, then either one
incoming quotient has an odd prime, in which case separate the two complete
words by types $1$ and $0$, or both quotients are powers of $2$.  In the
latter case delete $2$ from both.  Their height-one parent paths deleted the
same prime, so Lemma 2.2 applies.  Finally, the profile $(1,1,1,1)$ is a
chain and has no positive-level pair.

**Two roots.**  There are at most three nonroots.  The possible profiles are

\[
 (3),\ (2,1),\ (1,2),\ (1,1,1).
\tag{4.3}
\]

For $(3)$, either all three selected parents agree, when Lemma 2.1 applies,
or the children split $2+1$ between the two roots, when Lemma 3.1 applies.
For $(2,1)$, handle the two height-one nodes as follows.  If they share a
parent, use their common-prime type-$0$ deletion.  If their parents differ
and one quotient has an odd prime, separate their types.  If both quotients
are powers of $2$, delete $2$ from both; their cores are the two primitive
height-one sources divided by the common denominator $2$.  The height-two
node is a singleton.  For $(1,2)$, both height-two nodes have the unique
height-one node as parent and Lemma 2.1 applies.  The last profile is a chain.

**Three roots.**  There are at most two nonroots.  If both have height one
and share a selected parent, use Lemma 2.1.  If their parents differ, separate
their types when an odd prime is available; if both quotients are powers of
$2$, divide both height-one sources by $2$ and use Lemma 1.2.  If their
heights differ, every positive level is a singleton.

With four or five roots there is at most one nonroot, so every nonempty-word
batch is a singleton.  This exhausts all profiles.  Every local palette choice
was injective after adjoining its type, every type-$1$ deletion used an odd
prime, and every complete-word core batch was shown primitive and injective.
Thus the resulting choices satisfy HBC.  ∎

### Corollary 4.2 (new finite obstruction boundary)

Every finite counterexample to universal HBC has at least six elements.

This is a paper theorem, not a computational inference.  The archived exact
searches remain useful for testing larger cases, but no finite search proves
the universal statement.

## 5. Exact remaining gap

The proof uses all of the available five-point scarcity.  At six points new
configurations appear which are not covered by the argument, including:

1. five children of one root, for which a binary partition into primitive
   immediate-shadow classes is not supplied by Lemma 2.1;
2. three same-word nodes split among three distinct parents;
3. two consecutive non-singleton levels whose parent deleted products need
   not agree.

None of these configurations is asserted to be an obstruction.  They are the
next paper targets.  A route may be closed only by a strict all-choice
counterexample, not by failure of the present case analysis.  No
conjecture-level Lean formalization is appropriate before universal HBC (or a
sufficient replacement proving the original domination statement) is proved
and independently reviewed twice.
