#!/usr/bin/env python3
"""Merge your filled label_sheet.csv into leetcode_records.json, validate, assign split, print coverage.
Usage: python merge_labels.py [--records leetcode_records.json] [--sheet label_sheet.csv] [--schema benchmark_schema.json]
Exit code 1 if any filled row has errors.

Sheet rules:
  expected_tc / expected_sc : O(...) or the word Unknown. Leave BOTH blank if not labeled yet.
  expected_algorithms       : up to 3 catalog labels separated by ';'. Leave the cell EMPTY with the row filled to mean 'no catalog algorithm'.
                              Write NONE to say that explicitly.
  variables                 : subset of n,m,q,k,V,E,A separated by ';'
  case_type                 : worst | expected | amortized
  negative_for              : catalog labels this code looks like but must NOT trigger (';' separated)
  confirmed                 : yes only after you checked the code yourself
"""
import sys, os, re, json, csv, hashlib, collections

def opt(name, default):
    return sys.argv[sys.argv.index(name)+1] if name in sys.argv else default
rec_path = opt('--records', 'leetcode_records.json'); sheet = opt('--sheet', 'label_sheet.csv'); schema_path = opt('--schema', 'benchmark_schema.json')
FALLBACK = ["Two Pointers","Fast and Slow Pointers","Sliding Window","Prefix Sum","Difference Array","Binary Search","Binary Search on Answer","Sorting","Kadane's Algorithm","Coordinate Compression","Monotonic Stack","Monotonic Queue","Heap / Priority Queue","Top K","Two Heaps","Cycle Detection","Linked List Reversal","DFS","BFS","DSU","Dijkstra","MST","Topological Sort","Strongly Connected Components","LCA","Binary Lifting","Trie","Dynamic Programming","Tree DP","Bitmask DP","Backtracking","Divide and Conquer","Fenwick Tree","Segment Tree","Sparse Table","Sieve","KMP","Z Algorithm","Rolling Hash"]
CAT = set(json.load(open(schema_path))['allowed_algorithms']) if os.path.exists(schema_path) else set(FALLBACK)
VARS = {'n','m','q','k','V','E','A'}; CASES = {'worst','expected','amortized'}
split = lambda s: [x.strip() for x in s.split(';') if x.strip()]
TC = re.compile(r'^(O\(.+\)|Unknown)$')

data = json.load(open(rec_path)); recs = {r['id']: r for r in data['records']}
errors = []
for row in csv.DictReader(open(sheet, newline='', encoding='utf-8')):
    r = recs.get(row['id'])
    if r is None: errors.append(f"{row['id']}: not in records"); continue
    if not row['expected_tc'].strip() and not row['expected_sc'].strip(): continue   # not labeled yet
    before = len(errors)
    e = lambda m: errors.append(f"{row['id']}: {m}")
    tc, sc = row['expected_tc'].strip(), row['expected_sc'].strip()
    if not row['label_notes'].strip(): e("label_notes empty: write one line of structural evidence")
    if not TC.match(tc): e(f"expected_tc not O(...) or Unknown: {tc!r}")
    if not TC.match(sc): e(f"expected_sc not O(...) or Unknown: {sc!r}")
    algos = [] if row['expected_algorithms'].strip().upper() in ('', 'NONE') else split(row['expected_algorithms'])
    if len(algos) > 3: e("more than 3 expected_algorithms")
    for a in algos:
        if a not in CAT: e(f"label outside catalog: {a!r} (put other techniques in techniques_observed)")
    neg = split(row['negative_for'])
    for a in neg:
        if a not in CAT: e(f"negative_for outside catalog: {a!r}")
    vs = split(row['variables'])
    if not set(vs) <= VARS: e(f"variables must be within {sorted(VARS)}: {vs}")
    ct = row['case_type'].strip()
    if ct not in CASES: e(f"case_type must be one of {sorted(CASES)}")
    if len(errors) > before: continue   # invalid row is NOT applied
    r.update(expected_tc=tc, expected_sc=sc, expected_algorithms=algos, techniques_observed=split(row['techniques_observed']),
             variables=vs, case_type=ct, negative_for=neg, label_notes=row['label_notes'].strip(),
             constraints_note=row['constraints_note_own_words'].strip() or None)
    r['status'] = 'human_confirmed' if row['confirmed'].strip().lower() == 'yes' else 'needs_human_review'

# leakage-safe split: all records of the same problem go to the same side
for r in recs.values():
    h = int(hashlib.sha256(r['problem_slug'].encode()).hexdigest(), 16) % 10
    r['split'] = 'heldout' if h < 3 else 'dev'
data['records'] = list(recs.values())
json.dump(data, open(rec_path, 'w'), indent=2)
with open(rec_path.replace('.json', '.jsonl'), 'w') as f:
    for r in data['records']: f.write(json.dumps(r) + "\n")

rs = data['records']; conf = [r for r in rs if r['status'] == 'human_confirmed']
print(f"records {len(rs)} | by status {dict(collections.Counter(r['status'] for r in rs))} | by split {dict(collections.Counter(r['split'] for r in rs))}")
print(f"slugs {len({r['problem_slug'] for r in rs})} | cpp {sum(r['language']=='cpp' for r in rs)} | java {sum(r['language']=='java' for r in rs)}")
print("approaches", dict(collections.Counter(r['approach'] for r in rs)))
lab = collections.Counter(a for r in conf for a in (r['expected_algorithms'] or []))
neg = collections.Counter(a for r in conf for a in (r['negative_for'] or []))
print("confirmed positives per label:", dict(lab) or "none yet")
print("confirmed look-alike negatives per label:", dict(neg) or "none yet")
print("confirmed with no catalog algorithm:", sum(1 for r in conf if r['expected_algorithms'] == []))
for m in errors: print("ERROR", m)
sys.exit(1 if errors else 0)
