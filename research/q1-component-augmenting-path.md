# Nine-child stars: exact opposite-row covers and component augmenting paths

Date: 22 August 2026  
Scope: the B24/B26/B28 three-singleton regime for a nine-member one-root star  
Status: **independently reviewed paper result; nine-child HBC remains open**

This note keeps the nine-child theorem, universal HBC, and Erdős Problem 892
open.  It supplies two exact local interfaces after B28.

First, it rewrites a one-member deletion-plus-type exchange as an exact cover
of the admissible deleted primes by two explicitly defined fragile-surplus
families.  A simple support-count inequality is consequently sufficient for
such an exchange.

Second, it allows several types to change while all deleted primes remain
fixed.  The old-shadow comparability graph classifies *every* successful
fixed-deletion recolouring: on each connected component one must either keep
all types or flip all types.  Applied to the `(2,0)` blocker in the B24
three-singleton regime, the only possible obstruction to flipping its entire
component is a type-0 member whose deleted prime is `2`.  Thus every
hypothetical nine-member obstruction has an explicit even alternating path
from the `(2,0)` blocker to such a member.

Throughout, a **palette** is a finite primitive pairwise non-coprime family
`E` of integers greater than one.  A state of `f in E` is `(d,t)`, where `d|f`
is prime, `t in {0,1}`, and `t=1` is allowed only when `d` is odd.  Its shadow
is `f/d`.  An assignment is **successful** if the shadow image in each type
is injective and primitive.  Comparability includes equality.

## 1. Exact covers for one-member deletion-plus-type exchange

Let `A` be a successful assignment on a primitive palette `F`.  Write the
state of `f` as `(d_f,t_f)`.  For incomparable integers `x,y`, put

```
D(x,y)={ell prime : v_ell(x)>v_ell(y)}.
```

A prime `r` is a **fragile surplus of `x` over `y`** when

```
D(x,y)={r} and v_r(x)=v_r(y)+1.
```

For a target type `u`, let

```
P_u(h)={r|h prime : r is admissible in type u}.
```

Thus `P_0(h)=supp(h)`, whereas `P_1(h)` is the set of odd support primes of
`h`.  For `f != h` with `t_f=u`, define two forbidden-deletion sets

```
I_f(h,u) = {r in P_u(h) :
             r is a fragile surplus of h over f and d_f in D(f,h)},

II_f(h,u)= P_u(h) intersect D(h,f)
```

when `d_f` is a fragile surplus of `f` over `h`, and put
`II_f(h,u)=emptyset` otherwise.  Each `I_f(h,u)` has cardinality at most one;
the second set can contain several primes.

### Theorem 1.1 (exact opposite-row cover criterion)

Let `E=F union {e}` be in the B24/B26 situation.  Fix an admissible state
`(s,t)` of `e`, and let `h` be its unique blocker in the successful old
assignment `A` on `F`.  Put `u=1-t`.  Then changing only `h` to some state
`(r,u)` and inserting `e` in `(s,t)` is successful if and only if

```
P_u(h) is not contained in
  union_{f != h, t_f=u} (I_f(h,u) union II_f(h,u)).       (1.1)
```

More precisely, a prime `r in P_u(h)` works if and only if it is outside the
union in (1.1).

#### Proof

The immediate-shadow comparability criterion used in B15 and B28 says, for
incomparable palette members `h,f`, that

```
h/r | f/d_f
```

is equivalent to `r` being a fragile surplus of `h` over `f` and
`d_f in D(f,h)`.  This is exactly `r in I_f(h,u)`.  In the reverse
orientation,

```
f/d_f | h/r
```

is equivalent to `d_f` being a fragile surplus of `f` over `h` and
`r in D(h,f)`.  This is exactly `r in II_f(h,u)`.  Consequently `h/r` is
incomparable with every old shadow in row `u` if and only if `r` is outside
the union in (1.1).

Removing the old shadow of `h` leaves two primitive rows.  Inserting `h/r`
in the opposite row creates no old-old conflict exactly under the preceding
condition.  Moreover `h/r` is then in type `u != t`, so it cannot block the
insertion of `e/s` in type `t`.  Every unchanged member failed to block
`(s,t)`, because `h` was its unique blocker.  Thus the same condition is
necessary and sufficient for the final assignment.  This is also the
opposite-type specialization of B28, now expressed as an exact cover.  ∎

### Corollary 1.2 (support-count sufficient condition)

Under Theorem 1.1, a deletion-plus-type exchange exists whenever

```
|P_u(h)| > sum_{f != h, t_f=u}
              (|I_f(h,u)|+|II_f(h,u)|).                 (1.2)
```

In particular, since `|I_f(h,u)|<=1`, it is enough that

```
|P_u(h)| > |{f != h:t_f=u}|
 + sum_{f != h, t_f=u;
        d_f fragile surplus of f over h}
       |P_u(h) intersect D(h,f)|.                       (1.3)
```

#### Proof

The right side of (1.2) is an upper bound for the cardinality of the union
in (1.1).  If it is smaller than `|P_u(h)|`, the union cannot cover
`P_u(h)`, and Theorem 1.1 applies.  Replacing every `|I_f|` by its upper
bound one gives (1.3).  ∎

The inequalities are only sufficient.  Overlaps among the forbidden sets
can make the union strictly smaller than the displayed sum.  Conversely, in
a hypothetical nine-member obstruction, (1.1) must be a genuine cover for
every blocker of every successful assignment on every eight-member deletion.
This is a finite, valuation-level certificate; it does not assert that such a
cover actually exists for a full obstruction.

## 2. Fixed-deletion recolouring graph

Continue with a successful assignment `A` on a finite primitive palette `F`,
but do not yet assume the B24 shape.  Fix every deleted prime `d_f`, and write

```
x_f=f/d_f.
```

Define the **old-shadow comparability graph** `Gamma(A)` as the simple graph
with vertex set `F`, in which distinct `f,g` are adjacent exactly when
`x_f` and `x_g` are comparable.  Because `A` is successful, every edge joins
opposite old types.  Hence the old type map `t_f` is a proper two-colouring of
`Gamma(A)`.

Call a connected component `C` **flip-admissible** if every vertex
`f in C` of old type `0` has `d_f` odd.  This is precisely the requirement
for all vertices moved from type `0` to type `1` to retain admissible states;
vertices moved from type `1` to type `0` impose no restriction.

### Theorem 2.1 (component classification of all fixed-deletion exchanges)

Let `c:F->{0,1}` be any new type assignment, with the deleted primes `d_f`
fixed.  The resulting old assignment is successful if and only if:

1. on each connected component `C` of `Gamma(A)`, either
   `c_f=t_f` for every `f in C`, or `c_f=1-t_f` for every `f in C`; and
2. every component on which the second alternative is chosen is
   flip-admissible.

Thus fixed-deletion successful recolourings are exactly the admissible flips
of arbitrary unions of connected components.

#### Proof

For fixed shadows, success is equivalent to assigning different types to
the endpoints of every edge of `Gamma(A)`, together with type
admissibility.  Indeed, the edges are exactly all comparable or equal shadow
pairs, so a proper colouring is exactly primitivity and injectivity within
each type.

On a connected bipartite graph, a proper two-colouring is unique up to
interchanging the two colours: starting at one vertex, the colour of every
vertex is forced by the parity of a path from it.  This statement also holds
for a one-vertex component.  Since the old types already give one proper
two-colouring, every new proper colouring has precisely the componentwise
form in assertion 1.

If a component is flipped, exactly its old type-0 vertices move into type 1.
Their deleted primes must be odd, and this condition is sufficient.  This is
assertion 2.  ∎

For an admissible state `(s,t)` of a missing member `e`, define the old
**reverse-blocker set**

```
R_{s,t}={f in F : t_f=1-t and x_f is comparable with e/s},
```

and the **even-deletion barrier set**

```
B_2(A)={f in F : t_f=0 and d_f=2}.
```

### Theorem 2.2 (exact component-augmentation criterion)

Assume `(s,t)` has the unique old blocker `h`, and let `C(h)` be the
component of `h` in `Gamma(A)`.  There exists a successful fixed-deletion
recolouring of `F` after which `e` can be inserted in `(s,t)` if and only if

```
C(h) intersect R_{s,t}=emptyset
and
C(h) intersect B_2(A)=emptyset.                         (2.1)
```

When (2.1) holds, flipping only `C(h)` and then inserting `e/s` is successful.

#### Proof

Suppose first that (2.1) holds.  The second equality says that `C(h)` is
flip-admissible, so Theorem 2.1 permits flipping it.  The unique blocker `h`
moves out of type `t`.  Every member of `R_{s,t}` lies outside `C(h)` by the
first equality and is left unflipped, hence remains outside type `t`.  All
other members have shadows incomparable with `e/s`.  Therefore `(s,t)` is
unblocked after the flip and insertion succeeds.

Conversely, consider any successful fixed-deletion recolouring permitting
the insertion.  The unique old blocker `h` must change type.  By Theorem 2.1,
its whole component `C(h)` must be flipped.  Hence the component is
flip-admissible, which gives the second equality in (2.1).  If it contained a
member of `R_{s,t}`, that member would move from type `1-t` into type `t` and
would block `e/s`, contradicting the successful insertion.  This gives the
first equality.  ∎

This theorem is exact for the entire class of fixed-deletion multi-member
type exchanges.  It neither assumes nor asserts that a one-member exchange
exists.

## 3. The `(2,0)` reverse-blocker set is empty in the B24 regime

We now restore the full B24/B26 hypotheses.  Thus

```
E=F union {e},       supp(e)={2,p,q},
```

where `p,q` are distinct odd primes and `e` has minimum `Omega` in `E`.
The assignment on `F` is successful and all five admissible states of `e`
are saturated by the selected blockers

```
h_{2,0}, h_{p,0}, h_{p,1}, h_{q,0}, h_{q,1}.
```

The three remaining extras have the singleton signatures `{2}`, `{p}`,
`{q}` relative to `supp(e)`.  B26 says that the five selected blockers are
the unique blockers of their corresponding states.

### Lemma 3.1 (all-type uniqueness at the even option)

For every `f in F`, if its fixed old shadow `x_f=f/d_f` is comparable with
`e/2`, then `f=h_{2,0}`.  In particular,

```
R_{2,0}=emptyset.                                      (3.1)
```

#### Proof

Since `e` has minimum total prime-factor rank,

```
Omega(x_f)=Omega(f)-1 >= Omega(e)-1=Omega(e/2).
```

If `x_f | e/2`, equality of the two ranks is forced, and divisibility with
equal `Omega` implies `x_f=e/2`.  Thus in either orientation of the assumed
comparability one has

```
e/2 | x_f.                                             (3.2)
```

Apply the immediate-shadow criterion to the incomparable palette members
`e,f`.  Equation (3.2) implies

```
D(e,f)={2},       v_2(e)=v_2(f)+1,
```

and `d_f in D(f,e)`.  In particular `f` contains both `p` and `q`, because
their exponents in `f` are at least their positive exponents in `e`.

If `f` is one of the three extras, its support intersection with
`{2,p,q}` therefore contains `{p,q}`, contradicting its singleton
signature.  Hence `f` is one of the five selected blockers.  If its selected
state of `e` is `(r,u)`, the same immediate-shadow orientation for that block
gives `D(e,f)={r}`.  Therefore `r=2`.  Among the five admissible states only
`(2,0)` deletes `2`, so `f=h_{2,0}`.  This proves the lemma, and (3.1) follows
because `h_{2,0}` has old type `0`, not type `1`.  ∎

### Theorem 3.2 (component augmenting path dichotomy)

Let `C_2` be the component of `h_{2,0}` in `Gamma(A)`.  Exactly one of the
following conclusions holds.

1. `C_2 intersect B_2(A)=emptyset`.  Then flipping every type in `C_2` and
   inserting `e/2` in type `0` is a successful assignment on all nine
   members.
2. `C_2 intersect B_2(A)` is nonempty.  Then there is a shortest path

   ```
   h_{2,0}=v_0,v_1,...,v_{2k}=g,       k>=1,            (3.3)
   ```

   in `Gamma(A)` such that `g` has old type `0` and deleted prime `2`.
   The path alternates old types, has even length, no internal old type-0
   vertex deletes `2`, and has no chord between nonconsecutive vertices.

Consequently, if the nine-member palette has no successful assignment, the
second conclusion holds for every successful assignment on every
eight-member deletion arising in B24.

#### Proof

B26 proves that the deleted prime of `h_{2,0}` is odd, so
`h_{2,0} notin B_2(A)`.  Lemma 3.1 gives `R_{2,0}=emptyset`.  If the first
alternative holds, Theorem 2.2 applies and proves the asserted successful
assignment.

If the first alternative fails, choose `g in C_2 intersect B_2(A)` at
minimum graph distance from `h_{2,0}` and take a shortest path to it.  Every
edge of `Gamma(A)` crosses the old types, while both endpoints have old type
`0`; hence the length is even.  It is positive because the blocker itself
does not delete `2`, so it equals `2k` with `k>=1`.  Minimality of the
distance to `B_2(A)` says that no internal type-0 vertex deletes `2`.

A shortest path is simple.  If two nonconsecutive vertices on it were
adjacent, that chord would replace at least two edges of the displayed path
by one edge and give a shorter path to `g`; hence the path is chordless.
This proves alternative 2.

Finally, if the full palette has no successful assignment, alternative 1 is
impossible.  B24 supplies a successful assignment on each eight-member
deletion and imposes its conclusions for every such assignment, so the path
certificate is universally necessary as stated.  ∎

The path (3.3) is the smallest precise augmenting-path object exposed by the
fixed-deletion mechanism.  Flipping the component would propagate the type
change along all comparability edges.  The endpoint `g` is exactly where
that propagation becomes inadmissible: its deleted prime `2` cannot move
from type `0` to type `1`.

### Theorem 3.3 (one-endpoint deletion continuation)

Assume the second alternative of Theorem 3.2, but suppose

```
C_2 intersect B_2(A)={g}.                              (3.4)
```

Remove `g`, flip the old types of every remaining vertex in `C_2`, and leave
all other states fixed.  Call the resulting assignment on `F\{g}` by `A'`.
Then `A'` is successful.  If there is an odd prime `r|g` for which `g/r` is
incomparable with every type-1 shadow of `A'`, assigning `g` the state
`(r,1)` and inserting `e` in `(2,0)` gives a successful assignment on `E`.

Equivalently, the existence of such an `r` is decided by the two exact
fragile-surplus forbidden-set orientations used in the proof of Theorem 1.1,
computed against the type-1 row of `A'`; no unique-blocker hypothesis is
needed for this row-safety test.

#### Proof

Condition (3.4) says that every old type-0 member of `C_2` other than `g`
has an odd deleted prime.  Hence, after `g` is removed, the component flip is
type-admissible.  The proof of Theorem 2.1 shows directly that all remaining
fixed shadows form primitive injective rows, so `A'` is successful.

The assumed odd prime `r` is admissible in type `1`.  Its stated
incomparability condition permits insertion of `g/r` into the type-1 row of
`A'`, yielding a successful assignment on all of `F`.

It remains to insert `e/2` in type `0`.  By Lemma 3.1, among the *original*
fixed shadows only that of `h_{2,0}` was comparable with `e/2`; this shadow
was moved to type `1`.  Every other old shadow still has its original value,
and the only changed shadow, `g/r`, also lies in type `1`.  Thus no type-0
shadow is comparable with `e/2`, and the final insertion succeeds.  The last
sentence follows by applying the two fragile-surplus orientations in the
proof of Theorem 1.1 to the successful assignment `A'`.  ∎

This theorem is the first deletion-changing continuation past the exact
endpoint of the component mechanism.  It does not cover components with two
or more type-0/delete-2 vertices; those require simultaneous endpoint
changes or a new component after the first shadow changes.

### Corollary 3.4 (a new sufficient condition for the nine-child star)

If there exist a minimum-`Omega` member `e` and a successful assignment on
`F=E\{e}` satisfying the B24 conclusions for which the component of
`h_{2,0}` contains no old type-0 member deleting `2`, then `E` has a
successful assignment.

This is immediate from Theorem 3.2(1).  Notice the existential quantifier:
one suitable eight-member assignment is enough to solve the nine-member
palette.  A hypothetical obstruction forces the opposite condition for
every such assignment.

## 4. Simple and boundary examples

### Example 4.1 (isolated blocker)

If `h_{2,0}` is isolated in `Gamma(A)`, its component is the singleton
`{h_{2,0}}`.  Its deleted prime is odd by B26, so the component is
flip-admissible.  Flipping that one vertex is precisely the pure type flip,
and Theorem 3.2 inserts `e/2`.

### Example 4.2 (the B26 type-flip boundary is repaired by a two-vertex component)

In the parametric family of `q1-nine-type-flip-boundary.md`, the old shadow
of the `(2,0)` blocker `A` is

```
A/d_A=b c z u v,
```

and it has exactly one cross-type comparable old shadow,

```
G_b/b=b z u v | A/d_A.
```

Direct comparison with the displayed shadow lists in that note shows that
the component is exactly `{A,G_b}`.  Both vertices can be flipped: `A`
moves from type `0` to type `1` while deleting the odd prime `d_A`, and
`G_b` moves from type `1` to type `0`.  The shadow `G_b/b` lacks `c`, so it
does not block `e/2=bc`.  Theorem 3.2 therefore gives a successful repair
without changing either deleted prime.  This explains structurally why the
one-vertex pure flip fails but a length-one propagation succeeds.

### Boundary 4.3 (why the path endpoint cannot simply be flipped)

At an endpoint `g in B_2(A)`, the fixed state deletes `2` in type `0`.
Changing only its type to `1` is not an admissible state.  The component
theorem therefore cannot cross this endpoint without also changing its
deleted prime.  This is an exact limitation of the *fixed-deletion*
component mechanism, not a proof that a deletion-changing augmenting path
fails.  Theorem 1.1 gives the valuation cover that a new deletion must escape.

## 5. Exact relation to HBC and Erdős 892

For a root `r_0`, a successful assignment on a quotient palette `E` gives
HBC for the one-root Hasse star

```
{r_0} union {r_0 f:f in E}.
```

Therefore Corollary 3.4 proves HBC for the stated positive class of
nine-child stars.  Theorem 3.2 does not prove that every B24 assignment lacks
the path obstruction, and it constructs no all-assignment obstruction.
Even a proof for every one-root star would leave mixed-parent Hasse forests
open.  Thus none of the results here proves universal HBC, the historical
quasi-primitive domination implication, or either characterization in
Erdős Problem 892.

The next minimal Q1 lemma is now sharply split:

1. prove that some B24 eight-member assignment has no path (3.3); or
2. apply Theorem 3.3 at a unique endpoint, or change deleted primes at all
   endpoints using the exact cover criterion of Theorem 1.1 and continue the
   alternating propagation; or
3. construct a palette for which every eight-member assignment has both the
   path certificate and saturated deletion covers at every reachable
   endpoint.

Failure to prove any one of these is not a closure of the route.  A strict
negative result must quantify over all successful eight-member assignments,
not merely one displayed assignment.  No conjecture-level Lean
formalization is justified before this paper gap is closed.

## 6. Self-adversarial checklist

1. **Equality.**  Graph edges include equal shadows; proper colouring thus
   enforces injectivity as well as absence of strict divisibility.
2. **Type 1.**  Only old type-0 vertices in a flipped component require an
   odd deleted prime.  Old type-1 vertices move to type `0`, where deleting
   `2` would have been allowed, although their old type already forces their
   deletion to be odd.
3. **Non-squarefree `e`.**  Lemma 3.1 uses valuations and only the positivity
   of the `p,q` exponents.  It does not assume `e=2pq`.
4. **Rank orientation.**  If `x_f|e/2`, minimum `Omega` forces equality, so
   the orientation `e/2|x_f` remains valid.  This prevents a hidden reverse
   divisibility case.
5. **Quantifiers.**  Theorems 1.1 and 2.2 concern one fixed successful old
   assignment.  The universal obstruction certificate in Theorem 3.2 uses
   B24's quantification over every such assignment.
6. **Component versus path.**  Flipping only the vertices of a path need not
   be proper when internal vertices have edges leaving the path.  The
   positive move flips the entire component.  The shortest path is only a
   necessary obstruction certificate.
7. **Scope.**  An even-deletion endpoint blocks only the fixed-deletion
   recolouring mechanism.  It is not an HBC counterexample and does not
   close deletion-changing or larger augmenting-path routes.
