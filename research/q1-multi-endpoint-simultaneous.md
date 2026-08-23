# Nine-child stars: simultaneous even-endpoint continuation

Date: 22 August 2026  
Scope: continuation of the component-augmentation mechanism in PR #35  
Status: **independently reviewed paper result; nine-child HBC remains open**

This note treats the case left explicitly open by Theorem 3.3 of the
component-augmenting-path paper: the component of the `(2,0)` blocker may
contain several old type-0 vertices whose deleted prime is `2`.

The main result is an exact finite criterion.  Delete all such endpoints,
flip the remainder of the component, and try to reinsert every endpoint in
type 1 using an odd deletion.  The move succeeds precisely when the new
endpoint shadows are individually safe against the fixed type-1 row **and**
are pairwise incomparable.  Equivalently, the allowed deletion choices must
have an independent transversal in an explicitly defined interaction graph.

A genuine integer family then shows that the pairwise clause cannot be
discarded: every endpoint has a unique individually row-safe deletion, but
the two resulting shadows are equal.  This is a barrier only to the inference
"individual row-safety implies simultaneous row-safety".  The family is not
in the B24 three-singleton regime and is not an HBC counterexample.

Throughout, a **palette** is a finite primitive pairwise non-coprime family
of integers greater than one.  A state of a member `f` is `(d,t)`, where
`d|f` is prime, `t in {0,1}`, and `t=1` is allowed only for odd `d`.  The
shadow is `f/d`.  An assignment is **successful** if the shadows in each
type are injective and primitive.  Comparability always includes equality.

## 1. The base assignment after removing every even endpoint

Let `A` be a successful assignment on a finite palette `F`.  Write its states
as `(d_f,t_f)` and its shadows as `x_f=f/d_f`.  Its old-shadow comparability
graph `Gamma(A)` has vertex set `F` and an edge between distinct members
exactly when their shadows are comparable.  Every edge joins opposite old
types.

Fix a connected component `C` of `Gamma(A)` and define its **even endpoint
set**

```
G(C)={g in C : t_g=0 and d_g=2}.                       (1.1)
```

Delete all vertices of `G(C)`, flip the type of every vertex of
`C\G(C)`, and leave every state outside `C` fixed.  Deleted primes are not
changed.  Denote the resulting assignment on `F\G(C)` by `A^-`.

### Lemma 1.1 (simultaneous endpoint removal leaves a successful base)

The assignment `A^-` is successful.

#### Proof

Every old type-0 vertex left in `C\G(C)` has odd deleted prime by the
definition (1.1), so its flipped type-1 state is admissible.  Old type-1
vertices move to type 0, where no parity restriction is imposed.

Delete `G(C)` from `Gamma(A)`.  Each connected component of the induced
graph on `C\G(C)` is flipped in its entirety, and every component outside
`C` is left unchanged.  Therefore every remaining comparability edge still
has endpoints of opposite types.  Conversely, all comparabilities among the
fixed remaining shadows are edges of this induced graph.  Hence no two
shadows in either new row are comparable or equal.  Thus `A^-` is admissible,
injective, and primitive in both rows.  ∎

The word "endpoint" is mnemonic only: a member of `G(C)` need not have graph
degree one and need not be an endpoint of one chosen shortest path.

## 2. Simultaneous row-safety and the interaction graph

For `g in G(C)`, let

```
P_1(g)={r|g : r is an odd prime}.                       (2.1)
```

For `r in P_1(g)`, put `y(g,r)=g/r`.  Call `r` **base-safe for `g`** if
`y(g,r)` is incomparable with every type-1 shadow of `A^-`.  Define the
base-safe candidate fibre

```
S_g={r in P_1(g): r is base-safe for g}.                (2.2)
```

Equivalently, writing `(d_f,1)` for the state of a type-1 member `f` of
`A^-`, the audited B28 row-safety criterion gives the entirely valuation-level
formula

```
r in S_g
```

if and only if `r in P_1(g)` and, for every such `f`, neither

```
[r fragile surplus of g over f and d_f in D(f,g)]
```

nor

```
[d_f fragile surplus of f over g and r in D(g,f)]        (2.2a)
```

holds.  Here the state `(d_f,1)` is the state *after* endpoint removal and
component flipping; its deleted prime is nevertheless the original fixed
prime.

For a vector `r=(r_g)_{g in G(C)}` with `r_g in S_g`, call `r`
**simultaneously row-safe** when

```
y(g,r_g) and y(k,r_k) are incomparable
for every distinct g,k in G(C).                         (2.3)
```

This definition contains all quantifiers: base-safety is tested against
every already present type-1 shadow of `A^-`, while (2.3) is tested for every
unordered pair of distinct reinserted endpoints.  Equality is forbidden.

Define the **endpoint interaction graph** `J(A,C)` as follows.  Its vertex
set is the disjoint union

```
V(J)=coprod_{g in G(C)} ({g} times S_g).                (2.4)
```

Vertices `(g,r)` and `(k,q)` in different fibres are adjacent precisely when
`g/r` and `k/q` are comparable.  Edges within one fibre are irrelevant and
are omitted.  An **independent transversal** is an independent set containing
exactly one vertex from every fibre `{g} times S_g`.

For incomparable integers `a,b`, write

```
D(a,b)={ell prime:v_ell(a)>v_ell(b)}.
```

A prime `r` is a **fragile surplus of `a` over `b`** if

```
D(a,b)={r} and v_r(a)=v_r(b)+1.                         (2.5)
```

### Lemma 2.1 (valuation form of endpoint interaction)

For distinct endpoints `g,k`, choices `r in S_g` and `q in S_k` are adjacent
in `J(A,C)` if and only if at least one of the following holds:

1. `r` is a fragile surplus of `g` over `k` and `q in D(k,g)`;
2. `q` is a fragile surplus of `k` over `g` and `r in D(g,k)`.

#### Proof

The palette members `g,k` are incomparable.  The immediate-shadow criterion
applied to `(g,k)` says that `g/r | k/q` is equivalent to condition 1.
Applying it to `(k,g)` says that `k/q | g/r` is equivalent to condition 2.
Their disjunction is exactly comparability, including equality.  ∎

Thus both the fibres and every interaction edge are finite valuation tests;
no search over arbitrary integers is hidden in the definition.

For later estimates, Lemma 2.1 also gives the exact neighbourhood of one
choice `(g,r)` inside a different fibre `{k} times S_k`:

```
N_k(g,r)
= ({q in S_k intersect D(k,g): r is fragile surplus of g over k})
  union
  ({q in S_k: q is fragile surplus of k over g}
     if r in D(g,k), else emptyset).                    (2.5a)
```

The second set has cardinality at most one; the first can have several
members and is the precise place where a naive degree-one argument can fail.

### Theorem 2.2 (exact simultaneous reinsertion criterion)

Starting from `A^-`, there is a successful assignment on all of `F` obtained
by reinserting every `g in G(C)` in type 1, changing only its deleted prime,
if and only if `J(A,C)` has an independent transversal.

More explicitly, a deletion vector `(r_g)` works if and only if

```
r_g in S_g for every g in G(C),
```

and the pairwise conditions (2.3) hold.

#### Proof

By Lemma 1.1 the two rows of `A^-` are successful.  All new endpoints are
inserted in type 1, so the type-0 row is unchanged.  A new shadow `g/r_g`
has no comparison with an old type-1 shadow exactly when `r_g in S_g`.
After all endpoints are inserted, no two new type-1 shadows are comparable
exactly when (2.3) holds.  These two classes exhaust all possible new
same-row pairs: old-old, old-new, and new-new.  State admissibility follows
from `r_g` being odd.  Hence the conditions are necessary and sufficient.

Choosing one candidate in every fibre subject to no interaction edge is
precisely an independent transversal of `J(A,C)`.  ∎

### Corollary 2.3 (a deterministic greedy sufficient condition)

Order `G(C)={g_1,...,g_m}`.  For `j<i`, put

```
Delta_{i<-j}=max_{q in S_{g_j}}
 |{r in S_{g_i} : (g_i,r) is adjacent to (g_j,q)}|,     (2.6)
```

with maximum zero when `S_{g_j}` is empty.  If every fibre is nonempty and

```
|S_{g_i}| > sum_{j<i} Delta_{i<-j}                     (2.7)
```

for `i=1,...,m`, then simultaneous reinsertion succeeds.

#### Proof

Choose candidates in the displayed order.  Once candidates have been chosen
for `g_1,...,g_{i-1}`, the choice at `g_j` forbids at most
`Delta_{i<-j}` candidates in the `i`-th fibre.  The union of all forbidden
candidates has size at most the right side of (2.7), strictly less than the
fibre size.  Choose a remaining candidate.  Induction gives an independent
transversal, and Theorem 2.2 applies.  ∎

The strict inequality is only sufficient; overlap among neighbourhoods may
permit a transversal when (2.7) fails.

## 3. Application to the B24 `(2,0)` component

Assume now the complete B24/B26 hypotheses used in PR #35.  Thus

```
E=F union {e},   supp(e)={2,p,q},
```

`e` has minimum `Omega`, `A` is a successful assignment on `F`, and
`h=h_{2,0}` is the unique type-0 blocker of the option `(2,0)`.  Let `C_2` be
the component of `h` in `Gamma(A)` and set

```
G_2=C_2 intersect {g:t_g=0,d_g=2}.                     (3.1)
```

B26 gives `d_h` odd, hence `h notin G_2`.  Let `A^-` be the base assignment
of Section 1 for `C=C_2`.

### Theorem 3.1 (exact multi-endpoint continuation at `(2,0)`)

Perform the following prescribed move:

1. remove every member of `G_2`;
2. flip every remaining old type in `C_2`;
3. leave every state outside `C_2` fixed;
4. reinsert each `g in G_2` in type 1 after deleting an odd prime `r_g|g`;
5. insert `e` in state `(2,0)`.

This move is successful if and only if the interaction graph `J(A,C_2)` has
an independent transversal.  In particular, the choices are exactly the
simultaneously row-safe vectors of Section 2.

#### Proof

Lemma 1.1 proves that `A^-` is successful.  By Theorem 2.2, steps 1--4 give a
successful assignment on `F` exactly under the independent-transversal
condition.

It remains only to check step 5.  PR #35, Lemma 3.1 proves that among all
**original** fixed shadows, only the shadow of `h_{2,0}` is comparable with
`e/2`.  The member `h` lies in `C_2\G_2` and has therefore moved from type 0
to type 1.  All other unchanged shadows either stay outside type 0 or were
never comparable with `e/2`.  Every changed endpoint shadow is inserted in
type 1.  Hence no type-0 shadow is comparable with `e/2`, and insertion is
successful.

Conversely, success of the prescribed final assignment implies success of
its restriction to `F`, so Theorem 2.2 forces an independent transversal.
∎

### Boundary cases

- If `G_2` is empty, the empty set is an independent transversal and Theorem
  3.1 reduces to the component flip of PR #35, Theorem 3.2.
- If `|G_2|=1`, an independent transversal exists exactly when its sole
  fibre is nonempty.  This is PR #35, Theorem 3.3.
- For `|G_2|>=2`, nonempty fibres are necessary but not sufficient, as the
  next section proves.

The theorem is exact only for the five-step move stated above.  Failure of
its interaction graph does not exclude changing shadows outside `G_2`,
choosing another eight-member assignment, inserting another option of `e`,
or using a larger augmenting structure.

## 4. A strict barrier to endpointwise row-safety

Let

```
2,q,z,b,d,r_1,r_2,s,c_1,c_2
```

be pairwise distinct primes, all except `2` odd.  Put

```
h   = d q z b,             v   = q^2 z,
g_i = 2 q z r_i s,         w_i = 2 q^2 r_i,
u_i = 2 z r_i c_i          (i=1,2),                    (4.1)
```

and let

```
F={h,v,g_1,g_2,w_1,w_2,u_1,u_2}.
```

Give these members the states

| member | deleted prime | old type | old shadow |
|---|---:|---:|---:|
| `h` | `d` | 0 | `qzb` |
| `g_i` | `2` | 0 | `qzr_i s` |
| `v` | `q` | 1 | `qz` |
| `w_i` | `q` | 1 | `2qr_i` |
| `u_i` | `c_i` | 1 | `2zr_i` |

### Proposition 4.1 (individual candidates without a simultaneous choice)

For every choice of the primes above:

1. `F` is primitive and pairwise non-coprime, and the displayed assignment
   is successful;
2. the component of `h` in `Gamma(A)` is exactly
   `C={h,v,g_1,g_2}`, and `G(C)={g_1,g_2}`;
3. after deleting `g_1,g_2` and flipping `{h,v}`, the base-safe fibres are

   ```
   S_{g_1}={r_1},       S_{g_2}={r_2};                 (4.2)
   ```

4. the two forced new shadows are equal:

   ```
   g_1/r_1=2qzs=g_2/r_2.                              (4.3)
   ```

Consequently every endpoint separately has a base-safe deletion, but
`J(A,C)` has no independent transversal and simultaneous reinsertion fails.

#### Proof

Every pair of members in (4.1) has a displayed common factor.  More exactly,
`h` meets `v,g_i,w_i,u_i` at `qz,qz,q,z`, respectively; `v` meets
`g_i,w_i,u_i` at `qz,q^2,z`; `g_i` meets `g_j,w_j,u_j` at least at
`2qzs,2q,2z`; and any two members among the `w_i,u_j` meet at least at `2`.
Hence `F` is pairwise non-coprime.

For primitivity, the following table gives a prime or factor surplus in each
direction for every pair class.  An "extra `q`" means one additional unit of
the `q`-valuation.

| pair | surplus of first over second | surplus of second over first |
|---|---|---|
| `h,v` | `d` (also `b`) | extra `q` |
| `h,g_i` | `d` (also `b`) | `2` (also `r_i`) |
| `h,w_i` | `d` (also `z,b`) | `2` (also extra `q`) |
| `h,u_i` | `d` (also `q,b`) | `2` (also `r_i,c_i`) |
| `v,g_i` | extra `q` | `2` (also `r_i,s`) |
| `v,w_i` | `z` | `2` (also `r_i`) |
| `v,u_i` | `q` | `2` (also `r_i,c_i`) |
| `g_i,g_j`, `i!=j` | `r_i` | `r_j` |
| `g_i,w_i` | `z` (also `s`) | extra `q` |
| `g_i,w_j`, `i!=j` | `z` (also `r_i,s`) | extra `q` (also `r_j`) |
| `g_i,u_i` | `q` (also `s`) | `c_i` |
| `g_i,u_j`, `i!=j` | `q` (also `r_i,s`) | `r_j` (also `c_j`) |
| `w_i,w_j`, `i!=j` | `r_i` | `r_j` |
| `u_i,u_j`, `i!=j` | `r_i` | `r_j` |
| `w_i,u_j` | `q` | `z` |

Every unordered pair belongs to exactly one row of the table (with the
indices interchanged if necessary).  Thus neither member divides the other,
and `F` is primitive.

The type-0 shadows are

```
qzb, qzr_1s, qzr_2s,
```

which are pairwise incomparable by `b,r_1,r_2`.  The type-1 shadows are

```
qz, 2qr_1,2qr_2,2zr_1,2zr_2.
```

Here `qz` is separated from the other four by `2` versus `q` or `z`;
equal-family pairs are separated by `r_1,r_2`; and a `2qr_i` versus a
`2zr_j` pair is separated by `q,z` (and also by the `r_i` when `i!=j`).
Thus both rows are primitive and injective.

The shadow `qz` of `v` divides the shadows of `h,g_1,g_2`, so these four
vertices are connected.  None of `2qr_i,2zr_i` is comparable with any of the
three type-0 shadows: in the matching-index cases the surplus pairs are
`2` versus `z,s` or `2` versus `q,s`, and unequal indices add the missing
`r_i`.  Hence the component is exactly the asserted `C`, and its even
endpoint set is `{g_1,g_2}`.

After removal and flip, the type-1 base shadows are

```
qzb, 2qr_1,2qr_2,2zr_1,2zr_2.                         (4.4)
```

The odd support of `g_i` is `{q,z,r_i,s}`.  Deleting `q` is unsafe because

```
2zr_i | g_i/q=2zr_i s;
```

deleting `z` is unsafe because

```
2qr_i | g_i/z=2qr_i s;
```

and deleting `s` is unsafe because both `2qr_i` and `2zr_i` divide
`g_i/s=2qzr_i`.  On the other hand

```
g_i/r_i=2qzs
```

is incomparable with `qzb` (surpluses `2,s` versus `b`), with every
`2qr_j` (surpluses `z,s` versus `r_j`), and with every `2zr_j`
(surpluses `q,s` versus `r_j`).  This proves (4.2).  Equation (4.3) is
immediate, so the two singleton fibres are joined by an interaction edge and
no independent transversal exists.  ∎

One may adjoin `e=2qzb`: its `(2,0)` shadow is uniquely blocked in type 0 by
`h/d=qzb`, and it is incomparable and non-coprime with every member of `F`.
This makes the failed simultaneous move an actual missing-member insertion
problem.  However `e` is not in the B24 minimum-rank three-singleton setup;
the example is deliberately only a strict logical barrier to endpointwise
reasoning.

## 5. Exact remaining gap

Theorem 3.1 reduces the multi-endpoint continuation in a fixed B24 assignment
to an independent-transversal problem whose vertices and edges are given by
valuation tests.  To prove the nine-child star theorem through this route it
would suffice to establish, for at least one B24 eight-member assignment,
one of the following:

1. `J(A,C_2)` has an independent transversal;
2. the greedy inequalities (2.7) hold after a suitable endpoint ordering;
3. a different component/deletion change transforms the interaction graph
   into one with a transversal.

A negative conclusion about this precise five-step mechanism requires a
B24 palette for which `J(A,C_2)` lacks a transversal for **every** successful
assignment on every relevant eight-member deletion.  Proposition 4.1 does
not have those quantifiers and therefore does not close the route.

Even a universal nine-child-star proof would establish only the corresponding
one-root HBC class.  Arbitrary-cardinality stars, mixed-parent Hasse forests,
the historical quasi-primitive implication, and both characterizations in
Erdos Problem 892 remain open.  No conjecture-level Lean formalization is
justified by this local theorem.

## 6. Self-adversarial checklist

1. **Removal versus path.** `G(C)` contains every type-0/delete-2 vertex in
   the whole component, not only closest endpoints on chosen paths.
2. **Disconnected remainder.** Removing `G(C)` may disconnect `C`; flipping
   every remaining vertex still flips each induced component completely.
3. **Old-new and new-new pairs.** Base-safety controls only old-new pairs.
   The interaction graph is necessary for new-new pairs.
4. **Equality.** Equation (4.3) is a forbidden collision and is represented
   by an interaction edge.
5. **Admissibility.** Every reinserted endpoint deletes an odd prime and is
   placed in type 1.
6. **Insertion of `e/2`.** In the B24 application, all changed endpoint
   shadows lie in type 1, while the unique original comparable shadow of
   `h_{2,0}` is also moved to type 1.
7. **Quantifiers.** Theorem 3.1 is exact for one fixed old assignment and one
   prescribed move.  Proposition 4.1 is a family of fixed assignments, not
   an all-assignment HBC obstruction.
8. **Lean gate.** This draft needs two independent paper reviews before any
   theorem here is eligible for formalization.
