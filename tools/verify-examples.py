"""Check finite teaching examples, not complete protocol implementations.

Run from the repository root: python tools/verify-examples.py
No third-party dependency is required.
"""

from itertools import combinations, product


def verify_clocks():
    # P24/P26: preserve process order and all four send/receive dependencies.
    events = [
        (0, "local", None), (1, "local", None), (2, "local", None),
        (0, "send", "a"), (1, "recv", "a"), (0, "local", None),
        (1, "send", "b"), (1, "local", None), (2, "recv", "b"),
        (2, "local", None), (2, "send", "c"), (0, "recv", "c"),
        (0, "send", "d"), (1, "recv", "d"), (1, "local", None),
    ]
    scalar, vector = [0] * 3, [[0] * 3 for _ in range(3)]
    scalar_history, vector_history = [[] for _ in range(3)], [[] for _ in range(3)]
    messages, histories, recorded = {}, [set() for _ in range(3)], []
    for eid, (p, kind, mid) in enumerate(events):
        if kind == "recv":
            timestamp, v, ancestors = messages[mid]
            scalar[p] = max(scalar[p], timestamp)
            vector[p] = [max(a, b) for a, b in zip(vector[p], v)]
            histories[p] |= ancestors
        scalar[p] += 1
        vector[p][p] += 1
        histories[p].add(eid)
        if kind == "send":
            messages[mid] = scalar[p], vector[p].copy(), histories[p].copy()
        scalar_history[p].append(scalar[p])
        vector_history[p].append(vector[p].copy())
        recorded.append((eid, scalar[p], vector[p].copy(), histories[p].copy()))
    assert scalar_history == [[1, 2, 3, 8, 9], [1, 3, 4, 5, 10, 11], [1, 5, 6, 7]]
    assert vector_history == [
        [[1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 3, 4], [5, 3, 4]],
        [[0, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [5, 5, 4], [5, 6, 4]],
        [[0, 0, 1], [2, 3, 2], [2, 3, 3], [2, 3, 4]],
    ]
    # Compare vectors against independently accumulated event ancestry.
    for a, b in product(recorded, repeat=2):
        hb = a[0] != b[0] and a[0] in b[3]
        lt = a[2] != b[2] and all(x <= y for x, y in zip(a[2], b[2]))
        assert hb == lt
        assert not hb or a[1] < b[1]
    print("PASS: P24/P26 timestamps and 225 event-pair causality checks")


def verify_snapshots():
    # P33 local recording positions: B before receive; A after send.
    a, b, channel = 450, 200, [50]
    assert a + b + sum(channel) == 700
    # P36: message event positions strictly between numbered checkpoints.
    cps = [[0, 2, 4], [0, 1, 5], [0, 1, 3]]
    messages = [(1, 2, 0, 1), (0, 3, 1, 3), (2, 2, 1, 4)]

    def consistent(choice):
        return all(not (r <= cps[j][choice[j]]) or s <= cps[i][choice[i]]
                   for i, s, j, r in messages)

    choices = list(product(range(3), repeat=3))
    valid = [c for c in choices if consistent(c)]
    assert (0, 0, 0) in valid
    assert not any(c[0] == 1 for c in valid)
    assert (2, 2, 2) in valid
    # For the illustrated graph, check the no-path criterion independently.
    edges = [((0, 1), (0, 2)), ((1, 1), (1, 2)), ((2, 1), (2, 2)),
             ((1, 1), (0, 1)), ((0, 1), (1, 2)), ((2, 1), (1, 2))]
    reach = set(edges)
    while True:
        more = {(a, d) for a, b in reach for c, d in reach if b == c}
        if more <= reach:
            break
        reach |= more
    for c in product([1, 2], repeat=3):
        vertices = list(enumerate(c))
        no_paths = all((x, y) not in reach for x, y in permutations_pairs(vertices))
        assert no_paths == consistent(c)
    # Additional domino example: choose latest available, remove orphan receives.
    cps2 = [[0, 3], [0, 4]]
    msgs2 = [(0, 1, 1, 1), (1, 2, 0, 2), (0, 4, 1, 3)]
    selection, trace = [1, 1], [(1, 1)]
    while True:
        orphan = next(((j, r) for i, s, j, r in msgs2
                       if r <= cps2[j][selection[j]] and s > cps2[i][selection[i]]), None)
        if orphan is None:
            break
        j, r = orphan
        selection[j] = max(k for k, pos in enumerate(cps2[j]) if pos < r)
        trace.append(tuple(selection))
    assert trace == [(1, 1), (1, 0), (0, 0)]
    print("PASS: P33 conservation; 27 checkpoint combinations; R-Graph; domino trace")


def permutations_pairs(xs):
    return ((a, b) for a in xs for b in xs if a != b)


def verify_consensus_examples():
    for n in [3, 4, 5]:
        q = n // 2 + 1
        quorums = list(map(set, combinations(range(n), q)))
        assert all(a & b for a, b in product(quorums, repeat=2))
    reports = [(12, "Y"), (8, "X")]
    assert (20, max(reports, key=lambda r: r[0])[1]) == (20, "Y")
    # Removing adoption allows two distinct values to be chosen by intersecting quorums.
    votes = [(10, "X", {0, 1}), (20, "Y", {1, 2})]
    assert all(len(v[2]) == 2 for v in votes) and votes[0][1] != votes[1][1]
    local = (4, 8)  # Raft compares lastLogTerm first, then lastLogIndex.
    assert [(candidate >= local) for candidate in [(3, 100), (4, 7), (5, 6)]] == [False, False, True]
    # Five-server old-term example: S5 can receive S2/S4 votes after S1 crashes.
    logs = [[(1, "prefix"), (2, "X")] for _ in range(3)]
    logs += [[(1, "prefix")], [(1, "prefix"), (3, "Y")]]
    assert sum(len(log) > 1 and log[1] == (2, "X") for log in logs) == 3
    tail = lambda log: (log[-1][0], len(log))
    assert all(tail(logs[4]) >= tail(logs[i]) for i in [1, 3, 4])
    for i in [0, 1, 2]:
        logs[i].append((4, "no-op"))
    assert sum(tail(logs[4]) >= tail(log) for log in logs) < 3
    print("PASS: quorum intersections; adoption; Raft freshness and old-term counterexample")


if __name__ == "__main__":
    verify_clocks()
    verify_snapshots()
    verify_consensus_examples()
    print("All finite example checks passed; this is not a full protocol proof.")
