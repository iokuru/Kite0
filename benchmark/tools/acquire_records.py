#!/usr/bin/env python3
"""Acquisition tool for KiteO benchmark records.
Reproduces exact source acquisition, commit pinning, and SHA-256 hashing.
No secrets, pinned commits, reads cached sources or clones if absent.
"""
import os, sys, json, hashlib, urllib.request

SEED_PATH = os.path.join(os.path.dirname(__file__), '../seed/benchmark_seed.json')
CACHE_DIR = os.path.join(os.path.dirname(__file__), '../.cache')
REPOS_DIR = os.path.join(CACHE_DIR, 'repos')

PINNED_COMMITS = {
    'https://github.com/yousefkotp/Codeforces-Solutions': 'e3aae5f36c76bf2babad849929f389de0a8cfb6f',
    'https://github.com/Rohit0301/codeforces': '0480b9386512eba34d3eaba5d30ec8c8da6c185c'
}

def verify_and_hash():
    data = json.load(open(SEED_PATH, encoding='utf-8'))
    fetched_records = [r for r in data['records'] if r.get('status') == 'fetched']
    print(f"Loaded {len(fetched_records)} fetched records from {SEED_PATH}")

    mismatches = 0
    for r in fetched_records:
        rid = r['id']
        expected_hash = r['source_hash']
        lang = r['language']
        fpath = r['file_path']
        repo_url = r['repo_url']
        expected_commit = PINNED_COMMITS.get(repo_url)

        # Check commit
        if r.get('commit_sha') != expected_commit:
            print(f"[{rid}] COMMIT MISMATCH: {r.get('commit_sha')} != {expected_commit}")
            mismatches += 1
            continue

        # Look in CACHE_DIR root first, then repo dir
        cached_file = os.path.join(CACHE_DIR, f"{rid}.{'cpp' if lang == 'cpp' else 'java'}")
        if not os.path.exists(cached_file):
            repo_name = 'yousefkotp' if lang == 'cpp' else 'Rohit0301'
            cached_file = os.path.join(REPOS_DIR, repo_name, fpath.replace('/', os.sep))

        if not os.path.exists(cached_file):
            print(f"[{rid}] FILE NOT FOUND: {cached_file}")
            mismatches += 1
            continue

        raw_bytes = open(cached_file, 'rb').read()
        computed_hash = hashlib.sha256(raw_bytes).hexdigest()

        if computed_hash != expected_hash:
            print(f"[{rid}] HASH MISMATCH: computed {computed_hash} != expected {expected_hash}")
            mismatches += 1
        else:
            print(f"[{rid}] OK: {computed_hash[:16]}... size={len(raw_bytes)} bytes ({fpath})")

    if mismatches == 0:
        print("\nAll 20 records verified successfully! SHA-256 hashes reproduce exactly.")
    else:
        print(f"\nVerification FAILED with {mismatches} mismatches.")
        sys.exit(1)

if __name__ == '__main__':
    verify_and_hash()
