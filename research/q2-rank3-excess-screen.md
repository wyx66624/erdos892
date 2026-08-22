# Erdős 892, Question 2: rank-three actual-union attack, round 2

**Status (22 August 2026).**  This note does not prove either exact target
\((7.3)\) or \((7.6)\) of `q2_next_round.md`, and it does not decide the
logarithmic-barrier construction.  It gives three rigorous reductions:

1. maximality can be written exactly in the *cofactor* variables, with an
   explicit rank budget governed by the integral source excess;
2. rank-three anchors whose source excess is
   \(o(\sqrt{\log k})\) have total mass \(o(X_k)\), modulo the standard
   central-range Sathe--Selberg upper bound for \(\Omega\);
3. the remaining high-excess anchors satisfy a new rank-five screening
   condition.  Proving that the unweighted mass surviving this screen is
   \(o(X_k)\) would prove the symmetric target and would produce a
   deterministic selector satisfying the rank-three target.

The note also gives exact ordinary and mixed multiplicative-energy identities,
and records strict obstructions to two tempting shortcuts: variance without
anti-concentration, and pointwise growth of the same-layer multiplicity.

Throughout, retain the notation of `q2_next_round.md`, and put

\[
 L_j:=\lceil T_j\rceil .                                      \tag{1.1}
\]

Since \(\Omega\) is integer valued, the condition \(\Omega(n)\ge T_j\)
is exactly \(\Omega(n)\ge L_j\).

### External analytic sources

The central-range Sathe--Selberg estimate for \(\Omega\), including the
uniform range \(\ell\le(2-\varepsilon)\log\log x\), is used in the form
recorded in Gérald Tenenbaum, *Introduction to Analytic and Probabilistic
Number Theory*, third edition, Graduate Studies in Mathematics 163, American
Mathematical Society, 2015 (the Sathe--Selberg chapter).  Its fixed-rank
specialization supplies (2.3).  Prime reciprocal Mertens is the classical
theorem of F. Mertens, “Ein Beitrag zur analytischen Zahlentheorie,” *Journal
für die reine und angewandte Mathematik* **78** (1874), 46--62.  The
fixed-ratio prime existence used in Section 6 is the immediate consequence
\(\pi(\lambda x)-\pi(x)\sim(\lambda-1)x/\log x\), \(\lambda>1\), of the
prime number theorem; a standard source is H. Davenport, *Multiplicative
Number Theory*, third edition revised by H. L. Montgomery, Graduate Texts in
Mathematics 74, Springer, 2000.  These results are named external inputs, not
proved in this note.

## 1. Exact cofactor form of maximality

For an odd terminal integer \(m\), an index \(j<k\), and a divisor
\(c\mid m\), put \(e=m/c\).  Directly from the two defining inequalities for
\(C_j\),

\[
 e\in C_j
 \quad\Longleftrightarrow\quad
 \frac{m}{X_j}\le c<\frac{2m}{X_j}
 \quad\hbox{and}\quad
 \Omega(c)\le \Omega(m)-L_j .                    \tag{1.2}
\]

This is the quotient-side version of the coprime-swap spectrum.  It has the
advantage that the allowable quotient rank is visible without choosing a
particular old divisor.

### Proposition 1.1 (excess-budget maximality) -- proved

Suppose \(i<k\), \(m=dr\in C_k\), \(d\in C_i\), and
\(\Omega(r)=3\).  Define the integral
source excess

\[
 \tau_i(d):=\Omega(d)-L_i\ge0,
 \qquad \delta_{ij}:=L_j-L_i.                    \tag{1.3}
\]

Then \(i=\iota_k(m)\) if and only if, for every \(i<j<k\), there is no
divisor \(c\mid m\) such that

\[
 \frac{m}{X_j}\le c<\frac{2m}{X_j},
 \qquad
 \Omega(c)\le 3+\tau_i(d)-\delta_{ij}.           \tag{1.4}
\]

If \(c=b(r/a)\), where \(a\mid r\), \(b\mid d\), and \((a,b)=1\), then
the excluded cofactor in (1.4) is exactly the divisor complementary to the
coprime swap \(e=(d/b)a\).

#### Proof

Equation (1.2) says precisely when a later pool divisor exists.  Complete
additivity gives

\[
 \Omega(m)-L_j
 =\Omega(d)+3-L_j
 =3+\tau_i(d)-\delta_{ij},
\]

which proves (1.4).  For the last assertion,
\(m/((d/b)a)=b(r/a)\).  Conversely the canonical gcd decomposition in
Proposition 2.1 of `q2_next_round.md` writes every complementary divisor in
this form. \(\square\)

### Lemma 1.2 (only two threshold jumps on the critical strip) -- proved

Uniformly for \(k/3\le i\le2k/5\) and \(i\le j\le k\), for all sufficiently
large \(k\),

\[
 0\le \delta_{ij}\le2.                            \tag{1.5}
\]

#### Proof

The function \(T_x\) is increasing.  Moreover

\[
 U_k-U_i=\log(n_k/n_i)=\log(k/i)+o(1)
\]

uniformly on the strip, while
\(\sqrt{U_k}-\sqrt{U_i}=O((\log k)^{-1/2})\).  Hence

\[
 0\le T_k-T_i\le\log3+o_A(1)<2.
\]

Taking ceilings can create at most two integer jumps. \(\square\)

The point of (1.4) is that the full \(b>1\) mechanism is not an
unstructured error.  At rank three it asks for low-rank cofactors in a
specified family of dyadic windows; the allowable rank grows exactly with the
source excess \(\tau_i(d)\).

## 2. Low source excess has negligible rank-three mass

We use the standard Sathe--Selberg upper bound for the number
\(\pi_\ell(x)=\#\{n\le x:\Omega(n)=\ell\}\): for every fixed
\(\varepsilon>0\), uniformly in
\(1\le\ell\le(2-\varepsilon)\log\log x\),

\[
 \pi_\ell(x)\ll_\varepsilon
 \frac{x}{\log x}
 \frac{(\log\log x)^{\ell-1}}{(\ell-1)!}.       \tag{2.1}
\]

This is the precise external analytic input; no short-interval or local-CLT
asymptotic is being assumed.  If
\(\ell=U_i+A\sqrt{U_i}+o(\sqrt{U_i})\), Stirling's formula applied to
(2.1) gives

\[
 \pi_\ell(X_i)\ll_A X_i/\sqrt{U_i}.              \tag{2.2}
\]

The odd dyadic count is a subset of this count.  Setting \(\ell=3\) in the
same Sathe--Selberg estimate gives the fixed-rank specialization

\[
 \#\{n\le R:\Omega(n)=3\}
 \ll \frac{R(\log\log R)^2}{\log R}.             \tag{2.3}
\]

### Theorem 2.1 (low-excess erasure) -- proved modulo (2.1), (2.3)

Let \(H_k\to\infty\) with \(H_k=o(\sqrt{\log k})\).  The number of all
pairs \((i,d,r)\), even without imposing terminal membership or maximality,
such that

\[
 i\in I_k,\quad d\in C_i,\quad
 0\le\tau_i(d)\le H_k,\quad
 r\in\mathcal R_{i,k},\quad \Omega(r)=3,
\]

is

\[
 \ll_A \frac{H_k+1}{\sqrt{\log k}}X_k=o(X_k).    \tag{2.4}
\]

Consequently, the contribution of these anchors to both the deterministic
indicator sum (7.2) and the symmetric mass (7.4) is \(o(X_k)\), uniformly in
the deterministic rule.

#### Proof

Because \(L_i+h=U_i+A\sqrt{U_i}+o(\sqrt{U_i})\) uniformly for
\(0\le h\le H_k\), these ranks lie below
\((3/2)U_i\) for all large \(i\); after increasing the starting index their
standardized displacement is at most \(A+1\).  Thus (2.2) shows that, for a fixed \(i\), the number of
possible \(d\)'s is

\[
 \ll_A (H_k+1)X_i/\sqrt{U_i}.
\]

On the critical strip,

\[
 \log(2X_k/X_i)\asymp k(\log k)^2,
 \qquad
 \log\log(2X_k/X_i)\asymp\log k.
\]

Thus (2.3) gives \(O(X_k/(kX_i))\) possible rank-three quotients for
each \(d\).  Since \(|I_k|=O(k)\) and \(U_i\asymp\log k\), summation proves
(2.4).  Both exact sums are sub-sums of this unweighted pair count. \(\square\)

This reduction is stronger than discarding finitely many excess levels.  For
example, one may take \(H_k=(\log k)^{1/4}\).  Hence any non-negligible
rank-three obstruction must be supported on anchors for which
\(\tau_i(d)\to\infty\).

## 3. A rank-five screen for every remaining maximal pair

For a prime \(p\mid r\), define the moving rank-three divisor block

\[
 \mathcal B_j(d,p):=
 \left[\frac{dp}{X_j},\frac{2dp}{X_j}\right)
 \qquad(i<j<k).                                  \tag{3.1}
\]

### Proposition 3.1 (rank-five promotion screen) -- proved

For all sufficiently large \(k\), suppose
\(i\in I_k\), \(m=dr\in C_k\), \(d\in C_i\),
\(\Omega(r)=3\), and
\(\tau_i(d)\ge4\).  If there are a prime divisor \(p\mid r\), an index
\(i<j<k\), and a divisor \(b\mid d\) satisfying

\[
 \Omega(b)=3,\qquad b\in\mathcal B_j(d,p),       \tag{3.2}
\]

then \(e=dp/b\) belongs to \(C_j\).  In particular, \(d\) is not a
maximal old anchor of \(dr\).

#### Proof

The block condition is exactly

\[
 X_j/2<dp/b\le X_j.
\]

Moreover \(e\mid dr\), and \(e\) is odd.  Its complementary divisor
\(b(r/p)\) has rank five, whether or not \(b\) and \(p\) are coprime.
By Lemma 1.2,

\[
 \Omega(e)=\Omega(d)+1-3
 =L_i+\tau_i(d)-2\ge L_i+2\ge L_j.
\]

Thus \(e\in C_j\). \(\square\)

The same argument gives a larger deterministic screen.  If \(a\mid r\),
\(b\mid d\),

\[
 b\in[da/X_j,2da/X_j),\qquad
 \Omega(b)-\Omega(a)\le\tau_i(d)-2,              \tag{3.3}
\]

then \(da/b\in C_j\).  Its complementary cofactor has rank
\(3+\Omega(b)-\Omega(a)\le\tau_i(d)+1\).  Proposition 3.1 is the first
fixed-rank instance with \(\Omega(a)=1\), \(\Omega(b)=3\); it keeps the
cofactor rank equal to five independently of \(k\).  We retain this smaller
screen below because its analytic target has fixed rank.

Let \(\mathscr S_k(H)\) denote the set of triples \((i,d,r)\) with

\[
 i\in I_k,\quad d\in C_i,\quad r\in\mathcal R_{i,k},\quad
 \Omega(r)=3,\quad dr\in C_k^{A,B},\quad \tau_i(d)>H,
\]

for which (3.2) fails for **every** prime \(p\mid r\) and every
\(i<j<k\).  Full swap avoidance implies membership in
\(\mathscr S_k(H)\) whenever \(H\ge4\).

### Corollary 3.2 (one exact sufficient estimate) -- proved

If, for one function
\(H_k\to\infty\), \(H_k=o(\sqrt{\log k})\),

\[
 |\mathscr S_k(H_k)|=o(X_k),                     \tag{3.4}
\]

then

\[
 W_{k,3}^{A,B}=o_{A,B}(X_k).                     \tag{3.5}
\]

Moreover there is a deterministic maximal-layer divisor rule \(d_*\) for
which

\[
 |\mathcal M_{k,3}^{A,B}(d_*)|=o_{A,B}(X_k).     \tag{3.6}
\]

#### Proof

Split the exact sum (7.4) at \(\tau_i(d)=H_k\).  The low-excess part is
\(o(X_k)\) by Theorem 2.1.  Every high-excess maximal pair survives the
screen by Proposition 3.1, and its weight \(1/\nu_i(dr)\le1\), so the other
part is at most \(|\mathscr S_k(H_k)|\).

For the selector assertion, restrict to
\(m\in C_k^{A,B}\) having an old pool divisor and satisfying
\(\iota_k(m)\in I_k\).  For each such \(m\), choose a maximal-layer divisor
with non-rank-three cofactor whenever one exists, using least divisor as a
fixed tie-breaker; otherwise choose the least maximal-layer divisor.
This rule selects rank three only when every maximal-layer divisor has
rank-three cofactor.  Such an \(m\) contributes exactly one to (7.4), so the
number of these \(m\)'s is at most \(W_{k,3}^{A,B}\).  Extend the rule by the
least available maximal-layer divisor outside this target set; those values
do not affect (3.6). \(\square\)

Estimate (3.4), not the unconditioned rank-three pair count refuted in
Proposition 6.1 of `q2_next_round.md`, is the closest positive analytic
target found in this round.  It is a divisor-in-many-moving-intervals theorem
for rank-three divisors of a high-\(\Omega\) source.  A second-moment or
Janson proof has to retain the dependence caused by common prime factors of
the possible \(b\)'s.

There is a strict fixed-rank obstruction to using only the first moment of
those divisor events.  Let

\[
 \mathcal F_z=
 \{3pq:p<q\le z\text{ odd primes},\ p,q\ne3\}.
\]

Every member has rank three, and the prime reciprocal Mertens theorem cited
above gives

\[
 \sum_{b\in\mathcal F_z}\frac1b\asymp(\log\log z)^2\longrightarrow\infty.
\]

However, every odd integer not divisible by \(3\) avoids all of
\(\mathcal F_z\); the relative avoidance density among odd integers is at
least \(2/3\).  Thus a large rank-three reciprocal mass, by itself, cannot
prove (3.4).  This counterexample closes only the first-moment saturation
shortcut.  It does not close a pruned Janson, cluster-expansion, or
moving-block argument whose dependency term is controlled.

## 4. Exact multiplicity and multiplicative-energy bookkeeping

For a terminal integer with maximal layer \(i\), write

\[
 \mathcal D_i(m):=\{d\in C_i:d\mid m\},\qquad
 \nu_i(m)=|\mathcal D_i(m)|,
\]

\[
 f_{i,3}(m):=
 \#\{d\in\mathcal D_i(m):\Omega(m/d)=3\}.        \tag{4.1}
\]

Then the summand of the symmetric object is exactly
\(f_{i,3}(m)/\nu_i(m)\).

More generally, put

\[
 f_{i,q}(m):=\#\{d\in\mathcal D_i(m):\Omega(m/d)=q\}.
\]

If \(M=\Omega(m)\), then the pool threshold gives the exact rank
decomposition

\[
 \nu_i(m)=\sum_{0\le q\le M-L_i}f_{i,q}(m).       \tag{4.2}
\]

For a rank-three representation \(m=dr\), the top rank in (4.2) is
\(M-L_i=3+\tau_i(d)\).  Thus the high-excess regime isolated in Theorem 2.1
is precisely the regime in which the denominator has a growing range of
possible cofactor ranks.  This is an exact identity, not a claim that those
ranks are populated for each \(m\).

### Proposition 4.1 (rank-three collision parametrization) -- proved

Two rank-three representations of the same integer,

\[
 dr=d'r',\qquad \Omega(r)=\Omega(r')=3,           \tag{4.3}
\]

are parametrized uniquely by

\[
 r=ga,\quad r'=gb,\quad d=hb,\quad d'=ha,
 \quad (a,b)=1,\quad
 \Omega(g)+\Omega(a)=\Omega(g)+\Omega(b)=3,       \tag{4.4}
\]

where \(g=(r,r')\) and \(h=d/b=d'/a\).  Conversely every tuple in (4.4)
gives a collision (4.3).

#### Proof

Put \(g=(r,r')\), \(a=r/g\), and \(b=r'/g\).  Then \((a,b)=1\), and
cancelling \(g\) from (4.3) gives \(da=d'b\).  Euclid's lemma gives
\(b\mid d\) and \(a\mid d'\), hence the common integer \(h\).  Equality of
the two quotient ranks gives
\(\Omega(g)+\Omega(a)=\Omega(g)+\Omega(b)=3\).  The converse is
immediate. \(\square\)

Thus ordinary rank-three energy counts precisely equal-rank coprime swaps; it
does not see same-layer divisors whose complementary quotient has another
rank.

For a set \(\mathcal N\) of terminal integers all charged at their maximal
layers, put

\[
 P_3=\sum_{m\in\mathcal N}f_{i(m),3}(m),\quad
 E_3=\sum_{m\in\mathcal N}f_{i(m),3}(m)^2,
\]

\[
 E_{3,\mathrm{all}}
 =\sum_{m\in\mathcal N}f_{i(m),3}(m)\nu_{i(m)}(m),
\quad
 W_3=\sum_{m\in\mathcal N}\frac{f_{i(m),3}(m)}{\nu_{i(m)}(m)}. \tag{4.5}
\]

Cauchy--Schwarz gives the exact diagnostic inequalities

\[
 \#\{m:f_{i(m),3}(m)>0\}\ge \frac{P_3^2}{E_3},
 \qquad
 W_3\ge \frac{P_3^2}{E_{3,\mathrm{all}}}.         \tag{4.6}
\]

The second follows by writing
\(f=\sqrt{f/\nu}\sqrt{f\nu}\).  Hence, if a surviving maximal pair mass
has \(P_3\gg X_k\), then an \(o(X_k)\) symmetric mass is possible through
multiplicity only if the mixed energy satisfies
\(E_{3,\mathrm{all}}/P_3\to\infty\).  An *upper* bound
\(E_3=O(X_k)\), of the kind sought in a low-dependency Poisson argument,
would instead give a positive-density rank-three image when \(P_3\gg X_k\).

There is also a useful soft high/low multiplicity split.  The unrestricted
rank-three pair estimate (2.3) gives \(P_3=O(X_k)\) on the critical strip.
For every \(R\ge1\),

\[
 W_3\le \frac{P_3}{R}
 +\#\{m:f_{i(m),3}(m)>0,\ \nu_{i(m)}(m)<R\}.      \tag{4.7}
\]

Thus a multiplicity proof may equivalently show that low-multiplicity maximal
survivors are \(o(X_k)\) for some \(R=R_k\to\infty\).  Formula (4.6) explains
why ordinary rank-three energy is insufficient: the required object is the
mixed energy with *all* same-layer pool divisors.

The general mixed collision has the same canonical form.  If
\(dr=d's\), put \(g=(r,s)\), \(a=r/g\), \(b=s/g\).  Then

\[
 r=ga,\quad s=gb,\quad d=hb,\quad d'=ha,
 \quad(a,b)=1,                                    \tag{4.8}
\]

but now \(\Omega(a)-\Omega(b)=\Omega(r)-\Omega(s)\) need not vanish.
This is the precise multiplicative-energy object needed by the reciprocal
weight.

## 5. The local anti-concentration interface

For fixed \(m\) and its maximal layer \(i\), define the empirical rank law
on the actual same-layer pool divisors by

\[
 \pi_{m,i}(t):=
 \frac{\#\{d\in\mathcal D_i(m):\Omega(d)=t\}}
      {\nu_i(m)}.                                  \tag{5.1}
\]

Since \(M:=\Omega(m)\) is fixed,

\[
 \frac{f_{i,3}(m)}{\nu_i(m)}=\pi_{m,i}(M-3).       \tag{5.2}
\]

Therefore the following average two-dimensional local limit statement is a
sufficient input for (7.6):

\[
 \sum_{\substack{m\in C_k^{A,B}\\
                  \iota_k(m)\in I_k,\\
                  f_{\iota_k(m),3}(m)>0}}
 \max_t\pi_{m,\iota_k(m)}(t)=o(X_k).              \tag{AC}
\]

It is essential that (AC) is an **anti-concentration** theorem after
conditioning divisor size to one dyadic window.  Divergence of the variance
alone is logically insufficient: the probability laws assigning masses
\(1/2,1/4,1/4\) to \(0,-N,N\) have variance tending to infinity but maximal
atom \(1/2\).  One needs a concentration-function bound or a genuine local
limit theorem for the two coordinates \((\log d,\Omega(d))\).

Known one-dimensional divisor concentration results, such as the
Erdős--Hooley \(\Delta\)-function theory, control how many divisors occupy a
short logarithmic interval.  They do not by themselves compare the different
\(\Omega\)-levels inside that interval, so they do not imply (AC).  Ford's
divisor-in-an-interval theorems likewise show that multiplicities in a single
size window have delicate clustering; they cannot be inserted as an
anti-concentration statement without an additional rank refinement.

## 6. Strict obstruction to pointwise multiplicity growth

Here is an asymptotic family inside the correct source and terminal
size/rank bands.

Choose any integer sequence \(H_i\to\infty\) with
\(H_i=o(\sqrt{U_i})\), put
\(N_i=L_i+H_i\), and use the prime number theorem in fixed-ratio intervals to
choose an odd prime

\[
 q_i\in\left(\frac{X_i}{2\cdot3^{N_i}},
                    \frac{X_i}{3^{N_i}}\right].   \tag{6.1}
\]

Then \(d_i=3^{N_i}q_i\in C_i\) and
\(\tau_i(d_i)\to\infty\).  For any \(k\) with \(i\in I_k\), again by the
prime number theorem choose

\[
 P_{i,k}\in
 \left(\left(\frac{X_k}{2d_i}\right)^{1/3},
             \left(\frac{X_k}{d_i}\right)^{1/3}\right].          \tag{6.2}
\]

Put \(m_{i,k}=d_iP_{i,k}^3\).  Then
\(m_{i,k}\in(X_k/2,X_k]\), its displayed source quotient has rank three,
and for all large \(i\), \(m_{i,k}\in C_k^{A,B}\) for every fixed \(B>A\).

Indeed, \(3^{N_i}=\exp(O_A(U_i+H_i))=(\log X_i)^{O_A(1)}\), so the
endpoints in (6.1) tend to infinity and the fixed-ratio PNT applies; the same
is clear in (6.2).  Also

\[
 \Omega(m_{i,k})=N_i+4=L_i+H_i+4\ge L_k
\]

by Lemma 1.2.  On the other hand, uniformly for \(i\in I_k\),
\(U_k-U_i=O(1)\) and \(\sqrt{U_k}\sim\sqrt{U_i}\), so

\[
 U_k+B\sqrt{U_k}-\Omega(m_{i,k})
 =(B-A)\sqrt{U_k}-H_i+O_A(1)>0
\]

eventually.  This proves the asserted terminal two-sided band membership.

Every divisor of \(m_{i,k}\) has the form

\[
 3^a q_i^bP_{i,k}^c,qquad
 0\le a\le N_i,\quad b\in\{0,1\},\quad0\le c\le3.                \tag{6.3}
\]

For each fixed pair \((b,c)\), at most one value of \(a\) can put (6.3) in
the factor-two interval \((X_i/2,X_i]\), because consecutive values differ
by a factor of three.  Consequently

\[
 \#\{e\mid m_{i,k}:X_i/2<e\le X_i\}\le8.          \tag{6.4}
\]

In particular, whenever the displayed source layer is used,
\(\nu_i(m_{i,k})\le8\).

This is a strict counterexample to any pointwise assertion

> high source excess plus a rank-three representation forces the same-layer
> divisor multiplicity to tend to infinity.

It does **not** refute (AC), (3.4), (7.3), or (7.6): the family is sparse, and
we have not asserted that \(i\) is the maximal old layer of \(m_{i,k}\).
Rather, it proves that an average exceptional-set theorem using the full
factorization distribution (or full maximality) is indispensable.

The same example also shows why a two-dimensional Littlewood--Offord theorem
cannot be applied pointwise using only the number of prime factors.  The
logarithmic tokens may lie on a very sparse lattice, and a factor-two window
can meet only boundedly many subset sums.

## 7. What remains open, and the proof dependency chain

The rank-three problem is now reduced to two genuinely different live
analytic statements.

1. **Swap-hitting / rank-five screen.**  Prove (3.4).  A viable proof may use
   a rank-refined Ford estimate, a dependent Janson/Brun argument for the
   divisors \(b\) in (3.2), or a dispersion estimate for the six variables in
   \(d=hb\), \(r=p(r/p)\), \(e=hp\).  The common-prime clusters among the
   rank-three \(b\)'s must be retained; a small dependency estimate would, by
   (4.6), point toward a positive union rather than an upper bound.

2. **Symmetric multiplicity / local limit.**  Prove (AC), or more weakly use
   (4.7) to show that low-\(\nu\) full-maximal survivors are \(o(X_k)\).
   This requires a rank-refined, size-conditioned divisor theorem.  Variance
   alone and pointwise high \(\Omega\) have both been strictly ruled out as
   sufficient inputs.

The logical chain is

\[
 \text{central-range Sathe--Selberg upper bound for }\Omega
 \Longrightarrow \text{low-excess erasure},
\]

\[
 \text{(3.4) or (AC)}
 \Longrightarrow W_{k,3}^{A,B}=o(X_k)
 \Longrightarrow \text{a deterministic selector avoiding rank three}.
\]

Even after this chain is completed, ranks \(4,5,\ldots\) and then uniformity
up to \(O_{A,B}(\sqrt{\log k})\) remain.  No Lean formalization should begin
from this note: the analytic estimate (3.4)/(AC) is still open.
