# Q1 alternative route: rank--slack refinement of nonprimitive core batches

Date: 22 August 2026  
Scope: a mechanism-level strict relaxation of HBC for fixed shadow data in the
quasi-primitive part of Erdős Problem 892  
Status: **proved sufficient criterion; the universal rank--slack estimate is open**

The absorbed label-erasure theorem in `q1_next_round.md` needs a sublinear family of
primitive batches with deadlines paid by the deleted-prime product.  HBC achieves this
by requiring every complete binary-word batch to be primitive.  This note shows that
HBC is stronger than necessary: a nonprimitive word batch may be split by its internal
divisibility rank, provided the rank is paid by enough unused deletion slack.

Nothing below proves that every quasi-primitive set has such choices.  The new open
problem is an arithmetic chain-rank estimate, not a completed proof of Erdős 892.

## 1. Core preorder with multiplicities

Let \(X\) be finite or countable.  For every \(x\in X\), suppose that

\[
 b_x=c_x\Delta_x,
 \qquad c_x,\Delta_x\in\mathbb N.
\tag{1.1}
\]

Assume that \(X\) is partitioned into base batches \(X_t\), with a base deadline
\(W_t\ge1\) satisfying

\[
 W_t\le\Delta_x\qquad(x\in X_t).
\tag{1.2}
\]

Fix once and for all an enumeration of every \(X_t\).  On \(X_t\), define
\(x\triangleleft_t y\) when either

1. \(c_x\mid c_y\) and \(c_x<c_y\); or
2. \(c_x=c_y\) and \(x\) occurs earlier than \(y\) in the fixed enumeration.

Its reflexive closure is a partial order.  It resolves equal-core multiplicities and
has the essential property

\[
 x\ne y,\quad(c_x\mid c_y\text{ or }c_y\mid c_x)
 \quad\Longrightarrow\quad
 x,y\text{ are comparable under }\triangleleft_t.
\tag{1.3}
\]

Define the **terminal core rank**

\[
 R_t(x)=\sup\{m:\ x_1\triangleleft_t\cdots
                 \triangleleft_t x_m=x\}\in\mathbb N\cup\{\infty\}.
\tag{1.4}
\]

The value can be infinite, for example when infinitely many equal copies of a proper
divisor precede \(c_x\) in the divisibility order.  No finiteness is silently assumed.
When the supremum is a finite integer, it is attained because the set of possible
finite chain lengths is a nonempty subset of \(\mathbb N\).

### Lemma 1.1 (rank layers are primitive batches)

For every finite \(j\), the map \(x\mapsto c_x\) on

\[
 X_{t,j}=\{x\in X_t:R_t(x)=j\}
\tag{1.5}
\]

is injective and its image is primitive.

**Proof.**  If two distinct members of \(X_{t,j}\) had equal or comparable cores,
(1.3) would orient them, say \(x\triangleleft_t y\).  Appending \(y\) to a longest
chain ending at \(x\) gives \(R_t(y)\ge R_t(x)+1\), contrary to equality of the
ranks.  This also excludes equal cores.  ∎

## 2. The rank--slack erasure theorem

Fix \(0<s<1\).  Assume that the base deadlines satisfy the summability condition

\[
 \sum_t W_t^{-s}<\infty.
\tag{2.1}
\]

For a refined label \((t,j)\), with \(j\in\mathbb N_{\ge1}\), put

\[
 V_{t,j}=W_tj^{1/s}.
\tag{2.2}
\]

### Lemma 2.1 (sublinear refined-label count)

Writing \(S_s=\sum_tW_t^{-s}\), there is a constant
\(A_s=S_s<\infty\) such that

\[
 \#\{(t,j):V_{t,j}\le y\}\le A_sy^s
 \qquad(y\ge1).
\tag{2.3}
\]

**Proof.**  For a fixed \(t\), the number of possible \(j\)'s is at most
\((y/W_t)^s\).  Therefore

\[
 \#\{(t,j):V_{t,j}\le y\}
 \le y^s\sum_tW_t^{-s},
\]

which is (2.3).  ∎

### Theorem 2.2 (rank--slack primitive-batch erasure)

In addition to (1.1), (1.2), and (2.1), suppose that every \(x\in X_t\) has finite
rank and satisfies

\[
 W_tR_t(x)^{1/s}\le\Delta_x.
\tag{2.4}
\]

Then there is an injection \(\Phi:X\to\mathbb N\) whose image is primitive and

\[
 \Phi(x)\le D b_x\qquad(x\in X),
\tag{2.5}
\]

where \(D\) depends only on \(s\), the sum in (2.1), and the absolute constants in
the two-reservoir absorption lemma of `q1_next_round.md`.

**Proof.**  Refine the base partition to the nonempty rank layers \(X_{t,j}\).
Lemma 1.1 supplies the required injective primitive core batch.  Give this refined
batch deadline \(V_{t,j}\).  If \(x\in X_{t,j}\), (2.4) gives

\[
 V_{t,j}=W_tj^{1/s}\le\Delta_x.
\]

Lemma 2.1 gives the sublinear deadline count.  All hypotheses of the weighted
primitive-batch erasure theorem (`q1_next_round.md`, Theorem 3.1) now hold, so that
the latter theorem supplies a primitive injection with

\[
 \Phi(x)\le D c_x\Delta_x=Db_x.
\]

No HBC assumption was used.  ∎

The power \(1/s>1\) is not cosmetic.  Linear refined deadlines \(W_tj\) generally
give only \(O(y)\) labels.  The sparse absorbing reservoir used in the present proof
needs a genuinely sublinear deadline count.  A different arithmetic reservoir could
conceivably weaken this cost, but no such result is asserted here.

## 3. Binary shadow words

For the absorbed shadow construction, the base labels are all finite binary words
\(\epsilon\), and

\[
 W(\epsilon)=2^{\#0(\epsilon)}3^{\#1(\epsilon)}.
\tag{3.1}
\]

Fix once and for all an absolute \(s<1\) sufficiently close to \(1\) that

\[
 2^{-s}+3^{-s}<1.
\tag{3.2}
\]

Then

\[
 \sum_{\epsilon}W(\epsilon)^{-s}
 =\sum_{h\ge0}(2^{-s}+3^{-s})^h
 <\infty.
\tag{3.3}
\]

For fixed parent, shadow, and type choices, let \(c(b),\Delta(b)\), and
\(\epsilon(b)\) have their definitions from `q1_next_round.md`.  Resolve equal cores
by any enumeration and form \(R_\epsilon(b)\) from (1.4).

### Corollary 3.1 (rank--slack criterion for quasi-primitive shadow data)

If

\[
 W(\epsilon(b))R_{\epsilon(b)}(b)^{1/s}\le\Delta(b)
 \qquad(b\in B),
\tag{3.4}
\]

then \(B\) has an absolute-dilation primitive injection and, after sorting, a
primitive dominator \(a_n\le Db_n\).

**Proof.**  Equation (3.3) verifies (2.1), while the ordinary shadow budget gives
\(W(\epsilon(b))\le\Delta(b)\).  Apply Theorem 2.2 and then the order-statistics
argument of `q1_next_round.md`, Corollary 3.4.  ∎

HBC is the special case \(R_\epsilon(b)=1\) for every \(b\).  Corollary 3.1 permits
nonprimitive word batches of controlled internal height and multiplicity.

## 4. Strict extension beyond HBC for fixed shadow data

Consider the quasi-primitive set

\[
 B=\{2,3,42,330\}.
\tag{4.1}
\]

The only incomparable nonroot pair has gcd \(6\notin B\); the two roots \(2,3\)
have gcd \(1\notin B\), and both roots divide both top members.  Fix the lower-cover
and deletion choices

\[
 2\to42,\quad 42/2=21\mapsto3\ \text{(delete }7\text{)},
\]

\[
 3\to330,\quad330/3=110\mapsto10\ \text{(delete }11\text{)},
\tag{4.2}
\]

and give both edges type \(0\).  The common word-\(0\) batch has cores

\[
 6\mid30,
\tag{4.3}
\]

so these fixed data do **not** satisfy HBC.  Orient the two cores increasingly.
Their ranks are \(1,2\), their base deadline is \(W(0)=2\), and their deletion
budgets are \(7,11\).  For example \(s=9/10\) satisfies (3.2), and

\[
 2\cdot1^{10/9}\le7,
 \qquad
 2\cdot2^{10/9}<5<11.
\tag{4.4}
\]

The empty-word root batch has cores \(2,3\), rank \(1\), and
\(W(\varnothing)=\Delta=1\), so it also satisfies (3.4).

Thus the rank--slack criterion applies even though HBC fails for the displayed
choices.  This proves that Theorem 2.2 is a strict mechanism-level extension of the
absorbed HBC theorem.  It is not an infinite counterexample and says nothing against
the possibility that another choice on the same finite \(B\) satisfies HBC.

## 5. Exact remaining arithmetic target

For the same absolute \(s\) fixed before \(B\), and for a fixed word
\(\epsilon\), condition (3.4) is equivalent to

\[
 R_\epsilon(b)
 \le\left(\frac{\Delta(b)}{W(\epsilon)}\right)^s.
\tag{5.1}
\]

The ratio on the right is the unused product slack after paying the low-entropy
binary type word.  The closest open question on this route is:

> Can one jointly choose parents and immediate prime deletions so that every chain
> of equal/comparable same-word cores ending at \(b\), with equal-core multiplicity
> resolved, has length bounded by the \(s\)-power of the unused deletion slack?

A proof would yield the historical quasi-primitive implication through Corollary 3.1.
A strict finite counterexample would reject this particular rank--slack selector
criterion but would not refute Erdős 892 unless amplified into divergent domination
constants.  Until either is obtained, this route remains open alongside universal HBC,
prefix synchronization, exact-rank batching, and probabilistic conflict avoidance.

No Lean formalization is started: the universal rank estimate and the original
conjecture remain unproved.
