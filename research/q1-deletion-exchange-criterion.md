# Nine-child stars: an exact deletion-exchange criterion and an orthogonal boundary family

Date: 22 August 2026  
Scope: the B24/B26 three-singleton-signature regime for a nine-member one-root star  
Status: **paper draft for independent review; the nine-child theorem and universal HBC remain open**

This note studies the one-member exchange left open by B26 when the deleted
prime is allowed to change.  It has two purposes.

First, it gives an exact necessary-and-sufficient criterion for changing one
old state and then inserting the missing member.  In the B24 regime, the
criterion has a particularly rigid form: if the blocker stays in the type of
the option it blocks, the only deletions which can free the option are the
other support primes of the missing member which occur to exponent exactly
one in the blocker.

Second, an infinite family shows that neither of those two deletions need be
successful for the `(2,0)` blocker.  The family is nevertheless repaired by
changing both the deletion and the type of that blocker.  Thus the family
closes only the precisely defined *same-type deletion-only* mechanism.  It is
not an HBC counterexample.

Throughout, a **palette** is a finite primitive pairwise non-coprime family
`E` of integers greater than one.  A state of `f in E` is `(d,t)`, where `d|f`
is prime, `t in {0,1}`, and `t=1` is allowed only when `d` is odd.  Its shadow
is `f/d`.  An assignment is **successful** when the shadow image in each type
is injective and primitive.

## 1. Valuation form of row collisions

For incomparable positive integers `x,y`, put

```
D(x,y) = {l prime : v_l(x) > v_l(y)}.
```

A prime `r` is a **fragile surplus of `x` over `y`** if

```
D(x,y)={r}  and  v_r(x)=v_r(y)+1.                 (1.1)
```

We use the audited immediate-shadow criterion from the star-surplus note:
for primes `r|x` and `d|y`,

```
x/r | y/d
```

if and only if `r` is a fragile surplus of `x` over `y` and
`d in D(y,x)`.  Applying the same statement in the reverse orientation also
gives the following exact test.

### Lemma 1.1 (row-safety test)

Let `A` be a successful assignment on a primitive palette `F`.  Write the
state of `f` as `(d_f,t_f)`.  Fix `h in F`, a target type `u`, and a prime
`r|h` admissible in type `u`.  Then `h/r` is incomparable with every old
shadow in type `u` other than that of `h` if and only if, for every
`f != h` with `t_f=u`, neither of the following holds:

1. `r` is a fragile surplus of `h` over `f` and `d_f in D(f,h)`;
2. `d_f` is a fragile surplus of `f` over `h` and `r in D(h,f)`.

When these equivalent conditions hold, call `r` **row-safe for `(h,u)`**.

#### Proof

Primitivity of `F` makes `h` and `f` incomparable.  The audited criterion,
applied first to `(h,f)` and then to `(f,h)`, says respectively that condition
1 is equivalent to

```
h/r | f/d_f,
```

and condition 2 is equivalent to

```
f/d_f | h/r.
```

Thus excluding both conditions for every member of the target row is exactly
the assertion that no target-row shadow is comparable with `h/r`.  Equality
is included in both the usual divisibility relation and the forbidden
comparability, so injectivity requires no separate clause.  ∎

## 2. Exact one-state exchange

Let `E=F union {e}` be a nine-member palette in the B24 situation.  Thus

```
supp(e)={2,p,q}
```

for distinct odd primes `p,q`; `A` is a successful assignment on `F`; all
five states of `e` are blocked; and B26 says that each state has a unique
blocker.

Fix one state `(s,t)` of `e`, let `h` be its unique blocker, and suppose the
old state of `h` is `(d,t)`.  (A blocker necessarily has the same type as the
blocked option.)  For a new admissible state `(r,u)` of `h`, let
`A[h -> (r,u)]` denote the assignment obtained by changing only `h`.

### Theorem 2.1 (exact one-state exchange criterion)

Changing `h` to `(r,u)` and inserting `e` in state `(s,t)` produces a
successful assignment on `E` if and only if

1. `r` is row-safe for `(h,u)`; and
2. either `u != t`, or `h/r` is incomparable with `e/s`.

In particular, this is a finite valuation test involving only the exponent
vectors of the palette and the fixed old assignment.

#### Proof

Remove the old shadow of `h` from its row.  Both remaining rows are still
primitive and injective, because they are subfamilies of the two successful
old rows.  On placing `h/r` in row `u`, the only possible new old-old conflict
involves `h/r`.  By Lemma 1.1, there is no such conflict exactly when `r` is
row-safe for `(h,u)`.  Hence clause 1 is necessary and sufficient for the
modified old assignment to remain successful.

Every member other than `h` retains its old shadow and type.  Since `h` was
the unique blocker of `(s,t)`, none of these unchanged shadows is comparable
with `e/s` in type `t`.  If `u != t`, the new shadow of `h` lies in the other
row and cannot block the insertion.  If `u=t`, it fails to block precisely
when it is incomparable with `e/s`.  This proves sufficiency.

Conversely, a successful final assignment has no comparison between `h/r`
and an old target-row shadow, so clause 1 follows from Lemma 1.1.  When
`u=t`, it also has no comparison between `h/r` and `e/s`, which is clause 2.
Thus both conditions are necessary.  ∎

The theorem permits both a deletion change and a type change.  Its same-type
specialization can be made completely explicit.

### Lemma 2.2 (exact freeing deletions in the B24 regime)

Retain the hypotheses above and require `u=t`.  Then

```
h/r is incomparable with e/s
```

if and only if

```
r in supp(e)\{s}  and  v_r(h)=1.                 (2.1)
```

For type `1`, the prime `r` in (2.1) must additionally be odd, as required by
state admissibility.

#### Proof

Because `h` blocks `(s,t)`, one has `e/s | h/d`.  Apply the immediate-shadow
criterion to the incomparable palette members `e,h`.  It follows that `s` is
a fragile surplus of `e` over `h` and `d in D(h,e)`.  Since `e` is squarefree,

```
v_s(h)=0,              D(e,h)={s}.               (2.2)
```

Apply the criterion again, now with the proposed deletion `r`.  The first
orientation gives

```
e/s | h/r  iff  r in D(h,e),                     (2.3)
```

because `s` is already the fragile surplus of `e` over `h`.  The reverse
orientation gives

```
h/r | e/s
```

if and only if `r` is a fragile surplus of `h` over `e` (the other required
condition `s in D(e,h)` is automatic by (2.2)).

If `r|h` and `r notin D(h,e)`, then `v_r(h)<=v_r(e)`.  Equation (2.2) rules
out `r=s`; a prime outside `supp(e)` would have positive exponent in `h` and
zero exponent in `e`, putting it in `D(h,e)`.  Therefore
`r in supp(e)\{s}` and, by squarefreeness of `e`, `v_r(h)=1`.  Conversely,
these two conditions imply `r notin D(h,e)`.  They also make it impossible
for `r` to be a fragile surplus of `h` over `e`.  Equations (2.3) and its
reverse therefore exclude both orientations of comparability exactly under
(2.1).  ∎

Define the finite **unit-support candidate set**

```
U_t(s,h) = {r in supp(e)\{s} : v_r(h)=1 and r is admissible in type t}.
```

### Corollary 2.3 (same-type deletion-exchange criterion)

Changing only the deleted prime of `h`, keeping its type `t`, and inserting
`e` in `(s,t)` succeeds if and only if `U_t(s,h)` contains a prime row-safe
for `(h,t)`.

Consequently, a hypothetical nine-member obstruction forces every prime in
every set `U_t(s,h)` to have an explicit same-row fragile-surplus witness of
one of the two forms in Lemma 1.1.  This necessary certificate holds for
every successful assignment on every eight-member deletion supplied by B24.

#### Proof

Combine Theorem 2.1 with Lemma 2.2.  The final sentence follows by negating
the row-safety test and recalling the universal quantifier in B24.  ∎

This is stronger than a merely sufficient safe-prime statement: for the
fixed assignment, blocker and option it is an exact characterization of the
entire same-type deletion-only move.

## 3. A strict boundary for deletion-only repair of the `(2,0)` blocker

We now show that the witness condition in Corollary 2.3 is not vacuous.  Let

```
a=2, b, c, z, u, v, y,
d_A, d_B0, d_B1, d_C0, d_C1, delta
```

be pairwise distinct primes, all except `a` odd.  Define

```
e   = a b c,
A   = b c z u v d_A,
B0  = a c u d_B0,          B1 = a c v d_B1,
C0  = a b u d_C0,          C1 = a b v d_C1,
G_b = b^2 z u v d_A,
G_a = a z y,
G_c = c z u v d_A delta,
```

and put

```
E={e,A,B0,B1,C0,C1,G_b,G_a,G_c}.                (3.1)
```

### Proposition 3.1 (orthogonal boundary family)

For every choice of primes above:

1. `E` is primitive and pairwise non-coprime, and `e` has minimum
   `Omega`-rank;
2. the assignment on `F=E\{e}` given by

   | member | A | B0 | B1 | C0 | C1 | G_b | G_a | G_c |
   |---|---:|---:|---:|---:|---:|---:|---:|---:|
   | deleted prime | d_A | d_B0 | d_B1 | d_C0 | d_C1 | b | a | delta |
   | type | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |

   is successful;
3. `A,B0,B1,C0,C1` uniquely block `(a,0),(b,0),(b,1),(c,0),(c,1)`,
   respectively, and the three extras have signatures `{a},{b},{c}`;
4. every same-type deletion-only repair of the `(a,0)` blocker `A` fails;
   specifically, the only deletions which cease to block are `b,c`, and

   ```
   A/b = G_c/delta,       A/c = G_b/b;            (3.2)
   ```

5. nevertheless, moving `A` to type `1` while deleting `b`, and inserting
   `e` by deleting `a` in type `0`, is a successful assignment on `E`.

Thus same-type deletion-only repair of the `(2,0)` blocker is not a universal
mechanism, even for the full fixed-assignment B24 shape.  The family is not an
HBC obstruction.

#### Proof

We first check the palette conditions.  The member `e` has rank three;
`G_a` also has rank three, and every other member has rank at least four, so
`e` has minimum rank.

The five blockers are pairwise incomparable: each omits one of `a,b,c`, and
the four members `B0,B1,C0,C1` have their displayed private prime, while `A`
has `z` and `d_A`.  No blocker is comparable with `e`, since it omits a
support prime of `e` and has an auxiliary prime.  The member `G_a` has the
private prime `y` and only the support prime `a`.  The member `G_b` has
exponent two at `b`, whereas `A` has exponent one; it also has `z,u,v,d_A`,
which prevent it from dividing any other blocker, and every blocker has a
prime absent from `G_b`.  Similarly, `G_c` has `delta`, and `A` has `b`, so
`A` and `G_c` are incomparable; its `z,u,v,d_A,delta` prevent it from
dividing the remaining blockers, while their `a` or private prime prevents
the reverse divisibility.  Finally `G_b,G_c` differ at `b,c,delta`, and
`G_a` is incomparable with both because of `a,y` versus their other primes.
This proves primitivity.

Pairwise non-coprimality is also explicit.  The blockers meet through support
primes and, where useful, `u` or `v`.  The member `G_b` meets
`A,B0,B1,C0,C1` respectively at `b,u,v,b,b`; `G_c` meets them respectively
at `c,c,c,u,v`; and `G_a` meets `A` at `z` and each of the other four
blockers at `a`.  The three extras meet pairwise at `z`, and `e` meets every
old member in its displayed support signature.

The type-`0` shadows of the proposed assignment are

```
b c z u v,   a c u,   a b u,
b z u v d_A, z y,     c z u v d_A,               (3.3)
```

coming from `A,B0,C0,G_b,G_a,G_c`.  They are pairwise incomparable.  For the
only close pairs, the shadow of `A` has `c` versus the `d_A` of the `G_b`
shadow, and has `b` versus the `d_A` of the `G_c` shadow; the latter two
shadows differ at `b,c`.  Every shadow involving `B0` or `C0` is separated by
`a` and by `b` or `c`, and `y` separates the shadow of `G_a`.  The type-`1`
shadows are

```
a c v,       a b v,                              (3.4)
```

and are incomparable.  Hence the assignment is successful and injective.

Now

```
e/a=bc | A/d_A,
e/b=ac | B0/d_B0 and B1/d_B1,
e/c=ab | C0/d_C0 and C1/d_C1
```

in the indicated types.  Inspection of (3.3)--(3.4) shows that these are the
unique blockers.  The extras meet `{a,b,c}` in `{b},{a},{c}`, respectively.

For the `(a,0)` blocker `A`, Lemma 2.2 says that only `b` and `c` can cease to
block while `A` remains in type `0`; both occur to exponent one.  But the two
equalities in (3.2) show an injectivity, hence primitivity, failure in the old
type-`0` row for each choice.  Every other prime deletion leaves `bc` dividing
the shadow of `A`.  This proves assertion 4 without omitting any deletion
prime of `A`.

For the repair, remove `A/d_A` from type `0`, put

```
A/b = c z u v d_A
```

in type `1`, and insert `e/a=bc` in type `0`.  The new type-`1` shadow is
incomparable with both shadows in (3.4): it lacks `a`, while each of those
shadows lacks at least `z,u,d_A`.  The old type-`0` row without `A/d_A`
remains primitive, and `bc` is incomparable with all five remaining shadows:
`B0/d_B0` lacks `b`, `C0/d_C0` lacks `c`, `G_b/b` lacks `c`, `G_c/delta`
lacks `b`, and `G_a/a` lacks both.  Therefore the repaired assignment is
successful.  ∎

### Corollary 3.2 (two local mechanisms are genuinely different)

B26 gives a family where the pure type flip of the `(2,0)` blocker fails but
a same-type deletion change succeeds.  Proposition 3.1 gives a family where
every same-type deletion change of that blocker fails but a deletion-plus-type
change succeeds.  Hence neither restricted mechanism implies the other.  A
universal nine-member argument must use the full target-row criterion in
Theorem 2.1, change a different blocker, or use a multi-member augmenting path.

## 4. Exact relation to HBC and Erdős 892

For any root `r_0`,

```
{r_0} union {r_0 f : f in E}
```

is a quasi-primitive one-root Hasse star.  Proposition 3.1(5) explicitly
proves HBC for this star.  Consequently the boundary family does not refute
the nine-child star theorem, universal HBC, the quasi-primitive domination
implication, or either characterization in Erdős Problem 892.

Theorem 2.1 is a fixed-assignment local theorem.  In a hypothetical
nine-member counterexample, B24 applies it to every successful assignment on
every eight-member deletion.  To finish the nine-member theorem one must
still prove that at least one of those assignments has a row-safe exchange,
or else combine several individually unsafe exchanges into an augmenting
path.  Even a complete arbitrary-star theorem would still leave mixed-parent
Hasse forests open.  No conjecture-level Lean formalization is justified.

## 5. Self-adversarial review

1. **Quantifiers.**  Theorem 2.1 is exact for a fixed successful assignment
   and a fixed unique blocker.  Corollary 2.3 becomes a necessary condition
   for an obstruction only because B24 quantifies over every eight-member
   assignment.  Proposition 3.1 concerns the displayed fixed assignment, not
   all assignments of its palette.
2. **Equality.**  Row-safety excludes divisibility in both directions, so it
   also excludes equal shadows.  The failures in (3.2) are equality failures,
   not merely strict divisibility failures.
3. **Type admissibility.**  The original type-`1` deletions `d_B1,d_C1` are
   odd.  The repaired state deletes the odd prime `b`.  The prime `a=2` is
   deleted only in type `0`.
4. **Support exponents.**  Lemma 2.2 uses squarefreeness of
   `e=2pq`, not of the blockers.  It correctly excludes a support prime whose
   exponent in the blocker is at least two.  The exponent two at `b` in
   `G_b` is retained after deleting one copy.
5. **No private-prime shortcut for `A`.**  The prime `d_A` is deliberately
   shared by `A,G_b,G_c`; primitivity is checked by the missing support primes
   and by the extra exponent or `delta`.
6. **Scope of the counterexample.**  Assertion 4 excludes all deleted-prime
   changes of `A` that keep type `0`; it says nothing about changing a
   different blocker or several members.  Assertion 5 prevents promotion of
   this local failure into an HBC counterexample.
7. **Independent review required.**  Before promotion, reviewers should
   independently check all 36 unordered gcd/divisibility pairs, all 15
   type-`0` shadow pairs in (3.3), the type-`1` pair in (3.4), both collisions
   in (3.2), and all repaired-row pairs.  A deterministic enumeration may be
   saved as a certificate but must not replace the proofs above.

