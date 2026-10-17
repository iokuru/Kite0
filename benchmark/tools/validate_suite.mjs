#!/usr/bin/env node
/**
 * Benchmark Suite Validator.
 *
 * Validates integrity, schema compliance, and language parity across Kite0 benchmark corpora:
 * - snippets.json (Canonical Dev Suite, 152 cases)
 * - dev2.json (Synthetic Stress Suite, 70 cases)
 * - tough_benchmark.json (Comprehensive OA Taxonomy Suite, 500 cases)
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const CORPUS_DIR = path.resolve(__dirname, '..', 'corpus');

const SUITES = {
  'snippets.json': { expectedCases: 152, expectedProblems: 76 },
  'dev2.json': { expectedCases: 70, expectedProblems: 35 },
  'tough_benchmark.json': { expectedCases: 500, expectedProblems: 250 },
};

function validateCorpus(filename, expectedCases, expectedProblems) {
  const filepath = path.join(CORPUS_DIR, filename);
  if (!fs.existsSync(filepath)) {
    console.error(`[-] Missing corpus file: ${filepath}`);
    return false;
  }

  const cases = JSON.parse(fs.readFileSync(filepath, 'utf-8'));
  const actualLen = cases.length;
  if (actualLen !== expectedCases) {
    console.error(`[-] ${filename}: Expected ${expectedCases} cases, found ${actualLen}`);
    return false;
  }

  const ids = cases.map((c) => c.id);
  const uniqueIds = new Set(ids);
  if (ids.length !== uniqueIds.size) {
    console.error(`[-] ${filename}: Duplicate IDs found!`);
    return false;
  }

  const cppCount = cases.filter((c) => c.language === 'cpp').length;
  const javaCount = cases.filter((c) => c.language === 'java').length;
  if (cppCount !== expectedProblems || javaCount !== expectedProblems) {
    console.error(`[-] ${filename}: Language mismatch (cpp: ${cppCount}, java: ${javaCount})`);
    return false;
  }

  console.log(`[+] ${filename}: ${actualLen} cases (${expectedProblems} problems) verified successfully.`);
  return true;
}

function main() {
  console.log('=== Validating Kite0 Benchmark Corpora ===');
  let allOk = true;
  for (const [filename, config] of Object.entries(SUITES)) {
    const ok = validateCorpus(filename, config.expectedCases, config.expectedProblems);
    if (!ok) allOk = false;
  }

  if (allOk) {
    console.log('=== All benchmark corpora valid! ===');
    process.exit(0);
  } else {
    console.error('=== Benchmark validation failed! ===');
    process.exit(1);
  }
}

main();
