#!/usr/bin/env python3
"""Reproducible finite searches for universal HBC counterexamples.

This script imports the exact solver in hbc_checker.py.  The ``exact`` profile
exhausts every quasi-primitive subset of several explicitly listed universes.
The ``random`` profile performs deterministic seeded searches of larger grids.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import time

from hbc_checker import HBCChecker, exponent_grid, incomparable, quasi_primitive_violations


def forbidden_triples(universe):
    pos = {x: i for i, x in enumerate(universe)}
    bad = []
    for i, x in enumerate(universe):
        for j in range(i + 1, len(universe)):
            y = universe[j]
            g = math.gcd(x, y)
            if incomparable(x, y) and g in pos:
                bad.append((1 << i) | (1 << j) | (1 << pos[g]))
    return bad


def numeric_min_selector(checker):
    return {b: min(checker.covers[b]) for b in checker.nodes}


def max_height_selector(checker):
    """Choose a cover lying on a longest root-to-node chain; break ties by value."""
    height = {}
    for b in checker.B:
        height[b] = (0 if not checker.covers[b]
                     else 1 + max(height[d] for d in checker.covers[b]))
    return {
        b: min(d for d in checker.covers[b]
               if height[d] == max(height[e] for e in checker.covers[b]))
        for b in checker.nodes
    }


def chosen_selector(checker, selector_mode):
    if selector_mode == "existential":
        return None
    if selector_mode == "numeric-min":
        return numeric_min_selector(checker)
    if selector_mode == "max-height":
        return max_height_selector(checker)
    raise ValueError(selector_mode)


def exhaustive_universe(name, universe, selector_mode="existential",
                        global_seen=None):
    universe = tuple(sorted(set(universe)))
    bad = forbidden_triples(universe)
    start = time.time()
    checked = 0
    hardest = (0, ())
    for mask in range(1, 1 << len(universe)):
        if any(mask & triple == triple for triple in bad):
            continue
        B = tuple(universe[i] for i in range(len(universe)) if mask >> i & 1)
        if global_seen is not None:
            global_seen.add(B)
        checker = HBCChecker(B)
        witness, _ = checker.solve(chosen_selector(checker, selector_mode))
        checked += 1
        if witness is None:
            return {
                "name": name, "selector_mode": selector_mode,
                "universe": universe, "checked": checked,
                "counterexample": B, "visited": checker.visited,
                "seconds": time.time() - start,
            }
        if checker.visited > hardest[0]:
            hardest = (checker.visited, B)
    return {
        "name": name, "selector_mode": selector_mode,
        "universe": universe, "checked": checked,
        "counterexample": None,
        "hardest_first-witness_search": {
            "visited": hardest[0], "B": hardest[1],
        },
        "seconds": time.time() - start,
    }


def greedy_random_sets(universe, trials, seed, base=(), min_target=12, max_target=22):
    rng = random.Random(seed)
    universe = tuple(sorted(set(universe) - set(base)))
    for _ in range(trials):
        target = rng.randint(min_target, max_target)
        order = list(universe)
        rng.shuffle(order)
        B = list(base)
        for x in order:
            if len(B) >= target:
                break
            if rng.random() <= 0.72 and not quasi_primitive_violations(sorted(B + [x])):
                B.append(x)
        yield tuple(sorted(B))


def random_universe(name, universe, trials, seed, base=(), targets=(12, 22),
                    selector_mode="existential", global_seen=None):
    start = time.time()
    seen = set()
    hardest = (0, ())
    for B in greedy_random_sets(universe, trials, seed, base, *targets):
        if not B or B in seen:
            continue
        seen.add(B)
        if global_seen is not None:
            global_seen.add(B)
        checker = HBCChecker(B)
        witness, _ = checker.solve(chosen_selector(checker, selector_mode))
        if witness is None:
            return {
                "name": name, "selector_mode": selector_mode,
                "seed": seed, "trials": trials,
                "unique_checked": len(seen), "counterexample": B,
                "visited": checker.visited, "seconds": time.time() - start,
            }
        if checker.visited > hardest[0]:
            hardest = (checker.visited, B)
    return {
        "name": name, "selector_mode": selector_mode,
        "seed": seed, "trials": trials,
        "unique_checked": len(seen), "counterexample": None,
        "hardest_first-witness_search": {
            "visited": hardest[0], "B": hardest[1],
        },
        "seconds": time.time() - start,
    }


def fixed_selector_minimal_example():
    B = (2, 3, 4, 12)
    checker = HBCChecker(B)
    fixed = numeric_min_selector(checker)
    witness, count = checker.solve(fixed, count_limit=1)
    repaired, _ = checker.solve()
    return {
        "B": B, "fixed_parents": fixed,
        "fixed_satisfiable": witness is not None,
        "fixed_witness_count": count,
        "joint_satisfiable": repaired is not None,
        "joint_witness": checker.serialise_witness(repaired),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--profile", choices=("exact", "random", "all"), default="exact")
    ap.add_argument("--random-trials", type=int, default=100000)
    ap.add_argument("--seed-offset", type=int, default=0,
                    help="add this integer to each documented random seed")
    ap.add_argument("--selector-mode",
                    choices=("existential", "numeric-min", "max-height"),
                    default="existential",
                    help="fix a canonical selector or jointly optimize it")
    args = ap.parse_args()
    result = {"fixed_selector_test": fixed_selector_minimal_example(), "searches": []}
    if args.profile in ("exact", "all"):
        exact_global_seen = set()
        exact_results = [
            exhaustive_universe("interval-1-22", range(1, 23), args.selector_mode,
                                exact_global_seen),
            exhaustive_universe("grid-2^a3^b-a<=5-b<=3",
                                exponent_grid((2, 3), (5, 3)), args.selector_mode,
                                exact_global_seen),
            exhaustive_universe("grid-2^a3^b5^c-a,b<=2-c<=1",
                                exponent_grid((2, 3, 5), (2, 2, 1)),
                                args.selector_mode, exact_global_seen),
        ]
        result["searches"].extend(exact_results)
        exact_sum = sum(row["checked"] for row in exact_results)
        result["exact_count_summary"] = {
            "per_universe_check_sum": exact_sum,
            "globally_distinct_nonempty_sets": len(exact_global_seen),
            "cross_universe_duplicate_checks": exact_sum - len(exact_global_seen),
        }
    if args.profile in ("random", "all"):
        random_global_seen = set()
        suites = [
            ("random-grid-2^a3^b-a,b<=5", exponent_grid((2, 3), (5, 5)), 89201 + args.seed_offset),
            ("random-grid-2^a3^b5^c-3,3,2", exponent_grid((2, 3, 5), (3, 3, 2)), 89202 + args.seed_offset),
            ("random-grid-2^a3^b5^c-4,2,2", exponent_grid((2, 3, 5), (4, 2, 2)), 89203 + args.seed_offset),
            ("random-grid-2^a3^b5^c7^d-2,2,1,1",
             exponent_grid((2, 3, 5, 7), (2, 2, 1, 1)), 89204 + args.seed_offset),
        ]
        random_results = list(
            random_universe(name, universe, args.random_trials, seed,
                            targets=(10, 22), selector_mode=args.selector_mode,
                            global_seen=random_global_seen)
            for name, universe, seed in suites
        )
        result["searches"].extend(random_results)
        base = (1, 16, 22, 32, 36, 572, 576, 704, 1080)
        pool = [x for x in range(1, 2001)
                if x in base or not quasi_primitive_violations(sorted(base + (x,)))]
        bstar_result = (
            random_universe("random-quasi-primitive-supersets-of-B_star-up-to-2000",
                            pool, args.random_trials, 89205 + args.seed_offset,
                            base=base,
                            targets=(12, 24), selector_mode=args.selector_mode,
                            global_seen=random_global_seen)
        )
        result["searches"].append(bstar_result)
        random_results.append(bstar_result)
        random_sum = sum(row["unique_checked"] for row in random_results)
        result["random_count_summary"] = {
            "within_suite_distinct_check_sum": random_sum,
            "globally_distinct_sets": len(random_global_seen),
            "cross_suite_duplicate_checks": random_sum - len(random_global_seen),
        }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
