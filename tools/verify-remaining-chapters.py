"""Finite example checks for Chapters 05-09; no live cluster or blockchain node is contacted.

Run: python3 tools/verify-remaining-chapters.py
Only the Python standard library is needed.
"""

import hashlib
import heapq
import math


def verify_ch05_consistency_and_transactions():
    # P123: Interleaving combinations for two processes with 5 and 4 operations.
    interleavings = math.factorial(5 + 4) // (math.factorial(5) * math.factorial(4))
    assert interleavings == 126

    # P127: Sequential Consistency check on W(x,1), W(x,2) with observers P3, P4.
    # A valid global order has either (1 before 2) or (2 before 1), never both.
    p3_seen = (1, 2)
    p4_seen = (2, 1)
    assert p3_seen != p4_seen  # Contradictory global orders -> violates Sequential Consistency.

    # P145: ACID Isolation bank transfer invariant (A=500, B=200, total=700).
    a, b = 500, 200
    assert a + b == 700
    a_mid = a - 100
    dirty_audit = a_mid + b
    assert dirty_audit == 600  # Unisolated intermediate state.
    b_final = b + 100
    assert a_mid + b_final == 700

    # P150 & P154: 2PC + OCC Backward Validation (RS(Tv) intersect WS(Ti) == empty).
    ws_t2 = {"AccA"}
    ws_t3 = {"AccC"}
    rs_tv_conflict = {"AccA", "AccB"}
    rs_tv_safe = {"AccB", "AccD"}
    assert bool(rs_tv_conflict & (ws_t2 | ws_t3)) is True   # Vote No -> Abort
    assert bool(rs_tv_safe & (ws_t2 | ws_t3)) is False      # Vote Yes -> Phase 2 Update

    # P151: MVCC read version selection (T1 < T2 < T3 < T4).
    versions = [(1, "V1"), (2, "V2"), (4, "V4")]
    t3_ts = 3
    chosen = max((v for v in versions if v[0] < t3_ts), key=lambda v: v[0])
    assert chosen == (2, "V2")
    print("PASS Ch05: 126 interleavings, Sequential Consistency, Isolation invariant, 2PC+OCC validation, MVCC")


def verify_ch06_lsm_bloom_hbase():
    # P160: B+ Tree page-level write amplification.
    wa = 4096 / 100
    assert math.isclose(wa, 40.96)

    # P170-P171: Bloom Filter no false negatives + Bob false positive example.
    m = 8
    bits = [0] * m
    # Other key set index 3; Alice sets indices 1, 4, 7.
    bits[3] = 1
    alice_hashes = (1, 4, 7)
    for idx in alice_hashes:
        bits[idx] = 1
    assert bits == [0, 1, 0, 1, 1, 0, 0, 1]
    assert all(bits[idx] == 1 for idx in alice_hashes)  # No false negatives.
    bob_hashes = (1, 4, 7)  # Never inserted, collides with set bits -> false positive.
    assert all(bits[idx] == 1 for idx in bob_hashes)
    charlie_hashes = (1, 2, 7)  # Bit 2 is 0 -> definitely absent.
    assert not all(bits[idx] == 1 for idx in charlie_hashes)

    # Standard Bloom Filter FP rate for m/n = 10, k = 7.
    k_opt = 10 * math.log(2)
    assert math.isclose(k_opt, 6.9314718, rel_tol=1e-5)
    p_fp = (1 - math.exp(-7 / 10)) ** 7
    assert math.isclose(p_fp, 0.0081937, rel_tol=1e-4)

    # P173: K-Way Merge via Min-Heap.
    buffers = [[15, 40], [10, 45], [25, 30]]
    merged = list(heapq.merge(*buffers))
    assert merged == [10, 15, 25, 30, 40, 45]

    # P178-P179: HBase .META. Region range lookup & cache refresh.
    meta = [("Alice", "Bob", "192.168.1.50"), ("Bob", "Dave", "192.168.1.51")]

    def locate(row_key):
        for start, end, server in meta:
            if start <= row_key < end:
                return server
        return None

    assert locate("Amy") == "192.168.1.50"
    assert locate("Carl") == "192.168.1.51"
    print("PASS Ch06: WA=40.96x, Bloom Filter (no FN / FP / 0.82% rate), K-Way Merge, HBase .META. routing")


def verify_ch07_hdfs_yarn_spark():
    # P193: HDFS NameNode small-file RAM math.
    files_per_hour = 100_000
    bytes_per_inode = 150
    mb_per_hour = (files_per_hour * bytes_per_inode) / 1_000_000
    assert math.isclose(mb_per_hour, 15.0)
    gb_per_year = (mb_per_hour * 24 * 365) / 1_000
    assert math.isclose(gb_per_year, 131.4)

    # P202: DRF balanced allocation on <18 CPUs, 36 GB RAM>.
    total_cpu, total_ram = 18, 36
    j1_cpu, j1_ram = 2, 8
    j2_cpu, j2_ram = 6, 2
    assert j1_ram / total_ram > j1_cpu / total_cpu  # Job 1 is RAM-dominant (2/9).
    assert j2_cpu / total_cpu > j2_ram / total_ram  # Job 2 is CPU-dominant (1/3).
    x, y = 3, 2
    assert x * j1_cpu + y * j2_cpu <= total_cpu
    assert x * j1_ram + y * j2_ram <= total_ram
    share1 = (x * j1_ram) / total_ram
    share2 = (y * j2_cpu) / total_cpu
    assert math.isclose(share1, 2 / 3) and math.isclose(share2, 2 / 3)

    # P203-P204: Hazard rates (Exponential constant vs Pareto DFR).
    lam = 0.5
    for t in [1.0, 2.0, 10.0]:
        r_exp = (lam * math.exp(-lam * t)) / math.exp(-lam * t)
        assert math.isclose(r_exp, lam)
    alpha = 2.0
    r_pareto = [(alpha * (t ** (-alpha - 1))) / (t ** (-alpha)) for t in [1.0, 2.0, 4.0]]
    assert r_pareto == [2.0, 1.0, 0.5] and r_pareto[0] > r_pareto[1] > r_pareto[2]

    # P207: Spark RDD Lineage partial recomputation for a lost partition only.
    hdfs_partitions = {0: ["ERROR a", "INFO b"], 1: ["ERROR c", "ERROR d"]}
    transform = lambda recs: [r.lower() for r in recs if r.startswith("ERROR")]
    cached = {pid: transform(recs) for pid, recs in hdfs_partitions.items()}
    del cached[1]  # Worker holding partition 1 crashes.
    cached[1] = transform(hdfs_partitions[1])  # Recompute only partition 1.
    assert cached == {0: ["error a"], 1: ["error c", "error d"]}
    print("PASS Ch07: NameNode 131.4 GB/yr, DRF (3,2) at 66.7%, Exponential/Pareto DFR, RDD Lineage recovery")


def verify_ch08_kafka_streams():
    # P224: Consumer Group partition exclusivity (4 partitions).
    partitions = ["P0", "P1", "P2", "P3"]
    group_a = {"C1": ["P0", "P1"], "C2": ["P2", "P3"]}
    group_b = {"C3": ["P0"], "C4": ["P1"], "C5": ["P2"], "C6": ["P3"], "C7": []}
    for grp in (group_a, group_b):
        assigned = [p for ps in grp.values() for p in ps]
        assert sorted(assigned) == partitions and len(assigned) == len(set(assigned))
    assert group_b["C7"] == []  # Extra consumer remains idle.

    # P230: Traditional vs sendfile() copy counts.
    trad_cpu_copies, sendfile_cpu_copies = 2, 0
    trad_ctx_switches, sendfile_ctx_switches = 4, 2
    assert sendfile_cpu_copies < trad_cpu_copies and sendfile_ctx_switches < trad_ctx_switches

    # P235: Kafka Streams Changelog replay restores lost local state store.
    clicks = [("u1", 1), ("u2", 1), ("u1", 1), ("u1", 1)]
    local_store = {}
    changelog = []
    for k, inc in clicks:
        local_store[k] = local_store.get(k, 0) + inc
        changelog.append((k, local_store[k]))
    # Crash loses local_store; compact changelog keeps latest per key and rebuilds identically.
    compacted = dict(changelog)
    recovered_store = {}
    for k, v in compacted.items():
        recovered_store[k] = v
    assert recovered_store == local_store == {"u1": 3, "u2": 1}
    print("PASS Ch08: Consumer Group exclusivity, sendfile() copies, Changelog state store recovery")


def verify_ch09_blockchain():
    # P256: Merkle Tree root and inclusion proof for Tx0.
    def h(data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    txs = ["Tx0", "Tx1", "Tx2", "Tx3"]
    h0, h1, h2, h3 = [h(tx) for tx in txs]
    h4, h5 = h(h0 + h1), h(h2 + h3)
    root = h(h4 + h5)
    # Light node verifies Tx0 using only proof (h1, h5).
    assert h(h(h("Tx0") + h1) + h5) == root

    # P252: Simplified PoW Nonce search (leading "00").
    header_prefix = "TxData...HashPrev"
    nonce = 0
    while True:
        digest = h(f"{header_prefix}:{nonce}")
        if digest.startswith("00"):
            break
        nonce += 1
    assert h(f"{header_prefix}:{nonce}").startswith("00")

    # P257: PoW Fork resolution by Longest Chain Rule & orphan rollback to Mempool.
    branch_a = [("54A", {"tx_a1", "tx_shared"}), ("55A", {"tx_a2"})]
    branch_b = [("54B", {"tx_shared"}), ("55B", {"tx_b1"}), ("56B", {"tx_b2"})]
    winner = branch_b if len(branch_b) > len(branch_a) else branch_a
    loser = branch_a if winner is branch_b else branch_b
    winner_txs = set().union(*(txs_set for _, txs_set in winner))
    loser_txs = set().union(*(txs_set for _, txs_set in loser))
    returned_to_mempool = loser_txs - winner_txs
    assert winner is branch_b and returned_to_mempool == {"tx_a1", "tx_a2"}

    # P263 & P265: Smart Contract reactive check with Block Timestamp.
    deadline = 100
    goal = 10_000
    balance = 10_000
    # Triggered after deadline (Saturday timestamp 120 > 100) by external tx.
    def finalize(current_block_time, current_balance):
        if current_block_time <= deadline:
            return "NOT_YET"
        return "TRANSFER_TO_CREATOR" if current_balance >= goal else "ENABLE_REFUNDS"

    assert finalize(90, balance) == "NOT_YET"
    assert finalize(120, balance) == "TRANSFER_TO_CREATOR"
    assert finalize(120, 6_000) == "ENABLE_REFUNDS"
    print("PASS Ch09: Merkle proof, PoW nonce verification, Longest Chain fork rollback, Reactive Smart Contract")


if __name__ == "__main__":
    verify_ch05_consistency_and_transactions()
    verify_ch06_lsm_bloom_hbase()
    verify_ch07_hdfs_yarn_spark()
    verify_ch08_kafka_streams()
    verify_ch09_blockchain()
    print("All finite example checks for Chapters 05-09 passed; no live cluster or blockchain node was contacted.")
