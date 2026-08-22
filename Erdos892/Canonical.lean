module

public import Mathlib.Data.Finset.Interval
public import Mathlib.Tactic

/-!
# A finite canonical core for Erdős Problem 892

This file formalizes the order-theoretic content of Lemma 10.4 in the supplied
stage manuscript: a primitive kernel in the lower half of `[2, 2*M]` has a
canonical, maximal primitive completion in the upper half.

The statement deliberately uses only finite sets of natural numbers. It is the
lossless reduction on which the later finite factor-two feasibility model depends;
it makes no claim about the unresolved infinite conjecture.
-/

namespace Erdos892

/-- A finite set is primitive when divisibility between two members forces equality. -/
def IsPrimitive (A : Finset ℕ) : Prop :=
  ∀ ⦃a⦄, a ∈ A → ∀ ⦃b⦄, b ∈ A → a ∣ b → a = b

/-- The canonical completion of a lower-half kernel `H`: retain exactly the
upper-half integers which are not multiples of any member of `H`. -/
def canonicalCompletion (M : ℕ) (H : Finset ℕ) : Finset ℕ :=
  H ∪ (Finset.Ioc M (2 * M)).filter (fun n => ∀ h ∈ H, ¬h ∣ n)

private theorem upper_half_eq_of_dvd
    {M a b : ℕ}
    (haM : M < a) (ha2M : a ≤ 2 * M)
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
  simp only [canonicalCompletion, Finset.mem_union, Finset.mem_filter,
    Finset.mem_Ioc] at ha hb
  rcases ha with haH | ⟨haM, ha2M, haAvoid⟩
  · rcases hb with hbH | ⟨_hbM, _hb2M, hbAvoid⟩
    · exact hH haH hbH hab
    · exact False.elim ((hbAvoid a haH) hab)
  · rcases hb with hbH | ⟨hbM, hb2M, _hbAvoid⟩
    · rcases hHrange hbH with ⟨hb2, hbM'⟩
      have habLe : a ≤ b := Nat.le_of_dvd (by omega) hab
      omega
    · exact upper_half_eq_of_dvd haM ha2M hbM hb2M hab

/-- Every primitive set in `[2, 2*M]` is contained in the canonical completion
of its lower half. -/
theorem subset_canonicalCompletion_lowerHalf
    {M : ℕ} {A : Finset ℕ}
    (hA : IsPrimitive A)
    (hArange : A ⊆ Finset.Icc 2 (2 * M)) :
    A ⊆ canonicalCompletion M (A.filter (fun n => n ≤ M)) := by
  intro a ha
  by_cases haM : a ≤ M
  · simp [canonicalCompletion, ha, haM]
  · have haRange := hArange ha
    rcases haRange with ⟨_ha2, ha2M⟩
    simp only [canonicalCompletion, Finset.mem_union, Finset.mem_filter,
      Finset.mem_Ioc]
    right
    refine ⟨by omega, ha2M, ?_⟩
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
      exact ⟨(hArange hhA).1, hhM⟩
  · exact subset_canonicalCompletion_lowerHalf hA hArange

end Erdos892
