#!/usr/bin/env node
/**
 * KiteO benchmark checker (schema + coverage). Usage:
 *   node check_benchmark.mjs [benchmark_seed.json] [--allow-seed] [--write coverage_report.json]
 * Exit code 1 when schema errors exist or milestone targets are unmet (unless --allow-seed).
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const args = process.argv.slice(2);
const pathArg = args.find((a) => a.endsWith('.json') && !a.startsWith('--')) || 'benchmark_seed.json';
const allowSeed = args.includes('--allow-seed');
const writeIdx = args.indexOf('--write');
const out = writeIdx !== -1 ? args[writeIdx + 1] : null;
const catalogIdx = args.indexOf('--catalog');
const catalogArg = catalogIdx !== -1 ? args[catalogIdx + 1] : null;

const schemaCandidates = [
  'benchmark_schema.json',
  'benchmark/seed/benchmark_schema.json',
  path.join(__dirname, 'benchmark_schema.json'),
  path.dirname(pathArg) ? path.join(path.dirname(pathArg), 'benchmark_schema.json') : null,
];
const schemaFile = schemaCandidates.find((s) => s && fs.existsSync(s)) || 'benchmark_schema.json';
const schema = JSON.parse(fs.readFileSync(schemaFile, 'utf-8'));

const targetFile = fs.existsSync(pathArg) ? pathArg : path.join(__dirname, pathArg);
const data = JSON.parse(fs.readFileSync(targetFile, 'utf-8'));
const recs = data.records;
const CAT = new Set(schema.allowed_algorithms);
const errors = [];

// Verify catalog.toml
const catalogCandidates = catalogArg
  ? [catalogArg]
  : [
      'engine/src/algorithms/catalog.toml',
      '../../engine/src/algorithms/catalog.toml',
      '../engine/src/algorithms/catalog.toml',
      path.resolve(__dirname, '../../engine/src/algorithms/catalog.toml'),
    ];
const catalogFile = catalogCandidates.find((c) => c && fs.existsSync(c)) || null;
let CATALOG_ALL_NAMES = new Set();
if (catalogFile) {
  const catContent = fs.readFileSync(catalogFile, 'utf-8');
  const matches = catContent.matchAll(/name\s*=\s*"([^"]+)"/g);
  for (const m of matches) {
    CATALOG_ALL_NAMES.add(m[1]);
  }
  for (const l of Array.from(CAT).sort()) {
    if (!CATALOG_ALL_NAMES.has(l)) {
      errors.push(`catalog.toml mismatch: scored label '${l}' missing or renamed in ${catalogFile}`);
    }
  }
} else if (catalogArg) {
  errors.push(`Specified catalog file not found: ${catalogArg}`);
}

const ALLOWED_PLAIN_TECHNIQUES = new Set([
  'Greedy',
  'Math',
  'Implementation',
  'Brute Force',
  'Number Theory',
  'Simulation',
  'Game',
  'Hash Map',
  'Memoization',
  'Binary Exponentiation',
  'Bit Manipulation',
  'Combinatorics',
  'Geometry',
  'Constructive',
  'Recursion',
  'Interactive',
  'String',
  'Graph',
  'Trees',
  'DP',
]);
const ALLOWED_TECHNIQUES = new Set([...CATALOG_ALL_NAMES, ...ALLOWED_PLAIN_TECHNIQUES]);

function canon(tc) {
  if (tc === null || tc === undefined || tc === 'Unknown') return tc;
  const s = tc.replace(/\s+/g, '');
  const m = s.match(/^O\((.*)\)$/);
  if (!m) return 'INVALID';
  const body = m[1];
  const terms = body.split(/\+(?![^()]*\))/);
  const outTerms = [];
  for (const t of terms) {
    const letters = t.match(/^([nmqkVEA]+)$/);
    outTerms.push(letters ? letters[1].split('').sort().join('') : t);
  }
  return 'O(' + outTerms.sort().join('+') + ')';
}

const ids = new Set();
for (const r of recs) {
  const st = r.status;
  if (ids.has(r.id)) errors.push(`${r.id}: duplicate id`);
  ids.add(r.id);
  if (!schema.allowed_status.includes(st)) errors.push(`${r.id}: bad status ${st}`);

  const need = st === 'seed_only' ? schema.seed_required_fields : schema.final_required_fields;
  for (const f of need) {
    if (!(f in r)) errors.push(`${r.id}: missing field ${f}`);
  }

  if (schema.final_required_when_status_in.includes(st)) {
    for (const f of [
      'commit_sha',
      'file_path',
      'source_hash',
      'license',
      'fetched_at',
      'source_url',
      'contest_id',
      'problem_index',
    ]) {
      if (!r[f]) errors.push(`${r.id}: ${f} empty for status ${st}`);
    }
  }

  const a = schema.audit_fields_required_when_status_in;
  if (a.statuses.includes(st)) {
    for (const f of a.fields) {
      if (r[f] === null || r[f] === undefined) errors.push(`${r.id}: ${f} is null for audited status ${st}`);
    }
    if (r.audit_source !== 'source_read_only') errors.push(`${r.id}: audit_source must be source_read_only`);
  }

  if (st === 'human_confirmed' && !r.audited_by) {
    errors.push(`${r.id}: human_confirmed needs a human in audited_by`);
  }

  const ea = r.expected_algorithms;
  if (ea) {
    if (ea.length > 3) errors.push(`${r.id}: more than 3 expected_algorithms`);
    for (const l of ea) {
      if (!CAT.has(l)) errors.push(`${r.id}: label outside catalog: ${l}`);
    }
  }

  for (const l of r.negative_for || []) {
    if (!CAT.has(l)) errors.push(`${r.id}: negative_for label outside catalog: ${l}`);
  }

  for (const t of r.techniques_observed || []) {
    if (!ALLOWED_TECHNIQUES.has(t)) {
      errors.push(`${r.id}: techniques_observed contains invalid technique: '${t}'`);
    }
  }

  for (const k of ['expected_tc', 'expected_sc']) {
    if (r[k] !== null && r[k] !== undefined && canon(r[k]) === 'INVALID') {
      errors.push(`${r.id}: ${k} not canonical: ${r[k]}`);
    }
  }

  if (!schema.allowed_case_type.includes(r.case_type)) errors.push(`${r.id}: bad case_type`);
  if (!schema.allowed_test_case_semantics.includes(r.test_case_semantics)) errors.push(`${r.id}: bad test_case_semantics`);
  if (r.source_hash && !r.commit_sha) errors.push(`${r.id}: source_hash without commit_sha`);
}

const audited = recs.filter((r) => ['peer_reviewed', 'human_confirmed'].includes(r.status));
const confirmed = recs.filter((r) => r.status === 'human_confirmed');
function countMatch(f, pool) {
  return pool.filter(f).length;
}

const M = {
  total_cases_150: [recs.length, 150],
  cpp_60: [countMatch((r) => r.language === 'cpp', recs), 60],
  java_60: [countMatch((r) => r.language === 'java', recs), 60],
  rating_1600_1800_25: [countMatch((r) => r.rating && r.rating >= 1600 && r.rating <= 1800, recs), 25],
  no_catalog_algorithm_10: [countMatch((r) => Array.isArray(r.expected_algorithms) && r.expected_algorithms.length === 0, audited), 10],
  multi_variable_20: [countMatch((r) => r.variables && r.variables.length >= 2, audited), 20],
  amortized_10: [countMatch((r) => r.case_type === 'amortized', audited), 10],
  legit_unknown_10: [
    countMatch((r) => r.expected_tc === 'Unknown' || r.expected_sc === 'Unknown', audited),
    10,
  ],
  paired_cpp_java_20: [new Set(recs.filter((r) => r.pair_id).map((r) => r.pair_id)).size, 20],
};

const per = {};
for (const l of Array.from(CAT).sort()) {
  const pos = audited.filter((r) => (r.expected_algorithms || []).includes(l));
  const neg = audited.filter((r) => (r.negative_for || []).includes(l));
  const hpos = confirmed.filter((r) => r.split === 'heldout' && (r.expected_algorithms || []).includes(l));
  const hneg = confirmed.filter((r) => r.split === 'heldout' && (r.negative_for || []).includes(l));
  per[l] = {
    audited_positive: pos.length,
    audited_negative: neg.length,
    smoke_target: 3,
    smoke_met: pos.length >= 3 && neg.length >= 2,
    heldout_confirmed_positive: hpos.length,
    heldout_confirmed_negative: hneg.length,
    approval_eligible: hpos.length >= 10 && hneg.length >= 10,
  };
}

function countBy(arr, keyFn) {
  const map = {};
  for (const item of arr) {
    const k = keyFn(item);
    map[k] = (map[k] || 0) + 1;
  }
  return map;
}

const milestoneTargets = {};
for (const [k, v] of Object.entries(M)) {
  milestoneTargets[k] = { have: v[0], need: v[1], met: v[0] >= v[1] };
}

const report = {
  schema_version: schema.schema_version,
  catalog_version: schema.catalog_version,
  counts: {
    total: recs.length,
    by_status: countBy(recs, (r) => r.status),
    by_language: countBy(recs, (r) => r.language),
    by_rating: countBy(recs, (r) => String(r.rating)),
    audited: audited.length,
    human_confirmed: confirmed.length,
    heldout: countMatch((r) => r.split === 'heldout', recs),
  },
  milestone_targets: milestoneTargets,
  per_label: per,
  approval_gate:
    'A label may be marked approved in catalog.toml only when approval_eligible is true AND its detector reaches >=95% precision on the human-confirmed held-out set.',
  schema_errors: errors.slice(0, 200),
  schema_error_count: errors.length,
};

const txt = JSON.stringify(report, null, 2);
if (out) fs.writeFileSync(out, txt, 'utf-8');
console.log(txt);

const unmet = Object.entries(milestoneTargets).filter(([_, v]) => !v.met);
console.error(
  `\nSCHEMA ERRORS: ${errors.length}   UNMET MILESTONE TARGETS: ${unmet.length}   APPROVAL-ELIGIBLE LABELS: ${
    Object.values(per).filter((v) => v.approval_eligible).length
  }/39`
);

process.exit(errors.length > 0 || (unmet.length > 0 && !allowSeed) ? 1 : 0);
