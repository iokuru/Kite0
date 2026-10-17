#!/usr/bin/env node
/**
 * Kite0 Empirical Complexity Validator (Node.js).
 * Compares predicted asymptotic bounds with measured wall-clock power-law scaling (Δ ln T / Δ ln N).
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { performance } from 'perf_hooks';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..', '..');

function runConstant(n) {
  return n % 2 === 0 && n > 2;
}

function runLogarithmic(n) {
  let cnt = 0;
  let i = n;
  while (i > 0) {
    cnt++;
    i = Math.floor(i / 2);
  }
  return cnt;
}

function runLinear(n) {
  let s = 0;
  for (let i = 0; i < n; i++) {
    s += i;
  }
  return s;
}

function runLinearithmic(n) {
  const a = new Int32Array(n);
  for (let i = 0; i < n; i++) {
    a[i] = n - i;
  }
  a.sort();
  return a[0];
}

function runQuadratic(n) {
  let s = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      s += i ^ j;
    }
  }
  return s;
}

function runCubic(n) {
  let s = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      for (let k = 0; k < n; k++) {
        s += (i + j + k) & 1;
      }
    }
  }
  return s;
}

const BENCHMARKS = [
  {
    name: 'Constant O(1)',
    predicted: 'O(1)',
    expectedExponent: 0.0,
    func: runConstant,
    sizes: [100000, 200000, 400000, 800000],
    tolerance: 0.25,
  },
  {
    name: 'Logarithmic O(log n)',
    predicted: 'O(log n)',
    expectedExponent: 0.0,
    func: runLogarithmic,
    sizes: [1000000, 2000000, 4000000, 8000000],
    tolerance: 0.25,
  },
  {
    name: 'Linear O(n)',
    predicted: 'O(n)',
    expectedExponent: 1.0,
    func: runLinear,
    sizes: [2000000, 4000000, 8000000, 16000000],
    tolerance: 0.35,
  },
  {
    name: 'Linearithmic O(n log n)',
    predicted: 'O(n log n)',
    expectedExponent: 1.1,
    func: runLinearithmic,
    sizes: [50000, 100000, 200000, 400000],
    tolerance: 0.35,
  },
  {
    name: 'Quadratic O(n^2)',
    predicted: 'O(n^2)',
    expectedExponent: 2.0,
    func: runQuadratic,
    sizes: [1000, 2000, 4000, 8000],
    tolerance: 0.45,
  },
  {
    name: 'Cubic O(n^3)',
    predicted: 'O(n^3)',
    expectedExponent: 3.0,
    func: runCubic,
    sizes: [80, 160, 320, 640],
    tolerance: 0.6,
  },
];

function measureTime(func, n, repeats = 2) {
  func(Math.min(n, 50));
  let best = Infinity;
  for (let r = 0; r < repeats; r++) {
    const start = performance.now();
    func(n);
    const duration = (performance.now() - start) / 1000.0;
    if (duration < best) {
      best = duration;
    }
  }
  return best;
}

function computeScalingExponent(sizes, times) {
  const logN = sizes.map((s) => Math.log(s));
  const logT = times.map((t) => Math.log(Math.max(t, 1e-9)));
  const meanN = logN.reduce((a, b) => a + b, 0) / logN.length;
  const meanT = logT.reduce((a, b) => a + b, 0) / logT.length;

  let numerator = 0;
  let denominator = 0;
  for (let i = 0; i < sizes.length; i++) {
    numerator += (logN[i] - meanN) * (logT[i] - meanT);
    denominator += (logN[i] - meanN) ** 2;
  }
  return denominator === 0 ? 0.0 : numerator / denominator;
}

function main() {
  console.log('='.repeat(80));
  console.log('                  KITEO EMPIRICAL COMPLEXITY VALIDATOR                 ');
  console.log('='.repeat(80));

  const results = [];
  let allPassed = true;

  for (const bench of BENCHMARKS) {
    const times = [];
    for (const s of bench.sizes) {
      const t = measureTime(bench.func, s);
      times.append ? times.append(t) : times.push(t);
    }

    const alpha = computeScalingExponent(bench.sizes, times);
    const expected = bench.expectedExponent;
    const tol = bench.tolerance;

    let passed = false;
    if (expected === 0.0) {
      passed = alpha <= expected + tol + 0.15;
    } else {
      passed = Math.abs(alpha - expected) <= tol;
    }

    const status = passed ? 'PASS' : 'FAIL';
    if (!passed) allPassed = false;

    results.push({
      name: bench.name,
      predicted: bench.predicted,
      expectedExponent: expected,
      measuredExponent: alpha,
      status,
      sizes: bench.sizes,
      timesMs: times.map((t) => t * 1000),
    });

    console.log(
      `[${status}] ${bench.name.padEnd(25)} | Predicted: ${bench.predicted.padEnd(12)} | Exp Alpha: ${expected.toFixed(2)} | Meas Alpha: ${alpha.toFixed(2)}`
    );
  }

  console.log('-'.repeat(80));
  console.log(`Empirical validation status: ${allPassed ? 'ALL PASSED' : 'SOME FAILED'}`);
  console.log('='.repeat(80));

  const reportsDir = path.join(ROOT_DIR, 'benchmark', 'reports');
  fs.mkdirSync(reportsDir, { recursive: true });
  const reportPath = path.join(reportsDir, 'empirical_validation_report.md');

  let reportContent = '# Kite0 Empirical Complexity Scaling Report\n\n';
  reportContent +=
    'Empirical power-law scaling analysis comparing predicted asymptotic bounds with measured wall-clock scaling ($\\Delta \\ln T / \\Delta \\ln N$).\n\n';
  reportContent += '| Algorithm Class | Predicted Big-O | Theoretical Exponent | Measured Exponent | Status |\n';
  reportContent += '| :--- | :--- | :--- | :--- | :--- |\n';
  for (const r of results) {
    reportContent += `| ${r.name} | \`${r.predicted}\` | ${r.expectedExponent.toFixed(2)} | ${r.measuredExponent.toFixed(2)} | **${r.status}** |\n`;
  }

  reportContent += '\n\n## Per-Benchmark Timing Curves (ms)\n\n';
  for (const r of results) {
    reportContent += `### ${r.name}\n`;
    reportContent += `- Sizes: \`${JSON.stringify(r.sizes)}\`\n`;
    reportContent += `- Times (ms): \`${JSON.stringify(r.timesMs.map((t) => Number(t.toFixed(4))))}\`\n`;
    reportContent += `- Empirical Exponent: \`${r.measuredExponent.toFixed(3)}\`\n\n`;
  }

  fs.writeFileSync(reportPath, reportContent);
  console.log(`Wrote report to ${reportPath}`);

  if (!allPassed) {
    process.exit(1);
  }
}

main();
