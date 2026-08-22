# Erdős Problem 892 research repository

> **Status: OPEN.** This repository does not currently contain a complete proof of
> Erdős Problem 892. `main` contains only audited statements, reproducible
> infrastructure, and formally checked lemmas. Speculative research is developed on
> separate `research/*` branches.

This project studies the two questions usually grouped as Erdős Problem 892:

1. characterize increasing integer sequences \(b_1<b_2<\cdots\) that admit an
   increasing primitive sequence \(a_1<a_2<\cdots\) with \(a_n\le Cb_n\);
2. characterize exponent sequences \(n_1<n_2<\cdots\) for which a primitive set
   \(A\) has \(A(2^{n_i})\ge c2^{n_i}\) at every prescribed scale.

The historically intended special case in the first question forbids
\(\gcd(b_i,b_j)=b_r\) only when \(b_i\nmid b_j\) and \(b_j\nmid b_i\). Under the
literal stronger reading that forbids every solution except \(i=j=r\), the input
sequence is already primitive.

## Repository map

- [`STATUS.md`](STATUS.md): exact claim ledger and remaining proof obligations.
- [`PROTOCOL.md`](PROTOCOL.md): rules for proof admission, counterexamples, and
  branch isolation.
- [`paper/audited_baseline.tex`](paper/audited_baseline.tex): formal research note
  containing the verified baseline, audited partial advances, counterexamples, and
  exact unresolved interfaces.
- [`paper/audited_advances.tex`](paper/audited_advances.tex): modular proofs of the
  mixed-rank two-shadow theorem, Hasse-palette compression, the middle-anchor
  semiprime floor, and the period-free Bonferroni transfer lemma.
- [`paper/audited_baseline.pdf`](paper/audited_baseline.pdf): rendered version of
  that note.
- [`research/q1-mixed-rank-shadow.md`](research/q1-mixed-rank-shadow.md): extended
  Q1 proof, strict mechanism barriers, and live alternative routes.
- [`research/q2-actual-union.md`](research/q2-actual-union.md): extended Q2 proof,
  actual-union interfaces, counterexamples, and reproducible finite experiments.
- [`research/general-deadline-antichain.md`](research/general-deadline-antichain.md):
  fixed-dilation deadline margins, their weighted antichain dual, and an explicit
  integrality gap in the actual divisor poset `P_15`.
- [`archive/README.md`](archive/README.md): provenance and checksum of the supplied
  169-page partial-results manuscript.
- [`archive/stage-2026-08-20.pdf`](archive/stage-2026-08-20.pdf): directly readable
  copy of that supplied manuscript; it is preserved as a partial-results source, not
  admitted wholesale as a proof.
- [`Erdos892/Basic.lean`](Erdos892/Basic.lean): Lean definitions and foundational
  recoding lemmas, with no `sorry` or project axioms.

## Proof gate

A claimed solution may enter `main` only when all of the following hold:

1. every implication in the dependency ledger has a complete written proof;
2. two independent reviewers have checked all critical lemmas and quantified
   hypotheses;
3. computational claims include source, deterministic reproduction commands, and
   exact hashes;
4. the final theorem is present in Lean with no `sorry`, `axiom`, `admit`, or
   unreviewed `native_decide` shortcut;
5. CI builds the paper and Lean development and the claim status is changed only in
   the same reviewed commit.

## Local commands

```bash
latexmk -pdf -output-directory=paper/build paper/audited_baseline.tex
lake build
rg -n '\\b(sorry|admit|axiom)\\b' --glob '*.lean'
```

The Lean toolchain and Mathlib revision are pinned for reproducibility. GitHub CI is
the authoritative build while a local Lean installation is unavailable.

## Primary sources

- P. Erdős, A. Sárközy, E. Szemerédi, *On divisibility properties of sequences
  of integers*, Colloq. Math. Soc. János Bolyai 2 (1970), 35–49.
- P. Erdős, *A survey of problems in combinatorial number theory*, Ann. Discrete
  Math. 6 (1980), 89–115.
- G. Martin, C. Pomerance, *Primitive sets with large counting functions*, Publ.
  Math. Debrecen 79 (2011), 521–530.

The current public problem page still labels #892 as open; a status label is not a
proof, and this project applies the proof gate above independently.
