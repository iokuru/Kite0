# KiteO Benchmark Audit Specification (v3)

This specification defines the ground-truth audit protocol, data acquisition standards, and verification guidelines for KiteO benchmark records and platform adapters. KiteO evaluates implementation-level static complexity (Time Complexity, Space Complexity, Algorithmic Technique) on C++ and Java competitive programming solutions.

The benchmark tests AST structural analysis, not heuristic problem-name recognition. Auditors must adhere strictly to ground-truth labeling standards and must not tune analyzer heuristics while establishing baseline truth.

## Ground Rules

- The package seed is NOT ground truth. All records start as `seed_only`; `expected_*` fields are `null` until individually audited. Never treat `null` as `[]`.
- Never run KiteO to decide a ground-truth label. Labels must be derived by independent static code inspection (`audit_source: source_read_only`).
- Platform tags or problem classification metadata must never be blindly copied into `expected_algorithms`. External hints remain in `seed_tag`.
- Never fabricate acceptance status, problem ratings, licenses, labels, or hashes. If an attribute cannot be definitively verified, leave it `null` with rationale recorded in `label_notes`.
- Genuine ambiguity must be marked as `label_disputed` or `needs_human_review`. Do not arbitrarily guess.
- Preliminary audit status is marked as `peer_reviewed`. Only verified engineering review confirms `human_confirmed` (authoritative ground truth).
- Respect upstream service constraints, rate limits, and site terms. Do not automate credentialed access or bypass security controls.
- Third-party source bodies are cached in gitignored local directories (`benchmark/.cache/`). Only repository metadata, checksums, verified labels, and structural signatures are tracked in source control.

## Algorithmic Catalog

Use only the authoritative labels defined in `benchmark_schema.json` and mirrored in `engine/src/algorithms/catalog.toml`.

General techniques (e.g., Greedy, Math, Implementation, Brute Force, Simulation) are broad programming classifications rather than specific structural algorithmic techniques; record them in `techniques_observed` (unscored metadata).

`expected_algorithms`:
- `[]` when no catalog algorithm is structurally present.
- Otherwise, 1 to 3 dominant algorithmic labels, applying standard suppression logic (e.g., Tree DP suppresses Dynamic Programming; Dijkstra suppresses Breadth-First Search).

## Per-Record Audit Procedure

1. **Problem Identification**: Determine `contest_id`, `problem_index`, `rating`, and `rating_source` (via authoritative problemset APIs). `repo_entry_hint` serves strictly as discovery guidance.
2. **Source Pinning**: Fetch the solution source from public repository history. Record `commit_sha`, `file_path`, `source_url`, compute `source_hash` (SHA-256 of raw file bytes), and record `license`.
3. **Integrity Check**: Verify language compatibility and that the solution solves the target problem. If incompatible, mark as `excluded` with explicit reason.
4. **Acceptance Evidence**: Record verification evidence (repository claim or verified submission record).
5. **Asymptotic Derivation**:
   - Derive Time Complexity ($TC$) from loop structures, function invocations, recurrence relations, and library primitives.
   - Derive Space Complexity ($SC$) from auxiliary allocations, container capacities, recursion stack frames, and buffer cloning. Use standard asymptotic variables ($n, m, q, k, V, E, A$) only when justified by input parameters and problem constraints.
6. **Execution Semantics**: Specify `case_type` (`worst`, `expected`, `amortized`) and `test_case_semantics` (`single_test`, `per_test`, `total_over_tests`).
7. **Algorithmic Technique**: Identify catalog techniques from concrete AST evidence and document reasoning in `label_notes`.
8. **Negative Discrimination**: Populate `negative_for` when the code resembles a catalog algorithm superficially but implements a different pattern (e.g., a nested pointer loop that is not a sliding window).
9. **Cross-Language Validation**: Set `pair_id` when equivalent solutions for the identical problem exist in both C++ and Java.
10. **Review Triggers**: If any derived metric diverges from initial seed hints, flag the record in `needs_human_review.json`.

Complexity equivalence: mathematically isomorphic representations compare equal ($O(mn) \equiv O(nm)$); distinct parameter bounds remain distinct ($O(n + q) \not\equiv O(nq)$). The literal `Unknown` is the sound expected value when asymptotic bounds cannot be established from source structure.

## Quality and Coverage Gates

Run `node check_benchmark.mjs` to verify benchmark compliance against target gates:
- 150+ audited cases (balanced $\ge 60$ C++ and $\ge 60$ Java).
- 25+ problems in the 1600–1800 rating band.
- 10+ baseline cases with no catalog algorithm, 20+ multi-variable constraints, 10+ amortized patterns, 10+ sound `Unknown` fallbacks.
- 20+ cross-language pairs.
- Minimum 3 positive and 2 negative look-alike cases per catalog technique for smoke-test validation.

A detector is eligible for `approved` status in `catalog.toml` only when evaluated against at least 10 verified positive and 10 negative cases in held-out evaluation with $\ge 95\%$ precision.

## Partitioning & Held-Out Isolation

Benchmark splits must use deterministic, stratified 70/30 partitioning (`benchmark/split_manifest.json`) keyed by SHA-256 problem identity within each language, rating tier, and primary label stratum. Held-out test cases must be stored outside the active analyzer tuning path (`KITEO_HELD_OUT_DIR`) to prevent data leakage.

## Adapter Fixture Specifications

Platform adapter tests use minimal, deterministic fixtures (`fixture.html`, `editor_state.json`, `expected.json`) validating URL matching, DOM editor discovery, source extraction, and contest status detection without external network dependencies.
