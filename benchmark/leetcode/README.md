# KiteO LeetCode Dataset Kit

Builds a real-code dataset from solutions YOU write or already have accepted on LeetCode. No scraping, no third-party source, no problem statements.

KiteO is rule-based, so "training" here means: build a labeled dev set to improve the rules, and a held-out set to measure honestly. Never tune against the held-out set.

## Workflow

1. Open `leetcode_problem_list.csv`. It lists 69 free problems covering the 39 catalog labels (verify each slug on LeetCode; skip anything that has become premium).
2. For each problem, put your own accepted solutions in `submissions/`:
   `<slug>__<approach>.<cpp|java>`   approach = optimal, brute, alt, alt2
   Collect at least a brute force AND an optimal solution when you can. The brute/optimal pair is what teaches the engine to tell O(n^2) from O(n).
   Copy from your own LeetCode "Submissions" page, one by one, by hand. Do not scrape. Do not add solutions you did not write.
3. Run `python ingest_leetcode.py`. It creates `leetcode_records.json` and `label_sheet.csv`. The sheet shows each solution's entry signature (the method signature gives the sizes: nums.size(), s.length(), ...).
4. Open `label_sheet.csv` in a spreadsheet and fill, for each solution, from reading the CODE (not from the problem title and not from KiteO's output): expected_tc, expected_sc, expected_algorithms, variables, case_type, label_notes. Add negative_for for look-alikes. Put "yes" in confirmed only after you checked it.
5. Run `python merge_labels.py`. It validates, assigns the split, and prints coverage. Fix errors and repeat.

## Rules for labels

- expected_algorithms: only the 39 catalog labels, at most 3. Anything else (Greedy, Hash Map, Math...) goes in techniques_observed. An empty list means KiteO should output no label.
- Complexity: use n, m, q, k, V, E for sizes and A for value ranges. Space means auxiliary space (input and returned result not counted). Use the literal Unknown when no sound bound can be established.
- Label what the submitted code does, not what the optimal solution would do. A brute-force solution is O(n^2) even if the problem has an O(n) solution.
- Not sure? Leave confirmed blank. It becomes needs_human_review and is excluded from scoring.

## Split

`merge_labels.py` puts all solutions of the same problem (both languages, all approaches) on the same side, so held-out solutions never share a problem with development ones. Roughly 30% of problems are held out. Keep the held-out records out of the folder that you or an agent use while tuning.

## Legal and safety

- **Private Backup Note**: `leetcode_records.json` and `label_sheet.csv` are gitignored to prevent accidental public disclosure of personal benchmark solutions and labels. Keep a private backup of your filled `leetcode_records.json` and `label_sheet.csv` outside this repository.
- Only your own solutions. Do not commit problem statements or other people's code. Keep `submissions/` out of any public repo unless you are happy to publish your own code.
- LeetCode's terms restrict automated scraping. Use manual copying.
- Use practice only. Do not capture or analyze problems from a live contest.
- Public datasets and GitHub solution repos can add volume, but check each license before use, and audit labels the same way.

## Targets

- 69 problems x (brute + optimal) x (C++ + Java) is about 270 solutions. Start with 30 problems.
- Aim for 10+ human-confirmed positives and 10+ look-alike negatives per label before approving any detector, with 95% precision on held-out.
- Add problems your engine currently gets wrong. Do not add only easy ones.

## Files

- `leetcode_problem_list.csv`: suggested problems and hints (hints are NOT labels)
- `ingest_leetcode.py`, `merge_labels.py`: tools (Python 3, no packages)
- `benchmark_schema.json`: catalog and conventions shared with the Codeforces benchmark
- `examples/`: three sample solutions to test the tools
