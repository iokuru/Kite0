#!/usr/bin/env python3
"""Benchmark Suite Validator.

Validates integrity, schema compliance, and language parity across Kite0 benchmark corpora:
- snippets.json (Canonical Dev Suite, 152 cases)
- dev2.json (Synthetic Stress Suite, 70 cases)
- tough_benchmark.json (Comprehensive OA Taxonomy Suite, 500 cases)
"""

import json
import os
import sys

CORPUS_DIR = os.path.join(os.path.dirname(__file__), "..", "corpus")

SUITES = {
    "snippets.json": {"expected_cases": 152, "expected_problems": 76},
    "dev2.json": {"expected_cases": 70, "expected_problems": 35},
    "tough_benchmark.json": {"expected_cases": 500, "expected_problems": 250},
}


def validate_corpus(filename: str, expected_cases: int, expected_problems: int) -> bool:
    filepath = os.path.join(CORPUS_DIR, filename)
    if not os.path.exists(filepath):
        print(f"[-] Missing corpus file: {filepath}")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        cases = json.load(f)

    actual_len = len(cases)
    if actual_len != expected_cases:
        print(f"[-] {filename}: Expected {expected_cases} cases, found {actual_len}")
        return False

    ids = [c["id"] for c in cases]
    if len(ids) != len(set(ids)):
        print(f"[-] {filename}: Duplicate IDs found!")
        return False

    cpp_count = sum(1 for c in cases if c.get("language") == "cpp")
    java_count = sum(1 for c in cases if c.get("language") == "java")
    if cpp_count != expected_problems or java_count != expected_problems:
        print(f"[-] {filename}: Language mismatch (cpp: {cpp_count}, java: {java_count})")
        return False

    print(f"[+] {filename}: {actual_len} cases ({expected_problems} problems) verified successfully.")
    return True


def main():
    print("=== Validating Kite0 Benchmark Corpora ===")
    all_ok = True
    for filename, config in SUITES.items():
        ok = validate_corpus(filename, config["expected_cases"], config["expected_problems"])
        if not ok:
            all_ok = False

    if all_ok:
        print("=== All benchmark corpora valid! ===")
        sys.exit(0)
    else:
        print("=== Benchmark validation failed! ===")
        sys.exit(1)


if __name__ == "__main__":
    main()
