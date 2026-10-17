# Benchmark Corpora

This directory contains curated benchmark test suites:

- **`snippets.json`** (152 cases / 76 problems): Canonical reference suite covering fundamental algorithmic patterns across C++ and Java with 1:1 parity.
- **`dev2.json`** (70 cases / 35 problems): Synthetic stress suite validating edge-case induction bounds, nested loops, and recursion.
- **`tough_benchmark.json`** (500 cases / 250 problems): Scaled competitive programming and Online Assessment (OA) corpus spanning the full 68-algorithm taxonomy.

Evaluation on authentic competitive programming submissions is conducted strictly in `benchmark/real/`. To validate corpus integrity and parity, run `python benchmark/tools/validate_suite.py`.
