#!/usr/bin/env python3
"""Reproducible Cartesian-product cross-check of ``HBCChecker.solve``.

Candidate generation is seeded.  For every retained finite quasi-primitive set,
the script compares the DFS solver with a separate evaluator that iterates the raw
Cartesian product of all node domains and tests a completed assignment directly.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random

from hbc_checker import (
    HBCChecker,
    State,
    exponent_grid,
    is_primitive,
    quasi_primitive_violations,
)


def cartesian_satisfiable(checker, raw_cap):
    """Return (decision, raw assignments examined) by direct product enumeration."""
    nodes = checker.nodes
    domain_product = math.prod(len(checker.dom[b]) for b in nodes)
    if domain_product > raw_cap:
        raise ValueError(f"raw domain product {domain_product} exceeds cap {raw_cap}")

    examined = 0
    for values in itertools.product(*(checker.dom[b] for b in nodes)):
        examined += 1
        choices = dict(zip(nodes, values))

        local_pairs = {}
        locally_valid = True
        for b in nodes:
            option = choices[b]
            pair = (option.shadow, option.typ)
            used = local_pairs.setdefault(option.parent, set())
            if pair in used:
                locally_valid = False
                break
            used.add(pair)
        if not locally_valid:
            continue

        states = {
            r: State(None, None, None, None, (), r) for r in checker.roots
        }
        for b in nodes:
            option = choices[b]
            parent_state = states[option.parent]
            states[b] = State(
                option.parent,
                option.deleted_prime,
                option.shadow,
                option.typ,
                parent_state.word + (option.typ,),
                parent_state.core * option.shadow,
            )

        batches = {}
        for state in states.values():
            batches.setdefault(state.word, []).append(state.core)
        if all(is_primitive(cores) for cores in batches.values()):
            return True, examined

    return False, examined


def candidate_stream(seed, trials):
    """Yield deterministic structured candidates with many divisibility relations."""
    rng = random.Random(seed)
    universe = exponent_grid((2, 3, 5), (3, 3, 2))
    for _ in range(trials):
        target = rng.randint(4, 10)
        order = list(universe)
        rng.shuffle(order)
        B = []
        for value in order:
            if len(B) >= target:
                break
            if rng.random() > 0.72:
                continue
            trial = tuple(sorted(B + [value]))
            if not quasi_primitive_violations(trial):
                B.append(value)
        if B:
            yield tuple(sorted(B))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=8922026)
    parser.add_argument("--samples", type=int, default=150)
    parser.add_argument("--raw-cap", type=int, default=200000)
    parser.add_argument("--generation-trials", type=int, default=100000)
    args = parser.parse_args()

    seen = set()
    retained = 0
    generated = 0
    disagreements = []
    total_raw_examined = 0
    maximum_domain_product = 0
    satisfiable_count = 0

    for B in candidate_stream(args.seed, args.generation_trials):
        generated += 1
        if B in seen:
            continue
        seen.add(B)
        checker = HBCChecker(B)
        if len(checker.nodes) < 2:
            continue
        domain_product = math.prod(len(checker.dom[b]) for b in checker.nodes)
        if domain_product > args.raw_cap:
            continue

        dfs_witness, _ = checker.solve()
        dfs_decision = dfs_witness is not None
        cartesian_decision, examined = cartesian_satisfiable(checker, args.raw_cap)
        retained += 1
        total_raw_examined += examined
        maximum_domain_product = max(maximum_domain_product, domain_product)
        satisfiable_count += int(dfs_decision)
        if dfs_decision != cartesian_decision:
            disagreements.append({
                "B": B,
                "domain_product": domain_product,
                "dfs": dfs_decision,
                "cartesian": cartesian_decision,
            })
        if retained == args.samples:
            break

    if retained != args.samples:
        raise RuntimeError(
            f"retained only {retained} samples after {generated} generated candidates"
        )

    print(json.dumps({
        "seed": args.seed,
        "requested_samples": args.samples,
        "retained_samples": retained,
        "generated_candidates_examined": generated,
        "raw_assignment_cap_per_sample": args.raw_cap,
        "maximum_retained_domain_product": maximum_domain_product,
        "total_cartesian_assignments_examined": total_raw_examined,
        "satisfiable_samples": satisfiable_count,
        "unsatisfiable_samples": retained - satisfiable_count,
        "decision_disagreements": disagreements,
        "all_decisions_agree": not disagreements,
    }, indent=2))


if __name__ == "__main__":
    main()
