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
  <a href="#rigorous-multi-variation-testing--verification">Testing Methodology</a> •
  <a href="#development--testing">Development</a> •
  <a href="#contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Rust%20%7C%20TypeScript-orange.svg" alt="Rust & TypeScript" />
  <img src="https://img.shields.io/badge/Runtime-WebAssembly-654ff0.svg" alt="WebAssembly" />
  <img src="https://img.shields.io/badge/Privacy-100%25%20Offline%20%26%20Zero%20LLM-success.svg" alt="Zero Telemetry Zero LLM" />
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/Parity-100%25%20(752%2F752%20cases)-brightgreen.svg" alt="100% Native & WASM Parity" />
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
- **Dual-Engine Architecture**: Native tree-sitter C runtime on CLI/desktop paired with lightweight serialized AST in WebAssembly in the browser, verified to **100% mathematical parity across 750+ benchmark test cases**.

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

You can install and use Kite0 **without touching any terminal or command line**, or build it locally from source.

### Non-Terminal Installation (No CLI Required)

#### For Google Chrome, Brave, Microsoft Edge, or Opera:
1. **Download the Extension**:
   - Download **[`kiteo-chrome-v0.1.1.zip`](extension/dist-packages/kiteo-chrome-v0.1.1.zip)** directly from the [`extension/dist-packages/`](extension/dist-packages/) directory.
2. **Extract the ZIP Archive**:
   - Right-click the `.zip` file and select **Extract All...** to a folder on your computer (e.g., `Downloads/kiteo-chrome`).
3. **Load into Your Browser**:
   - Open your browser and navigate to:
     - Chrome / Brave / Opera: `chrome://extensions/`
     - Microsoft Edge: `edge://extensions/`
   - In the top-right corner, toggle **Developer mode** to **ON**.
   - Click the **Load unpacked** button in the top-left corner.
   - Select the extracted folder containing `manifest.json`.
4. **Pin & Use**:
   - Click the puzzle piece icon on your browser toolbar and pin **Kite0**.
   - Open any problem on LeetCode or Codeforces—the Kite0 assistant will appear passively right next to the code editor!

#### For Mozilla Firefox:
1. Download **[`kiteo-firefox-v0.1.1.zip`](extension/dist-packages/kiteo-firefox-v0.1.1.zip)** directly from [`extension/dist-packages/`](extension/dist-packages/).
2. Extract the archive to a folder.
3. Open Firefox and navigate to `about:debugging#/runtime/this-firefox`.
4. Click **Load Temporary Add-on...**.
5. Select the `manifest.json` file inside the extracted folder.

---

### Non-Terminal Web Playground (Zero Install)

You can run static analysis immediately without installing an extension or opening a terminal:
1. Open [`extension/test-page.html`](extension/test-page.html) directly in any web browser (or double-click `test-page.html` inside the extracted zip bundle).
2. Select your language (**C++** or **Java**) from the dropdown.
3. Paste any solution code into the editor box.
4. Click **Analyze Locally (WASM)** — Time Complexity, Space Complexity, and Detected Algorithms appear instantly on-screen powered by WebAssembly.

---

### Developer Installation (Build From Source via Terminal)

If you are developing or compiling the extension locally:
```bash
# 1. Clone repository
git clone https://github.com/iokuru/Kite0.git
cd Kite0/extension

# 2. Install dependencies & build production packages
npm install
npm run package
```
The compiled extensions will be ready in:
- `extension/dist-chrome/` (Unpacked Chrome/Edge MV3)
- `extension/dist-firefox/` (Unpacked Firefox MV3)
- `extension/dist-packages/` (Pre-packaged `.zip` archives)

---

## Verified Problem Catalog

Kite0 has been rigorously tested against real-world LeetCode and Codeforces Online Assessment (OA) solutions across our **752 verified test implementations (600 tough OA cases + 152 canonical dev cases)**, achieving **100% exact parity** across native Rust and WebAssembly.

The catalog below is divided by core algorithmic category:

### 1. Two Pointers & In-Place Array Transformations
| Problem | Languages | Time Complexity | Space Complexity | Primary Algorithm |
| :--- | :--- | :--- | :--- | :--- |
| [LC 42: Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| [LC 11: Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| [LC 15: 3Sum](https://leetcode.com/problems/3sum/) | C++ / Java | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| [LC 16: 3Sum Closest](https://leetcode.com/problems/3sum-closest/) | C++ / Java | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| [LC 167: Two Sum II - Sorted Array](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| [LC 75: Sort Colors (Dutch Flag)](https://leetcode.com/problems/sort-colors/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| [LC 125: Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| [LC 977: Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Two Pointers` |

### 2. Sliding Window Techniques
| Problem | Languages | Time Complexity | Space Complexity | Primary Algorithm |
| :--- | :--- | :--- | :--- | :--- |
| [LC 3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Sliding Window` |
| [LC 76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Sliding Window` |
| [LC 209: Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Sliding Window` |
| [LC 643: Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Sliding Window` |

### 3. Binary Search & Binary Search on Answer
| Problem | Languages | Time Complexity | Space Complexity | Primary Algorithm |
| :--- | :--- | :--- | :--- | :--- |
| [LC 704: Binary Search](https://leetcode.com/problems/binary-search/) | C++ / Java | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | `Binary Search` |
| [LC 33: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | C++ / Java | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | `Binary Search` |
| [LC 153: Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | C++ / Java | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | `Binary Search` |
| [LC 875: Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | C++ / Java | $\mathcal{O}(n \log A)$ | $\mathcal{O}(1)$ | `Binary Search on Answer` |
| [LC 1011: Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | C++ / Java | $\mathcal{O}(n \log A)$ | $\mathcal{O}(1)$ | `Binary Search on Answer` |
| [LC 410: Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | C++ / Java | $\mathcal{O}(n \log A)$ | $\mathcal{O}(1)$ | `Binary Search on Answer` |

### 4. Linked List Structural Manipulation
| Problem | Languages | Time Complexity | Space Complexity | Primary Algorithm |
| :--- | :--- | :--- | :--- | :--- |
| [LC 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| [LC 876: Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| [LC 141: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| [LC 21: Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | C++ / Java | $\mathcal{O}(n + m)$ | $\mathcal{O}(1)$ | `Two Pointers` |
| [LC 19: Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Two Pointers` |

### 5. Stacks, Monotonic Queues & Expression Parsing
| Problem | Languages | Time Complexity | Space Complexity | Primary Algorithm |
| :--- | :--- | :--- | :--- | :--- |
| [LC 84: Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Monotonic Stack` |
| [LC 739: Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Monotonic Stack` |
| [LC 503: Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Monotonic Stack` |
| [LC 239: Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(k)$ | `Monotonic Queue` |
| [LC 1425: Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(k)$ | `Monotonic Queue` |
| [LC 20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Stack` |
| [LC 150: Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Stack` |

### 6. Binary Trees & Binary Search Trees
| Problem | Languages | Time Complexity | Space Complexity | Primary Algorithm |
| :--- | :--- | :--- | :--- | :--- |
| [LC 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `DFS` |
| [LC 226: Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `DFS` |
| [LC 102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `BFS` |
| [LC 236: Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `LCA` |
| [LC 98: Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Binary Search Tree` |
| [LC 230: Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Binary Search Tree` |

### 7. Graph Traversals & Connectivity (BFS / DFS)
| Problem | Languages | Time Complexity | Space Complexity | Primary Algorithm |
| :--- | :--- | :--- | :--- | :--- |
| [LC 200: Number of Islands](https://leetcode.com/problems/number-of-islands/) | C++ / Java | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | `BFS` or `DFS` |
| [LC 695: Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | C++ / Java | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | `DFS` |
| [LC 785: Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | C++ / Java | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | `BFS` or `DFS` |

### 8. Shortest Path & Topological Sort
| Problem | Languages | Time Complexity | Space Complexity | Primary Algorithm |
| :--- | :--- | :--- | :--- | :--- |
| [LC 743: Network Delay Time](https://leetcode.com/problems/network-delay-time/) | C++ / Java | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}(V + E)$ | `Dijkstra` |
| [LC 1631: Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | C++ / Java | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}(V + E)$ | `Dijkstra` |
| [LC 207: Course Schedule I](https://leetcode.com/problems/course-schedule/) | C++ / Java | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | `Topological Sort` |
| [LC 210: Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | C++ / Java | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | `Topological Sort` |

### 9. Disjoint Set Union (DSU) & Minimum Spanning Tree (MST)
| Problem | Languages | Time Complexity | Space Complexity | Primary Algorithm |
| :--- | :--- | :--- | :--- | :--- |
| [LC 684: Redundant Connection](https://leetcode.com/problems/redundant-connection/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `DSU` |
| [LC 547: Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `DSU` |
| [LC 1584: Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | C++ / Java | $\mathcal{O}(E \log V)$ | $\mathcal{O}(V + E)$ | `MST` |

### 10. Dynamic Programming Paradigms
| Problem | Languages | Time Complexity | Space Complexity | Primary Algorithm |
| :--- | :--- | :--- | :--- | :--- |
| [LC 53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | `Kadane's Algorithm` |
| [LC 70: Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 1D DP recurrence |
| [LC 198: House Robber](https://leetcode.com/problems/house-robber/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 1D DP recurrence |
| [LC 322: Coin Change](https://leetcode.com/problems/coin-change/) | C++ / Java | $\mathcal{O}(n \cdot A)$ | $\mathcal{O}(A)$ | 1D DP table |
| [LC 300: Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | C++ / Java | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ | `Binary Search` |
| [LC 1143: Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | C++ / Java | $\mathcal{O}(n \cdot m)$ | $\mathcal{O}(n)$ | 2D DP table |
| [LC 416: Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | C++ / Java | $\mathcal{O}(n \cdot A)$ | $\mathcal{O}(A)$ | `Knapsack DP` |
| [LC 124: Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Tree DP` |
| [LC 543: Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Tree DP` |
| [LC 847: Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | C++ / Java | $\mathcal{O}(2^n \cdot n)$ | $\mathcal{O}(2^n \cdot n)$ | `Bitmask DP` |

### 11. Advanced Data Structures & String Algorithms
| Problem | Languages | Time Complexity | Space Complexity | Primary Algorithm |
| :--- | :--- | :--- | :--- | :--- |
| [LC 208: Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Trie` |
| [LC 307: Range Sum Query Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | C++ / Java | $\mathcal{O}(n + q \log n)$ | $\mathcal{O}(n)$ | `Segment Tree` |
| [LC 315: Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | C++ / Java | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ | `Fenwick Tree` |
| [LC 28: Find Index of First Occurrence (KMP)](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | C++ / Java | $\mathcal{O}(n + m)$ | $\mathcal{O}(m)$ | `KMP` |
| [LC 1480: Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | C++ / Java | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | `Prefix Sum` |
| [LC 204: Count Primes (Sieve of Eratosthenes)](https://leetcode.com/problems/count-primes/) | C++ / Java | $\mathcal{O}(n \log \log n)$ | $\mathcal{O}(n)$ | `Sieve` |

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
│   ├── corpus/              # 152 canonical dev cases & 600 tough OA cases
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

## Rigorous Multi-Variation Testing & Verification

A robust static analyzer cannot rely on textbook code snippets or brittle formatting assumptions. In competitive programming and technical interviews, solutions are written under strict time pressure with wildly varying code styles, idiosyncratic loop constructs, and zero-whitespace formatting.

To guarantee mathematical correctness and developer trust, **Kite0 was verified through a multi-tiered testing methodology covering hundreds of code variations across both C++ and Java**:

### 1. Multi-Variation Stress Testing Per Problem
For every problem and algorithmic pattern in our catalog, we authored and validated **multiple real-world code variations**:
- **Formatting & Whitespace Diversity**: From ultra-compact, zero-whitespace contest submissions (e.g., `for(int i=0;i<n;++i){while(l<r){...}}`) to standard, clean idiomatic formatting.
- **Syntactic Loop Varieties**: Standard 3-part `for` loops, range-based and enhanced `for-each` loops (`for (int x : nums)`), `while` loops, and `do-while` constructs.
- **Boundary & Indexing Conventions**: 0-indexed vs. 1-indexed array traversals, pointer offsets (`i < n - 2`, `i <= n - 1`), and decrementing step-bounds (`while (n-- > 0)`).
- **Data Structure Variations**: Primitive arrays (`int[]`, raw pointer offsets) versus standard library abstractions (`std::vector`, `std::deque`, `ArrayList`, `ArrayDeque`, `LinkedList`).
- **Identifier Diversity**: Variable naming variations across standard conventions (`l`/`r`, `low`/`high`, `left`/`right`, `lo`/`hi`, `j`/`k`, `p`/`q`, `idx`).
- **Modular Code Structures**: Multi-method class architectures, helper function reachability, and pass-by-reference state mutators.

### 2. 1:1 Cross-Language Symmetry (C++ & Java)
Every problem in our benchmark suites is implemented with **100% exact symmetry across C++ and Java**:
- Both languages are lowered into a shared, language-agnostic Intermediate Representation (IR).
- Both language frontends must derive the **exact same Time Complexity, Space Complexity, and Algorithm classification** on corresponding implementations.

### 3. Dual-Engine Bit-Level Parity (Native Rust vs. WebAssembly)
Kite0 runs on two distinct execution targets:
1. **Native Rust Binary**: Uses compiled C tree-sitter libraries for CLI, desktop, and CI evaluation.
2. **WebAssembly (`wasm32-unknown-unknown`)**: Runs inside the browser with `web-tree-sitter` for 100% client-side privacy.

Every commit runs [`benchmark/parity_test.mjs`](benchmark/parity_test.mjs) across **all 752 test cases**, enforcing **100% mathematical parity** across Time Complexity, Space Complexity, and Algorithm labels between the native engine and WebAssembly runtime.

### 4. Comprehensive Benchmark Corpora
- **Canonical Reference Suite (`snippets.json` — 152 cases / 76 problems)**: Covers fundamental algorithmic archetypes across C++ and Java.
- **Synthetic Stress Suite (`dev2.json` — 70 cases / 35 problems)**: Targets tricky induction bounds, nested loops, break/continue flow, and pointer aliasing.
- **Tough OA & Competitive Programming Suite (`tough_benchmark.json` — 600 cases / 300 problems)**: Real-world LeetCode (Hard/Medium) and Codeforces (Div 1/Div 2) problems spanning all 68 taxonomy labels.
- **Total Suite**: **822+ verified test cases and benchmark problems**.

### 5. Empirical CPU Scaling Validation
Beyond static symbolic evaluation, [`benchmark/empirical/validator.mjs`](benchmark/empirical/validator.mjs) runs empirical execution benchmarks across doubling input sizes ($N = 10^3 \to 8 \times 10^6$). It fits power-law log-log regression curves ($\Delta \ln T / \Delta \ln N$) to verify that our symbolic Big-O derivations match real CPU cycle scaling.

### 6. Formal Property-Based Testing (`proptest`)
Using property-based testing, we prove mathematical invariants (commutativity, associativity, and dominance elimination in complexity algebra) over tens of thousands of randomly synthesized AST and IR expressions.

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
Verifies 100% identical Time Complexity, Space Complexity, and Algorithm labels across all 752 benchmark cases:
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
