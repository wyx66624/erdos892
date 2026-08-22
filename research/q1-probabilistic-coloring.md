# Q1 probabilistic round: coherent conflict colouring and local-lemma criteria

Date: 22 August 2026  
Scope: the universal HBC selection gap in the quasi-primitive route to Erdős 892  
Status: **new exact reformulation and rigorous sufficient criteria; universal HBC remains open**

This note treats HBC as a forbidden-pattern problem rather than continuing the deterministic
induction or finite counterexample search. There are two outputs.

* For a fixed parent selector, admissible local two-shadow states form a product variable
  model. HBC failures are cylinder events on a conflict hypergraph whose support starts
  only after two paths diverge. The asymmetric Lovász local lemma gives an explicit
  sufficient condition.
* Once one prime deletion (hence one unlabelled shadow) is fixed on every edge, the
  remaining choices are edge bits. HBC is exactly a coherent proper colouring of depthwise
  core-comparability graphs. This gives an exact one-level extension test, a global
  bipartite sufficient condition, a union-bound criterion, and a local-lemma criterion.

None of these criteria is proved to hold for every quasi-primitive set. A strict family
at the end shows that randomising only the two type bits cannot repair an arbitrary fixed
shadow choice. The same family has an HBC repair using different shadows, so it does not
refute universal HBC.

## 1. Fixed-selector local-state model

Let $B\subseteq\mathbb N$ be finite and quasi-primitive. Fix a lower-cover selector

\[
 \sigma(v)\in B,\qquad \sigma(v)\prec v
\]

for every nonminimal $v\in B$. This gives a rooted forest. Write $r(v)$ for the root,
$h(v)$ for the depth, and

\[
 e_v=\frac{v}{\sigma(v)}.
\]

For a parent $d$, let $\operatorname{Ch}(d)=\{v:\sigma(v)=d\}$. A **local weighted
two-shadow state** at $d$ is a simultaneous assignment

\[
 v\longmapsto (p_v,\delta_v,t_v)\qquad(v\in\operatorname{Ch}(d))
\tag{1.1}
\]

such that

1. $p_v$ is prime, $p_v\mid e_v$, and $\delta_v=e_v/p_v$;
2. $t_v\in\{0,1\}$, with $q_{t_v}\le p_v$, where $q_0=2,q_1=3$;
3. the pairs $(\delta_v,t_v)$, $v\in\operatorname{Ch}(d)$, are distinct.

Let $\Omega_d$ be the finite set of local states. The mixed-rank two-shadow theorem
used in the main Q1 note says that $\Omega_d\ne\varnothing$ for every Hasse palette.
Choose a probability measure $\mu_d$ on $\Omega_d$, and choose the random states
$X_d$ independently over the parents $d$.

If the path to $v$ is

\[
 r=v_0\to v_1\to\cdots\to v_h=v,
\]

define the random word and core

\[
 T(v)=(t_{v_1},\ldots,t_{v_h}),\qquad
 C(v)=r\prod_{j=1}^h\delta_{v_j}.
\tag{1.2}
\]

For distinct vertices $x,y$ of the same depth, define the bad event

\[
 A_{x,y}=\{T(x)=T(y)\text{ and }(C(x)\mid C(y)\text{ or }C(y)\mid C(x))\}.
\tag{1.3}
\]

Equality of cores is included. Pairs at different depths never have equal complete type
words and need no bad event. The local-state definition has already imposed labelled-map
injectivity inside each parent palette.

For this note, a realisation **satisfies HBC** when those local labelled maps are
injective and, for every finite binary word $w$, the map

\[
 v\longmapsto C(v)\qquad(T(v)=w)
\]

is injective with primitive image. This includes the empty word: its image is the
divisibility-minimal root set.

### Lemma 1.1 (HBC is avoidance of the pair events)

A realisation of the local states satisfies HBC if and only if none of the events
$A_{x,y}$ occurs.

**Proof.** Fix a word $w$. Its core batch fails injectivity or primitivity exactly when
two distinct vertices with word $w$ have equal or comparable cores. Such vertices have
the same depth $|w|$, and this is precisely an event in (1.3). Conversely, every event
(1.3) is such a batch failure. ∎

### Lemma 1.2 (the common prefix cancels from the event support)

Suppose $x,y$ have the same root and let $z$ be their last common ancestor. Write

\[
 z=u_0\to u_1\to\cdots\to u_s=x,
 \qquad
 z=w_0\to w_1\to\cdots\to w_s=y.
\tag{1.4}
\]

The suffix lengths are equal because $h(x)=h(y)$. Then $A_{x,y}$ depends only on

\[
 \{X_{u_0},X_{u_1},\ldots,X_{u_{s-1}},
   X_{w_0},X_{w_1},\ldots,X_{w_{s-1}}\}.
\tag{1.5}
\]

Here $u_0=w_0=z$, so the support has at most $2s-1$ local blocks. If $x,y$ have
different roots and common depth $h$, the support consists of the parent blocks on both
complete paths and has at most $2h$ blocks.

**Proof.** Along a common prefix, the type coordinates are the same random variables and
impose no equality condition. Also

\[
 C(x)=C(z)\prod_{i=1}^{s}\delta_{u_i},\qquad
 C(y)=C(z)\prod_{i=1}^{s}\delta_{w_i}.
\]

Cancelling the common positive integer $C(z)$ shows that core comparability depends only
on the two suffix products. The different-root assertion follows directly from (1.2),
since the two root values are fixed rather than random. ∎

Thus the conflict hypergraph does **not** put the complete ancestral path into every
event. Its variable vertices are the parent blocks $X_d$, and its hyperedge for
$\{x,y\}$ is the reduced support in Lemma 1.2. Two bad events are adjacent when their
reduced supports intersect.

### Theorem 1.3 (product-state asymmetric local-lemma criterion)

In the finite setting above, write $\Gamma(A)$ for the **other** bad events whose reduced
supports intersect the reduced support of $A$. Suppose there are numbers $z_A\in(0,1)$
such that

\[
 \mathbb P(A)\le z_A\prod_{A'\in\Gamma(A)}(1-z_{A'})
\tag{1.6}
\]

for every bad event $A$. Then some choice of the local states satisfies HBC.

**Proof.** Events with disjoint reduced supports are functions of disjoint independent
local blocks, so the intersection graph of the supports is a dependency graph. We recall
the short asymmetric local-lemma argument. Induction on $|S|$ gives

\[
 \mathbb P\!\left(A\mid\bigcap_{A'\in S}\overline{A'}\right)\le z_A
\tag{1.7}
\]

whenever the conditioning event has positive probability. Split $S$ into neighbours and
non-neighbours of $A$. The joint non-neighbour conditioning is independent of $A$;
exposing the neighbours one at a time and using the induction hypothesis bounds the
denominator from below by the product of their $1-z_{A'}$ factors. Inequality (1.6)
then proves (1.7). Finally expose all bad events one at a time. The conditional probability
of avoiding the next event is at least $1-z_A>0$, so the probability of avoiding every
bad event is positive. Lemma 1.1 completes the proof. ∎

This theorem permits the shadow and type choices at one parent to be correlated in any
way required by local labelled injectivity.

### Corollary 1.4 (collision entropy plus sparse conflicts)

For a pair $\{x,y\}$, let $s(x,y)$ be the post-LCA suffix length in (1.4), or the
full depth when the roots differ. Suppose that, under the product measures $\mu_d$, every
corresponding pair of suffix type coordinates has collision probability at most
$\theta<1$. At the first coordinate after a common last ancestor this refers to the
joint distribution of two child labels in the single state $X_z$; at all later
coordinates it refers to marginals from two independent parent states. Then

\[
 \mathbb P(A_{x,y})\le \theta^{s(x,y)}.
\tag{1.8}
\]

Consequently, if every conflict event has $s(x,y)\ge R$, meets at most $D$ other
reduced supports, and

\[
 e\,\theta^R(D+1)\le1,
\tag{1.9}
\]

then HBC choices exist.

**Proof.** The bad event is contained in the event that all corresponding suffix type
coordinates agree. The coordinate-equality tests use disjoint sets of parent blocks:
the first test may use the last-common-ancestor block, and every later test uses two new
parent blocks. Hence these tests are independent and their joint probability is at most
$\theta^{s(x,y)}$. The symmetric local lemma with $p=\theta^R$ gives (1.9). ∎

The requirement $\theta<1$ is substantive. Two forced type-$0$ edges have collision
probability $1$. Such a pair may still be harmless if its possible cores are never
comparable; the theorem only needs collision bounds for coordinate pairs occurring in
actual bad-event estimates.

## 2. Fixed shadows: HBC as a coherent binary colouring

Keep the parent selector fixed and choose, for every nonroot $v$, a prime $p_v\mid e_v$
and a shadow

\[
 \delta_v=e_v/p_v.
\tag{2.1}
\]

No injectivity is assumed of these unlabelled shadows. Put

\[
 \mathcal A_v=
 \begin{cases}
  \{0\},&p_v=2,\\
  \{0,1\},&p_v\ge3.
 \end{cases}
\tag{2.2}
\]

The core is deterministic:

\[
 c(v)=r(v)\prod_{u\text{ on the nonroot part of the path to }v}\delta_u.
\tag{2.3}
\]

For every depth $h$, define the **core-conflict graph** $G_h$. Its vertices are the
forest vertices of depth $h$, and distinct $x,y$ are adjacent exactly when

\[
 c(x)\mid c(y)\quad\text{or}\quad c(y)\mid c(x).
\tag{2.4}
\]

Core equality is an edge. If $t_v\in\mathcal A_v$ is an edge bit, let
$\lambda(v)\in\{0,1\}^{h(v)}$ be the word of edge bits on the root path.

### Proposition 2.1 (exact coherent-colouring reformulation)

For a fixed-shadow datum, a type assignment satisfies HBC if and only if, for every
$h$, the map

\[
 \lambda:V(G_h)\longrightarrow\{0,1\}^{h}
\tag{2.5}
\]

is a proper colouring of $G_h$, with every last edge bit in $\mathcal A_v$.

**Proof.** Two depth-$h$ vertices lie in the same HBC batch exactly when their path words
$\lambda$ agree. Such a batch is injective and primitive exactly when no edge of $G_h$
is monochromatic.

This condition also enforces the local labelled-map requirement. Indeed, if two siblings
$u,v$ have the same unlabelled shadow, then
$c(u)=c(\sigma(u))\delta_u=c(\sigma(v))\delta_v=c(v)$, so they are adjacent in $G_h$.
Their parent prefixes are identical; properness therefore forces their last bits to differ,
making $(\delta_u,t_u)\ne(\delta_v,t_v)$. If the shadows differ, the labelled pairs already
differ. Thus no separate shadow-injectivity assumption is needed. ∎

The colours in (2.5) are not arbitrary $2^h$ colours: a child's colour must extend its
parent's colour by one bit. Call this a **coherent binary separation**.

Two boundary conditions are immediate.

* At depth $0$, roots have empty word, but their cores are primitive, so $G_0$ has no edge.
* At depth $h$, HBC implies $\chi(G_h)\le2^h$, hence every clique in $G_h$ has size
  at most $2^h$. This is necessary but not sufficient by itself because it forgets
  coherence with depth $h-1$.

### Proposition 2.2 (exact one-level extension test)

Suppose coherent proper words have been assigned through depth $h-1$. For every word
$w\in\{0,1\}^{h-1}$, let

\[
 U_{h,w}=\{v:h(v)=h,\ \lambda(\sigma(v))=w\}.
\tag{2.6}
\]

The assignment extends through depth $h$ if and only if every induced graph
$G_h[U_{h,w}]$ has a proper two-colouring $v\mapsto t_v$ with
$t_v\in\mathcal A_v$.

Equivalently, every such graph is bipartite and, in each connected component, all vertices
forced to type $0$ lie on the same side of the bipartition (equivalently, every two forced
vertices in that component have even graph distance).

**Proof.** Vertices whose parents have different words already receive different
length-$h$ words, regardless of last bits. Inside $U_{h,w}$, two full words agree exactly
when their last bits agree. Thus the condition is precisely a proper allowed two-colouring.

A graph admits a proper two-colouring exactly when it is bipartite. A connected bipartite
graph has exactly two colourings up to swapping sides. Since there are no forced-$1$
vertices, an allowed orientation exists exactly when every forced-$0$ vertex belongs to
one side, equivalently when every pair is at even distance. This holds componentwise for
infinite graphs as well. ∎

If all deleted primes satisfy $p_v\ge3$, there are no forced vertices.

### Lemma 2.3 (two-colour obstruction is a three-core multichain)

For any finite or countable family of positive integers, with repetitions represented by
distinct vertices, its comparability graph is bipartite if and only if it has no three vertices
whose values are pairwise comparable. Thus, in the fully flexible case, the extension
in Proposition 2.2 fails exactly when some prefix class contains a three-vertex core
multichain.

**Proof.** Three pairwise comparable vertices form a triangle. Conversely, suppose the
comparability graph has an odd cycle of minimum length. If it has length three, we are
done. A longer shortest odd cycle is chordless. No equality edge can occur on it:
equal-valued adjacent vertices have the same neighbours, producing a triangle or chord.
Orient every remaining cycle edge by strict divisibility. At a cycle vertex, one incoming
and one outgoing incident edge would give a two-step divisibility chain, hence a chord
between its two cycle neighbours. Thus every vertex is a source or sink. Sources and sinks
must alternate, impossible on an odd cycle. ∎

### Corollary 2.4 (global last-bit sufficient condition)

Suppose that, for every depth $h\ge1$, the full graph
$G_h$ is bipartite with all forced-$0$ vertices in each component on one bipartition
side. Then the datum admits HBC.

In particular, if every $p_v\ge3$ and no depth contains a three-vertex core multichain,
then HBC holds.

**Proof.** Choose an allowed proper two-colouring $t_h$ of the entire graph $G_h$,
independently at each depth, and use $t_h(v)$ as the last edge bit of $v$. Adjacent
vertices at depth $h$ have different last bits, hence different complete words.
Proposition 2.1 applies. The last assertion is Lemma 2.3. ∎

Corollary 2.4 is stronger than the exact prefix test. A dense $G_h$ can still be harmless
when its edges run between vertices already separated by prefixes.

## 3. Exact probability bounds in the fixed-shadow model

Choose every flexible edge bit independently and uniformly from $\{0,1\}$, leaving edges
with $p_v=2$ fixed at $0$. For a conflict edge $\{x,y\}\in E(G_h)$, remove the common
path prefix as in Lemma 1.2. Define $\eta(x,y)$ to be the number of corresponding suffix
positions at which at least one of the two edges is flexible. For different roots, use
all $h$ positions.

### Lemma 3.1 (exact word-collision probability)

\[
 \mathbb P(\lambda(x)=\lambda(y))=2^{-\eta(x,y)}.
\tag{3.1}
\]

**Proof.** At a suffix coordinate where both bits are forced $0$, equality has probability
$1$. If exactly one is flexible, equality has probability $1/2$. If both are flexible,
the distinct edge variables agree with probability $1/2$. After the last common ancestor
the paths are disjoint, so tests at different coordinates use disjoint variables and are
independent. The common prefix agrees identically. ∎

### Theorem 3.2 (summable-conflict criterion)

For a finite or countable fixed-shadow datum, if

\[
 \sum_{h\ge1}\ \sum_{\{x,y\}\in E(G_h)}2^{-\eta(x,y)}<1,
\tag{3.2}
\]

then an HBC type assignment exists.

**Proof.** Every summand is the probability of the corresponding word-collision event.
The union bound shows their union has probability less than one. Hence some assignment
avoids every event, and Proposition 2.1 gives HBC. The countable union bound handles
countable data. ∎

The strict inequality is only sufficient; equality or divergence does not prove
nonexistence.

Let $S_{x,y}$ be the set of flexible suffix edge variables used by the equality event
for $\{x,y\}$. Join two conflict edges when their $S$-sets intersect.

### Theorem 3.3 (fixed-shadow local-lemma criterion)

Suppose every conflict edge has $\eta(x,y)\ge R$, and every set $S_{x,y}$ intersects
at most $D$ other such sets. If

\[
 e\,2^{-R}(D+1)\le1,
\tag{3.3}
\]

then the datum admits HBC.

More generally, it is enough to find $z_{x,y}\in(0,1)$ satisfying

\[
 2^{-\eta(x,y)}
 \le z_{x,y}
 \prod_{\substack{\{u,v\}\ne\{x,y\}\\
                   S_{u,v}\cap S_{x,y}\ne\varnothing}}(1-z_{u,v}).
\tag{3.4}
\]

These assertions remain valid for countable data when the symmetric bounds $R,D$ are
uniform.

**Proof.** Lemma 3.1 gives event probabilities, and disjoint $S$-sets give independent
events. The finite assertions are Theorem 1.3 and its symmetric specialization. For
countable data under (3.3), every finite family of bad events is avoidable by the finite
lemma. Each avoidance condition is clopen in the compact product of finite edge domains.
The finite-intersection property gives an assignment avoiding all bad events. ∎

If every bad event uses at most $L$ flexible edge variables and every flexible edge
belongs to at most $M$ bad events, then

\[
 D\le L(M-1).
\tag{3.5}
\]

Indeed, charge every neighbouring event to a shared variable; overcounting improves the
bound.

## 4. A strict capacity obstruction to type-only randomisation

The local-lemma route cannot be applied uniformly after an arbitrary fixed choice of
shadows. There is a simple unbounded obstruction family.

### Proposition 4.1 (depth-one chain obstruction)

Let $m\ge3$, choose distinct odd primes $p_1,\ldots,p_m$, and put

\[
 B_m=\{1\}\cup\{2^ip_i:1\le i\le m\}.
\tag{4.1}
\]

Then $B_m$ is quasi-primitive and every top vertex has the unique lower cover $1$.
For the fixed shadow choices

\[
 2^ip_i\longmapsto 2^i\qquad(\text{delete }p_i),
\tag{4.2}
\]

the displayed shadows are distinct and all bits are flexible, but no assignment of the
two type bits satisfies HBC. On the other hand, deleting $2$ on every edge gives an HBC
assignment.

**Proof.** The top elements are pairwise incomparable because $p_i$ occurs in only the
$i$-th one. For $i<j$,

\[
 \gcd(2^ip_i,2^jp_j)=2^i\notin B_m.
\]

Thus $B_m$ is quasi-primitive. There is no member of $B_m$ strictly between $1$ and a
top element, so $1$ is its lower cover.

Under (4.2), the depth-one cores are $2,4,\ldots,2^m$, a clique of size $m$ in
$G_1$. There are only two length-one words. Proposition 2.1 shows HBC is impossible
when $m\ge3$. Every deleted prime $p_i$ is at least $3$, so all bits are free; lack of
type capacity is the only failure.

If instead one deletes $2$, the shadows are

\[
 2^{i-1}p_i\qquad(1\le i\le m).
\]

They are pairwise incomparable because of their distinct private odd primes. The deletion
prime $2$ forces type $0$, but the sole word-$0$ core batch is primitive. Hence the
second shadow choice satisfies HBC. ∎

This proposition rigorously excludes the strategy

> fix arbitrary immediate shadows first, then hope that random binary types always repair
> the global collisions.

It does **not** exclude a probabilistic proof that randomises shadows, local states, or
the parent selector: the displayed repair certifies HBC for the same set.

The family gives the sharp depth-one capacity boundary when all corresponding bits are
flexible: one or two depth-one cores in a chain can be separated by two types, whereas
three cannot. With forced-$0$ lists, even a comparable pair can be impossible, as the
even-distance condition in Proposition 2.2 records. More generally, Proposition 2.1 gives
the necessary condition

\[
 \omega(G_h)\le2^h\qquad(h\ge0)
\tag{4.3}
\]

for every fixed-shadow HBC datum.

## 5. What the probabilistic route has and has not reduced

The route now has three precise sufficient targets.

1. **Global last-bit target.** Choose a parent selector and one prime deletion per edge so
   every depth graph $G_h$ is allowed-bipartite as in Corollary 2.4.
2. **Coherent prefix target.** Choose earlier bits so every induced prefix graph
   $G_h[U_{h,w}]$ passes the exact precoloured bipartite test of Proposition 2.2. With
   no forced bits, no prefix class may contain a three-core multichain.
3. **Local-lemma target.** For arbitrary admissible local states, construct product
   measures satisfying (1.6), or verify collision entropy and reduced-support sparsity
   as in (1.9). Only divergent suffix blocks contribute to the event hyperedge.

The following are genuine obstacles, but none refutes the full route.

* Forced $p=2$ labels can supply zero type entropy. They must instead be made harmless
  arithmetically, as in the repair in Proposition 4.1 and the repeated-$2$ stress test.
* A common parent block may coordinate the first two divergent edge labels, and a
  high-branching block may lie in many reduced event supports. A bounded-$D$ estimate is
  not automatic.
* Failure of the union bound, symmetric local-lemma inequality, or global bipartite
  condition is not evidence of nonexistence: all three are only sufficient.
* Proposition 4.1 proves shadow optimisation is necessary for this route. It gives no
  robust set defeating every selector and every local state.

Combining a universal version of any target with the absorbed primitive-batch erasure
theorem in the main Q1 note would yield a bounded primitive injection, and sorting would
give ordered domination for the quasi-primitive case. At present the exact unproved
implication remains

\[
 \text{quasi-primitivity}
 \quad\Longrightarrow\quad
 \text{some selector and admissible local states meeting an HBC criterion above}.
\]

No Lean formalisation is started because that implication has not been proved and the
original conjecture remains open.
