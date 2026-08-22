# Formalization experiment: canonical top-half saturation

Status: **experimental until CI is green**.

This branch formalizes the finite core of manuscript Lemma 10.4. The theorem says
that a primitive lower-half kernel `H ⊆ [2,M]` can be completed by every upper-half
integer in `(M,2M]` not divisible by `H`; the completion remains primitive and
contains every primitive `A ⊆ [2,2M]` having that lower half.

This is a lossless finite reduction, not a solution of Erdős Problem 892. The next
formal nodes, if this branch compiles, are the exact deadline formulation (Theorem
10.5) and the Boolean feasibility model (Proposition 10.7).
