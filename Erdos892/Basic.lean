module

public import Mathlib.Data.Nat.GCD.Basic
public import Mathlib.Data.Set.Lattice

/-!
# Primitive and quasi-primitive sets

Foundational definitions for Erdős Problem 892.  The definition of
`QuasiPrimitive` uses the historical convention: only incomparable source pairs are
tested for a gcd that is another source element.
-/

@[expose] public section

open Set

namespace Erdos892

/-- A set of natural numbers is primitive when divisibility between two of its
members forces equality. -/
def Primitive (A : Set ℕ) : Prop :=
  ∀ ⦃m n : ℕ⦄, m ∈ A → n ∈ A → m ∣ n → m = n

/-- The historically intended gcd-free condition from Erdős Problem 892. -/
def QuasiPrimitive (A : Set ℕ) : Prop :=
  ∀ ⦃m n d : ℕ⦄, m ∈ A → n ∈ A → d ∈ A →
    ¬m ∣ n → ¬n ∣ m → Nat.gcd m n ≠ d

theorem Primitive.mono {A B : Set ℕ} (hA : Primitive A) (hBA : B ⊆ A) :
    Primitive B := by
  intro m n hm hn hmn
  exact hA (hBA hm) (hBA hn) hmn

theorem primitive_range_iff {ι : Type*} (u : ι → ℕ) :
    Primitive (Set.range u) ↔ ∀ i j, u i ∣ u j → u i = u j := by
  constructor
  · intro h i j hij
    exact h ⟨i, rfl⟩ ⟨j, rfl⟩ hij
  · intro h m n hm hn hij
    rcases hm with ⟨i, rfl⟩
    rcases hn with ⟨j, rfl⟩
    exact h i j hij

theorem Primitive.quasiPrimitive {A : Set ℕ} (hA : Primitive A) :
    QuasiPrimitive A := by
  intro m n d hm hn hd hmn _ hEq
  have hdm : d = m := hA hd hm (hEq ▸ Nat.gcd_dvd_left m n)
  have hdn : d ∣ n := hEq ▸ Nat.gcd_dvd_right m n
  exact hmn (hdm ▸ hdn)

/-- A recoding that reflects divisibility preserves primitivity.  This is
the abstract core used by many marker and prime-substitution constructions. -/
theorem Primitive.image_of_reflects_dvd {A : Set ℕ} {f : ℕ → ℕ}
    (hA : Primitive A)
    (hreflect : ∀ ⦃m n : ℕ⦄, m ∈ A → n ∈ A → f m ∣ f n → m ∣ n) :
    Primitive (f '' A) := by
  intro x y hx hy hdiv
  rcases hx with ⟨m, hm, rfl⟩
  rcases hy with ⟨n, hn, rfl⟩
  exact congrArg f (hA hm hn (hreflect hm hn hdiv))

/-- Existence of a primitive sequence obeying one uniform multiplicative deadline. -/
def HasPrimitiveDominator (b : ℕ → ℕ) : Prop :=
  ∃ (a : ℕ → ℕ) (C : ℕ), 0 < C ∧ StrictMono a ∧
    Primitive (Set.range a) ∧ ∀ n, a n ≤ C * b n

end Erdos892
