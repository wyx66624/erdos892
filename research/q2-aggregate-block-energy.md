# Erdős 892, Q2: an aggregate-block incidence-energy criterion

**Draft status.**  This note does not prove the rank-three estimate and does
not decide Q2.  It proves a sufficient first/second-moment criterion on the
actual maximal, high-excess, rank-five-screen survivors.  It also sharpens the
sparse-source boundary example: divergent source excess does not even force
two nontrivial source-local witnesses pointwise.

Retain the notation of `research/q2-rank3-excess-screen.md` and
`research/q2-source-local-block-decomposition.md`.  Fix `A<B`, let
`H_k -> infinity` with `H_k=o(sqrt(log k))`, and put

\[
 \mathcal N_k=\{m\in C_k^{A,B}:\iota_k(m)\in I_k,
                         f_{\iota_k(m),3}(m)>0\}.
\]

Let `L_k` be the subset of terminals which admit a maximal-layer
rank-three representation `m=dr`, `d in C_i`, `i=iota_k(m)`, with
`tau_i(d)<=H_k`.  Theorem 2.1 of the excess-screen note gives

\[
 |\mathcal L_k|=o_{A,B}(X_k).                                   \tag{1.1}
\]

Indeed, choosing one such representation injects the terminal set into a
subset of the pairs counted there; no uniqueness of representation is used.

For every `m in G_k:=N_k\L_k`, select the least maximal-layer divisor `d(m)`
whose complementary quotient `r(m)=m/d(m)` has rank three.  Write `i=iota_k(m)`
and define

\[
 A_m:=1+Q^+_{i,d(m),r(m)},\qquad
 B_m:=1+D^+_{i,d(m),r(m)}.                                      \tag{1.2}
\]

The exact source-local decomposition gives, without any distributional
assumption,

\[
 A_m=\nu_i(m),\qquad B_m=f_{i,3}(m),\qquad
 \frac{B_m}{A_m}=\frac{f_{i,3}(m)}{\nu_i(m)}.                   \tag{1.3}
\]

Since `m notin L_k`, its selected source has `tau_i(d)>H_k`; when `H_k>=4`,
maximality and Proposition 3.1 of the excess-screen note imply that this
selected triple survives every rank-five promotion block.  Thus every object
below is already conditioned on full maximality and on rank-five-screen
survival.

## 1. A conditional incidence-energy lemma

Put

\[
 K_k:=\max_{m\in C_k^{A,B}}\binom{\Omega(m)}3
       \ll_{A,B}(\log k)^3.                                    \tag{1.4}
\]

For `0<=s<=ceil(log_2 K_k)`, define the diagonal bin

\[
 \mathcal G_{k,s}:=\{m\in\mathcal G_k:2^s\le B_m<2^{s+1}\}.  \tag{1.5}
\]

For a nonempty bin set

\[
 M_s:=|\mathcal G_{k,s}|,\quad I_s:=\sum_{m\in\mathcal G_{k,s}}A_m,
 \quad E_s:=\sum_{m\in\mathcal G_{k,s}}A_m^2,
 \quad \mu_s:=I_s/M_s.                                        \tag{1.6}
\]

### Theorem 1.1 (binned incidence-energy criterion)

Suppose there are `R_k -> infinity` and sets `J_k` of nonempty bins such
that

\[
 \sum_{s\notin J_k}M_s=o_{A,B}(X_k),                            \tag{1.7}
\]

\[
 \mu_s\ge4R_k2^s\qquad(s\in J_k),                              \tag{1.8}
\]

and

\[
 \sum_{s\in J_k}
 \frac{E_s-I_s^2/M_s}{\mu_s^2}=o_{A,B}(X_k).                   \tag{1.9}
\]

Then

\[
 W_{k,3}^{A,B}=o_{A,B}(X_k).                                   \tag{1.10}
\]

#### Proof

For `s in J_k`, call `m in G_{k,s}` bad when `A_m<R_kB_m`.  By (1.5),

\[
 A_m<R_k2^{s+1}\le\mu_s/2.
\]

Chebyshev's inequality, here merely the deterministic second-moment identity,
therefore gives

\[
 \#\{m\in\mathcal G_{k,s}:m\text{ bad}\}
 \le {4\over\mu_s^2}\sum_{m\in\mathcal G_{k,s}}(A_m-\mu_s)^2
 ={4(E_s-I_s^2/M_s)\over\mu_s^2}.                              \tag{1.11}
\]

Summing (1.11), and using (1.7) and (1.9), shows that all but `o(X_k)`
members of `G_k` satisfy `A_m>=R_kB_m`.  By (1.3), their total contribution
to the symmetric rank-three mass is at most `X_k/R_k`; every exceptional
terminal contributes at most one.  Finally (1.1) handles the low-excess
terminals.  This proves (1.10).  □

### Exact meaning of the energy

For the selected representation, let `W(m)` be the set of pairs `(a,b)` with

\[
 a\mid r(m),\quad b\mid d(m),\quad(a,b)=1,
 \quad {d(m)a\over X_i}\le b<{2d(m)a\over X_i},
 \quad\Omega(b)\le\tau_i(d(m))+\Omega(a).                       \tag{1.12}
\]

Then `A_m=|W(m)|`.  Consequently `I_s` is exactly the number of incidences
`(m,a,b)` in the bin, while `E_s` is exactly the number of ordered pairs of
such incidences with common terminal `m`.  Thus (1.9) is a source-local
divisor-window energy estimate, not an independence assumption.  Common
prime factors, repeated primes in `r`, and collisions between different
`a`-blocks are all retained in `E_s`.

A first/second-moment attack may now aim directly at (1.8)--(1.9), after the
rank-five screen.  There are only `O(log log k)` diagonal bins.  This is an
average alternative to a pointwise lower bound for `Q^+`; neither condition is
claimed to imply the other.  It retains substantially more information than
a global unconditioned first moment.

### Why a bounded second-moment ratio is not enough

The little-`o` variance in (1.9) cannot be replaced merely by
`E_s=O(I_s^2/M_s)`.  As a finite-array counterexample, take `M` even,
`B_m=1` for all `m`, and let `A_m=1` on half the indices and `A_m=2R` on the
other half.  Then `A_m>=B_m`, the mean is asymptotic to `R`, and
`E/(I^2/M)->2`, but half the indices fail every threshold `A_m>=cR B_m`
with fixed `c>0`.  This closes only a proof schema based on a global mean and
a bounded relative second moment; it makes no claim that this abstract array
is realized by divisor blocks.

## 2. A sharp pointwise obstruction for aggregate blocks

The sparse-source construction in Section 6 of the excess-screen note can be
sharpened from `nu_i(m)<=8` to `Q^+<=1`.

### Proposition 2.1 (divergent excess with at most one nontrivial witness)

Let `H_i -> infinity`, `H_i=o(sqrt(U_i))`, put `N_i=L_i+H_i`, and choose
primes exactly as in that construction:

\[
 q_i\in\left({X_i\over2\,3^{N_i}},{X_i\over3^{N_i}}\right),
 \qquad d_i=3^{N_i}q_i,                                         \tag{2.1}
\]

and, for `i in I_k`,

\[
 P_{i,k}\in\left((X_k/(2d_i))^{1/3},(X_k/d_i)^{1/3}\right),
 \qquad m_{i,k}=d_iP_{i,k}^3.                                  \tag{2.2}
\]

For every fixed `A<B` and all sufficiently large admissible `i,k`, the
displayed representation has divergent source excess, lies in the correct
source and terminal size/rank bands, and satisfies

\[
 Q^+_{i,d_i,P_{i,k}^3}\le1,
 \qquad \nu_i(m_{i,k})\le2.                                    \tag{2.3}
\]

#### Proof

The band and excess assertions were proved in Section 6 of the excess-screen
note.  Write `S=3^{N_i}`, `q=q_i`, and `P=P_{i,k}`.  Uniformly for
`k/3<=i<=2k/5`, the established growth of `X_i` gives

\[
 S=o(P),\qquad P=o(q),\qquad d_i=o(P^3).                        \tag{2.4}
\]

For completeness, `log S=O_A(log k)`, whereas

\[
 \log P={1\over3}(\log X_k-\log X_i)+o(\log X_k),\qquad
 \log q=\log X_i+o(\log X_k).
\]

Here the previously established critical-strip relation
`n_i/n_k=i/k+o(1)` (equivalently
`log X_i/log X_k=i/k+o(1)`) is used.  Hence the coefficient of `log X_k` in `log(q/P)` is at
least `1/9+o(1)`, and that in `log(P^3/d_i)` is at least `1/5+o(1)`.
Hence (2.4), with arbitrarily large fixed separation factors, follows.

The integer divisors of `r=P^3` are `a=1,P,P^2,P^3`; those of `d_i` are
`b=3^tq^epsilon`, `0<=t<=N_i`, `epsilon in {0,1}`.  For `a=P`, the block
window is contained in `(P/2,2P)`.  By (2.4), divisors with `epsilon=0`
are at most `S<P/2`, while divisors with `epsilon=1` are at least `q>2P`.
Thus this block is empty.

For `a=P^2`, the divisors with `epsilon=0` are again below the window.  The
divisors with `epsilon=1` form the geometric progression `q,3q,...,Sq`.
The block window has endpoint ratio exactly two, so it contains at most one
member of a progression of ratio three.  Imposing the coprimality and rank
cutoff can only remove members.

For `a=P^3`, (2.4) gives

\[
 {d_iP^3\over X_i}>{P^3\over2}>d_i,
\]

so its block contains no divisor of `d_i`.  The only remaining block is
`a=1`, whose unique member is `b=1`.  Therefore `Q^+<=1`; the exact block
decomposition gives `nu_i(m)=1+Q^+<=2`.  □

This is a strict arithmetic counterexample to the pointwise implication

> divergent source excess and a rank-three representation force aggregate
> nontrivial source-local population to tend to infinity.

It does not refute Theorem 1.1, the rank-five-screen estimate, or Q2: the
construction is sparse and `i` has not been proved to be the maximal old
layer of `m`.  Instead it proves that maximality and averaging cannot be
dropped from the incidence-energy target.

## 3. Audit of quantifiers and boundaries

1. **Maximality.**  It is imposed in `N_k` through `i=iota_k(m)`.  It is used
   to place every selected high-excess triple among rank-five-screen
   survivors.  Proposition 2.1 deliberately makes no maximality claim.
2. **Domains.**  Theorem 1.1 concerns only terminal integers in the fixed
   two-sided rank band and critical source strip.  The selected divisor is a
   maximal-layer divisor with rank-three complement.
3. **Endpoints.**  Every witness window in (1.12) is weak on the left and
   strict on the right, exactly equivalent to `X_i/2<d a/b<=X_i`.  The
   factor-two argument in Proposition 2.1 uses the same half-open window.
4. **Repeated factors.**  The index `a|r` is over integer divisors.  In
   Proposition 2.1, `r=P^3` has four, not eight, such divisors.  The canonical
   gcd decomposition and `(a,b)=1` prevent double counting.
5. **Rank five.**  No screen-survivor estimate is assumed secretly.  The
   screen is used only to specify the smaller family on which the new energy
   estimates (1.8)--(1.9) may be attacked.
6. **Remaining gap.**  Neither (1.8) nor (1.9) is proved.  Even if both are
   established, only the rank-three symmetric target follows; ranks at least
   four and uniformity across the full terminal rank range remain open.
7. **Formalization boundary.**  This is a paper-level reduction plus a
   boundary counterexample.  It does not justify conjecture-level Lean code.
