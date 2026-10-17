#!/usr/bin/env python3
"""Turn your own LeetCode solution files into KiteO benchmark records.
Usage: python ingest_leetcode.py [submissions_dir] [--out leetcode_records.json] [--sheet label_sheet.csv]
File names: <problem-slug>__<approach>.<cpp|java>   approach: optimal | brute | alt | alt2
Example:   two-sum__optimal.cpp   two-sum__brute.java
Existing records and filled label-sheet rows are kept; only new files are added."""
import sys, os, re, json, csv, hashlib

args = [a for a in sys.argv[1:] if not a.startswith('--')]
sub = args[0] if args else 'submissions'
def opt(name, default):
    return sys.argv[sys.argv.index(name)+1] if name in sys.argv else default
out = opt('--out', 'leetcode_records.json'); sheet = opt('--sheet', 'label_sheet.csv')
LANG = {'.cpp': 'cpp', '.java': 'java'}
APPROACH = {'optimal', 'brute', 'alt', 'alt2'}

def entry_cpp(src):
    m = re.search(r'public\s*:', src)
    body = src[m.end():] if m else src
    for mm in re.finditer(r'(?m)^\s*(?:static\s+)?([A-Za-z_][\w:<>,\s\*&]*?)\s+([A-Za-z_]\w*)\s*\(([^)]*)\)\s*(?:const\s*)?\{', body):
        if mm.group(2) in ('if', 'for', 'while', 'switch', 'return', 'catch'): continue
        return f"{mm.group(1).strip()} {mm.group(2)}({' '.join(mm.group(3).split())})"
    return None

def entry_java(src):
    for mm in re.finditer(r'public\s+(?:static\s+)?([\w<>\[\],\s\?]+?)\s+(\w+)\s*\(([^)]*)\)\s*(?:throws [\w, ]+)?\{', src):
        if mm.group(1).strip() in ('class', 'interface', 'enum'): continue
        return f"{mm.group(1).strip()} {mm.group(2)}({' '.join(mm.group(3).split())})"
    return None

records = json.load(open(out))['records'] if os.path.exists(out) else []
have = {r['id'] for r in records}
added, skipped = 0, []
for fn in sorted(os.listdir(sub)) if os.path.isdir(sub) else []:
    base, ext = os.path.splitext(fn)
    if ext not in LANG: continue
    if '__' not in base: skipped.append((fn, 'name must be <slug>__<approach>.<ext>')); continue
    slug, approach = base.rsplit('__', 1)
    if approach not in APPROACH: skipped.append((fn, f'approach must be one of {sorted(APPROACH)}')); continue
    rid = f"lc-{LANG[ext]}-{slug}-{approach}"
    if rid in have: continue
    data = open(os.path.join(sub, fn), 'rb').read()
    src = data.decode('utf-8', 'replace')
    sig = entry_cpp(src) if ext == '.cpp' else entry_java(src)
    records.append({
        "id": rid, "platform": "leetcode", "problem_slug": slug, "language": LANG[ext], "approach": approach,
        "source_file": os.path.join(sub, fn).replace('\\', '/'), "source_hash": hashlib.sha256(data).hexdigest(),
        "provenance": "own_submission", "license": "own work", "accepted_evidence": "user_attested_not_verified",
        "entry_signature": sig, "constraints_note": None,
        "expected_tc": None, "expected_sc": None, "expected_algorithms": None, "techniques_observed": None,
        "variables": None, "case_type": "pending", "negative_for": None, "label_notes": "",
        "status": "fetched", "split": None})
    have.add(rid); added += 1
json.dump({"schema": "kiteo-leetcode-1", "catalog_version": "kiteo-39-v1", "records": records}, open(out, 'w'), indent=2)

cols = ["id", "slug", "language", "approach", "entry_signature", "constraints_note_own_words",
        "expected_tc", "expected_sc", "expected_algorithms", "techniques_observed", "variables", "case_type", "negative_for", "label_notes", "confirmed"]
rows = {}
if os.path.exists(sheet):
    for r in csv.DictReader(open(sheet, newline='', encoding='utf-8')): rows[r['id']] = r
for r in records:
    if r['id'] not in rows:
        rows[r['id']] = {c: '' for c in cols}
        rows[r['id']].update(id=r['id'], slug=r['problem_slug'], language=r['language'], approach=r['approach'], entry_signature=r['entry_signature'] or '')
with open(sheet, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows.values())
print(f"records: {len(records)} (+{added} new) | sheet rows: {len(rows)}")
for fn, why in skipped: print("SKIPPED", fn, "-", why)
