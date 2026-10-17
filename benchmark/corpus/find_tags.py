import re

with open('engine/src/algorithms/mod.rs', 'r', encoding='utf-8') as f:
    text = f.read()

# Look for patterns like (AlgorithmCategory::... or algos.push("...") or AlgorithmCategory
patterns = set(re.findall(r'"([A-Za-z0-9 _/()\-+]+)"', text))
for p in sorted(patterns):
    p_lower = p.lower()
    if any(w in p_lower for w in ['queue', 'heap', 'bfs', 'dfs', 'sort', 'union', 'dsu', 'dijkstra', 'dp', 'trie', 'tree', 'binary', 'stack', 'pointer', 'window', 'kadane', 'prefix', 'segment', 'fenwick', 'sparse', 'kmp', 'hash', 'rabin', 'sieve', 'euler', 'tarjan', 'bridge', 'bit', 'knapsack', 'linear']):
        print(p)
