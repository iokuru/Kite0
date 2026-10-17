# Antigravity Master Prompt: KiteO Benchmark v3

You are building the audited benchmark and the adapter fixtures for KiteO, a local static analyzer for competitive-programming C++ and Java code. KiteO displays only: TC, SC, Algorithm.

The benchmark tests implementation-level analysis, not problem-tag recognition. You are the ACQUISITION AND AUDIT role only. Do not change analyzer code and do not tune anything while doing this job.

## Ground rules

- The package seed is NOT ground truth. All 80 records are `seed_only`; `expected_*` fields are `null` (not audited). Never treat `null` as `[]`.
- Never run KiteO to decide a label. `audit_source` must be `source_read_only`.
- Never copy a platform or repository tag into `expected_algorithms`. Tags stay in `seed_tag`.
- Never fabricate accepted status, ratings, licenses, labels or hashes. If something cannot be found, leave it null and say why.
- Uncertainty is allowed. Use `label_disputed` or `needs_human_review`. Do not silently resolve it.
- You may set status up to `agent_audited`. Only a human sets `human_confirmed`.
- Respect robots.txt, rate limits and site terms. Do not automate logins or bypass bot protection.
- Do not commit third-party source bodies unless the license clearly allows it. Keep them in a gitignored cache (`benchmark/.cache/`). Commit metadata, hashes, labels and references.

## Catalog

Use only the 39 labels in `benchmark_schema.json` (`catalog_version: kiteo-39-v1`). If `engine/src/algorithms/catalog.toml` in the KiteO repo differs, stop and report the difference.

Other techniques (Greedy, Math, Implementation, Brute Force, Number Theory, Simulation, Game, Hash Map, Memoization...) are not labels. Record them in `techniques_observed` (not scored).

`expected_algorithms`: `[]` when no catalog algorithm is clearly implemented; otherwise 1 to 3 labels, dominant first. Apply the same suppression logic as the catalog (for example Tree DP over Dynamic Programming, Dijkstra over BFS).

## Per-record procedure

1. Identify the problem: `contest_id`, `problem_index`, `rating`, `rating_source` (use the official Codeforces problemset API; never guess). `repo_entry_hint` is only a discovery hint.
2. Fetch the exact source from the public repository. Pin `commit_sha`, `file_path`, `source_url`, compute `source_hash` (SHA-256 of the file bytes), record `license` (or `none found`) and `fetched_at`.
3. Verify the language matches and that the file solves that problem. Otherwise `excluded` with a reason.
4. Record `accepted_evidence` honestly (repo claim only, or a submission link).
5. Read the code. Derive TC from loops, calls, recursion and data structures. Derive SC from allocations, containers, recursion depth and copies. Use the variables n, m, q, k, V, E, A only when the code and constraints justify them.
6. Set `case_type` (worst, expected, amortized) and `test_case_semantics` (single_test, per_test, total_over_tests). Do not turn `sum(n) <= 2e5` into t*n.
7. Derive `expected_algorithms` from structural evidence. Write that evidence in `label_notes`.
8. Fill `negative_for` when the code deliberately looks like a catalog algorithm but is not (for example a nested loop that is not a sliding window).
9. Set `pair_id` when the same problem appears in both languages.
10. If the seed hint or `seed_tc`/`seed_sc` differ from your result, keep both and add the record to `needs_human_review.json`.

Canonical complexity: equivalent forms compare equal (O(mn) = O(nm)); different forms stay different (O(n + q) != O(nq)). The literal `Unknown` is a valid expected value when no sound bound can be determined from the code.

## Coverage to reach (run `node check_benchmark.mjs`)

Milestone targets (all must be met before declaring the benchmark complete):
- 150+ cases, 60+ C++, 60+ Java
- 25+ cases rated 1600 to 1800 (include 1800 for advanced detectors)
- 10+ with no catalog algorithm, 20+ multi-variable, 10+ amortized, 10+ legitimate Unknown
- 20+ cross-language pairs
- At least 3 positive and 2 negative cases per catalog label (smoke level only)
- Different authors and styles: macro-heavy C++, plain C++, STL-heavy C++, Java Scanner, BufferedReader, custom fast input, recursive and iterative versions

These smoke targets do NOT approve any detector. A label becomes eligible for `approved` only with at least 10 human-confirmed positives and 10 human-confirmed negatives in the held-out set, plus 95% precision. The checker prints which labels are eligible. Expect this to need roughly 400+ cases; do not pad with easy 800-rated problems.

Propose additional repositories (list only, with licenses and why) and wait for approval before bulk fetching.

## Split

Create `benchmark/split_manifest.json`: a deterministic, stratified 70/30 split. Sort records by a stable hash of the identity inside each stratum (language, rating band, primary label), then assign the first 30% of each stratum to held-out. Store the manifest hash. Held-out labels and sources must be kept outside the engine-development workspace (path from environment variable `KITEO_HELDOUT_DIR`) and must never be shown to whoever tunes the analyzer.

## Adapter fixtures

Use `adapter_fixtures.json`. For each platform build a sanitized minimal fixture (fixture.html, editor_state.json, expected.json) that tests platform detection, page type, editor detection, getSource, getLanguage and contest vs practice state. Pages that need login or JavaScript must be provided by me by hand; list what you need from me instead of automating logins. Mark each adapter `untested`, `mock_page`, `saved_real_page` or `live_verified`. Do not list an adapter as supported below `saved_real_page`.

Adapters only read editor state. No complexity logic in adapters.

## Deliverables

- `benchmark/corpus/` (records, no third-party source bodies), `benchmark/labels/`, `benchmark/provenance/`, `benchmark/reports/`
- `benchmark/labels/needs_human_review.json` (every record meeting a trigger listed in that file)
- `benchmark/reports/acquisition.md`: requested, fetched, failed, missing files, language mismatches, duplicates, license problems, provenance problems
- `benchmark/reports/audit.md`: counts audited, agreed with seed hint, changed, disputed, excluded; by language, rating, label, case type; Unknown and multi-variable counts
- `benchmark/reports/coverage.md`: generated from `check_benchmark.py`
- `benchmark/split_manifest.json` with its hash

## Before you report done

Run `node check_benchmark.mjs` and paste its output. Confirm: every source resolves, every hash matches, every record has a pinned commit, every label is in the catalog, every disputed record is flagged, duplicates removed, language balance checked, split locked.

Then stop. Do not start analyzer feature work from these labels until a human has confirmed the audit and the split manifest.
