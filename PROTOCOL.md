# Research and proof-admission protocol

## 1. Claim labels

Every research note must label each assertion as exactly one of:

- **THEOREM** — complete proof supplied, dependencies pinned;
- **CONDITIONAL** — implication proved from an explicitly named missing input;
- **COMPUTATION** — finite result with deterministic certificate;
- **CONJECTURE** — precise statement not proved;
- **HEURISTIC** — motivation only;
- **BARRIER** — a precisely delimited mechanism is disproved; this does not refute
  the target conjecture unless the logical implication is separately proved.

## 2. Route preservation

For every active direction, record:

1. definitions and quantifiers;
2. its strongest proved intermediate statement;
3. the next minimal lemma;
4. small and extremal examples;
5. every attempted counterexample;
6. the exact reason for closure, if closed.

Lack of a current tool, a nonstandard method, or a failed first proof is not a closure
reason. Failed directions should yield a counterexample family, a boundary theorem,
or a corrected conjecture whenever possible.

## 3. Independent review

Critical lemmas require two reviews with different failure searches:

- a quantifier/dependency audit;
- an adversarial audit using edge cases, finite search, or an alternative proof.

The author of a proof cannot supply both reviews. Reviews record exact commits.

## 4. Computation

Computational evidence must include:

- a mathematically complete description of the searched space;
- proof that pruning is lossless;
- exact software versions and command line;
- node/case counts and hashes;
- an independent checker when the output is used as a certificate.

Computation over finitely many bounds is never extrapolated to the infinite problem.

## 5. Lean

The `main` branch forbids `sorry`, `admit`, project-defined axioms, and hidden oracle
assumptions. CI performs a normal build plus an axiom audit. A theorem depending on
classical choice or propositional extensionality may do so only when the dependency is
reported by the audit and is mathematically harmless.

## 6. Solution declaration

The repository may say “solved” only if the paper's final theorem implies the exact
historical formulation, the dependency ledger has no open node, both independent
reviews are recorded, and Lean CI checks the final theorem. Until then the front page
must say **OPEN**.
