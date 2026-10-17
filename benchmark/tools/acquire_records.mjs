#!/usr/bin/env node
/**
 * Acquisition tool for KiteO benchmark records (Node.js).
 * Reproduces exact source acquisition, commit pinning, and SHA-256 hashing.
 */

import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const SEED_PATH = path.resolve(__dirname, '../seed/benchmark_seed.json');
const CACHE_DIR = path.resolve(__dirname, '../.cache');
const REPOS_DIR = path.join(CACHE_DIR, 'repos');

const PINNED_COMMITS = {
  'https://github.com/yousefkotp/Codeforces-Solutions': 'e3aae5f36c76bf2babad849929f389de0a8cfb6f',
  'https://github.com/Rohit0301/codeforces': '0480b9386512eba34d3eaba5d30ec8c8da6c185c',
};

function verifyAndHash() {
  const data = JSON.parse(fs.readFileSync(SEED_PATH, 'utf-8'));
  const fetchedRecords = data.records.filter((r) => r.status === 'fetched');
  console.log(`Loaded ${fetchedRecords.length} fetched records from ${SEED_PATH}`);

  let mismatches = 0;
  for (const r of fetchedRecords) {
    const rid = r.id;
    const expectedHash = r.source_hash;
    const lang = r.language;
    const fpath = r.file_path;
    const repoUrl = r.repo_url;
    const expectedCommit = PINNED_COMMITS[repoUrl];

    if (r.commit_sha !== expectedCommit) {
      console.log(`[${rid}] COMMIT MISMATCH: ${r.commit_sha} != ${expectedCommit}`);
      mismatches++;
      continue;
    }

    let cachedFile = path.join(CACHE_DIR, `${rid}.${lang === 'cpp' ? 'cpp' : 'java'}`);
    if (!fs.existsSync(cachedFile)) {
      const repoName = lang === 'cpp' ? 'yousefkotp' : 'Rohit0301';
      cachedFile = path.join(REPOS_DIR, repoName, ...fpath.split('/'));
    }

    if (!fs.existsSync(cachedFile)) {
      console.log(`[${rid}] FILE NOT FOUND: ${cachedFile}`);
      mismatches++;
      continue;
    }

    const rawBytes = fs.readFileSync(cachedFile);
    const computedHash = crypto.createHash('sha256').update(rawBytes).digest('hex');

    if (computedHash !== expectedHash) {
      console.log(`[${rid}] HASH MISMATCH: computed ${computedHash} != expected ${expectedHash}`);
      mismatches++;
    } else {
      console.log(`[${rid}] OK: ${computedHash.slice(0, 16)}... size=${rawBytes.length} bytes (${fpath})`);
    }
  }

  if (mismatches === 0) {
    console.log('\nAll records verified successfully! SHA-256 hashes reproduce exactly.');
  } else {
    console.log(`\nVerification FAILED with ${mismatches} mismatches.`);
    process.exit(1);
  }
}

verifyAndHash();
