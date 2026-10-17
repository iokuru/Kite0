#!/usr/bin/env node
/**
 * Split leetcode_records.json into dev and held-out records (Node.js).
 * Writes:
 *   (a) leetcode_records.dev.json inside the repo with dev records only.
 *   (b) leetcode_records.heldout.json ONLY to the directory specified by KITEO_HELDOUT_DIR.
 * Fails if KITEO_HELDOUT_DIR is unset.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const heldoutDir = process.env.KITEO_HELDOUT_DIR;
if (!heldoutDir) {
  console.error(
    'ERROR: Environment variable KITEO_HELDOUT_DIR is unset. Cannot split records without a secure heldout directory.'
  );
  process.exit(1);
}

if (!fs.existsSync(heldoutDir) || !fs.statSync(heldoutDir).isDirectory()) {
  console.error(`ERROR: KITEO_HELDOUT_DIR='${heldoutDir}' does not exist or is not a directory.`);
  process.exit(1);
}

const recPath = path.join(__dirname, 'leetcode_records.json');
if (!fs.existsSync(recPath)) {
  console.error(`ERROR: '${recPath}' does not exist.`);
  process.exit(1);
}

const data = JSON.parse(fs.readFileSync(recPath, 'utf-8'));
const records = data.records || [];
const devRecords = records.filter((r) => r.split === 'dev');
const heldoutRecords = records.filter((r) => r.split === 'heldout');

const devData = { ...data, records: devRecords };
const devPath = path.join(__dirname, 'leetcode_records.dev.json');
fs.writeFileSync(devPath, JSON.stringify(devData, null, 2), 'utf-8');

const heldoutData = { ...data, records: heldoutRecords };
const heldoutPath = path.join(heldoutDir, 'leetcode_records.heldout.json');
fs.writeFileSync(heldoutPath, JSON.stringify(heldoutData, null, 2), 'utf-8');

console.log('Split completed successfully:');
console.log(`  Dev records: ${devRecords.length} -> ${devPath}`);
console.log(`  Held-out records: ${heldoutRecords.length} -> ${heldoutPath}`);
