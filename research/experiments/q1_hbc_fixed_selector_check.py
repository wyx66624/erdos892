#!/usr/bin/env python3
"""Check the finite fixed-selector HBC barrier and its repaired selector."""

from itertools import product
from math import prod


B_STAR = (1, 16, 22, 32, 36, 572, 576, 704, 1080)
BAD_SELECTOR = {
    16: 1,
    22: 1,
    36: 1,
    32: 16,
    572: 22,
    576: 36,
    704: 22,
    1080: 36,
}
REPAIRED_SELECTOR = BAD_SELECTOR | {576: 32, 704: 32}


def prime_divisors(n: int) -> tuple[int, ...]:
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            result.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result.append(n)
    return tuple(result)


def lower_covers(b: int) -> tuple[int, ...]:
    divisors = [d for d in B_STAR if d < b and b % d == 0]
    return tuple(
        d
        for d in divisors
        if not any(d < z < b and z % d == 0 and b % z == 0 for z in B_STAR)
    )


def admissible_options(b: int, parent: int) -> tuple[tuple[int, int, int], ...]:
    quotient = b // parent
    result = []
    for deleted_prime in prime_divisors(quotient):
        shadow = quotient // deleted_prime
        result.append((shadow, 0, deleted_prime))
        if deleted_prime >= 3:
            result.append((shadow, 1, deleted_prime))
    return tuple(result)


def local_injective(
    selector: dict[int, int], choices: dict[int, tuple[int, int, int]]
) -> bool:
    for parent in set(selector.values()):
        pairs = [
            choices[b][:2] for b in selector if selector[b] == parent
        ]
        if len(pairs) != len(set(pairs)):
            return False
    return True


def word_and_core(
    b: int,
    selector: dict[int, int],
    choices: dict[int, tuple[int, int, int]],
) -> tuple[tuple[int, ...], int]:
    types = []
    shadows = []
    current = b
    while current in selector:
        shadow, type_bit, _ = choices[current]
        types.append(type_bit)
        shadows.append(shadow)
        current = selector[current]
    core = current
    for shadow in reversed(shadows):
        core *= shadow
    return tuple(reversed(types)), core


def hbc(
    selector: dict[int, int], choices: dict[int, tuple[int, int, int]]
) -> tuple[bool, dict[tuple[int, ...], tuple[int, ...]]]:
    if not local_injective(selector, choices):
        return False, {}
    batches: dict[tuple[int, ...], list[int]] = {}
    for b in B_STAR:
        word, core = word_and_core(b, selector, choices)
        batches.setdefault(word, []).append(core)
    for values in batches.values():
        for i, x in enumerate(values):
            for y in values[i + 1 :]:
                if x % y == 0 or y % x == 0:
                    return False, {k: tuple(v) for k, v in batches.items()}
    return True, {k: tuple(v) for k, v in batches.items()}


def main() -> None:
    assert all(B_STAR.count(x) == 1 for x in B_STAR)
    assert all(
        parent in lower_covers(b) for b, parent in BAD_SELECTOR.items()
    )
    expected_gcds = {2, 4, 8, 44, 64, 72}
    incomparable_gcds = set()
    from math import gcd

    for i, x in enumerate(B_STAR):
        for y in B_STAR[i + 1 :]:
            if x % y != 0 and y % x != 0:
                incomparable_gcds.add(gcd(x, y))
    assert incomparable_gcds == expected_gcds
    assert incomparable_gcds.isdisjoint(B_STAR)

    nodes = tuple(BAD_SELECTOR)
    option_lists = tuple(
        admissible_options(b, BAD_SELECTOR[b]) for b in nodes
    )
    assert prod(map(len, option_lists)) == 135
    locally_admissible = 0
    hbc_count = 0
    for values in product(*option_lists):
        choices = dict(zip(nodes, values))
        if local_injective(BAD_SELECTOR, choices):
            locally_admissible += 1
            hbc_count += int(hbc(BAD_SELECTOR, choices)[0])
    assert locally_admissible == 135
    assert hbc_count == 0

    repaired_choices = {
        16: (8, 0, 2),
        22: (11, 0, 2),
        36: (18, 0, 2),
        32: (1, 0, 2),
        572: (13, 0, 2),
        576: (9, 0, 2),
        704: (11, 0, 2),
        1080: (15, 0, 2),
    }
    assert all(
        REPAIRED_SELECTOR[b] in lower_covers(b) for b in REPAIRED_SELECTOR
    )
    assert all(
        choice in admissible_options(b, REPAIRED_SELECTOR[b])
        for b, choice in repaired_choices.items()
    )
    repaired_ok, batches = hbc(REPAIRED_SELECTOR, repaired_choices)
    assert repaired_ok
    assert batches == {
        (): (1,),
        (0,): (8, 11, 18),
        (0, 0): (8, 143, 270),
        (0, 0, 0): (72, 88),
    }

    print(f"fixed_selector_choices={prod(map(len, option_lists))}")
    print(f"fixed_selector_hbc_choices={hbc_count}")
    print(f"repaired_batches={batches}")


if __name__ == "__main__":
    main()
