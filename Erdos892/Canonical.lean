module

public import Erdos892.Basic
public import Mathlib.Data.Finset.Interval
public import Mathlib.Tactic

/-!
# A finite canonical core for Erdős Problem 892

This file formalizes the order-theoretic content of Lemma 10.4 in the
stage manuscript: a primitive kernel in the lower half of `[2, 2*M]` has a
canonical, maximal primitive completion in the upper half.

The statement deliberately uses only finite sets of natural numbers.  It is
the lossless reduction on which the later finite factor-two feasibility model
depends; it makes no claim about the unresolved infinite conjecture.
-/

@[expose] public section

namespace Erdos892

/-- A finite set is primitive when divisibility between two members forces
equality. -/
def IsPrimitive (A : Finset ℕ) : Prop :=
  ∀ ⦃a⦄, a ∈ A → ∀ ⦃b⦄, b ∈ A → a ∣ b → a = b

/-- The canonical completion of a lower-half kernel `H`: retain exactly the
upper-half integers which are not multiples of any member of `H`. -/
def canonicalCompletion (M : ℕ) (H : Finset ℕ) : Finset ℕ :=
  H ∪ (Finset.Ioc M (2 * M)).filter (fun n => ∀ h ∈ H, ¬h ∣ n)

/-- The finite predicate is exactly the restriction of the project's set-level
notion of primitivity to the coercion of a finset. -/
@[simp] theorem isPrimitive_iff_primitive_coe (A : Finset ℕ) :
    IsPrimitive A ↔ Primitive (↑A : Set ℕ) := by
  constructor
  · intro h a b ha hb hab
    exact h ha hb hab
  · intro h a ha b hb hab
    exact h ha hb hab

private theorem upper_half_eq_of_dvd
    {M a b : ℕ}
    (haM : M < a)
    (hbM : M < b) (hb2M : b ≤ 2 * M)
    (hab : a ∣ b) : a = b := by
  obtain ⟨k, rfl⟩ := hab
  have hk0 : k ≠ 0 := by
    intro hk
    simp [hk] at hbM
  by_cases hk : k = 1
  · simp [hk]
  have hk2 : 2 ≤ k := by omega
  have htwice : a * 2 ≤ a * k := Nat.mul_le_mul_left a hk2
  omega

/-- The first assertion of manuscript Lemma 10.4. -/
theorem canonicalCompletion_isPrimitive
    {M : ℕ} {H : Finset ℕ}
    (hH : IsPrimitive H)
    (hHrange : H ⊆ Finset.Icc 2 M) :
    IsPrimitive (canonicalCompletion M H) := by
  intro a ha b hb hab
  rcases Finset.mem_union.mp ha with haH | haUpper
  · rcases Finset.mem_union.mp hb with hbH | hbUpper
    · exact hH haH hbH hab
    · have hbAvoid := (Finset.mem_filter.mp hbUpper).2
      exact False.elim ((hbAvoid a haH) hab)
  · rcases Finset.mem_filter.mp haUpper with ⟨haIoc, _haAvoid⟩
    rcases Finset.mem_Ioc.mp haIoc with ⟨haM, _ha2M⟩
    rcases Finset.mem_union.mp hb with hbH | hbUpper
    · rcases Finset.mem_Icc.mp (hHrange hbH) with ⟨hb2, hbM'⟩
      have habLe : a ≤ b := Nat.le_of_dvd (by omega) hab
      omega
    · rcases Finset.mem_filter.mp hbUpper with ⟨hbIoc, _hbAvoid⟩
      rcases Finset.mem_Ioc.mp hbIoc with ⟨hbM, hb2M⟩
      exact upper_half_eq_of_dvd haM hbM hb2M hab

/-- The second assertion of manuscript Lemma 10.4: every primitive set in
`[2, 2*M]` is contained in the canonical completion of its lower half. -/
theorem subset_canonicalCompletion_lowerHalf
    {M : ℕ} {A : Finset ℕ}
    (hA : IsPrimitive A)
    (hArange : A ⊆ Finset.Icc 2 (2 * M)) :
    A ⊆ canonicalCompletion M (A.filter (fun n => n ≤ M)) := by
  intro a ha
  by_cases haM : a ≤ M
  · apply Finset.mem_union.mpr
    left
    exact Finset.mem_filter.mpr ⟨ha, haM⟩
  · have haRange := Finset.mem_Icc.mp (hArange ha)
    apply Finset.mem_union.mpr
    right
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_Ioc.mpr ⟨by omega, haRange.2⟩, ?_⟩
    intro h hh hdiv
    have hhA : h ∈ A := (Finset.mem_filter.mp hh).1
    have hhM : h ≤ M := (Finset.mem_filter.mp hh).2
    have heq : h = a := hA hhA ha hdiv
    omega

/-- A bundled version of the canonical top-half saturation lemma. -/
theorem canonical_top_half_saturation
    {M : ℕ} {A : Finset ℕ}
    (hA : IsPrimitive A)
    (hArange : A ⊆ Finset.Icc 2 (2 * M)) :
    let H := A.filter (fun n => n ≤ M)
    IsPrimitive (canonicalCompletion M H) ∧
      A ⊆ canonicalCompletion M H := by
  dsimp
  constructor
  · apply canonicalCompletion_isPrimitive
    · intro a ha b hb hab
      exact hA (Finset.mem_filter.mp ha).1 (Finset.mem_filter.mp hb).1 hab
    · intro h hh
      have hhA : h ∈ A := (Finset.mem_filter.mp hh).1
      have hhM : h ≤ M := (Finset.mem_filter.mp hh).2
      exact Finset.mem_Icc.mpr ⟨(Finset.mem_Icc.mp (hArange hhA)).1, hhM⟩
  · exact subset_canonicalCompletion_lowerHalf hA hArange

end Erdos892
