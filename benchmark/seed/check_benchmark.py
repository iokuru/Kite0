#!/usr/bin/env python3
"""KiteO benchmark checker (schema + coverage). Usage:
  python check_benchmark.py [benchmark_seed.json] [--allow-seed] [--write coverage_report.json]
Exit code 1 when schema errors exist or milestone targets are unmet (unless --allow-seed)."""
import json, sys, re, collections, os

path = next((a for a in sys.argv[1:] if a.endswith('.json') and not a.startswith('--')), 'benchmark_seed.json')
allow_seed = '--allow-seed' in sys.argv
out = sys.argv[sys.argv.index('--write')+1] if '--write' in sys.argv else None
catalog_arg = sys.argv[sys.argv.index('--catalog')+1] if '--catalog' in sys.argv else None

schema_candidates = [
    'benchmark_schema.json',
    'benchmark/seed/benchmark_schema.json',
    os.path.join(os.path.dirname(__file__), 'benchmark_schema.json'),
    os.path.join(os.path.dirname(path), 'benchmark_schema.json') if os.path.dirname(path) else None
]
schema_file = next((s for s in schema_candidates if s and os.path.exists(s)), 'benchmark_schema.json')
schema = json.load(open(schema_file, encoding='utf-8'))
data = json.load(open(path, encoding='utf-8'))
recs = data['records']
CAT = set(schema['allowed_algorithms'])
errors = []

# Verify catalog.toml
catalog_candidates = [catalog_arg] if catalog_arg else [
    'engine/src/algorithms/catalog.toml',
    '../../engine/src/algorithms/catalog.toml',
    '../engine/src/algorithms/catalog.toml'
]
catalog_file = next((c for c in catalog_candidates if c and os.path.exists(c)), None)
CATALOG_ALL_NAMES = set()
if catalog_file:
    with open(catalog_file, 'r', encoding='utf-8') as cf:
        cat_content = cf.read()
    CATALOG_ALL_NAMES = set(re.findall(r'name\s*=\s*"([^"]+)"', cat_content))
    for l in sorted(CAT):
        if l not in CATALOG_ALL_NAMES:
            errors.append(f"catalog.toml mismatch: scored label '{l}' missing or renamed in {catalog_file}")
elif catalog_arg:
    errors.append(f"Specified catalog file not found: {catalog_arg}")

ALLOWED_PLAIN_TECHNIQUES = {
    "Greedy", "Math", "Implementation", "Brute Force", "Number Theory",
    "Simulation", "Game", "Hash Map", "Memoization", "Binary Exponentiation",
    "Bit Manipulation", "Combinatorics", "Geometry", "Constructive", "Recursion",
    "Interactive", "String", "Graph", "Trees", "DP"
}
ALLOWED_TECHNIQUES = CATALOG_ALL_NAMES | ALLOWED_PLAIN_TECHNIQUES

def canon(tc):
    """Canonical form so O(mn) == O(nm) but O(n+q) != O(nq)."""
    if tc in (None, 'Unknown'): return tc
    s = tc.replace(' ', '')
    m = re.fullmatch(r'O\((.*)\)', s)
    if not m: return 'INVALID'
    body = m.group(1)
    terms = re.split(r'\+(?![^()]*\))', body)
    out = []
    for t in terms:
        # split product factors at top level by commas-free multiplication of single-letter vars
        letters = re.fullmatch(r'([nmqkVEA]+)', t)
        out.append(''.join(sorted(letters.group(1))) if letters else t)
    return 'O(' + '+'.join(sorted(out)) + ')'

ids = set()
for r in recs:
    st = r.get('status')
    if r['id'] in ids: errors.append(f"{r['id']}: duplicate id")
    ids.add(r['id'])
    if st not in schema['allowed_status']: errors.append(f"{r['id']}: bad status {st}")
    need = schema['seed_required_fields'] if st == 'seed_only' else schema['final_required_fields']
    for f in need:
        if f not in r: errors.append(f"{r['id']}: missing field {f}")
    if st in schema['final_required_when_status_in']:
        for f in ('commit_sha','file_path','source_hash','license','fetched_at','source_url','contest_id','problem_index'):
            if not r.get(f): errors.append(f"{r['id']}: {f} empty for status {st}")
    a = schema['audit_fields_required_when_status_in']
    if st in a['statuses']:
        for f in a['fields']:
            if r.get(f) is None: errors.append(f"{r['id']}: {f} is null for audited status {st}")
        if r.get('audit_source') not in ('source_read_only',): errors.append(f"{r['id']}: audit_source must be source_read_only")
    if st == 'human_confirmed' and not r.get('audited_by'): errors.append(f"{r['id']}: human_confirmed needs a human in audited_by")
    ea = r.get('expected_algorithms')
    if ea is not None:
        if len(ea) > 3: errors.append(f"{r['id']}: more than 3 expected_algorithms")
        for l in ea:
            if l not in CAT: errors.append(f"{r['id']}: label outside catalog: {l}")
    for l in (r.get('negative_for') or []):
        if l not in CAT: errors.append(f"{r['id']}: negative_for label outside catalog: {l}")
    for t in (r.get('techniques_observed') or []):
        if t not in ALLOWED_TECHNIQUES:
            errors.append(f"{r['id']}: techniques_observed contains invalid technique: '{t}'")
    for k in ('expected_tc','expected_sc'):
        if r.get(k) is not None and canon(r[k]) == 'INVALID': errors.append(f"{r['id']}: {k} not canonical: {r[k]}")
    if r.get('case_type') not in schema['allowed_case_type']: errors.append(f"{r['id']}: bad case_type")
    if r.get('test_case_semantics') not in schema['allowed_test_case_semantics']: errors.append(f"{r['id']}: bad test_case_semantics")
    if r.get('source_hash') and r.get('commit_sha') is None: errors.append(f"{r['id']}: source_hash without commit_sha")

audited = [r for r in recs if r['status'] in ('agent_audited','human_confirmed')]
confirmed = [r for r in recs if r['status'] == 'human_confirmed']
def cnt(f, pool): return sum(1 for r in pool if f(r))
M = {}
M['total_cases_150'] = (len(recs), 150)
M['cpp_60'] = (cnt(lambda r: r['language']=='cpp', recs), 60)
M['java_60'] = (cnt(lambda r: r['language']=='java', recs), 60)
M['rating_1600_1800_25'] = (cnt(lambda r: r.get('rating') and 1600<=r['rating']<=1800, recs), 25)
M['no_catalog_algorithm_10'] = (cnt(lambda r: r.get('expected_algorithms')==[], audited), 10)
M['multi_variable_20'] = (cnt(lambda r: r.get('variables') and len(r['variables'])>=2, audited), 20)
M['amortized_10'] = (cnt(lambda r: r.get('case_type')=='amortized', audited), 10)
M['legit_unknown_10'] = (cnt(lambda r: 'Unknown' in (r.get('expected_tc'), r.get('expected_sc')) or r.get('expected_algorithms')==[] and False, audited), 10)
M['paired_cpp_java_20'] = (len({r['pair_id'] for r in recs if r.get('pair_id')}), 20)
per = {}
for l in sorted(CAT):
    pos = [r for r in audited if l in (r.get('expected_algorithms') or [])]
    neg = [r for r in audited if l in (r.get('negative_for') or [])]
    hpos = [r for r in confirmed if r.get('split')=='heldout' and l in (r.get('expected_algorithms') or [])]
    hneg = [r for r in confirmed if r.get('split')=='heldout' and l in (r.get('negative_for') or [])]
    per[l] = {"audited_positive": len(pos), "audited_negative": len(neg), "smoke_target": 3, "smoke_met": len(pos)>=3 and len(neg)>=2,
              "heldout_confirmed_positive": len(hpos), "heldout_confirmed_negative": len(hneg),
              "approval_eligible": len(hpos)>=10 and len(hneg)>=10}
report = {
 "schema_version": schema['schema_version'], "catalog_version": schema['catalog_version'],
 "counts": {"total": len(recs), "by_status": dict(collections.Counter(r['status'] for r in recs)),
            "by_language": dict(collections.Counter(r['language'] for r in recs)),
            "by_rating": {str(k): v for k,v in sorted(collections.Counter(r['rating'] for r in recs).items(), key=lambda kv: (kv[0] is None, kv[0] or 0))},
            "audited": len(audited), "human_confirmed": len(confirmed),
            "heldout": cnt(lambda r: r.get('split')=='heldout', recs)},
 "milestone_targets": {k: {"have": v[0], "need": v[1], "met": v[0]>=v[1]} for k,v in M.items()},
 "per_label": per,
 "approval_gate": "A label may be marked approved in catalog.toml only when approval_eligible is true AND its detector reaches >=95% precision on the human-confirmed held-out set.",
 "schema_errors": errors[:200], "schema_error_count": len(errors)
}
txt = json.dumps(report, indent=2)
if out: open(out,'w').write(txt)
print(txt)
unmet = [k for k,v in report['milestone_targets'].items() if not v['met']]
print(f"\nSCHEMA ERRORS: {len(errors)}   UNMET MILESTONE TARGETS: {len(unmet)}   APPROVAL-ELIGIBLE LABELS: {sum(1 for v in per.values() if v['approval_eligible'])}/39", file=sys.stderr)
sys.exit(1 if errors or (unmet and not allow_seed) else 0)
