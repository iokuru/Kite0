#!/usr/bin/env node
/**
 * Turn your own LeetCode solution files into KiteO benchmark records (Node.js).
 * Usage: node ingest_leetcode.mjs [submissions_dir] [--out leetcode_records.json] [--sheet label_sheet.csv]
 */

import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const args = process.argv.slice(2).filter((a) => !a.startsWith('--'));
const subDir = args[0] || path.join(__dirname, 'submissions');

function opt(name, def) {
  const argv = process.argv.slice(2);
  const idx = argv.indexOf(name);
  return idx !== -1 && argv[idx + 1] ? argv[idx + 1] : def;
}

const out = opt('--out', path.join(__dirname, 'leetcode_records.json'));
const sheet = opt('--sheet', path.join(__dirname, 'label_sheet.csv'));
const LANG = { '.cpp': 'cpp', '.java': 'java' };
const APPROACH = new Set(['optimal', 'brute', 'alt', 'alt2']);

function entryCpp(src) {
  const m = src.match(/public\s*:/);
  const body = m ? src.slice(m.index + m[0].length) : src;
  const regex = /^\s*(?:static\s+)?([A-Za-z_][\w:<>,\s*&]*?)\s+([A-Za-z_]\w*)\s*\(([^)]*)\)\s*(?:const\s*)?\{/gm;
  let match;
  while ((match = regex.exec(body)) !== null) {
    if (['if', 'for', 'while', 'switch', 'return', 'catch'].includes(match[2])) continue;
    return `${match[1].trim()} ${match[2]}(${match[3].replace(/\s+/g, ' ').trim()})`;
  }
  return null;
}

function entryJava(src) {
  const regex = /public\s+(?:static\s+)?([\w<>[\]\s,?]+?)\s+(\w+)\s*\(([^)]*)\)\s*(?:throws [\w, ]+)?\{/gm;
  let match;
  while ((match = regex.exec(src)) !== null) {
    if (['class', 'interface', 'enum'].includes(match[1].trim())) continue;
    return `${match[1].trim()} ${match[2]}(${match[3].replace(/\s+/g, ' ').trim()})`;
  }
  return null;
}

const records = fs.existsSync(out) ? JSON.parse(fs.readFileSync(out, 'utf-8')).records || [] : [];
const have = new Set(records.map((r) => r.id));
let added = 0;

if (fs.existsSync(subDir) && fs.statSync(subDir).isDirectory()) {
  const files = fs.readdirSync(subDir).sort();
  for (const fn of files) {
    const ext = path.extname(fn);
    if (!LANG[ext]) continue;
    const base = path.basename(fn, ext);
    if (!base.includes('__')) continue;

    const [slug, approach] = base.split('__');
    if (!APPROACH.has(approach)) continue;

    const rid = `lc-${LANG[ext]}-${slug}-${approach}`;
    if (have.has(rid)) continue;

    const filePath = path.join(subDir, fn);
    const data = fs.readFileSync(filePath);
    const src = data.toString('utf-8');
    const sig = ext === '.cpp' ? entryCpp(src) : entryJava(src);

    records.push({
      id: rid,
      platform: 'leetcode',
      problem_slug: slug,
      language: LANG[ext],
      approach,
      source_file: filePath.replace(/\\/g, '/'),
      source_hash: crypto.createHash('sha256').update(data).digest('hex'),
      provenance: 'own_submission',
      license: 'own work',
      accepted_evidence: 'user_attested_not_verified',
      entry_signature: sig,
      constraints_note: null,
      expected_tc: null,
      expected_sc: null,
      expected_algorithms: null,
      techniques_observed: null,
      variables: null,
      case_type: 'pending',
      negative_for: null,
      label_notes: '',
      status: 'fetched',
      split: null,
    });
    have.add(rid);
    added++;
  }
}

fs.writeFileSync(
  out,
  JSON.stringify(
    { schema: 'kiteo-leetcode-1', catalog_version: 'kiteo-39-v1', records },
    null,
    2
  ),
  'utf-8'
);

console.log(`Ingest complete. Added ${added} new records. Total records: ${records.length}`);
