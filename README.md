# Kite0

<p align="center">
  <strong>Deterministic, 100% offline static complexity analyzer for competitive programming and tech assessments.</strong>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#quick-start--installation">Installation</a> •
  <a href="#supported-platforms--languages">Supported Targets</a> •
  <a href="#how-it-works">Architecture</a> •
  <a href="#verified-problem-catalog">Verified Problems</a> •
  <a href="#development--testing">Development</a> •
  <a href="#contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Rust%20%7C%20TypeScript-orange.svg" alt="Rust & TypeScript" />
  <img src="https://img.shields.io/badge/Runtime-WebAssembly-654ff0.svg" alt="WebAssembly" />
  <img src="https://img.shields.io/badge/Privacy-100%25%20Offline%20%26%20Zero%20LLM-success.svg" alt="Zero Telemetry Zero LLM" />
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/Parity-100%25%20(652%2F652%20cases)-brightgreen.svg" alt="100% Native & WASM Parity" />
</p>

---

## What is Kite0?

**Kite0** is an open-source, non-generative browser extension and static analysis engine built for competitive programmers, software engineers, and computer science students.

Unlike generative AI assistants that guess or hallucinate asymptotic complexity from problem titles, **Kite0 uses mathematical loop induction, control-flow graph (CFG) analysis, recursion tree solving, and AST pattern matching** to derive mathematically sound:
1. **Time Complexity ($\mathcal{O}(TC)$)**
2. **Space Complexity ($\mathcal{O}(SC)$)**
3. **Algorithmic Classification** (from a closed 68-algorithm catalog)

All computation runs **locally inside your browser via compiled WebAssembly**. Zero telemetry, zero analytics, zero external API requests, and zero remote code execution.

---

## Key Features

- **Strict 3-Field Output Contract**:
  - **Time Complexity**: Exact symbolic Big-O notation derived via monomial dominance algebra, loop bounds, geometric scaling, harmonic series recognition, and call-graph cycles ($\mathcal{O}(1)$, $\mathcal{O}(\log n)$, $\mathcal{O}(n)$, $\mathcal{O}(n \log n)$, $\mathcal{O}(n^2)$, $\mathcal{O}(n \cdot m)$, $\mathcal{O}((V + E) \log V)$, $\mathcal{O}(2^n \cdot n)$, $\mathcal{O}(n^3)$, etc.).
  - **Space Complexity**: Evaluates auxiliary memory consumption—distinguishing parameter inputs from dynamic heap containers (`vector`, `ArrayList`, `HashSet`), recursion call stacks, and value-indexed arrays ($\mathcal{O}(A)$) versus input-indexed buffers ($\mathcal{O}(n)$).
  - **Algorithm Classification**: Identifies up to 3 primary algorithms drawn strictly from our closed 68-label catalog, applying evidence-based suppression rules (e.g., Dijkstra suppresses BFS; Sliding Window suppresses Two Pointers).
- **100% Offline & Private**: Zero network calls. Your code never leaves your computer. Completely safe for practice, contests, and proprietary codebases.
- **Passive Contest Mode**: Reads only the editor DOM without mutating the webpage, touching contest timers, or interfering with Monaco, CodeMirror, or ACE editors.
- **Dual-Engine Architecture**: Native tree-sitter C runtime on CLI/desktop paired with lightweight serialized AST in WebAssembly in the browser, verified to **100% mathematical parity across 650+ benchmark test cases**.

---

## Supported Platforms & Languages

### Languages
- **C++**: C++11 through C++23 (standard loops, STL containers, CP macro templates, pointer arithmetic).
- **Java**: Java 8 through 21 (standard loops, enhanced for loops, `java.util` collections, recursion).

Both languages compile down to a shared **Language-Agnostic Arena-Allocated Intermediate Representation (IR)**.

### Competitive Platforms & Online Evaluators
- **Competitive Platforms**: Codeforces, LeetCode, CodeChef, AtCoder, HackerRank, GeeksforGeeks, HackerEarth, CSES.
- **Web IDEs & Sandboxes**: OnlineGDB, JDoodle, Programiz, Replit.
- **Browsers**: Chrome, Brave, Opera, Edge (Manifest V3), and Firefox (Gecko MV3).

---

## Quick Start & Installation

### Option 1: Load in Chrome / Brave / Edge (Developer Mode)

1. Clone or download this repository:
   ```bash
   git clone https://github.com/iokuru/Kite0.git
   cd Kite0/extension
   npm install
   npm run package
   ```
2. Open your browser and go to `chrome://extensions/`.
3. Enable **Developer mode** (toggle in the top-right corner).
4. Click **Load unpacked** and select the `Kite0/extension/dist-chrome` folder.
5. Pin Kite0 to your extension bar!

### Option 2: Load in Firefox

1. Build or download the Firefox distribution:
   ```bash
   cd Kite0/extension
   npm install
   npm run package
   ```
2. Open Firefox and go to `about:debugging#/runtime/this-firefox`.
3. Click **Load Temporary Add-on...**.
4. Select `Kite0/extension/dist-firefox/manifest.json`.

### Option 3: Browser Standalone Test Page

You can test Kite0 without visiting an external platform:
1. Open `extension/public/test-page.html` in your browser.
2. Paste any standard C++ or Java solution.
3. Click **Analyze** to inspect immediate AST normalizer and complexity output.

---

## Verified Problem Catalog

Kite0 has been rigorously tested against real-world LeetCode and Codeforces Online Assessment (OA) solutions, achieving **100% exact parity** across native Rust and WebAssembly:

| Category | Real-World Problem | Lang | Time Complexity | Space Complexity | Detected Algorithm |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Two Pointers** | [LC 42: Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | C++/Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| **Two Pointers** | [LC 11: Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | C++/Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| **Two Pointers** | [LC 15: 3Sum](https://leetcode.com/problems/3sum/) | C++/Java | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| **Sliding Window** | [LC 3: Longest Substring Without Repeating](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | C++/Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Sliding Window` |
| **Sliding Window** | [LC 76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | C++/Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Sliding Window` |
| **Binary Search** | [LC 33: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | C++/Java | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | `Binary Search` |
| **BS on Answer** | [LC 875: Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | C++/Java | $\mathcal{O}(n \log A)$ | $\mathcal{O}(1)$ | `Binary Search on Answer` |
| **BS on Answer** | [LC 1011: Capacity To Ship Packages](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | C++/Java | $\mathcal{O}(n \log A)$ | $\mathcal{O}(1)$ | `Binary Search on Answer` |
| **Monotonic Stack** | [LC 84: Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | C++/Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Monotonic Stack` |
| **Monotonic Stack** | [LC 739: Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | C++/Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Monotonic Stack` |
| **Monotonic Queue** | [LC 239: Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | C++/Java | $\mathcal{O}(n)$ | $\mathcal{O}(k)$ | `Monotonic Queue` |
| **Graph Traversal** | [LC 200: Number of Islands](https://leetcode.com/problems/number-of-islands/) | C++/Java | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | `BFS` or `DFS` |
| **Shortest Path** | [LC 743: Network Delay Time](https://leetcode.com/problems/network-delay-time/) | C++/Java | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}(V + E)$ | `Dijkstra` |
| **Topological Sort** | [LC 207: Course Schedule](https://leetcode.com/problems/course-schedule/) | C++/Java | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | `Topological Sort` |
| **Disjoint Set** | [LC 684: Redundant Connection](https://leetcode.com/problems/redundant-connection/) | C++/Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `DSU` |
| **Minimum Spanning Tree**| [LC 1584: Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | C++/Java | $\mathcal{O}(E \log V)$ | $\mathcal{O}(V + E)$ | `MST` |
| **Dynamic Programming** | [LC 53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | C++/Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Kadane's Algorithm` |
| **Dynamic Programming** | [LC 70: Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | C++/Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 1D DP recurrence |
| **Dynamic Programming** | [LC 1143: Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | C++/Java | $\mathcal{O}(n \cdot m)$ | $\mathcal{O}(n)$ | 2D DP table |
| **Tree DP** | [LC 124: Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | C++/Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Tree DP` |
| **Bitmask DP** | [LC 847: Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | C++/Java | $\mathcal{O}(2^n \cdot n)$ | $\mathcal{O}(2^n \cdot n)$ | `Bitmask DP` |
| **Advanced DS** | [LC 307: Range Sum Query Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | C++/Java | $\mathcal{O}(n + q \log n)$ | $\mathcal{O}(n)$ | `Segment Tree` |
| **String Algorithms** | [LC 28: Find Index of First Occurrence](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | C++/Java | $\mathcal{O}(n + m)$ | $\mathcal{O}(m)$ | `KMP` |
| **Prefix Sum** | [LC 1480: Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | C++/Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Prefix Sum` |

---

## How It Works

```
┌────────────────────────────────────────────────────────┐
│  Browser DOM / Editor (Monaco, CodeMirror, ACE)         │
└──────────────────────────┬─────────────────────────────┘
                           │ Passive Read-Only Source Extraction
┌──────────────────────────▼─────────────────────────────┐
│  Tree-Sitter Parsing (web-tree-sitter / native C)      │
└──────────────────────────┬─────────────────────────────┘
                           │ Raw Concrete Syntax Tree (CST)
┌──────────────────────────▼─────────────────────────────┐
│  Unified Arena-Allocated IR (CppNormalizer / Java)     │
└────────────┬─────────────────────────────┬─────────────┘
             │                             │
┌────────────▼────────────┐   ┌────────────▼─────────────┐
│ Loop & Recursion Engine │   │ Structural Algorithm     │
│ - Monomial bound algebra│   │ Catalog & Detectors      │
│ - Harmonic series detection │ - 68 canonical labels    │
│ - CFG basic-block cycles│   │ - Priority suppression   │
│ - Call-graph recurrence │   │ - $\ge 95\%$ status gate │
└────────────┬────────────┘   └────────────┬─────────────┘
             │                             │
             └──────────────┬──────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ Output Contract: Time Complexity, Space Complexity,    │
│                  and Primary Algorithmic Technique     │
└────────────────────────────────────────────────────────┘
```

1. **Passive Ingestion**: The platform adapter isolates the active code text and programming language without modifying webpage events or triggering contest anti-cheat flags.
2. **IR Normalization**: Language syntax is transformed into a lightweight, typed arena IR with unified statements, expressions, and memory bindings.
3. **Loop & Complexity Analysis**: Nested loops, pointer steps, step-halving (`low <= high`), and amortized pointer traversals are computed symbolically.
4. **Closed Catalog Matching**: Algorithms are detected through structural code fingerprints (e.g., in-degree counts + queue for Topological Sort; relaxation conditions + min-heap for Dijkstra).
5. **Suppression & Gate**: Higher-specificity labels suppress primitive ones, and results are formatted strictly according to the 3-field output contract.

---

## Repository Layout

```
Kite0/
├── benchmark/
│   ├── corpus/              # 152 canonical dev cases & 500 tough OA cases
│   ├── empirical/           # Empirical scaling validators (power-law regression)
│   ├── leetcode/            # LeetCode problem suite & ground-truth tools
│   ├── runner/              # Rust benchmark accuracy evaluator & status gate
│   └── seed/                # Benchmark audit specification & schema
├── docs/
│   └── ADR/                 # 11 Architecture Decision Records (ADRs)
├── engine/                  # Core Rust static analysis engine
│   ├── src/
│   │   ├── algorithms/      # Closed 68-label catalog & structural detectors
│   │   ├── amortized/       # Two-pointer and degree sum amortized rules
│   │   ├── callgraph/       # Recursive call graph & recurrence solving
│   │   ├── cfg/             # Control Flow Graph basic blocks
│   │   ├── complexity/      # Symbolic monomial dominance simplification
│   │   ├── cost_model/      # Embedded TOML cost models for C++ STL & Java
│   │   ├── ir/              # Language-agnostic arena IR & AST normalizers
│   │   ├── loops/           # Linear, geometric, halving, harmonic loop rules
│   │   ├── preprocessor/    # CP macro expansion & header template cleaning
│   │   └── space/           # Auxiliary array classification & stack depth
│   └── tests/               # Unit, snapshot, and proptest property tests
├── extension/               # Browser extension (Preact, TypeScript, Vite, WASM)
│   ├── e2e/                 # Playwright end-to-end and privacy audit tests
│   ├── public/icons/        # Vector and high-contrast extension icons
│   ├── scripts/             # Native Node.js packaging & AMO source bundler
│   └── src/                 # Platform adapters, popup UI, content scripts
└── website/                 # Documentation & interactive web landing site
```

---

## Development & Testing

### Prerequisites
- **Rust** $\ge 1.75$ (`cargo`, `rustup`)
- **wasm-pack** (`cargo install wasm-pack`)
- **Node.js** $\ge 20$ (`node`, `npm`)
- **C++ Compiler** (`g++` or `clang` for native tree-sitter builds)

### 1. Run Rust Engine Tests
```bash
cargo test --workspace
cargo clippy --all-targets --all-features -- -D warnings
cargo fmt --all -- --check
```

### 2. Run Parity Verification (Native vs WebAssembly)
Verifies 100% identical Time Complexity, Space Complexity, and Algorithm labels across all 652 benchmark cases:
```bash
node benchmark/parity_test.mjs
node benchmark/parity_test.mjs --tough
```

### 3. Run Empirical Scaling Validator
Verifies theoretical scaling exponents ($\Delta \ln T / \Delta \ln N$) across doubling input sizes ($N \le 8,000,000$):
```bash
node benchmark/empirical/validator.mjs
node benchmark/empirical/synthetic_pattern_validator.mjs
```

### 4. Build Extension Distribution
```bash
cd extension
npm install
npm run package           # Builds Chrome and Firefox zip bundles
npm run package:source    # Bundles clean reproducible source code for Mozilla AMO
```

---

## Contributing & Community

We welcome contributions from competitive programmers, compiler engineers, and developers of all backgrounds!

- **Found a problem where Kite0 returned an unexpected bound?** Open an issue with the code snippet using our [Issue Tracker](https://github.com/iokuru/Kite0/issues).
- **Want to add a new algorithm or improve existing detectors?** Review our [Contributing Guidelines](CONTRIBUTING.md) and check [catalog.toml](engine/src/algorithms/catalog.toml).
- **Architecture Questions?** Read through our [Architecture Decision Records (ADRs)](docs/ADR/).

---

## License

This project is licensed under the [MIT License](LICENSE). Built with zero telemetry, deterministic proofs, and complete privacy.
