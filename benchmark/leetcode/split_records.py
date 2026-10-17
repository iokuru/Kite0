#!/usr/bin/env python3
"""Split leetcode_records.json into dev and held-out records.
Writes:
  (a) leetcode_records.dev.json inside the repo with dev records only.
  (b) leetcode_records.heldout.json ONLY to the directory specified by KITEO_HELDOUT_DIR.
Fails if KITEO_HELDOUT_DIR is unset.
"""
import os, sys, json

heldout_dir = os.environ.get('KITEO_HELDOUT_DIR')
if not heldout_dir:
    print("ERROR: Environment variable KITEO_HELDOUT_DIR is unset. Cannot split records without a secure heldout directory.", file=sys.stderr)
    sys.exit(1)

if not os.path.isdir(heldout_dir):
    print(f"ERROR: KITEO_HELDOUT_DIR='{heldout_dir}' does not exist or is not a directory.", file=sys.stderr)
    sys.exit(1)

base_dir = os.path.dirname(__file__)
rec_path = os.path.join(base_dir, 'leetcode_records.json')
if not os.path.exists(rec_path):
    print(f"ERROR: '{rec_path}' does not exist.", file=sys.stderr)
    sys.exit(1)

with open(rec_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

records = data.get('records', [])
dev_records = [r for r in records if r.get('split') == 'dev']
heldout_records = [r for r in records if r.get('split') == 'heldout']

dev_data = dict(data)
dev_data['records'] = dev_records
dev_path = os.path.join(base_dir, 'leetcode_records.dev.json')
with open(dev_path, 'w', encoding='utf-8') as f:
    json.dump(dev_data, f, indent=2)

heldout_data = dict(data)
heldout_data['records'] = heldout_records
heldout_path = os.path.join(heldout_dir, 'leetcode_records.heldout.json')
with open(heldout_path, 'w', encoding='utf-8') as f:
    json.dump(heldout_data, f, indent=2)

print(f"Split completed successfully:")
print(f"  Dev records: {len(dev_records)} -> {dev_path}")
print(f"  Held-out records: {len(heldout_records)} -> {heldout_path}")
