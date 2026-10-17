# ADR 0012: LeetCode Entry Point Discovery and Signature Dimension Binding

## Status
Accepted

## Context
Unlike competitive programming solutions that read from standard input (`cin` / `Scanner`) within a top-level `int main()` or `public static void main()`, LeetCode solutions are defined inside `class Solution`:
- In C++, the entry point is the public member function declared within `class Solution`.
- In Java, the entry point is the public instance or static method declared within `class Solution`.
Helper functions, nested methods, and recursive calls reachable from the entry point must be analyzed.
Furthermore, input dimensions are not read via `cin >> n`, but arrive directly as method arguments in the entry method signature.

## Decision

1. **Entry Point Identification**:
   - The analyzer inspects classes named `Solution`.
   - In C++, the candidate methods are functions inside `class Solution` under `public:` visibility (or top public member if unmarked). Constructors and operator overloads are excluded.
   - In Java, the candidate methods are `public` methods inside `class Solution` (excluding constructors).
   - If a class contains multiple helper methods, the entry point is identified as the public method that is not called by any other method in the class (or the designated entry signature if provided).
   - Auxiliary functions and recursion reachable from this entry point are included in callgraph analysis and complexity aggregation.
   - If no valid entry point method can be determined, the analyzer returns `Unknown` for Time and Space Complexity, rather than guessing.

2. **Dimension Variable Binding from Signature**:
   Input dimensions are bound to symbolic variables based on the entry parameter types and usage:
   - **Vectors / Arrays / Lists**:
     - Single 1D container (e.g., `vector<int>& nums`, `int[] nums`, `string s`): bounded by $n$ (size / length).
     - Second 1D container of distinct type or name: bound to $m$ or $k$.
     - 2D grid/matrix (e.g., `vector<vector<int>>& grid`, `char[][] board`): rows bound to $m$, columns bound to $n$ (or $m \times n$).
   - **Trees and Graphs**:
     - Pointer or reference to node (`TreeNode* root`, `ListNode* head`, `Node* node`): bound to $V$ (or $n$) node count.
   - **Scalar Integers**:
     - Loop bound counter or size limit (e.g., `int n`, `int k`): bound to variable $n$ or $k$ according to parameter name and loop condition comparison.
     - Value ranges or numeric search spaces (e.g., `int target`, `int maxVal`): bound to value bound $A$ if used in binary search or frequency table sizing.
   - If parameter sizes cannot be soundly bound, loops bounded by those parameters evaluate to `Unknown`.

3. **Auxiliary Space Complexity Semantics**:
   - Space complexity measures strictly **auxiliary memory** allocated by the algorithm.
   - The input arguments (parameters passed into the entry point) are **never counted** as auxiliary space.
   - The returned data structure (e.g., `return new int[]{i, j};`, `return {};`, `vector<int> res`) is **never counted** as auxiliary space.
   - Local dynamically allocated collections (e.g., `unordered_map`, `HashMap`, `vector`, `HashSet`, `new int[n]`) and recursion stack frames are counted toward auxiliary space ($O(n)$, $O(V)$, etc.).

4. **Soundness & Fallback**:
   - Guessing is prohibited. When AST analysis cannot determine a loop bound or when entry point discovery is ambiguous/unsupported, KiteO returns `Unknown`.
