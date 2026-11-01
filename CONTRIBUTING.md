# Contributing to Kite0

Thank you for your interest in contributing to Kite0! We welcome contributions from developers, competitive programmers, and compiler enthusiasts of all experience levels.

Kite0 is a **deterministic, non-generative, 100% offline static analyzer** built in **Rust** and compiled to **WebAssembly**. It determines asymptotic Time Complexity ($TC$), Space Complexity ($SC$), and algorithmic techniques for C++ and Java competitive programming code without network calls or LLMs.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Architectural Principles](#architectural-principles)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs & False Positives](#reporting-bugs--false-positives)
  - [Suggesting Features & Patterns](#suggesting-features--patterns)
  - [Adding Benchmark Test Cases](#adding-benchmark-test-cases)
  - [Implementing New Detectors](#implementing-new-detectors)
  - [Extending Platform Adapters](#extending-platform-adapters)
- [Development Setup](#development-setup)
  - [Prerequisites](#prerequisites)
  - [Building from Source](#building-from-source)
  - [Running the Test Suites](#running-the-test-suites)
  - [Testing the Extension Locally](#testing-the-extension-locally)
- [Pull Request Guidelines](#pull-request-guidelines)

---

## Architectural Principles

Before writing code or opening a PR, please review our core architectural rules:

1. **Deterministic Static Analysis Only**: Zero external network requests, zero telemetry, zero analytics, and zero LLM calls. All analysis must be local, reproducible, and mathematically sound.
2. **Unified Arena IR**: Both C++ and Java ASTs are normalized into the language-agnostic arena-allocated Intermediate Representation (`CppNormalizer`, `JavaNormalizer`). Analysis passes run on the unified IR.
3. **Closed Catalog & Status Gate**: Algorithm labels are strictly limited to the 68 canonical labels defined in [`engine/src/algorithms/catalog.toml`](engine/src/algorithms/catalog.toml). A detector cannot be marked `"approved"` until it achieves $\ge 95\%$ precision with $\ge 10$ positive and $\ge 10$ negative test cases.
4. **Native and WebAssembly Parity**: Every change in the engine must produce **100% identical results** between native Rust and the WebAssembly build (`npm run test:parity`).
5. **Passive Contest Mode**: The browser extension only reads DOM editor state. It must never tamper with contest timers, submission buttons, or editor instances.

---

## How Can I Contribute?

### Reporting Bugs & False Positives

If Kite0 miscalculates complexity or misidentifies an algorithm:
1. Check existing [GitHub Issues](https://github.com/iokuru/Kite0/issues) to see if it has already been reported.
2. Open a new issue with:
   - The minimal code snippet in C++ or Java reproducing the issue.
   - Expected Output vs Actual Output (Time Complexity, Space Complexity, Algorithm).
   - Problem source or platform context (e.g., LeetCode, Codeforces).

### Suggesting Features & Patterns

We welcome ideas for new loop structures, standard library container cost models, or platform adapters. Please open an issue with the `proposal` tag explaining the pattern, its mathematical recurrence, and real-world examples.

### Adding Benchmark Test Cases

We maintain extensive benchmark corpora:
- `benchmark/corpus/snippets.json`: 152 canonical dev cases (76 C++, 76 Java).
- `benchmark/corpus/tough_benchmark.json`: 500 tough OA benchmark cases.

To add a verified test case:
1. Provide valid C++ or Java code.
2. Specify exact expected $TC$, $SC$, and catalog algorithm.
3. Ensure both native and WebAssembly parity tests pass:
   ```bash
   node benchmark/parity_test.mjs
   node benchmark/parity_test.mjs --tough
   ```

### Implementing New Detectors

1. Check [`engine/src/algorithms/catalog.toml`](engine/src/algorithms/catalog.toml) for the label definition.
2. Implement structural AST/IR recognition in `engine/src/algorithms/`.
3. Add positive and look-alike negative unit tests in `engine/tests/`.
4. Ensure suppression rules are defined (e.g. dynamic programming subtypes suppress general DP).

### Extending Platform Adapters

Platform adapters live in `extension/src/adapters/`. Each adapter implements `PlatformAdapter`:
```typescript
export interface PlatformAdapter {
  matches(url: string): boolean;
  getSource(): string | null;
  getLanguage(): 'cpp' | 'java' | null;
  isContestActive(): boolean;
}
```
Adapters must only read editor state (DOM/Monaco/CodeMirror/ACE) without modifying the page.

---

## Development Setup

### Prerequisites

- **Rust**: `rustup` with `stable` toolchain ($\ge 1.75$)
- **wasm-pack**: `cargo install wasm-pack`
- **Node.js**: LTS version ($\ge 20$) and `npm`
- **C++ Compiler**: `g++` or `clang` (for native tree-sitter builds and empirical validation)

### Building from Source

```bash
# Clone the repository
git clone https://github.com/iokuru/Kite0.git
cd Kite0

# Build Rust engine & CLI
cargo build --workspace

# Build WebAssembly module for extension
cd engine
wasm-pack build --target web --out-dir ../extension/src/wasm/pkg
cd ..

# Install extension dependencies & build
cd extension
npm install
npm run build
cd ..
```

### Running the Test Suites

We enforce strict test coverage across Rust, WebAssembly, and browser platforms:

```bash
# 1. Rust engine unit, snapshot, and proptest suites (135+ tests)
cargo test --workspace

# 2. Benchmark suite accuracy
cargo run -p kiteo-runner
cargo run -p kiteo-runner -- --dev2

# 3. Native vs WebAssembly parity tests (152 canonical + 500 tough cases)
node benchmark/parity_test.mjs
node benchmark/parity_test.mjs --tough

# 4. Empirical scaling validator (power-law regression)
node benchmark/empirical/validator.mjs
node benchmark/empirical/synthetic_pattern_validator.mjs

# 5. Browser extension packaging
cd extension
npm run package
```

### Testing the Extension Locally

1. Build the extension:
   ```bash
   cd extension
   npm run build
   ```
2. **In Chrome / Brave / Edge**:
   - Navigate to `chrome://extensions/`.
   - Enable **Developer mode** (top-right toggle).
   - Click **Load unpacked** and select `Kite0/extension/dist-chrome` (or `Kite0/extension/dist`).
3. **In Firefox**:
   - Navigate to `about:debugging#/runtime/this-firefox`.
   - Click **Load Temporary Add-on...**.
   - Select `Kite0/extension/dist-firefox/manifest.json`.
4. Open `extension/public/test-page.html` or visit LeetCode / Codeforces to test live analysis!

---

## Pull Request Guidelines

1. **Keep PRs focused**: Each PR should address a single feature, bug fix, or detector enhancement.
2. **Preserve Parity**: Always verify that `node benchmark/parity_test.mjs` and `cargo test --workspace` pass before submitting.
3. **Format & Lint**:
   ```bash
   cargo fmt --all -- --check
   cargo clippy --all-targets --all-features -- -D warnings
   ```
4. **Write Clear Commit Messages**: Use concise, imperative messages describing the change (e.g., `Add detector for Bitmask DP with subset iteration`).

Thank you for helping make Kite0 the fastest, most reliable offline complexity analyzer for competitive programmers!
