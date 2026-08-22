# Universal HBC countersearch: exact finite CSP, canonical selectors, and boundaries

Date: 22 August 2026  
Scope: Conjecture 6.2 (universal hybrid primitive-batch selection) in `q1_next_round.md`  
Status: **no universal-HBC counterexample found; one cardinality-minimal failing fixed-selector pair and one proved small-cardinality boundary**

This note reports a reverse/computational attack. It does **not** prove universal HBC,
the historical quasi-primitive implication, or Erdős Problem 892. A finite counterexample
to universal HBC, if found, would refute only the hybrid mechanism unless it were separately
amplified into a lower bound for primitive domination.

## 1. Exact finite decision problem

Let $B$ be a finite historically quasi-primitive set. For every nonminimal $b\in B$,
let $L(b)$ be its lower covers in the induced divisibility poset. A local choice at $b$
is a quadruple

\[
 (d,p,\psi,t),\qquad d\in L(b),\quad p\mid b/d\text{ prime},\quad
 \psi=(b/d)/p,\quad t\in\{0,1\},
\]

subject to $q_t\le p$, where $q_0=2$ and $q_1=3$. Choices of two children with the same
parent may not use the same pair $(\psi,t)$. This is exactly the admissible weighted local
labelled-map condition: choosing an immediate shadow is equivalent to choosing the deleted
prime $p$.

Once all ancestors of $b$ are chosen, recursively define

\[
 \epsilon(b)=\epsilon(d)t,\qquad c(b)=c(d)\psi,
\]

with $\epsilon(r)=\varnothing$ and $c(r)=r$ at a root. HBC holds exactly when, for every
word $\epsilon$, the cores $c(b)$ with $\epsilon(b)=\epsilon$ are distinct and pairwise
incomparable under divisibility.

The checker is `hbc_checker.py`. It uses integer arithmetic only. Nodes are processed
increasingly, so every possible parent has already been assigned. At a node it enumerates
every quadruple above, rejects a duplicate local pair, and rejects a core as soon as it is
equal or comparable to an earlier core in the same complete-word batch.

### Proposition 1.1 (checker correctness)

For every finite quasi-primitive $B$, the checker returns `satisfiable=true` if and only if
$B$ admits a lower-cover selector and admissible weighted shadow/type choices satisfying
HBC. With `--fixed-parents`, the same equivalence holds for the displayed selector.

**Proof.** The domain belonging to $b$ lists every lower cover, every prime divisor of its
edge quotient, and every type allowed by $q_t\le p$. Thus the Cartesian product of the
domains contains every possible joint choice. The local rejection is precisely injectivity
of $(\psi,t)$ inside a parent palette. Since divisors are numerically smaller, recursion
computes the complete word and core exactly when a choice is visited. Equality or
divisibility between two completed same-word cores cannot be repaired by choices at later
descendants, so this pruning loses no solution. A surviving leaf satisfies all local and
HBC constraints, and conversely every HBC assignment follows one unrejected branch to a
surviving leaf. ∎

The reproducible development cross-check is `hbc_crosscheck.py`. It uses a separate raw
Cartesian-product evaluator. The command

```text
python hbc_crosscheck.py
```

uses seed 8922026 and retains 150 structured quasi-primitive samples having at least two
nonroots and at most 200,000 raw assignments. The archived run generated 162 candidates,
retained 150, had maximum retained raw-domain size 54,432, examined 5,675 assignments before
its early satisfiable exits, and found zero decision disagreements with the DFS. This is a
software check, not a substitute for Proposition 1.1.

## 2. A cardinality-minimal failing pair for the numerical-minimum selector

Put

\[
 B_0=\{2,3,4,12\}.
\]

It is quasi-primitive: the gcd of every incomparable pair is $1\notin B_0$. The lower
covers are

\[
 L(4)=\{2\},\qquad L(12)=\{3,4\}.
\]

Let $\sigma_{\min}$ choose the numerically smallest lower cover. It fixes

\[
 2\longrightarrow4,
 \qquad
 3\longrightarrow12.
\]

Both quotients, $2$ and $4$, have only the deleted prime $2$; hence both types are forced
to be $0$. The shadows are $1,2$, so the two word-$0$ cores are

\[
 c(4)=2\cdot1=2,
 \qquad
 c(12)=3\cdot2=6.
\]

Since $2\mid6$, HBC fails. There are no remaining shadow or type choices. This paper
certificate is reproduced by

```text
python hbc_checker.py '2,3,4,12' --fixed-parents '{"4":2,"12":3}'
```

This is **not** a universal-HBC counterexample. Selecting $4\to12$ instead and deleting
$3$ gives words $0$ and $00$; each nonempty batch is a singleton, so HBC holds. The
maximum-height selector makes exactly this repair.

### Proposition 2.1 (cardinality minimality of the failing pair)

Every fixed selector on a quasi-primitive set of at most three elements admits HBC choices.
Therefore the pair $(B_0,\sigma_{\min})$ has the smallest possible **cardinality** among
failing fixed-selector instances, and hence among failures of the numerical-minimum
selector rule. No numerical-value, lexicographic, or uniqueness minimality is claimed.

**Proof.** With zero or one nonroot there is nothing to compare. With two nonroots and at
most three total elements, they either form a chain, in which case their complete words
have different lengths, or are two children of the same root. In the latter case their
quotient palette $\{e,f\}$ is primitive and non-coprime. Delete one common prime
$p\mid\gcd(e,f)$ from both and give both type $0$. The shadows $e/p,f/p$ are distinct and
incomparable, since divisibility between them would imply divisibility between $e,f$.
Hence their common-word core batch is primitive. ∎

## 3. A non-computational small-cardinality boundary

Define the intrinsic divisibility height by

\[
 h(b)=\max\{m:b_0\mid b_1\mid\cdots\mid b_m=b,
                  \ b_i\in B,\ b_i<b_{i+1}\}.
\]

A **maximum-height selector** chooses, for each nonroot $b$, a lower cover $d$ with
$h(d)=h(b)-1$; if several exist, the search script breaks ties by numerical value.

### Proposition 3.1

Every quasi-primitive $B$ with $|B|\le4$ admits some joint selector/shadow/type choice
satisfying HBC. Therefore a universal-HBC counterexample, if one exists, has at least five
elements.

**Proof.** Proposition 2.1 covers at most three elements. We first record a sibling
construction. If two selected children of a parent $d$ have quotients $e,f$, then
$\{e,f\}$ is primitive: otherwise one child would lie strictly between $d$ and the other,
contradicting the lower-cover condition. It is also non-coprime, because
$\gcd(e,f)=1$ would give $\gcd(de,df)=d\in B$ for an incomparable pair. Delete a common
prime from both and give both type $0$. The two shadows are incomparable, because
$e/p\mid f/p$ would imply $e\mid f$.

Now assume $|B|=4$ and use a maximum-height selector. The forest shapes are exhausted as
follows.

1. If there is at most one nonroot, every nonempty word batch is a singleton.
2. Suppose there is one root. If all three nonroots are its children, their quotient
   palette $\{e_1,e_2,e_3\}$ is primitive and pairwise non-coprime. If none is a power of
   $2$, choose two members, delete a common prime from that pair and give them type $0$;
   the third has an odd prime and receives type $1$. If one member is a power of $2$, it
   is the only such member, because two distinct powers of $2$ cannot form a primitive
   pair. Pair it with another member, delete $2$ from both and use type $0$; the remaining
   member has an odd prime and receives type $1$. If the forest is not a three-child star,
   every possible same-depth pair has a common parent: a depth-one pair shares the root,
   while a depth-two pair can have only the single available depth-one parent. Apply the
   sibling construction.
3. Suppose there are two roots and two nonroots $b_1,b_2$. If $b_1,b_2$ are comparable,
   the lower one is a lower cover of the upper one: no fifth element can lie between them,
   and a root cannot lie strictly above a nonroot. Select that edge, placing them at
   different depths. If they are incomparable and their selected parents agree, use the
   sibling construction. If their parents differ and one quotient has an odd prime,
   assign that edge type $1$ by deleting an odd prime and assign the other edge type $0$.
   If both quotients are powers of $2$, both edges are forced to delete $2$ with type $0$.
   Their cores are then $b_1/2$ and $b_2/2$, and
   $b_1/2\mid b_2/2$ holds if and only if $b_1\mid b_2$. Hence the cores remain
   incomparable.
4. With three or four roots there is at most one nonroot, returning to case 1.

All same-word batches are therefore injective and primitive. ∎

## 4. Exhaustive universal-HBC search

The driver is `hbc_search.py`. The command

```text
python hbc_search.py --profile exact --selector-mode existential
```

exhausted every **nonempty** quasi-primitive subset of each universe below. For each set,
the inner decision ranges over all selectors and all admissible shadows/types.

| universe | per-universe checks | universal-HBC counterexample |
|---|---:|---:|
| $[1,22]$ | 316,667 | none |
| $\{2^a3^b:0\le a\le5,\ 0\le b\le3\}$ | 237,685 | none |
| $\{2^a3^b5^c:0\le a,b\le2,\ 0\le c\le1\}$ | 14,451 | none |

The **per-universe check sum** is 568,803. Because the universes overlap, this is not a
global distinct-set count. Their union contains 567,646 globally distinct nonempty sets,
so 1,157 checks are cross-universe duplicates. No UNSAT instance occurred.

The second and third universes contain exponent-vector rectangles, diamonds, repeated
power-of-$2$ edges, and competing lower covers. Thus the computation directly stresses
forced-type-$0$ edges and selector cycles, but it remains only a finite search boundary.

The same exact sets were also checked with the fixed maximum-height selector:

```text
python hbc_search.py --profile exact --selector-mode max-height
```

Again the per-universe sum is 568,803, the global distinct-set count is 567,646, and no
UNSAT instance occurred. Within each fixed-selector instance, all admissible shadow/type
choices are decided exactly.

## 5. Deterministic sampled searches

The command

```text
python hbc_search.py --profile random --random-trials 100000 \
  --selector-mode existential
```

generated quasi-primitive sets in four larger exponent grids and among supersets of
$B_\ast$ with entries at most 2000. The within-suite-distinct counts were

\[
 98{,}346+99{,}915+99{,}787+94{,}376+100{,}000=492{,}424.
\]

This is a **per-suite check sum**, not a global distinct-set count. The union contains
492,421 globally distinct tuples, so three checks are cross-suite duplicates. The exact
inner solver found an HBC witness for every tested tuple. The seeds were 89201--89205.

For the maximum-height fixed-selector sub-conjecture, run

```text
python hbc_search.py --profile random --random-trials 100000 \
  --selector-mode max-height --seed-offset 10
```

The seeds 89211--89215 produced the within-suite-distinct counts

\[
 98{,}335+99{,}907+99{,}765+94{,}519+100{,}000=492{,}526.
\]

This is likewise a per-suite check sum. The union contains 492,523 globally distinct
tuples, so three checks are cross-suite duplicates. No UNSAT instance occurred. Random
generation affects only which finite sets are tested: every retained set receives an exact
CSP decision over the indicated selector and all admissible shadow/type choices.

No counterexample to the maximum-height selector was found in these exact or sampled
ranges. This is a search statement, not a theorem.

## 6. What the countersearch establishes

1. A fixed selector can fail at the smallest possible cardinality. The pair
   $(B_0,\sigma_{\min})$ refutes the numerical-minimum-cover rule, while another selector
   repairs the same set.
2. In this example the core relation $2\mid6$ accompanies the source relation $4\mid12$;
   selecting $4\to12$ separates the words by depth. Larger searches repeatedly exhibited
   this conflict-repair pattern.
3. Any universal-HBC counterexample must have at least five elements and defeat every
   selector repair. Isolated bad fixed selectors are insufficient; a counterexample needs
   a closed obstruction among alternative covers, shadows, and type words.
4. No such obstruction appeared in the tested intervals, exponent grids, or structured
   $B_\ast$ supersets. This keeps universal HBC alive but does not prove it.

The next reverse-search target is to encode cycles of alternative lower covers directly
and realize them arithmetically while preserving quasi-primitivity. In parallel, the
positive route can seek a terminating potential showing that a maximum-height reparenting
removes a first same-word core divisibility without creating an earlier obstruction. The
computations alone supply neither result.

## 7. Reproducibility

The scripts require only Python's standard library:

```text
python -m py_compile hbc_checker.py hbc_search.py hbc_crosscheck.py
python hbc_crosscheck.py
python hbc_search.py --profile exact --selector-mode existential
python hbc_search.py --profile exact --selector-mode max-height
python hbc_search.py --profile random --random-trials 100000 --selector-mode existential
python hbc_search.py --profile random --random-trials 100000 --selector-mode max-height --seed-offset 10
```

The final hashes after all reproducibility reruns are

```text
SHA256 hbc_checker.py             049f95406d18cef85fa8a0bc632d770d726bc9a250471fb515f7c3d7996c8afe
SHA256 hbc_search.py              919d4260a2896cd73cd446b168165253382972070170f94d3187eafe5e7d113b
SHA256 hbc_crosscheck.py          c6c3a94da4458cb9497f77725f74ae6009db32fb48d9fc0e8ed2772af5708ff3
```

No repository or Lean file was modified in this round.
