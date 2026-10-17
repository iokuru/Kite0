#!/usr/bin/env node
/**
 * Merge filled label_sheet.csv into leetcode_records.json, validate, assign split, print coverage (Node.js).
 * Usage: node merge_labels.mjs [--records leetcode_records.json] [--sheet label_sheet.csv] [--schema benchmark_schema.json]
 */

import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const args = process.argv.slice(2);
function opt(name, def) {
  const idx = args.indexOf(name);
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : def;
}

const recPath = opt('--records', path.join(__dirname, 'leetcode_records.json'));
const sheet = opt('--sheet', path.join(__dirname, 'label_sheet.csv'));
const schemaPath = opt('--schema', path.join(__dirname, 'benchmark_schema.json'));

const FALLBACK = [
  'Two Pointers', 'Fast and Slow Pointers', 'Sliding Window', 'Prefix Sum', 'Difference Array',
  'Binary Search', 'Binary Search on Answer', 'Sorting', "Kadane's Algorithm", 'Coordinate Compression',
  'Monotonic Stack', 'Monotonic Queue', 'Heap / Priority Queue', 'Top K', 'Two Heaps',
  'Cycle Detection', 'Linked List Reversal', 'DFS', 'BFS', 'DSU', 'Dijkstra', 'MST',
  'Topological Sort', 'Strongly Connected Components', 'LCA', 'Binary Lifting', 'Trie',
  'Dynamic Programming', 'Tree DP', 'Bitmask DP', 'Backtracking', 'Divide and Conquer',
  'Fenwick Tree', 'Segment Tree', 'Sparse Table', 'Sieve', 'KMP', 'Z Algorithm', 'Rolling Hash',
];

const CAT = new Set(
  fs.existsSync(schemaPath)
    ? JSON.parse(fs.readFileSync(schemaPath, 'utf-8')).allowed_algorithms
    : FALLBACK
);

const VARS = new Set(['n', 'm', 'q', 'k', 'V', 'E', 'A']);
const CASES = new Set(['worst', 'expected', 'amortized']);
const splitList = (s) => (s ? s.split(';').map((x) => x.trim()).filter(Boolean) : []);
const TC_PATTERN = /^(O\(.+\)|Unknown)$/;

if (!fs.existsSync(recPath)) {
  console.log(`Records file ${recPath} does not exist yet.`);
  process.exit(0);
}

const data = JSON.parse(fs.readFileSync(recPath, 'utf-8'));
const recs = {};
for (const r of data.records || []) {
  recs[r.id] = r;
}

const errors = [];
if (fs.existsSync(sheet)) {
  const content = fs.readFileSync(sheet, 'utf-8');
  const lines = content.split('\n').filter((l) => l.trim());
  if (lines.length > 1) {
    const headers = lines[0].split(',').map((h) => h.trim());
    for (let i = 1; i < lines.length; i++) {
      const parts = lines[i].split(',').map((p) => p.trim());
      const row = {};
      headers.forEach((h, idx) => (row[h] = parts[idx] || ''));

      const r = recs[row.id];
      if (!r) {
        errors.push(`${row.id}: not in records`);
        continue;
      }
      if (!row.expected_tc && !row.expected_sc) continue;

      const before = errors.length;
      const tc = row.expected_tc;
      const sc = row.expected_sc;
      if (!row.label_notes) errors.push(`${row.id}: label_notes empty: write one line of structural evidence`);
      if (!TC_PATTERN.test(tc)) errors.push(`${row.id}: expected_tc not O(...) or Unknown: ${tc}`);
      if (!TC_PATTERN.test(sc)) errors.push(`${row.id}: expected_sc not O(...) or Unknown: ${sc}`);

      const algos =
        row.expected_algorithms.toUpperCase() === 'NONE' || !row.expected_algorithms
          ? []
          : splitList(row.expected_algorithms);
      if (algos.length > 3) errors.push(`${row.id}: more than 3 expected_algorithms`);
      for (const a of algos) {
        if (!CAT.has(a)) errors.push(`${row.id}: label outside catalog: '${a}'`);
      }

      const neg = splitList(row.negative_for);
      for (const a of neg) {
        if (!CAT.has(a)) errors.push(`${row.id}: negative_for outside catalog: '${a}'`);
      }

      const vs = splitList(row.variables);
      for (const v of vs) {
        if (!VARS.has(v)) errors.push(`${row.id}: variable '${v}' invalid`);
      }

      const ct = row.case_type;
      if (!CASES.has(ct)) errors.push(`${row.id}: case_type must be worst|expected|amortized`);

      if (errors.length > before) continue;

      Object.assign(r, {
        expected_tc: tc,
        expected_sc: sc,
        expected_algorithms: algos,
        techniques_observed: splitList(row.techniques_observed),
        variables: vs,
        case_type: ct,
        negative_for: neg,
        label_notes: row.label_notes,
        constraints_note: row.constraints_note_own_words || null,
        status: row.confirmed.toLowerCase() === 'yes' ? 'human_confirmed' : 'needs_human_review',
      });
    }
  }
}

// Leakage-safe split: all records of the same problem go to the same side
for (const r of Object.values(recs)) {
  const hash = crypto.createHash('sha256').update(r.problem_slug).digest('hex');
  const h = parseInt(hash.slice(0, 8), 16) % 10;
  r.split = h < 3 ? 'heldout' : 'dev';
}

data.records = Object.values(recs);
fs.writeFileSync(recPath, JSON.stringify(data, null, 2), 'utf-8');

if (errors.length > 0) {
  console.error(`Validation errors found (${errors.length}):`);
  errors.forEach((e) => console.error(`  - ${e}`));
  process.exit(1);
} else {
  console.log(`Merged and validated successfully. Total records: ${data.records.length}`);
}
