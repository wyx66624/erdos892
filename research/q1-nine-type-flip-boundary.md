# Nine-child stars: unique blockers and a strict boundary for the pure type flip

Date: 22 August 2026  
Scope: the B24 three-singleton-signature regime for a nine-member one-root star  
Status: **research-branch draft; independent review required; the nine-child theorem and universal HBC remain open**

This note makes two local advances at the first case beyond the audited
eight-child theorem.

First, in the B24 three-singleton-signature regime the five selected blockers
are not merely representatives: each is the unique blocker of its option.
Consequently a one-member exchange succeeds exactly when the changed old
assignment remains successful and the changed member ceases to block its old
option.

Second, the apparently canonical exchange for the `(2,0)` blocker—keep its
deleted prime and change only its type from `0` to `1`—is not universally
valid.  An infinite parametric family realizes the complete B24 local shape,
but the type flip creates a divisibility conflict with the singleton-`p`
extra.  The same family has an explicit one-deletion repair, so this is a
strict counterexample to one proof mechanism, not an HBC counterexample.

Throughout, a **palette** is a finite primitive pairwise non-coprime family
`E` of integers greater than one.  A state of `f in E` is a pair `(d,t)`, where
`d | f` is prime, `t in {0,1}`, and `t=1` is allowed only for odd `d`.  Its
shadow is `f/d`.  An assignment is **successful** when, in each type, its
shadow image is injective and primitive.

## 1. The unique-blocker exchange lemma

Fix a nine-member palette `E`, a minimum-`Omega` member `e`, and put

```
S = supp(e) = {2,p,q},     F = E \ {e},
```

where `p,q` are distinct odd primes.  Fix a successful assignment `A` on
`F`.  The five admissible states of `e` are

```
(2,0), (p,0), (p,1), (q,0), (q,1).
```

An old member `f` **blocks** `(s,t)` if `f` has type `t` under `A` and its
shadow is comparable with `e/s`.  Since `e` has minimum total prime-factor
rank, the audited blocking orientation gives

```
e/s | f/d_f.                                      (1.1)
```

Assume all five options are blocked.  Choose one blocker for every option;
the audited one-blocker-per-old-member lemma makes the five choices distinct.
Call their set `H`, put `G=F\H`, and assume that the three extras can be
labelled `g_2,g_p,g_q` with

```
supp(g_r) intersect S = {r}        (r in {2,p,q}). (1.2)
```

These are precisely the local conclusions forced by B24 for a hypothetical
nine-member obstruction.

### Lemma 1.1 (unique blockers)

Under the preceding hypotheses:

1. no member of `G` blocks any option of `e`;
2. every option of `e` has exactly one blocker in `F`, namely its selected
   member of `H`;
3. let `h in H` be the unique blocker of an option `o`.  Replace only the
   state of `h`, leaving all other states on `F` fixed.  If the modified
   assignment on `F` is successful and the new state of `h` does not block
   `o`, then inserting `e` in state `o` gives a successful assignment on
   `E`.

#### Proof

Let `g_r in G`.  If it blocked `(s,t)`, (1.1) would imply that every prime in
`S\{s}` divides `g_r`.  This two-element set cannot be contained in
`supp(g_r) intersect S={r}`.  Thus no extra blocks an option.

The five selected members of `H` block five distinct options.  Each old
member blocks at most one option, so none of these five members can also block
a second option.  The extras block none.  Hence the selected blocker of each
option is unique in all of `F`.

For the final assertion, every unchanged old member still fails to block `o`
by uniqueness, and the changed member fails to block it by hypothesis.  Thus
`o` is unblocked in the modified successful assignment on `F`.  The audited
insertion criterion then permits the shadow of `e` in state `o`; all old
within-type relations remain valid because the modified old assignment was
assumed successful.  This proves the claim.  ∎

### Corollary 1.2 (the canonical type flip is admissible)

Let `h_{2,0}` be the unique blocker of `(2,0)`, and let its assigned deleted
prime be `d`.  Then `d` is odd.  Hence keeping `d` and changing only the type
of `h_{2,0}` from `0` to `1` is an admissible state change.

#### Proof

The relation `e/2 | h_{2,0}/d`, together with incomparability of `e` and
`h_{2,0}`, invokes the exact immediate-shadow comparability lemma: `2` is the
fragile surplus of `e` over `h_{2,0}` and `d` belongs to `D(h_{2,0},e)`.
In particular `d != 2`; therefore `d` is odd.  ∎

Corollary 1.2 does **not** say that the resulting old assignment stays
successful.  The next section proves that this missing condition is real.

## 2. A parametric failure of the pure type flip

### Definition 2.1 (pure `(2,0)` type-flip mechanism)

In the setting of Lemma 1.1, the pure `(2,0)` type-flip mechanism performs
only the following operations:

1. keep the deleted prime of `h_{2,0}` and change its type from `0` to `1`;
2. keep every other old state fixed;
3. insert `e` by deleting `2` in type `0`.

The mechanism is declared successful only if the resulting assignment is
successful.  Thus this is a precise universal claim about one fixed local
move, not about arbitrary one-member exchanges.

Let

```
a=2, b, c, z, u, v, w, x, y,
d_A, d_B0, d_B1, d_C0, d_C1, d_C
```

be pairwise distinct primes; all except `a` are odd.  Define

```
e   = a b c,
A   = b c z u v d_A,
B0  = a c u d_B0,          B1 = a c v d_B1,
C0  = a b w d_C0,          C1 = a b x d_C1,
G_b = b^2 z u v,
G_a = a z y,
G_c = c z w x d_C,
```

and let

```
E = {e,A,B0,B1,C0,C1,G_b,G_a,G_c}.             (2.1)
```

### Proposition 2.2 (strict type-flip counterexample family)

For every choice of primes in Definition 2.1:

1. `E` is primitive and pairwise non-coprime, and `e` has minimum
   `Omega`-rank;
2. the assignment on `F=E\{e}` given by

   | member | A | B0 | B1 | C0 | C1 | G_b | G_a | G_c |
   |---|---:|---:|---:|---:|---:|---:|---:|---:|
   | deleted prime | d_A | d_B0 | d_B1 | d_C0 | d_C1 | b | a | d_C |
   | type | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |

   is successful;
3. `A,B0,B1,C0,C1` uniquely block `(a,0),(b,0),(b,1),(c,0),(c,1)`,
   respectively, while the extras have the three signatures

   ```
   {a}, {b}, {c};
   ```

4. the pure `(a,0)` type flip fails: after moving `A` to type `1`, the
   unchanged type-`1` shadow of `G_b` divides the shadow of `A`;
5. nevertheless, changing the deletion on `A` from `d_A` to `b` in type `0`
   and inserting `e` by deleting `a` in type `0` gives a successful assignment
   on all of `E`.

Consequently the pure `(2,0)` type-flip mechanism is false even on an infinite
parametric family realizing the full fixed-assignment B24 local shape.  The
family is not an HBC obstruction.

#### Proof

Every member other than `e` omits at least one of `a,b,c`, so `e` divides no
old member.  Conversely, each of `A,B0,B1,C0,C1` contains its private prime
`d_*`, `G_a` contains the private prime `y`, and `G_c` contains the private
prime `d_C`.  The only remaining possible divisibility needing attention is
`G_b | A`, but `G_b` contains `b^2` whereas `A` contains only `b`.  Directly
comparing the displayed supports excludes every other old-old divisibility.
Thus `E` is primitive.  Also `Omega(e)=3`, while every old member has total
rank at least `3`, so `e` has minimum rank.

Pairwise non-coprimality can be read from the construction.  The five
blockers meet one another through the two support primes they inherit from
`e`.  The extra `G_b` meets `A,C0,C1` at `b`, meets `B0` at `u`, and meets
`B1` at `v`.  The extra `G_a` meets `B0,B1,C0,C1` at `a` and meets `A` at
`z`.  The extra `G_c` meets `A,B0,B1` at `c`, meets `C0` at `w`, and meets
`C1` at `x`.  Finally all three extras meet pairwise at `z` whenever one is
`G_a` or `G_b`, while `G_b` and `G_c` also meet at `z`.  Every old member
meets `e` in its displayed singleton or two-element support signature.

The type-`0` shadows of the proposed old assignment have supports

```
{b,c,z,u,v}, {a,c,u}, {a,b,w}, {z,y}, {c,z,w,x},
```

coming from `A,B0,C0,G_a,G_c`.  The type-`1` shadows have supports

```
{a,c,v}, {a,b,x}, {b,z,u,v},
```

coming from `B1,C1,G_b`.  In each row these squarefree support sets are
pairwise incomparable.  Hence both shadow images are primitive and injective.

Now

```
e/a = bc | A/d_A,
e/b = ac | B0/d_B0 and B1/d_B1,
e/c = ab | C0/d_C0 and C1/d_C1
```

in the indicated types.  Inspection of the same support lists shows that no
other same-type shadow contains the relevant two-prime shadow.  Thus these
are the five unique blockers.  Moreover

```
supp(G_a) intersect supp(e) = {a},
supp(G_b) intersect supp(e) = {b},
supp(G_c) intersect supp(e) = {c}.
```

The pure type flip keeps the shadow

```
A/d_A = b c z u v
```

but moves it to type `1`.  The unchanged type-`1` shadow

```
G_b/b = b z u v
```

strictly divides it.  Therefore the modified old assignment is not primitive,
and the pure type-flip mechanism fails.

For the asserted repair, delete `b` from `A` in type `0`, keep every other
old state fixed, and insert `e` by deleting `a` in type `0`.  The new type-`0`
support sets are

```
{b,c}, {c,z,u,v,d_A}, {a,c,u}, {a,b,w}, {z,y}, {c,z,w,x}.
```

They are pairwise incomparable: `{b,c}` is contained in none of the other
five because each misses `b` or misses `c`, and direct inspection gives
incomparability among the remaining five.  The type-`1` row is unchanged and
was already primitive and injective.  This is a successful assignment on all
nine members.  ∎

### Corollary 2.3 (what a valid exchange theorem must use)

No proof of the nine-child theorem can rely solely on the following data:

- the uniqueness of the `(2,0)` blocker;
- admissibility of changing its type to `1`; and
- the fact that this type change frees `(2,0)` among the unchanged type-`0`
  shadows.

A valid exchange theorem must additionally control comparabilities created in
the destination type, or it must allow the deleted prime and/or another old
state to change.  Proposition 2.2 shows that allowing the deleted prime can be
strictly stronger than the pure type flip.

## 3. Boundary cases and exact relation to HBC

Lemma 1.1 uses all three parts of the B24 local shape.  If an extra signature
contains two support primes, that extra may itself block an option.  If
`supp(e)` has more than three primes, the counting and signature conclusion
change.  If the modified old assignment is not successful, uniqueness of the
old blocker alone does not justify insertion; Proposition 2.2 is an explicit
instance of exactly this boundary.

For any root `r_0`, the set

```
{r_0} union {r_0 f : f in E}
```

formed from Proposition 2.2 is a quasi-primitive one-root Hasse star.  The
assignment in assertion 5 proves HBC for this star.  Therefore the proposition
does not refute the nine-child theorem, universal HBC, the historical
quasi-primitive domination implication, or either characterization asked for
in Erdos Problem 892.  It only closes one precisely defined local proof route.

The closest surviving Q1 target is now: prove that in every B24-shaped
saturated assignment some unique blocker admits a successful state change
that ceases to block its option, where the change may alter the deleted prime;
or construct an all-assignment integer certificate showing that even this
broader exchange statement fails.  No conjecture-level Lean work is justified.

## 4. Self-adversarial review checklist

1. **Quantifiers.**  Proposition 2.2 is universal over every pairwise-distinct
   choice of the displayed primes, but it concerns the displayed fixed old
   assignment.  It does not assert that the family has B24 behavior for every
   assignment; indeed the family is explicitly solvable.
2. **Type admissibility.**  All original type-`1` deletions (`d_B1,d_C1,b`)
   are odd.  The failed flip deletes the odd prime `d_A`.  Deleting `a=2`
   occurs only in type `0`.
3. **Prime powers.**  `G_b/b=bzuv`; deletion removes one copy of `b`, as
   required for an immediate prime shadow.  The remaining `b` is essential
   both for the destination-type conflict and for preventing `G_b | A`.
4. **Primitivity versus equal rank.**  The old members have different ranks,
   so equal-rank shorthand is not used.  The proof relies on private primes,
   the exponent-two check for `G_b`, and explicit support comparisons.
5. **Uniqueness.**  Saturation alone does not imply unique blockers.  Lemma
   1.1 also uses the three singleton signatures and the audited fact that one
   old member blocks at most one option.
6. **Scope.**  The counterexample invalidates only the pure type flip.  The
   successful deletion exchange is included to prevent accidental promotion
   of a failed proof move into an HBC counterexample.
7. **Independent checks still required.**  Before promotion beyond a research
   branch, two reviewers should independently enumerate all 36 unordered
   pairs of palette members for gcd and divisibility, all within-type shadow
   pairs in the old assignment, and all 15 within-type shadow pairs in the
   repaired type-`0` assignment.
