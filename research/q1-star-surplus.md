# Q1 star route: fragile surplus primes and safe one-shadow deletions

Date: 22 August 2026  
Scope: the one-root height-one subproblem inside universal HBC  
Status: **exact pair criterion and new sufficient theorem; the arbitrary star remains open**

Let \(E\) be a primitive pairwise non-coprime family of integers greater than one.
Then

\[
 B=\{r\}\cup\{re:e\in E\}
\tag{0.1}
\]

is the basic one-root Hasse star.  HBC for this star asks for a prime deletion
\(p_e\mid e\) and a type \(t_e\in\{0,1\}\), with type \(1\) allowed only when
\(p_e\ge3\), such that the labelled shadows are locally injective and each type class
of \(e/p_e\)'s is primitive.

For completeness, (0.1) is quasi-primitive.  Primitivity of \(E\) makes every
\(r\to re\) a lower-cover edge.  For distinct \(e,f\in E\), pairwise
non-coprimality gives \(1<\gcd(e,f)\), so the top-pair gcd is not the root \(r\).
If it were \(re'\) for some \(e'\in E\), then \(e'\mid e,f\); primitivity would
force first \(e'=e\) and then \(e'=f\), a contradiction.  The combinatorial
safe-deletion theorem below itself needs only primitivity; pairwise
non-coprimality is used here to place it inside the quasi-primitive star problem.

The exact-rank theorem in the positive HBC round solves this when all
\(\Omega(e)\) are equal.  This note instead isolates exactly when two arbitrary-rank
immediate shadows can become comparable.

## 1. Unique unit surplus

For positive integers \(e,f\), define

\[
 D(e,f)=\{\ell\text{ prime}:v_\ell(e)>v_\ell(f)\}.
\tag{1.1}
\]

When \(e,f\) are incomparable, both \(D(e,f)\) and \(D(f,e)\) are nonempty.
Call a prime \(p\) a **fragile surplus of \(e\) over \(f\)** if

\[
 D(e,f)=\{p\},
 \qquad v_p(e)=v_p(f)+1.
\tag{1.2}
\]

Thus \(e\) exceeds \(f\) in exactly one prime coordinate and by exactly one unit.

### Lemma 1.1 (exact immediate-shadow comparability)

Let \(e,f\) be incomparable positive integers, and let \(p\mid e\), \(q\mid f\)
be prime.  Then

\[
 \frac e p\mid\frac f q
\tag{1.3}
\]

if and only if \(p\) is a fragile surplus of \(e\) over \(f\) and
\(q\in D(f,e)\).

In particular \(p\ne q\).  Moreover,

\[
 \frac e p=\frac f q
\tag{1.4}
\]

if and only if \(p\) is a fragile surplus of \(e\) over \(f\), \(q\) is a fragile
surplus of \(f\) over \(e\), and all other prime exponents agree.

**Proof.**  Put \(\alpha_\ell=v_\ell(e)\) and
\(\beta_\ell=v_\ell(f)\).  If (1.3) holds, then

\[
 \alpha_\ell-\mathbf1_{\ell=p}
 \le \beta_\ell-\mathbf1_{\ell=q}
 \qquad(\ell\text{ prime}).
\tag{1.5}
\]

Because \(e\nmid f\), some coordinate has \(\alpha_\ell>\beta_\ell\).
Equation (1.5) shows that the only possible such coordinate is \(p\), that its
excess is exactly one, and that \(p\ne q\).  At \(q\), (1.5) says
\(\beta_q\ge\alpha_q+1\), so \(q\in D(f,e)\).  This proves necessity.

Conversely, if (1.2) holds and \(q\in D(f,e)\), then subtracting one at \(p\)
removes the sole excess of \(e\), while subtracting one at \(q\) still leaves
\(\beta_q-1\ge\alpha_q\).  Every coordinate of (1.5) follows, proving (1.3).

Equality holds exactly when (1.5) is equality at every coordinate.  Applying the
already proved characterization in both orientations gives (1.4).  ∎

This lemma shows that a one-prime shadow conflict is a codimension-one phenomenon.
If \(e\) exceeds \(f\) in two prime coordinates, or exceeds it by at least two in
its only surplus coordinate, then no immediate shadow of \(e\) can divide an
immediate shadow of \(f\).

## 2. Safe deletion primes

For \(e\in E\), call a prime \(p\mid e\) **safe in \(E\)** if \(p\) is not a
fragile surplus of \(e\) over any \(f\in E\setminus\{e\}\).

### Theorem 2.1 (safe-deletion star criterion)

Suppose every \(e\in E\) has a safe prime \(p_e\mid e\).  Then

\[
 e\longmapsto e/p_e
\tag{2.1}
\]

is injective and has primitive image.  Consequently the one-root star (0.1) satisfies
HBC using type \(0\) on every edge, and hence has an absolute-dilation primitive
dominator through the absorbed HBC theorem.

**Proof.**  If two distinct selected shadows were equal or comparable, orient them
so that \(e/p_e\mid f/p_f\).  Lemma 1.1 would say that \(p_e\) is a fragile surplus
of \(e\) over \(f\), contradicting its safety.  Thus the shadows are distinct and
primitive.  Type \(0\) costs \(2\le p_e\), and multiplication by the common root
preserves equality and divisibility.  This is HBC for the sole length-one word.  ∎

The theorem is independent of exact \(\Omega\)-rank.  It is also constructive once
the exponent vectors are known.

### Example 2.2 (the unbounded private-prime chain is safe)

Let

\[
 E_m=\{2^ip_i:1\le i\le m\},
\tag{2.2}
\]

where the \(p_i\) are distinct odd primes.  Deleting \(p_i\) produces the forbidden
shadow chain \(2,4,\ldots,2^m\), so these fixed shadows cannot be repaired by two
types when \(m\ge3\).

For every \(i\), however, the prime \(2\) is safe.  If \(i<j\), the only surplus of
\(2^ip_i\) over \(2^jp_j\) is \(p_i\), while if \(i>j\) there are surpluses at both
\(2\) and \(p_i\).  Theorem 2.1 therefore deletes \(2\) throughout and gives the
primitive shadows

\[
 2^{i-1}p_i.
\tag{2.3}
\]

This recovers the strict repair in the probabilistic HBC round by an exact local
criterion rather than by inspection.

### Example 2.3 (the first mixed-rank obstruction is repaired)

For \(E=\{6,20\}\), the prime \(3\) is a fragile surplus of \(6\) over \(20\),
which explains the bad choice \(6/3=2\mid4=20/5\).  The prime \(2\) is safe for
both members.  Deleting it gives \(3,10\), a primitive one-type shadow batch.

## 3. Exact conflict probabilities

Lemma 1.1 also gives a closed formula for random deletion conflicts.  Let
\(\mu_e\) be any probability measure on the distinct prime divisors of \(e\), and
choose the deletion primes independently.  Write

\[
 \mu_e(S)=\sum_{\ell\in S}\mu_e(\ell).
\tag{3.1}
\]

### Corollary 3.1

For incomparable \(e,f\),

\[
 \Pr\!\left(\frac e{P_e}\mid\frac f{P_f}\right)
 =
 \begin{cases}
 \mu_e(p)\,\mu_f(D(f,e)),
 &\text{if \(p\) is the fragile surplus of \(e\) over \(f\),}\\
 0,&\text{if no such \(p\) exists.}
 \end{cases}
\tag{3.2}
\]

**Proof.**  Lemma 1.1 says that the event is exactly
\(\{P_e=p,\ P_f\in D(f,e)\}\).  Independence gives (3.2).  ∎

The probability of comparability is the union of the two oriented events.  Their
intersection is precisely equality of shadows and is characterized by (1.4), so it
can be included exactly rather than estimated twice:

\[
\Pr(\text{comparable})
=\Pr(e/P_e\mid f/P_f)+\Pr(f/P_f\mid e/P_e)
 -\Pr(e/P_e=f/P_f).
\tag{3.3}
\]

In the equality case of Lemma 1.1, the last probability is
\(\mu_e(p)\mu_f(q)\); otherwise it is zero.  Formula (3.2) therefore supplies
concrete event weights for the product-state LLL criterion in the probabilistic HBC
round.

For an exact type factor, let \(\kappa_e(t\mid p)\) be a probability kernel supported
on the types admissible for \(p\), so in particular \(\kappa_e(1\mid2)=0\), and
choose the types conditionally independently after the deletion primes.  Put

\[
 K_{e,f}(p,q)=\sum_{t=0}^1\kappa_e(t\mid p)\kappa_f(t\mid q).
\tag{3.4}
\]

The probability of the oriented HBC bad event is then

\[
\Pr\!\left(\frac e{P_e}\mid\frac f{P_f}\ \text{and}\ T_e=T_f\right)
=
\sum_{\substack{p\mid e\\p\text{ fragile from }e\text{ to }f}}
\mu_e(p)\sum_{q\in D(f,e)}\mu_f(q)K_{e,f}(p,q).
\tag{3.5}
\]

For independent uniform choices among the admissible types, Lemma 1.1 gives
\(p\ne q\), so at most one of \(p,q\) is \(2\); in every case
\(K_{e,f}(p,q)=1/2\).  Other local-state distributions may be correlated inside a
parent block and should instead use their actual joint same-type probability.

## 4. Exact remaining star problem

The safe-prime condition is sufficient, not declared necessary.  If an element has no
safe prime, every possible deletion is fragile against at least one other member, but
the resulting conflicts may still be split between the two types or removed by jointly
changing the other deletions.  Exact-rank stars already show that global matching can
succeed without a common safe choice visible one element at a time.

The nearest unresolved subproblem is:

> Does every primitive pairwise non-coprime family admit immediate prime deletions and
> admissible binary types such that, on each type class, the shadow map is injective
> and its image is primitive?

A positive answer would prove HBC for every one-root height-one Hasse star, but would
not prove universal HBC for arbitrary height.  A strict star counterexample would,
on the other hand, refute Conjecture 6.2 (universal HBC), because the star is
quasi-primitive and its parent selector is unique.  It would still not refute the
historical quasi-primitive domination implication or Erdős 892: HBC is a sufficient
arithmetic mechanism, not a proved necessary condition for bounded primitive
domination.  Lemma 1.1 reduces both the deterministic and probabilistic attacks on
this subproblem to the directed graph of fragile surplus primes.

No Lean formalization is started because the arbitrary-star statement and the original
conjecture remain open.
