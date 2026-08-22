#!/usr/bin/env python3
"""Reproduce the finite computations in research/q2-actual-union.md.

All output is evidence only.  The MILP uses every divisibility pair, hence models finite
primitive sets exactly, but this script does not emit independently checkable solver certificates.
"""

from __future__ import annotations

import itertools
import math

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def gamma_milp(exponents: list[int], time_limit: float = 30.0):
    """Compute the finite compactness parameter Gamma for a small exponent list."""
    n_max = 2 ** exponents[-1]
    rows: list[int] = []
    cols: list[int] = []
    vals: list[float] = []
    lower: list[float] = []
    upper: list[float] = []
    row = 0

    for a in range(1, n_max // 2 + 1):
        for b in range(2 * a, n_max + 1, a):
            rows.extend((row, row))
            cols.extend((a - 1, b - 1))
            vals.extend((1.0, 1.0))
            lower.append(-np.inf)
            upper.append(1.0)
            row += 1

    for exponent in exponents:
        cutoff = 2**exponent
        rows.extend([row] * (cutoff + 1))
        cols.extend(range(cutoff))
        cols.append(n_max)  # the continuous variable t
        vals.extend([-1.0] * cutoff)
        vals.append(float(cutoff))
        lower.append(-np.inf)
        upper.append(0.0)
        row += 1

    matrix = coo_matrix(
        (vals, (rows, cols)), shape=(row, n_max + 1)
    ).tocsr()
    objective = np.zeros(n_max + 1)
    objective[-1] = -1.0
    integrality = np.ones(n_max + 1)
    integrality[-1] = 0
    result = milp(
        objective,
        integrality=integrality,
        bounds=Bounds(np.zeros(n_max + 1), np.ones(n_max + 1)),
        constraints=LinearConstraint(matrix, lower, upper),
        options={"time_limit": time_limit, "mip_rel_gap": 0.0},
    )
    if result.x is None:
        return None, None, result.message
    chosen = np.rint(result.x[:-1]).astype(np.int8)
    counts = [int(chosen[: 2**exponent].sum()) for exponent in exponents]
    return float(result.x[-1]), counts, result.message


def odd_window_generators(gap: int, blocks: int, phase: float = 0.0):
    generators: list[int] = []
    for h in range(1, blocks + 1):
        left = 2 ** (h * gap + phase - 1)
        right = 2 ** (h * gap + phase)
        first = max(3, math.floor(left) + 1)
        if first % 2 == 0:
            first += 1
        generators.extend(range(first, math.floor(right) + 1, 2))
    return generators


def exact_avoidance(y: int, generators: list[int]):
    low = y // 2 + 1
    hit = np.zeros(y - low + 1, dtype=np.bool_)
    for divisor in generators:
        first = ((low + divisor - 1) // divisor) * divisor
        if first % 2 == 0:
            first += divisor
        if first <= y:
            hit[first - low :: 2 * divisor] = True
    values = np.arange(low, y + 1)
    odd = values % 2 == 1
    return float((~hit[odd]).mean())


def bonferroni_values(y: int, generators: list[int], orders=(2, 4, 6, 8)):
    odd_values = [r for r in range(y // 2 + 1, y + 1) if r % 2]
    exact = sum(all(r % a for a in generators) for r in odd_values) / len(odd_values)
    output = []
    for order in orders:
        model = 1.0
        actual = 1.0
        for size in range(1, order + 1):
            model_sum = 0.0
            actual_sum = 0.0
            for subset in itertools.combinations(generators, size):
                lcm = 1
                for item in subset:
                    lcm = math.lcm(lcm, item)
                model_sum += 1.0 / lcm
                actual_sum += sum(r % lcm == 0 for r in odd_values) / len(odd_values)
            sign = -1.0 if size % 2 else 1.0
            model += sign * model_sum
            actual += sign * actual_sum
        output.append((order, model, actual))
    return exact, output


def omega_sieve(limit: int):
    omega = np.zeros(limit + 1, dtype=np.int16)
    for prime in range(2, limit + 1):
        if omega[prime] != 0:
            continue
        for multiple in range(prime, limit + 1, prime):
            residual = multiple
            while residual % prime == 0:
                omega[multiple] += 1
                residual //= prime
    return omega


def rank_pool(exponent: int, kind: str, omega: np.ndarray):
    x = 2**exponent
    mean = math.log(math.log(x))
    sigma = math.sqrt(mean)
    values = np.arange(x // 2 + 1, x + 1, 2)
    if kind == "half":
        mask = omega[values] >= math.ceil(mean)
    elif kind == "band":
        mask = (omega[values] >= math.ceil(mean - 0.65 * sigma)) & (
            omega[values] <= math.floor(mean + 0.65 * sigma)
        )
    else:
        raise ValueError(kind)
    return values[mask]


def rank_band_toy():
    terminal_exponent = 20
    source_exponents = [8, 12, 16]
    limit = 2**terminal_exponent
    omega = omega_sieve(limit)
    rows = []
    for kind in ("half", "band"):
        terminal = rank_pool(terminal_exponent, kind, omega)
        hit = np.zeros(limit + 1, dtype=np.bool_)
        for exponent in source_exponents:
            for divisor in rank_pool(exponent, kind, omega):
                hit[divisor : limit + 1 : divisor] = True
        rows.append((kind, len(terminal), int(hit[terminal].sum()), float(hit[terminal].mean())))
    return rows


def main():
    print("Finite Gamma MILPs")
    for exponents in ([2], [2, 5], [2, 5, 9], [2, 5, 9, 12], [2, 4, 7, 10]):
        gamma, counts, message = gamma_milp(list(exponents))
        print(exponents, "Gamma=", gamma, "counts=", counts, "status=", message)

    print("\nShifted-block toy, gap=2, phase=0")
    for blocks in range(1, 6):
        y = 2 ** (2 * (blocks + 2))
        generators = odd_window_generators(2, blocks)
        print("H=", blocks, "Y=", y, "avoidance=", exact_avoidance(y, generators))

    print("\nBonferroni toy")
    y = 2048
    generators = odd_window_generators(2, 3)
    exact, rows = bonferroni_values(y, generators)
    print("Y=", y, "generators=", len(generators), "exact=", exact)
    for order, model, actual in rows:
        print("order=", order, "model=", model, "actual_partial=", actual)

    print("\nRank-band toy")
    for row in rank_band_toy():
        print("kind=", row[0], "terminal_size=", row[1], "hit=", row[2], "fraction=", row[3])


if __name__ == "__main__":
    main()

