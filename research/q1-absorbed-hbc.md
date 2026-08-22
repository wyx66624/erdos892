# Q1 next round: absorbed hybrid shadow--batching

Date: 22 August 2026  
Scope: parent/type-label erasure for the quasi-primitive part of Erdős Problem 892  
Status: **partial theorem and strict method barriers; the original problem remains open**

This note isolates a sufficient condition under which all parent and binary shadow-type
labels can be erased arithmetically at a cost paid by the prime factors deleted along the
source path.  The arithmetic erasure is proved completely (modulo the standard prime
number theorem in dyadic intervals).  What is not proved is that every quasi-primitive
Hasse forest admits the required primitive batching of its shadow cores.

## 1. Hasse forests, shadow cores, and deletion budgets

Let $B\subseteq\mathbb N$ be finite or countable and quasi-primitive in the historical
sense: if $x,y\in B$ are incomparable, then $\gcd(x,y)\notin B$.
For each nonminimal $b\in B$, choose a lower cover $\sigma(b)\in B$.  Direct every
edge from $\sigma(b)$ to $b$.  This is a rooted forest because every edge increases
the integer by a factor at least two, so every backwards path terminates after finitely
many steps.  Its roots form the primitive set $R$ of divisibility-minimal members.

For a parent $d$, its quotient palette is

\[
 E_d=\{e=b/d:\sigma(b)=d\}.
\]

The audited Hasse-palette lemma says that every $E_d$ is primitive and pairwise
non-coprime.  The audited mixed-rank two-shadow theorem therefore supplies, for each
$d$, maps

\[
 e\longmapsto(\psi_d(e),t_d(e))\in\mathbb N\times\{0,1\},
 \qquad e/\psi_d(e)\text{ prime},
\tag{1.1}
\]

such that the displayed pairs are injective.  Call a choice **admissible weighted** if,
with $p_d(e)=e/\psi_d(e)$,

\[
 q_{t_d(e)}\le p_d(e),\qquad q_0=2,\quad q_1=3.
\tag{1.2}
\]

Such an admissible labelling always exists: label a singleton shadow fibre by $0$.
In a two-element fibre the two deleted primes are distinct; label the member with the
smaller prime by $0$ and the other by $1$.  The smaller prime is at least $2$, and
the larger is at least $3$.  This is only a canonical existence choice, not a
restriction on the later HBC optimization: a singleton or unique shadow with deleted
prime at least $3$ may instead receive type $1$, provided the labelled pairs remain
injective inside the palette.

For $b\in B$, write its forest path as

\[
 r=b_0\to b_1\to\cdots\to b_h=b,
 \qquad e_j=b_j/b_{j-1},\qquad
 d_j=\psi_{b_{j-1}}(e_j),\qquad p_j=e_j/d_j.
\]

Define its **type word**, **shadow core**, and **deletion budget** by

\[
 \epsilon(b)=(t_{b_0}(e_1),\ldots,t_{b_{h-1}}(e_h)),
 \qquad c(b)=r\prod_{j=1}^h d_j,
 \qquad \Delta(b)=\prod_{j=1}^h p_j.
\tag{1.3}
\]

For a root, the word is empty, $c(r)=r$, and $\Delta(r)=1$.  Unique factorization is
not needed for the exact identity

\[
 b=c(b)\Delta(b).
\tag{1.4}
\]

For a binary word $\epsilon$, put

\[
 W(\epsilon)=2^{\#\{j:\epsilon_j=0\}}
              3^{\#\{j:\epsilon_j=1\}},\qquad W(\varnothing)=1.
\tag{1.5}
\]

Equation (1.2) gives the pointwise budget inequality

\[
 W(\epsilon(b))\le \Delta(b).
\tag{1.6}
\]

### Definition 1.1 (hybrid primitive-batch condition)

A choice of parent selector and two-shadow maps satisfies **HBC** if, for every finite
binary word $\epsilon$, the map

\[
 b\longmapsto c(b)\qquad(\epsilon(b)=\epsilon)
\tag{1.7}
\]

is injective and its image is primitive.  Thus an HBC batch may contain infinitely many
parents.  No disjointness of prime supports, no common value of $\Omega$, and no bound
on the number of parents is part of the definition.

The rest of the note proves that HBC is sufficient.  In particular, once HBC is known,
there is no further parent/type-label erasure problem.

There is also an unconditional local batching which explains exactly why the remaining
problem is global.

### Lemma 1.2 (actual-deleted-prime batches)

Let $E$ be primitive, and choose one prime divisor $p(e)\mid e$ for each $e\in E$.
For every prime $p$, the map

\[
 e\longmapsto e/p\qquad(p(e)=p)
\]

is injective and has primitive image.

**Proof.**  If $e_1/p\mid e_2/p$, then $e_1\mid e_2$, so primitivity forces
$e_1=e_2$.  Equality of two images is included in the same argument.  ∎

Thus mixed $\Omega$-ranks cause no local loss if one retains the complete deleted-prime
label.  Section 4.5 proves that the words formed from all such labels have too much entropy
to be stored universally within their product budgets.  HBC asks whether the labels can
instead be merged into the two low-entropy type-word batches without losing primitivity.

## 2. An absorbing reservoir

The terminal type marker cannot be required to avoid the source supports: a source may
use every prime.  The following sparse-reservoir lemma absorbs all occurrences of its own
primes before installing a terminal tag.

### Lemma 2.1 (summable dyadic renewal)

Put $a_n=(n+1)^{-2}$ for $n\ge0$.  There is $C_a<\infty$ such that

\[
 (a*a)_n\le C_a a_n\qquad(n\ge0).
\tag{2.1}
\]

Consequently, if $0\le u_n\le\delta a_n$ and $\delta C_a<1$, then

\[
 \sum_{k\ge1}(u^{*k})_n\le
 \frac{\delta}{1-\delta C_a}a_n.
\tag{2.2}
\]

**Proof.**  In every term of the convolution, either $j\le n/2$ or
$n-j\le n/2$.  On the first range, $a_{n-j}\ll a_n$, and the sum of
$a_j$ is finite; the second range is symmetric.  This proves (2.1).
Inductively, $u^{*k}\le\delta^k C_a^{k-1}a$; summing the geometric series
proves (2.2).  ∎

### Lemma 2.2 (two-reservoir absorption)

There are disjoint sets $P,Q$ of odd primes, a constant $D_0$, and an injection

\[
 \chi:\langle P\cup Q\rangle\longrightarrow P,
 \qquad \chi(z)\le D_0z,
\tag{2.3}
\]

where the domain is the multiplicative semigroup generated by $P\cup Q$, including
$1$.  Write \(P(x)=|P\cap[1,x]|\) and \(Q(x)=|Q\cap[1,x]|\).
Moreover, for all sufficiently large $x$,

\[
 Q(x)\gg \frac{x}{(\log x)^2}.
\tag{2.4}
\]

The only analytic input is the standard dyadic prime-number theorem
$\pi(2x)-\pi(x)\gg x/\log x$.

**Proof.**  Let $I_n=(2^n,2^{n+1}]$.  Fix a sufficiently large absolute
$n_0\ge1$, leave all
earlier shells empty, and for every $n\ge n_0$ choose
disjoint prime sets $P_n,Q_n\subset I_n$, each of cardinality

\[
 A_n=\left\lfloor\varepsilon\frac{2^n}{(n+1)^2}\right\rfloor,
\]

where $\varepsilon>0$ will be fixed small.  The dyadic prime-number theorem
provides enough primes.  Set $P=\bigcup P_n$, $Q=\bigcup Q_n$, and
$s_n=|P_n|+|Q_n|$.  Then $u_n=2^{-n}s_n\le2\varepsilon a_n$.
Choose $\varepsilon$ so that Lemma 2.1 applies.

Write
\[
 H_{P\cup Q}(x)=|\langle P\cup Q\rangle\cap[1,x]|.
\]
Count these semigroup elements by ordered prime factorizations.
If the factors lie in shells with indices summing to $m$, then $m\le N$, and
the number of ordered choices is bounded by $2^m(u^{*k})_m$.  Hence (2.2) gives

\[
 H_{P\cup Q}(2^N)
 \le1+\sum_{m\le N}2^m\sum_{k\ge1}(u^{*k})_m
 \ll\sum_{m\le N}\frac{2^m}{(m+1)^2}
 \ll\frac{2^N}{(N+1)^2}.
\tag{2.5}
\]

The last bound follows by splitting at $N/2$.  The same estimate holds for arbitrary
$x$, with $2^N\asymp x$.  A completed preceding shell gives
$P(x),Q(x)\gg x/(\log x)^2$, proving (2.4).  After multiplying the argument by a
fixed sufficiently large dyadic constant $D_0$, (2.5) gives

\[
 H_{P\cup Q}(x)\le P(D_0x)\qquad(x\ge1),
\]

where enlarging $D_0$ handles the finite initial range.  Enumerate the semigroup
and $P$ increasingly as
\[
 z_1<z_2<\cdots,\qquad p_1<p_2<\cdots.
\]
Since \(j\le H_{P\cup Q}(z_j)\le P(D_0z_j)\), one has
\(p_j\le D_0z_j\).  Defining \(\chi(z_j)=p_j\) gives (2.3).  ∎

For $c\ge1$, let

\[
 z(c)=\prod_{p\in P\cup Q}p^{v_p(c)},
 \qquad
 \kappa(c)=\chi(z(c))\frac{c}{z(c)}.
\tag{2.6}
\]

Then $\kappa(c)\le D_0c$, $\kappa(c)$ is $Q$-free, and

\[
 \kappa(c)\mid\kappa(c')\quad\Longrightarrow\quad c\mid c'.
\tag{2.7}
\]

Indeed, the complete $P$-part of $\kappa(c)$ is the single prime $\chi(z(c))$.
Divisibility in (2.7) first forces these two $P$-parts to agree, then injectivity of
$\chi$ gives $z(c)=z(c')$, and comparison outside $P\cup Q$ gives $c\mid c'$.

## 3. The arithmetic label-erasure theorem

The next result is slightly more general than the binary Hasse application.

### Theorem 3.1 (weighted primitive-batch erasure)

Let $X$ be countable.  For every $x\in X$, let $c_x,\Delta_x$ be positive
integers, and suppose $b_x=c_x\Delta_x$.  Partition $X=\bigsqcup_{t\in T}X_t$.
Assume:

1. for each $t$, the $c_x$, $x\in X_t$, are distinct and form a primitive set;
2. every batch has a deadline $W_t\ge1$ with $W_t\le\Delta_x$ for $x\in X_t$;
3. for some $A<\infty$ and $0<s<1$,
   
   \[
   \#\{t:W_t\le y\}\le Ay^s\qquad(y\ge1).
   \tag{3.1}
   \]

Then there is an injection $\Phi:X\to\mathbb N$ whose image is primitive and

\[
 \Phi(x)\le D b_x\qquad(x\in X),
\tag{3.2}
\]

where $D$ depends only on $A,s$ and the absolute reservoir constants.  More
precisely, the terminal marker attached to $x\in X_t$ is at most
$D_1W_t\le D_1\Delta_x$.

**Proof.**  By (2.4) and $s<1$, after increasing $D_1$ we have

\[
 \#\{t:W_t\le y\}\le Q(D_1y)\qquad(y\ge1).
\]

Enumerate the nonempty batches so that
\(W_{t_1}\le W_{t_2}\le\cdots\), and enumerate \(Q\) increasingly as
\(\vartheta_1<\vartheta_2<\cdots\).  The deadline bound makes every bounded
initial set of batches finite, and
\[
 j\le\#\{t:W_t\le W_{t_j}\}\le Q(D_1W_{t_j}),
\]
so \(\vartheta_j\le D_1W_{t_j}\).  This increasing matching assigns distinct
primes \(\vartheta_t\in Q\) with the required bound.  Define

\[
 \Phi(x)=\vartheta_t\kappa(c_x)\qquad(x\in X_t).
\tag{3.3}
\]

Because $\kappa(c_x)$ is $Q$-free, divisibility $\Phi(x)\mid\Phi(y)$ forces
the complete $Q$-parts, hence the tags and the batches, to agree.  Equation (2.7)
then gives $c_x\mid c_y$; batchwise primitivity and distinctness give $x=y$.
Thus the image is primitive and the map injective.  Finally,

\[
 \Phi(x)\le D_0D_1W_tc_x\le D_0D_1\Delta_xc_x=D_0D_1b_x.
\]

This also proves the asserted marker-cost statement.  ∎

### Lemma 3.2 (binary word deadlines)

For all finite binary words, including the empty word,

\[
 \#\{\epsilon:W(\epsilon)\le y\}=O_s(y^s)
\tag{3.4}
\]

for some $0<s<1$.

**Proof.**  Choose $0<s<1$ sufficiently close to $1$ that
$2^{-s}+3^{-s}<1$.  Then

\[
 \sum_{\epsilon}W(\epsilon)^{-s}
 =\sum_{h\ge0}(2^{-s}+3^{-s})^h<\infty.
\]

Multiplying the summands with $W(\epsilon)\le y$ by $y^s$ proves (3.4).  ∎

### Theorem 3.3 (absorbed hybrid shadow--batching criterion)

If a finite or countable quasi-primitive set $B$ admits a lower-cover selector and
mixed-rank two-shadow maps satisfying HBC, then $B$ has a pointwise bounded injection
into a primitive set.  The bound is absolute (independent of $B$, its height, its
number of roots, all local ranks, and all deleted primes).

**Proof.**  Apply Theorem 3.1 with $X=B$, batches indexed by the complete type word,
$c_x=c(b)$, $\Delta_x=\Delta(b)$, and deadline $W_t=W(\epsilon)$.
HBC is hypothesis 1, (1.6) is hypothesis 2, and Lemma 3.2 is hypothesis 3.
The identity (1.4) then gives the required bound.  ∎

### Corollary 3.4 (ordered domination)

Under the hypotheses of Theorem 3.3, write the source increasingly as
\(b_1<b_2<\cdots\), and enumerate the primitive image increasingly as
\(a_1<a_2<\cdots\).  Then

\[
 a_n\le D b_n\qquad(n\ge1).
\]

**Proof.**  The first \(n\) source elements have \(n\) distinct images, all at most
\(Db_n\).  Hence the full image contains at least \(n\) elements in
\([1,Db_n]\), so its \(n\)-th order statistic is at most \(Db_n\).  The finite
case is identical for \(1\le n\le|B|\).  ∎

This theorem performs the desired arithmetic erasure: it installs only one terminal tag
for a complete type word, reuses that tag over an arbitrary (even infinite) primitive batch,
and absorbs every overlap between tag primes and source primes.  It neither pays one marker
per parent nor requires prime-support separation.  The sole unproved structural input is HBC.

## 4. Required stress tests

### 4.1 Repeated prime $2$ and infinitely many parents are not obstructions to the theorem

Let

\[
 B_2=\{2^jp:p\text{ odd prime},\ j\ge0\}.
\]

This is quasi-primitive.  Elements over a fixed $p$ form a chain; for $p\ne q$,

\[
 \gcd(2^ip,2^jq)=2^{\min(i,j)}\notin B_2.
\]

Choose the parent $2^{j-1}p$ of $2^jp$.  Every edge quotient is $2$, so its
shadow is $1$, its deleted prime is $2$, and its type is $0$.  For the word
$0^j$, the cores are exactly the odd primes $p$, hence form an infinite primitive
batch.  Thus HBC holds, $W(0^j)=2^j=\Delta(2^jp)$, and Theorem 3.3 applies.

The subfamily $\{p,2p:p\text{ odd prime}\}$ already shows why this reuse is necessary:
any rule demanding a distinct marker $m_p\le2C$ for every parent has only finitely many
available markers.  Theorem 3.3 uses one tag for the entire word-$0$ batch instead.

### 4.2 Cross-Ω comparability is a genuine batch failure

The set $B=\{1,6,20\}$ is quasi-primitive.  Its unique nontrivial palette
$E_1=\{6,20\}$ is primitive and pairwise non-coprime.  The valid immediate-shadow
choices

\[
 6\mapsto2\quad(\text{delete }3),\qquad
 20\mapsto4\quad(\text{delete }5)
\]

have distinct shadows, so both singleton fibres may receive type $0$.  Nevertheless
$2\mid4$, and the word-$0$ core batch is not primitive.  Therefore the audited
two-shadow theorem by itself does not imply HBC.  This is a strict counterexample to
"injective labelled shadows may simply be batched by type".  It is not robust under all
shadow choices: deleting $2$ from both sources gives the primitive shadows $3,10$.

### 4.3 Commutative path-boundary loss is not a support-bookkeeping technicality

Let $p,q>3$ be distinct primes and

\[
 B_{p,q}=\{2,3,6p,6q\}.
\]

The roots are $2,3$; both are lower covers of each of the other two members.
The only incomparable root pair has gcd $1\notin B_{p,q}$, and the two top members
have gcd $6\notin B_{p,q}$; all other relevant pairs are comparable.  Thus
$B_{p,q}$ is quasi-primitive.

Select $2$ as parent of $6p$ and $3$ as parent of $6q$.  Both selected palettes
are singletons.  Use

\[
 3p\mapsto3\quad(\text{delete }p),\qquad
 2q\mapsto2\quad(\text{delete }q),
\]

and give both type $0$.  Every local shadow batch is primitive, but the two global
word-$0$ cores are

\[
 2\cdot3=6=3\cdot2.
\]

Hence even local primitive batches do not imply global injectivity after parent boundaries
are forgotten.  This gives a strict counterexample family to the automatic local-to-global
batching rule.  Other selectors or shadows may repair this four-element example, so it is
not a counterexample to the existence of HBC or to Erdős Problem 892.

### 4.4 A fixed selector can defeat every two-type shadow choice

The preceding example used a deliberately bad shadow choice.  The next finite example is
stronger: after the displayed lower-cover selector is fixed, **no** allowable weighted
two-shadow choice satisfies HBC.

Put

\[
 B_\ast=\{1,16,22,32,36,572,576,704,1080\}
\]

and select parents by

\[
 \begin{array}{c|cccccccc}
 b&16&22&36&32&572&576&704&1080\\ \hline
 \sigma(b)&1&1&1&16&22&36&22&36.
 \end{array}
\tag{4.1}
\]

These are lower covers in the full set.  The selected quotient palettes are

\[
 E_1=\{16,22,36\},\quad E_{16}=\{2\},\quad
 E_{22}=\{26,32\},\quad E_{36}=\{16,30\};
\]

each is primitive and pairwise non-coprime.  The set $B_\ast$ is quasi-primitive:
using

\[
 16=2^4,\ 22=2\cdot11,\ 32=2^5,\ 36=2^2 3^2,\
 572=2^2\!\cdot11\cdot13,\ 576=2^6 3^2,\
 704=2^6\!\cdot11,\ 1080=2^3 3^3\!\cdot5,
\]

a direct check shows that the gcd of an incomparable pair lies in
$\{2,4,8,44,64,72\}$, disjoint from $B_\ast$.

The edge $16\to32$ has quotient $2$, so its shadow, deleted prime, and type are
forced to be $1,2,0$.  The root edge $1\to16$ similarly has shadow $8$ and
type $0$.  Hence $c(32)=8$ in the word-$00$ batch.

Now $36\to576$ has quotient $16$, whose shadow and type are forced to be $8,0$.
If the root edge $1\to36$ had type $0$, then $c(576)$ would be a multiple of
$8=c(32)$ in the word-$00$ batch.  Therefore its root type must be $1$.  Of the
two immediate shadows of $36$, the choice $18$ deletes $2$ and cannot pay type
$1$; consequently this forces

\[
 36\mapsto12\quad(\text{delete }3),\qquad t=1.
\tag{4.2}
\]

Likewise, $22\to704$ has quotient $32$, with forced shadow/type $16,0$.
A root type $0$ would again put a multiple of $8$ in the word-$00$ batch, so the
root edge $1\to22$ must have type $1$.  The shadow $11$ deletes $2$ and cannot
pay that type, forcing

\[
 22\mapsto2\quad(\text{delete }11),\qquad t=1.
\tag{4.3}
\]

But the two root-level word-$1$ cores in (4.2)--(4.3) are $12$ and $2$, and
$2\mid12$.  This contradicts HBC, independently of every remaining shadow choice.

This is a strict counterexample to the statement that **every fixed** lower-cover selector
admits HBC.  It is not a counterexample to existential HBC: in the same set, selecting
$32$ as parent of both $576$ and $704$, and deleting $2$ on every edge, gives
word-\(0\) cores \(8,11,18\), word-\(00\) cores \(8,143,270\), and
word-\(000\) cores \(72,88\); each displayed batch is primitive.  Hence the parent
selector and the shadow batching must be optimized jointly.  The dependency-free
checker \`research/experiments/q1_hbc_fixed_selector_check.py\` enumerates all 135
admissible choices for the displayed bad selector and verifies this repaired certificate;
the finite paper proof above does not depend on that enumeration.

### 4.5 Recording the entire deleted-prime word has too much entropy

A tempting repair is to retain the order of all deleted primes in one distinct terminal
marker and charge the marker to their product.  This is impossible even if markers may be
arbitrary positive integers rather than primes.

### Proposition 4.2 (three-symbol word-capacity barrier)

There is no constant $C$ and no injection $M$ from all finite words over
$\{2,3,5\}$ to $\mathbb N$ such that

\[
 M(p_1,\ldots,p_h)\le C\prod_{j=1}^h p_j
\tag{4.4}
\]

for every word.

**Proof.**  Put $S=1/2+1/3+1/5=31/30$, and let

\[
 \alpha_2=\frac{15}{31},\qquad
 \alpha_3=\frac{10}{31},\qquad
 \alpha_5=\frac6{31}.
\]

For large $h$, consider words containing $\alpha_ph+O(1)$ copies of each symbol.
Stirling's formula gives

\[
 \#\mathcal W_h=\exp(hH(\alpha)+o(h)),
 \qquad
 \prod_jp_j=\exp(hL+o(h)),
\]

where $L=\sum_p\alpha_p\log p$ and

\[
 H(\alpha)=-\sum_p\alpha_p\log\alpha_p
           =L+\log S>L.
\]

Thus, if $x_h=\exp(hL+o(h))$ bounds the weights of this family, then
\[
 \frac{\#\mathcal W_h}{x_h}
 =\exp\!\left(h(H(\alpha)-L)+o(h)\right)\longrightarrow\infty.
\]
For large $h$ there are more than $Cx_h$ such words, but only
$\lfloor Cx_h\rfloor$ positive integers at most $Cx_h$, contradicting (4.4).  ∎

The binary type alphabet avoids this barrier exactly because
$1/2+1/3<1$, allowing Lemma 3.2.  Consequently a universal proof cannot merely add
an independently recorded third low-cost symbol for rank or parent data.  Such information
must be erased by batching, encoded in the numerical core without destroying primitivity, or
paid for by additional contraction.  Proposition 4.2 is a barrier to the full-prime-word
terminal-tag mechanism, not to adaptive arithmetic recoding.

## 5. A checkable sufficient condition for HBC

The global batch condition is automatic under a familiar but non-universal separation
hypothesis.

### Lemma 5.1 (separated-support verifier)

Suppose that:

1. for each parent and each type $t$, the chosen shadows of type $t$ are distinct and
   primitive;
2. the unions of prime supports of the chosen shadows at different parents are pairwise
   disjoint and are disjoint from the union of root supports;
3. for roots $r\ne r'$, neither $r\mid r'$ nor $r'\mid r$.

Then HBC holds.

**Proof.**  Fix a type word and suppose $c(b)\mid c(b')$.  Projection to the union of
root supports gives $r\mid r'$, so root primitivity forces $r=r'$.  If the two paths
first diverge at a parent $d$, projection to the private support block belonging to $d$
gives divisibility between two distinct same-type local shadows, contrary to hypothesis 1.
Thus one path is an initial segment of the other.  The words have the same length, so the
paths coincide.  This proves both injectivity and primitivity within the batch.  ∎

This recovers the terminal-word mechanism for separated forests and allows mixed local
ranks whenever the two type classes are locally primitive.  The hypothesis is sufficient,
not necessary: the repeated-$2$ family $B_2$ violates separation at every level but
satisfies HBC directly.

## 6. Compactness and the exact remaining gap

For a fixed countable induced divisibility poset, every node has finitely many lower
covers and every integer has finitely many immediate shadows.  Give each nonroot node
\(b\) one finite-domain variable whose values are admissible triples
\[
 (\sigma(b),\psi_b,t_b).
\]
The local labelled-map condition is the family of pairwise constraints saying that
two nodes which select the same parent may not select the same pair
\((\psi,t)\).  For each pair of distinct nodes, add the HBC constraint forbidding
equal type words together with equal or comparable cores.  Although the selected
parent path is variable, every possible ancestor of \(b\) is a divisor of \(b\);
there are only finitely many such variables.  Hence every one of these local or
pairwise conditions is a finite-coordinate cylinder constraint.  Therefore the
usual finite-domain compactness argument gives:

### Lemma 6.1 (finite-obstruction compactness for HBC)

A fixed countable quasi-primitive set admits HBC choices if and only if every finite set
of local and pairwise HBC constraints can be satisfied simultaneously.

**Proof.**  The choice space is a product of finite discrete spaces.  By the
finite-divisor observation above, each atomic constraint defines a clopen cylinder
condition.  If every finite collection is satisfiable, compactness gives a point in
their total intersection.  Pairwise labelled-map constraints give the required local
injections, while the second family gives HBC.  The converse is immediate.  ∎

The closest unresolved statement is now the following.

### Conjecture 6.2 (universal HBC selection; open)

Every finite or countable quasi-primitive set has a lower-cover selector and weighted
two-shadow maps satisfying HBC.

Conjecture 6.2 plus Theorem 3.3 would prove the historical quasi-primitive implication.
No proof and no robust counterexample (one that defeats **every** selector and every allowable
shadow choice) is obtained here.  Sections 4.2--4.4 show respectively that local Hall
matchings, local primitive batches, and an arbitrary fixed selector are insufficient; they
do not refute Conjecture 6.2.

The exact dependency chain is

\[
 \text{quasi-primitivity}
 \Longrightarrow \text{primitive pairwise-noncoprime Hasse palettes}
 \Longrightarrow \text{weighted two-shadow choices}
 \xRightarrow{\textbf{OPEN: choose them with HBC}}
 \text{primitive core batches}
 \Longrightarrow \text{bounded arithmetic erasure (Theorem 3.3)}.
\]

Thus the marker construction, repeated prime $2$, infinitely many parents, and overlap
between source primes and marker primes are no longer separate gaps.  The single surviving
gap is global: choose the local shadows so that, within each complete type word, cross-
$\Omega$ comparability and commutative path-boundary collisions never occur.  Failure of
Conjecture 6.2 would still be only a barrier to this hybrid mechanism unless it were further
amplified into divergent primitive-domination constants.
