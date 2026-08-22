# Independent review record: Q1 component augmenting paths

Date: 22 August 2026  
Reviewed manuscript: `research/q1-component-augmenting-path.md`  
Frozen author SHA-256: `5ff5116b324f538dfa1160f42a5a6fe8eb44dc7246947238396bea70a246005d`

## Review 1 — graph, valuation, and endpoint audit

Final grade: **A**.

The reviewer reconstructed the equivalence between successful fixed-shadow
recolourings and proper two-colourings of the full comparability graph,
including equal shadows, isolated vertices, and the type-1 prohibition on
deleting 2.  The non-squarefree minimum-rank argument in Lemma 3.1, the
all-assignment quantifiers in Theorem 3.2, and the deletion-changing
one-endpoint continuation in Theorem 3.3 were checked independently.  A
corollary number and a potentially misleading unique-blocker reference were
repaired before the frozen version.

## Review 2 — component flip and adversarial family audit

Final grade: **A**.

The reviewer independently checked both fragile-surplus forbidden-set
orientations, every necessity/sufficiency direction of the component
criterion, deletion of the unique even endpoint followed by a component
flip, and insertion of the missing even option.  The B26 family was checked
against its displayed shadow lists: the blocker component is exactly the
two-vertex component claimed.

## Admission boundary

The reviews certify the exact opposite-row cover, the classification of all
fixed-deletion recolourings, the necessary chordless even-path obstruction,
and the one-endpoint continuation.  They do not prove that every nine-member
star escapes the endpoint covers, universal HBC, Q1, Erdős 892, or any
conjecture-level Lean theorem.
