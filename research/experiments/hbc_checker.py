#!/usr/bin/env python3
"""Exact finite checker for the hybrid primitive-batch condition (HBC).

For a finite set B of positive integers, the program

* verifies historical quasi-primitivity;
* constructs all lower-cover choices in the induced divisibility poset;
* constructs all admissible immediate-shadow/type choices; and
* decides, by exhaustive depth-first search, whether at least one joint choice
  satisfies HBC.

There are no random or floating-point steps in the decision procedure.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, Iterable, Iterator, List, Optional, Sequence, Tuple


def prime_divisors(n: int) -> Tuple[int, ...]:
    ans: List[int] = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            ans.append(p)
            while n % p == 0:
                n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        ans.append(n)
    return tuple(ans)


def divides(x: int, y: int) -> bool:
    return y % x == 0


def incomparable(x: int, y: int) -> bool:
    return not divides(x, y) and not divides(y, x)


def is_primitive(values: Iterable[int]) -> bool:
    a = list(values)
    return all(not divides(a[i], a[j]) and not divides(a[j], a[i])
               for i in range(len(a)) for j in range(i + 1, len(a)))


def quasi_primitive_violations(B: Sequence[int]) -> List[Tuple[int, int, int]]:
    S = set(B)
    bad = []
    for i, x in enumerate(B):
        for y in B[i + 1:]:
            if incomparable(x, y):
                g = math.gcd(x, y)
                if g in S:
                    bad.append((x, y, g))
    return bad


def lower_covers(B: Sequence[int], b: int) -> Tuple[int, ...]:
    proper = [d for d in B if d != b and divides(d, b)]
    return tuple(d for d in proper
                 if not any(d != z and z != b and divides(d, z) and divides(z, b)
                            for z in B))


@dataclass(frozen=True)
class Choice:
    parent: int
    deleted_prime: int
    shadow: int
    typ: int


@dataclass(frozen=True)
class State:
    parent: Optional[int]
    deleted_prime: Optional[int]
    shadow: Optional[int]
    typ: Optional[int]
    word: Tuple[int, ...]
    core: int


def domains(B: Sequence[int]) -> Dict[int, Tuple[Choice, ...]]:
    answer: Dict[int, Tuple[Choice, ...]] = {}
    for b in B:
        opts: List[Choice] = []
        for d in lower_covers(B, b):
            e = b // d
            for p in prime_divisors(e):
                psi = e // p
                opts.append(Choice(d, p, psi, 0))
                if p >= 3:
                    opts.append(Choice(d, p, psi, 1))
        answer[b] = tuple(opts)
    return answer


class HBCChecker:
    def __init__(self, B: Iterable[int]):
        self.B = tuple(sorted(set(B)))
        if not self.B or self.B[0] < 1:
            raise ValueError("B must be a nonempty finite set of positive integers")
        bad = quasi_primitive_violations(self.B)
        if bad:
            raise ValueError(f"B is not quasi-primitive; first violation {bad[0]}")
        self.covers = {b: lower_covers(self.B, b) for b in self.B}
        self.roots = tuple(b for b in self.B if not self.covers[b])
        self.dom = domains(self.B)
        self.nodes = tuple(b for b in self.B if self.covers[b])
        self.visited = 0
        self.dead_ends = 0
        self.first_conflict: Optional[dict] = None

    @staticmethod
    def _batch_compatible(core: int, other: int) -> bool:
        return not divides(core, other) and not divides(other, core)

    def solve(self, fixed_parents: Optional[Dict[int, int]] = None,
              count_limit: Optional[int] = None) -> Tuple[Optional[Dict[int, State]], int]:
        """Return one HBC witness and the number of witnesses up to count_limit.

        If count_limit is None, stop after the first witness.  If it is positive,
        count all witnesses until that cap is reached.
        """
        # Diagnostics describe this solve call only, even when a checker is reused.
        self.visited = 0
        self.dead_ends = 0
        self.first_conflict = None
        fixed_parents = fixed_parents or {}
        for b, d in fixed_parents.items():
            if b not in self.dom or d not in self.covers[b]:
                raise ValueError(f"{d} is not a lower cover of {b}")

        states: Dict[int, State] = {
            r: State(None, None, None, None, (), r) for r in self.roots
        }
        # Same-word roots are automatically primitive because they are minimal.
        batches: Dict[Tuple[int, ...], List[Tuple[int, int]]] = {
            (): [(r, r) for r in self.roots]
        }
        local_pairs: Dict[int, set[Tuple[int, int]]] = {}
        witness: Optional[Dict[int, State]] = None
        count = 0

        def dfs(k: int) -> bool:
            nonlocal witness, count
            self.visited += 1
            if k == len(self.nodes):
                count += 1
                if witness is None:
                    witness = dict(states)
                if count_limit is None or count >= count_limit:
                    return True
                return False

            b = self.nodes[k]
            opts = self.dom[b]
            if b in fixed_parents:
                opts = tuple(o for o in opts if o.parent == fixed_parents[b])

            any_extension = False
            for o in opts:
                # Parent is smaller than child, hence already assigned.
                ps = states[o.parent]
                pair = (o.shadow, o.typ)
                used = local_pairs.setdefault(o.parent, set())
                if pair in used:
                    continue
                word = ps.word + (o.typ,)
                core = ps.core * o.shadow
                conflict = next(((u, c) for u, c in batches.get(word, [])
                                 if not self._batch_compatible(core, c)), None)
                if conflict is not None:
                    if self.first_conflict is None:
                        self.first_conflict = {
                            "new_node": b, "old_node": conflict[0],
                            "word": list(word), "new_core": core,
                            "old_core": conflict[1], "choice": o.__dict__,
                        }
                    continue

                any_extension = True
                states[b] = State(o.parent, o.deleted_prime, o.shadow, o.typ,
                                  word, core)
                used.add(pair)
                batches.setdefault(word, []).append((b, core))
                stop = dfs(k + 1)
                batches[word].pop()
                if not batches[word]:
                    del batches[word]
                used.remove(pair)
                del states[b]
                if stop:
                    return True

            if not any_extension:
                self.dead_ends += 1
            return False

        dfs(0)
        return witness, count

    def check_witness(self, states: Dict[int, State]) -> None:
        assert set(states) == set(self.B)
        for r in self.roots:
            assert states[r] == State(None, None, None, None, (), r)
        local: Dict[int, set] = {}
        batches: Dict[Tuple[int, ...], List[int]] = {}
        for b in self.B:
            s = states[b]
            if b not in self.roots:
                assert s.parent in self.covers[b]
                assert s.deleted_prime in prime_divisors(b // s.parent)
                assert s.shadow == (b // s.parent) // s.deleted_prime
                assert s.typ in (0, 1)
                assert (2 if s.typ == 0 else 3) <= s.deleted_prime
                assert (s.shadow, s.typ) not in local.setdefault(s.parent, set())
                local[s.parent].add((s.shadow, s.typ))
                ps = states[s.parent]
                assert s.word == ps.word + (s.typ,)
                assert s.core == ps.core * s.shadow
            batches.setdefault(s.word, []).append(s.core)
        assert all(is_primitive(v) for v in batches.values())

    def serialise_witness(self, states: Optional[Dict[int, State]]) -> Optional[dict]:
        if states is None:
            return None
        return {str(b): {
            "parent": s.parent, "deleted_prime": s.deleted_prime,
            "shadow": s.shadow, "type": s.typ,
            "word": "".join(map(str, s.word)), "core": s.core,
        } for b, s in sorted(states.items())}


def exponent_grid(primes: Sequence[int], max_exponents: Sequence[int],
                  include_zero: bool = True) -> List[int]:
    ranges = [range(m + 1) for m in max_exponents]
    ans = []
    for a in itertools.product(*ranges):
        if not include_zero and not any(a):
            continue
        ans.append(math.prod(p ** e for p, e in zip(primes, a)))
    return sorted(ans)


def all_quasi_primitive_subsets(universe: Sequence[int], min_size: int = 1,
                                max_size: Optional[int] = None) -> Iterator[Tuple[int, ...]]:
    """Enumerate all quasi-primitive subsets, intended only for small universes."""
    U = tuple(sorted(set(universe)))
    max_size = len(U) if max_size is None else min(max_size, len(U))
    for k in range(min_size, max_size + 1):
        for B in itertools.combinations(U, k):
            if not quasi_primitive_violations(B):
                yield B


def random_quasi_primitive_subsets(universe: Sequence[int], trials: int,
                                   seed: int, target_size: Optional[int] = None
                                   ) -> Iterator[Tuple[int, ...]]:
    rng = random.Random(seed)
    U = tuple(sorted(set(universe)))
    for _ in range(trials):
        order = list(U)
        rng.shuffle(order)
        B: List[int] = []
        for x in order:
            if target_size is not None and len(B) >= target_size:
                break
            candidate = sorted(B + [x])
            if not quasi_primitive_violations(candidate) and rng.random() < 0.72:
                B.append(x)
        if B:
            yield tuple(sorted(B))


def parse_int_list(text: str) -> List[int]:
    return [int(x) for x in text.replace(",", " ").split()]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("B", nargs="?", help="comma/space separated finite set")
    ap.add_argument("--fixed-parents", help="JSON object child->parent")
    ap.add_argument("--count", type=int, help="count witnesses up to this cap")
    args = ap.parse_args()
    if not args.B:
        ap.error("provide B, e.g. '1,16,22,32,36,572,576,704,1080'")
    B = parse_int_list(args.B)
    fixed = ({int(k): int(v) for k, v in json.loads(args.fixed_parents).items()}
             if args.fixed_parents else None)
    checker = HBCChecker(B)
    witness, count = checker.solve(fixed, args.count)
    if witness is not None:
        checker.check_witness(witness)
    print(json.dumps({
        "B": checker.B,
        "quasi_primitive": True,
        "roots": checker.roots,
        "covers": {str(k): v for k, v in checker.covers.items()},
        "domain_sizes": {str(k): len(v) for k, v in checker.dom.items()},
        "satisfiable": witness is not None,
        "witness_count_at_cap": count,
        "visited_nodes": checker.visited,
        "dead_ends": checker.dead_ends,
        "witness": checker.serialise_witness(witness),
        "first_rejected_conflict": checker.first_conflict,
    }, indent=2))


if __name__ == "__main__":
    main()
