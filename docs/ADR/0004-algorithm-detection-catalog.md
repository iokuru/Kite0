# ADR 0004: Algorithm Detection Catalog and Precision Policy

## Status
Accepted

## Context
Heuristic classifiers and probabilistic code tools frequently speculate and produce noisy, inaccurate algorithmic labels (such as classifying arbitrary loops containing conditionals as "Greedy"). Kite0 requires compiler-grade structural precision and zero speculative guesswork.

## Decision
1. **Catalog**: Kite0 recognizes only the following 26 canonical algorithm labels:
   - Binary Search
   - Binary Search on Answer
   - Two Pointers
   - Sliding Window
   - Prefix Sum
   - Sorting (only when it is the primary algorithmic technique)
   - BFS
   - DFS
   - Topological Sort
   - DSU
   - Dijkstra
   - MST
   - Fenwick Tree
   - Segment Tree
   - Sparse Table
   - Monotonic Stack
   - Monotonic Queue
   - Binary Lifting
   - LCA
   - Tree DP
   - Bitmask DP
   - Sieve
   - KMP
   - Z Algorithm
   - Rolling Hash
   - Trie
2. **Exclusions**: No `Greedy` label is permitted.
3. **Cardinality**: Kite0 outputs at most 3 detected labels for any given solution.
4. **Precision Bias**: Prefer an omitted label over a false positive. Every detector pattern requires negative look-alike test cases.
