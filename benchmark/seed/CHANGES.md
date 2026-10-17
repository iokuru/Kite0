# Changes from v2 to v3

Problems found in v2 and what v3 does about them.

1. Catalog mismatch. v2 used the old 26 labels while the KiteO repo (ADR 0010) uses 39. v3 uses the 39 and names the repo's catalog.toml as the source of truth.
2. Fake negatives. v2 set `expected_algorithms` to `[]` for 60 records and copied the tag into the other 20, which looks audited but is not. v3 uses `null` (pending) for all, and keeps the tag in `seed_algorithm_hint` only.
3. Schema did not fit the records. 80/80 records lacked `contest_id`, `problem_index`, `source_url`, `expected_tc`, `expected_sc`, so a validator would fail every one. v3 has a seed tier and a final tier, and the checker enforces them by status.
4. No automated checker existed. v3 ships `check_benchmark.mjs`.
5. Wrong coverage targets. Three positives per label cannot approve a detector (the gate needs 10 held-out positives and 10 negatives). v3 separates smoke targets from the approval gate and reports eligibility per label.
6. Missing negatives. v3 adds `negative_for` for look-alike cases.
7. "Audited" overstated. v3 splits preliminary `peer_reviewed` from `human_confirmed`; only the latter is locked ground truth.
8. Lost audit facts. Greedy, Math and similar were discarded. v3 adds `techniques_observed` (unscored).
9. Vague multi-test semantics. v3 adds `test_case_semantics`.
10. Identity and acceptance. v3 adds `rating_source`, `accepted_evidence`, `pair_id` (C++/Java equivalence) and keeps `repo_entry` as `repo_entry_hint` only.
11. Split. v3 requires a stratified deterministic split with held-out labels kept outside the engine workspace.
12. Adapter fixtures. v2 used home pages and static HTML ideas that cannot represent Monaco. v3 defines a fixture format (minimal DOM plus editor-state stub), marks pages needing login as user-captured, forbids automated logins and bot-protection bypass, adds support-status levels, and flags URLs as unverified.
13. Role separation. The benchmark auditor must not tune the analyzer rules while reviewing ground truth.

Still true of the data itself: only 3 of 80 records are rated 1600 or above, 6 have no rating, and there are 2 source repositories. Expanding that is part of the task.
