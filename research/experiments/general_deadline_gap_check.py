#!/usr/bin/env python3
"""Deterministic certificate checker for the P_15 deadline integrality gap."""

from fractions import Fraction
from itertools import combinations


DEADLINES = (3, 5, 7, 9, 11, 13, 15)
A0 = (2, 3, 5, 7, 11, 13)
A1 = (4, 6, 7, 9, 10, 11, 13, 15)
CHAINS = (
    (1, 3, 6),
    (1, 2, 4, 8),
    (1, 3, 9),
    (1, 5, 10),
    (11,),
    (1, 2, 4, 12),
    (1, 13),
    (1, 7, 14),
    (5, 15),
)


def is_antichain(values: tuple[int, ...]) -> bool:
    return all(y % x != 0 for x, y in combinations(values, 2))


def counts(values: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(x <= deadline for x in values) for deadline in DEADLINES)


def margin(values: tuple[int, ...]) -> Fraction:
    c = counts(values)
    return min(Fraction(c[i], i + 1) for i in range(len(DEADLINES)))


def all_antichains() -> list[tuple[int, ...]]:
    result = []
    for mask in range(1 << 15):
        values = tuple(i + 1 for i in range(15) if mask & (1 << i))
        if is_antichain(values):
            result.append(values)
    return result


def main() -> None:
    antichains = all_antichains()
    assert len(antichains) == 1133
    assert is_antichain(A0) and is_antichain(A1)

    integer_margin = max(map(margin, antichains))
    assert integer_margin == Fraction(6, 7)

    c0, c1 = counts(A0), counts(A1)
    expected = tuple(Fraction(x + y, 2) for x, y in zip(c0, c1))
    assert all(expected[i] >= i + 1 for i in range(7))

    for chain in CHAINS:
        assert all(y % x == 0 for x, y in zip(chain, chain[1:]))
    coverage = tuple(sum(m in chain for chain in CHAINS) for m in range(1, 16))
    assert coverage == (7, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    weighted_max = max(counts(a)[1] + counts(a)[6] for a in antichains)
    assert weighted_max == 9
    assert all(counts(a)[1] + counts(a)[6] <= 9 for a in antichains)

    print(f"antichains={len(antichains)}")
    print(f"integer_rho={integer_margin}")
    print(f"A0_counts={c0}")
    print(f"A1_counts={c1}")
    print(f"half_mixture={expected}")
    print(f"chain_coverage={coverage}")
    print("fractional_rho=1 (half-mixture lower bound; nine-chain upper bound)")


if __name__ == "__main__":
    main()
