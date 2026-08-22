# Nine-child stars: the exact three-singleton-signature target

Date: 22 August 2026  
Scope: the first one-root star case beyond the audited eight-child theorem  
Status: **paper reduction proposed for review; the nine-child theorem remains open**

This note identifies the only possible shape of a nine-member quotient palette
which is not already solved by minimum-rank insertion and the saturated
support-transversal repair.  It does not construct an HBC counterexample.

Throughout, \(E\subseteq\mathbb Z_{\ge2}\) is primitive and pairwise
non-coprime.  A successful assignment chooses one immediate prime deletion and
an admissible type \(0\) or \(1\) for every member, with primitive injective
shadow images in each type.

## 1. A three-subset transversal fact

### Lemma 1.1

Let \(S\) be a three-element set and let
\(\mathcal T=\{T_1,T_2,T_3\}\) be three nonempty subsets of \(S\), counted
with their indices.  If no two-element subset of \(S\) meets all three
\(T_i\), then the three \(T_i\) are exactly the three distinct singleton
subsets of \(S\).

#### Proof

If some \(T_i\) contains at least two elements, its complement has at most one
element.  Choose one point from each of the other two nonempty sets.  If one
chosen point lies in \(T_i\), these at most two points hit all three sets.  If
neither lies in \(T_i\), both chosen points equal the unique point outside
\(T_i\); adjoining any point of \(T_i\) again gives a transversal of size two.
Thus every \(T_i\) must be a singleton.  If two singleton sets agree, their
common point together with the point in the third singleton is a transversal
of size at most two.  Hence all three are distinct.  ∎

## 2. Necessary structure of a nine-member obstruction

### Theorem 2.1 (exact nine-member reduction)

Assume the audited theorem that every palette of at most eight members has a
successful assignment.  Let \(E\) have nine members and suppose \(E\) has no
successful assignment.  Then for every minimum-\(\Omega\) member \(e\in E\):

1. \(\operatorname{supp}(e)=\{2,p,q\}\) for distinct odd primes \(p,q\);
2. for every successful assignment on \(F=E\setminus\{e\}\), all five
   options

   \[
    (2,0),(p,0),(p,1),(q,0),(q,1)
   \tag{2.1}
   \]

   are blocked;
3. choosing one blocker per option gives five distinct blockers \(H\), and
   the three extras \(G=F\setminus H\) have support signatures

   \[
   \bigl\{\operatorname{supp}(g)\cap\{2,p,q\}:g\in G\bigr\}
   =\bigl\{\{2\},\{p\},\{q\}\bigr\}.
   \tag{2.2}
   \]

The equality in (2.2) is as an indexed three-member family.  In particular,
the three extras can be labelled \(g_2,g_p,g_q\) so that each meets the
support of \(e\) in exactly its subscripted prime.

#### Proof

Fix a minimum-\(\Omega\) member \(e\), and let
\(r=\omega(e)\).  If \(r\le2\), the audited support-at-most-two theorem solves
the entire palette, contrary to the hypothesis.  Hence \(r\ge3\).

The eight-member theorem gives a successful assignment on
\(F=E\setminus\{e\}\).  The member \(e\) has

\[
 L(e)=2r-\mathbf1_{2\mid e}
\tag{2.3}
\]

admissible insertion options, and each old member blocks at most one.  If an
option were unblocked, inserting it would solve \(E\).  Therefore every
option is blocked.

Choose one blocker for every option.  These blockers are distinct, since one
old member blocks at most one option.  Let \(H\) be the selected blocker set
and \(G=F\setminus H\).  In particular, saturation forces \(L(e)\le8\), and
\[
 |G|=8-L(e)\ge0.
\tag{2.4}
\]
The saturated support-transversal lemma says that
every two support primes of \(e\) cover \(H\), and that \(E\) is solvable
whenever the nonempty signatures

\[
 \operatorname{supp}(g)\cap\operatorname{supp}(e),\qquad g\in G,
\tag{2.5}
\]

have a transversal of size at most two.

If \(r\ge4\), then \(L(e)\ge7\), so
\[
 |G|=8-L(e)\le1.
\]
The signatures in (2.5) are nonempty by pairwise non-coprimality, and one
nonempty set has a one-point transversal.  This would solve \(E\), a
contradiction.

Suppose \(r=3\) and \(e\) is odd.  Then \(L(e)=6\), so \(|G|=2\).  Choosing
one point from each nonempty signature gives a transversal of size at most
two, again a contradiction.  Consequently \(r=3\) and \(e\) is even, which
proves assertion 1 and gives exactly the five options in (2.1).

Now \(L(e)=5\), so \(|H|=5\) and \(|G|=3\).  If the three signatures had a
transversal of size at most two, saturated support-transversal repair would
solve \(E\).  They do not.  Lemma 1.1, applied to
\(S=\{2,p,q\}\), gives exactly (2.2).  The argument began with an arbitrary
successful assignment on \(F\), so assertions 2--3 hold for every such
assignment.  ∎

### Corollary 2.2 (minimal-counterexample form)

Any cardinality-minimal counterexample to the arbitrary-star shadow theorem
has at least nine members.  If it has exactly nine, every minimum-rank member
and every solution of its eight-member deletion obey Theorem 2.1.

This follows because the audited eight-member theorem excludes smaller
palettes, while Theorem 2.1 applies to a nine-member counterexample.

## 3. Exact remaining exchange problem

The nine-member boundary family in the eight-child note realizes all of
Theorem 2.1's support signatures and saturates the five options, but a single
change to the \((2,0)\)-blocker frees an insertion option.  Hence conditions
(2.1)--(2.2) are necessary, not sufficient for obstruction.

The nearest unresolved statement is:

> Given the forced three extras \(g_2,g_p,g_q\), can one always change the
> deletion/type choice of at least one saturated blocker—or jointly recolour
> an extra and a blocker—so that one option of \(e\) becomes free without
> creating a new same-type comparability?

A negative answer must be an all-assignment integer certificate, not merely a
fixed saturated solution.  A positive answer would prove the nine-child
one-root theorem but would still leave arbitrary stars and mixed-parent Hasse
forests open.  No conjecture-level Lean work is justified at this stage.
