"""Finite example checks for Chapter 03/04; no live cluster is contacted.

Run: python tools/verify-coordination-p2p.py
Only the Python standard library is needed.
"""

from itertools import combinations, product
from math import exp, isclose


def verify_coordination():
    assert 4 // 2 + 1 == 3  # P78: leader + three voting followers.
    assert 3 // 2 + 1 == 2
    version, data = 4, 10
    expected_a, expected_b = 4, 4
    assert expected_a == version
    version, data = version + 1, 11
    assert expected_b != version  # B must reread; no silent overwrite.
    assert (version, data) == (5, 11)

    # Every nonempty subset of requests has a unique queue minimum.
    ids = [1, 2, 3, 4]
    for size in range(1, len(ids) + 1):
        for queue in combinations(ids, size):
            holders = [n for n in queue if n == min(queue)]
            assert len(holders) == 1
            watches = {n: queue[i - 1] for i, n in enumerate(queue) if i > 0}
            assert sum(p == min(queue) for p in watches.values()) <= 1

    # Deletion between listing and exists: absent means retry, not waiting.
    queue = [1, 2, 3]
    predecessor = queue[queue.index(2) - 1]
    queue.remove(1)
    exists_result = predecessor in queue
    assert not exists_result and min(queue) == 2
    # Deletion after watch registration: retain signal even before local wait.
    watch_armed, signalled = True, False
    if watch_armed:
        signalled = True
        watch_armed = False
    assert signalled
    # Storage accepts generation 42, then rejects a delayed 41.
    greatest = 42
    assert 41 < greatest
    assert not (42 < greatest)
    print("PASS: quorum count, CAS, 15 lock queues, predecessor races and fencing example")


def verify_gossip():
    push, pull = .9, .9
    expected = [
        (.900000, .900000), (.814354, .810000), (.676376, .656100),
        (.489373, .430467), (.293682, .185302), (.144919, .034337),
        (.061627, .001179),
    ]
    for p, q in expected:
        assert round(push, 6) == p and round(pull, 6) == q
        push, pull = push * exp(push - 1), pull * pull
    # Enumerate all partner selections for one finite round, not an approximation.
    for n in range(2, 6):
        for susceptible in range(1, n):
            susceptible_ids = set(range(susceptible))
            infective_ids = set(range(susceptible, n))
            push_outcomes = list(product(range(n), repeat=n - susceptible))
            push_mean = sum(len(susceptible_ids - set(targets)) for targets in push_outcomes) / len(push_outcomes)
            assert isclose(push_mean, susceptible * (1 - 1 / n) ** (n - susceptible))
            pull_outcomes = list(product(range(n), repeat=susceptible))
            pull_mean = sum(sum(target not in infective_ids for target in targets)
                            for targets in pull_outcomes) / len(pull_outcomes)
            assert isclose(pull_mean, susceptible * susceptible / n)
    assert isclose(.9 * (.99 ** 10), .813943867507924)
    rounds = [[("A", "B")], [("A", "C"), ("B", "D")],
              [("A", "B"), ("B", "E"), ("C", "F"), ("D", "A")]]
    known = {"A"}
    for exchanges in rounds:
        assert all(sender in known for sender, _ in exchanges)
        known |= {target for _, target in exchanges}
    assert known == set("ABCDEF")
    print("PASS: seven-row Gossip table, exact finite-round expectations, six-node dissemination")


def verify_can():
    # Half-open rectangles; D is split into D and J at x=.75.
    before = [("A", 0, .5, 0, .5), ("B", .5, 1, 0, .5),
              ("C", 0, .5, .5, 1), ("D", .5, 1, .5, 1)]
    after = before[:-1] + [("D", .5, .75, .5, 1), ("J", .75, 1, .5, 1)]

    def owners(zones, point):
        x, y = point
        return [name for name, lo, hi, bottom, top in zones if lo <= x < hi and bottom <= y < top]

    assert owners(before, (.8, .6)) == ["D"]
    assert owners(after, (.8, .6)) == ["J"]
    assert sum((hi - lo) * (top - bottom) for _, lo, hi, bottom, top in after) == 1
    for point in product([i / 20 for i in range(20)], repeat=2):
        assert len(owners(after, point)) == 1
    assert owners(after, (.75, .5)) == ["J"]
    print("PASS: CAN split, area conservation and 400 coordinate ownership checks")


def verify_chord():
    nodes, modulus = [0, 10, 20, 32, 45, 55], 64

    def owner(k, ring=nodes):
        return next((n for n in ring if n >= k), ring[0])

    fingers = {n: [owner((n + 2 ** i) % modulus) for i in range(6)] for n in nodes}
    assert fingers[0] == [10, 10, 10, 10, 20, 32]
    assert fingers[32] == [45, 45, 45, 45, 55, 0]

    def distance(a, b):
        return (b - a) % modulus

    def route(start, k):
        current, visited = start, [start]
        while current != k:
            successor = nodes[(nodes.index(current) + 1) % len(nodes)]
            if 0 < distance(current, k) <= distance(current, successor):
                visited.append(successor)
                return successor, visited
            candidates = [n for n in fingers[current] if 0 < distance(current, n) < distance(current, k)]
            current = max(candidates, key=lambda n: distance(visited[-1], n)) if candidates else successor
            assert current not in visited, (start, k, visited)
            visited.append(current)
            assert len(visited) <= len(nodes)
        return current, visited

    for start, k in product(nodes, range(modulus)):
        found, _ = route(start, k)
        assert found == owner(k), (start, k, found)
    assert route(0, 42) == (45, [0, 32, 45])
    assert route(45, 60) == (0, [45, 55, 0])
    # Original single-join example: 10 asks 20 for its newly updated predecessor.
    successor, predecessor = {10: 20, 15: 20}, {20: 10, 15: None}
    predecessor[20] = 15
    x = predecessor[successor[10]]
    assert 10 < x < successor[10]
    successor[10] = x
    predecessor[15] = 10
    assert (successor[10], predecessor[15], successor[15]) == (15, 10, 20)
    moved = [k for k in range(64) if owner(k) != owner(k, sorted(nodes + [15]))]
    assert moved == list(range(11, 16))
    print("PASS: Chord fingers, 384 lookups, wraparound, single join and transferred keys")


if __name__ == "__main__":
    verify_coordination()
    verify_gossip()
    verify_can()
    verify_chord()
    print("Finite examples passed; no live cluster, full protocol proof or arbitrary churn test.")
