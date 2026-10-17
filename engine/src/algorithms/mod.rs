use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum AllowedAlgorithm {
    // Arrays, Hashing and Searching
    TwoPointers,
    FastAndSlowPointers,
    SlidingWindow,
    PrefixSum,
    DifferenceArray,
    BinarySearch,
    BinarySearchOnAnswer,
    Sorting,
    HashMap,
    HashSet,
    FrequencyCounting,
    KadanesAlgorithm,
    Intervals,
    MatrixGrid,
    CoordinateCompression,

    // Stack, Queue and Heap
    Stack,
    MonotonicStack,
    Queue,
    MonotonicQueue,
    HeapPriorityQueue,
    TopK,
    TwoHeaps,

    // Linked Lists
    LinkedList,
    LinkedListReversal,
    CycleDetection,
    MergeLinkedLists,

    // Trees
    Bfs,
    Dfs,
    BinarySearchTree,
    Trie,
    Lca,
    BinaryLifting,
    TreeDp,

    // Graphs
    Dsu,
    Dijkstra,
    Mst,
    TopologicalSort,
    ShortestPath,
    StronglyConnectedComponents,
    BridgesAndArticulationPoints,
    EulerianPath,

    // Dynamic Programming
    DynamicProgramming,
    Memoization,
    OneDDp,
    TwoDDp,
    KnapsackDp,
    BitmaskDp,
    IntervalDp,

    // String Algorithms
    Kmp,
    ZAlgorithm,
    RollingHash,

    // General Algorithms and Techniques
    Greedy,
    Backtracking,
    DivideAndConquer,
    BitManipulation,
    MeetInTheMiddle,
    SweepLine,

    // Advanced Data Structures
    FenwickTree,
    SegmentTree,
    SparseTable,
    LazySegmentTree,

    // Mathematics and Number Theory
    Sieve,
    Gcd,
    Lcm,
    FastExponentiation,
    ModularArithmetic,
    PrimeFactorization,
    Combinatorics,
}

impl AllowedAlgorithm {
    pub const ALL: [AllowedAlgorithm; 68] = [
        AllowedAlgorithm::SegmentTree,
        AllowedAlgorithm::FenwickTree,
        AllowedAlgorithm::SparseTable,
        AllowedAlgorithm::LazySegmentTree,
        AllowedAlgorithm::Dijkstra,
        AllowedAlgorithm::Mst,
        AllowedAlgorithm::StronglyConnectedComponents,
        AllowedAlgorithm::BridgesAndArticulationPoints,
        AllowedAlgorithm::EulerianPath,
        AllowedAlgorithm::TopologicalSort,
        AllowedAlgorithm::Lca,
        AllowedAlgorithm::BinaryLifting,
        AllowedAlgorithm::Trie,
        AllowedAlgorithm::Dsu,
        AllowedAlgorithm::Kmp,
        AllowedAlgorithm::ZAlgorithm,
        AllowedAlgorithm::RollingHash,
        AllowedAlgorithm::Sieve,
        AllowedAlgorithm::KadanesAlgorithm,
        AllowedAlgorithm::TreeDp,
        AllowedAlgorithm::BitmaskDp,
        AllowedAlgorithm::IntervalDp,
        AllowedAlgorithm::KnapsackDp,
        AllowedAlgorithm::TwoDDp,
        AllowedAlgorithm::OneDDp,
        AllowedAlgorithm::DynamicProgramming,
        AllowedAlgorithm::Memoization,
        AllowedAlgorithm::Backtracking,
        AllowedAlgorithm::DivideAndConquer,
        AllowedAlgorithm::BinarySearchOnAnswer,
        AllowedAlgorithm::TwoHeaps,
        AllowedAlgorithm::TopK,
        AllowedAlgorithm::HeapPriorityQueue,
        AllowedAlgorithm::MonotonicStack,
        AllowedAlgorithm::MonotonicQueue,
        AllowedAlgorithm::CycleDetection,
        AllowedAlgorithm::LinkedListReversal,
        AllowedAlgorithm::MergeLinkedLists,
        AllowedAlgorithm::FastAndSlowPointers,
        AllowedAlgorithm::SlidingWindow,
        AllowedAlgorithm::TwoPointers,
        AllowedAlgorithm::BinarySearch,
        AllowedAlgorithm::DifferenceArray,
        AllowedAlgorithm::PrefixSum,
        AllowedAlgorithm::CoordinateCompression,
        AllowedAlgorithm::Intervals,
        AllowedAlgorithm::MatrixGrid,
        AllowedAlgorithm::HashMap,
        AllowedAlgorithm::HashSet,
        AllowedAlgorithm::FrequencyCounting,
        AllowedAlgorithm::Stack,
        AllowedAlgorithm::Queue,
        AllowedAlgorithm::LinkedList,
        AllowedAlgorithm::BinarySearchTree,
        AllowedAlgorithm::ShortestPath,
        AllowedAlgorithm::Greedy,
        AllowedAlgorithm::BitManipulation,
        AllowedAlgorithm::MeetInTheMiddle,
        AllowedAlgorithm::SweepLine,
        AllowedAlgorithm::Gcd,
        AllowedAlgorithm::Lcm,
        AllowedAlgorithm::FastExponentiation,
        AllowedAlgorithm::ModularArithmetic,
        AllowedAlgorithm::PrimeFactorization,
        AllowedAlgorithm::Combinatorics,
        AllowedAlgorithm::Sorting,
        AllowedAlgorithm::Bfs,
        AllowedAlgorithm::Dfs,
    ];

    pub fn as_str(&self) -> &'static str {
        match self {
            Self::SegmentTree => "Segment Tree",
            Self::FenwickTree => "Fenwick Tree",
            Self::SparseTable => "Sparse Table",
            Self::LazySegmentTree => "Lazy Segment Tree",
            Self::Dijkstra => "Dijkstra",
            Self::Mst => "MST",
            Self::StronglyConnectedComponents => "Strongly Connected Components",
            Self::BridgesAndArticulationPoints => "Bridges and Articulation Points",
            Self::EulerianPath => "Eulerian Path",
            Self::TopologicalSort => "Topological Sort",
            Self::Lca => "LCA",
            Self::BinaryLifting => "Binary Lifting",
            Self::Trie => "Trie",
            Self::Dsu => "DSU",
            Self::Kmp => "KMP",
            Self::ZAlgorithm => "Z Algorithm",
            Self::RollingHash => "Rolling Hash",
            Self::Sieve => "Sieve",
            Self::KadanesAlgorithm => "Kadane's Algorithm",
            Self::TreeDp => "Tree DP",
            Self::BitmaskDp => "Bitmask DP",
            Self::IntervalDp => "Interval DP",
            Self::KnapsackDp => "Knapsack DP",
            Self::TwoDDp => "2D DP",
            Self::OneDDp => "1D DP",
            Self::DynamicProgramming => "Dynamic Programming",
            Self::Memoization => "Memoization",
            Self::Backtracking => "Backtracking",
            Self::DivideAndConquer => "Divide and Conquer",
            Self::BinarySearchOnAnswer => "Binary Search on Answer",
            Self::TwoHeaps => "Two Heaps",
            Self::TopK => "Top K",
            Self::HeapPriorityQueue => "Heap / Priority Queue",
            Self::MonotonicStack => "Monotonic Stack",
            Self::MonotonicQueue => "Monotonic Queue",
            Self::CycleDetection => "Cycle Detection",
            Self::LinkedListReversal => "Linked List Reversal",
            Self::MergeLinkedLists => "Merge Linked Lists",
            Self::FastAndSlowPointers => "Fast and Slow Pointers",
            Self::SlidingWindow => "Sliding Window",
            Self::TwoPointers => "Two Pointers",
            Self::BinarySearch => "Binary Search",
            Self::DifferenceArray => "Difference Array",
            Self::PrefixSum => "Prefix Sum",
            Self::CoordinateCompression => "Coordinate Compression",
            Self::Intervals => "Intervals",
            Self::MatrixGrid => "Matrix / Grid",
            Self::HashMap => "Hash Map",
            Self::HashSet => "Hash Set",
            Self::FrequencyCounting => "Frequency Counting",
            Self::Stack => "Stack",
            Self::Queue => "Queue",
            Self::LinkedList => "Linked List",
            Self::BinarySearchTree => "Binary Search Tree",
            Self::ShortestPath => "Shortest Path",
            Self::Greedy => "Greedy",
            Self::BitManipulation => "Bit Manipulation",
            Self::MeetInTheMiddle => "Meet in the Middle",
            Self::SweepLine => "Sweep Line",
            Self::Gcd => "GCD",
            Self::Lcm => "LCM",
            Self::FastExponentiation => "Fast Exponentiation",
            Self::ModularArithmetic => "Modular Arithmetic",
            Self::PrimeFactorization => "Prime Factorization",
            Self::Combinatorics => "Combinatorics",
            Self::Sorting => "Sorting",
            Self::Bfs => "BFS",
            Self::Dfs => "DFS",
        }
    }

    pub fn from_canonical_name(s: &str) -> Option<Self> {
        Self::ALL.iter().copied().find(|a| a.as_str() == s)
    }

    pub fn priority(&self) -> u32 {
        let name = self.as_str();
        get_catalog()
            .iter()
            .find(|item| item.name == name)
            .map(|item| item.priority)
            .unwrap_or(999)
    }

    pub fn is_approved(&self) -> bool {
        let name = self.as_str();
        get_catalog()
            .iter()
            .find(|item| item.name == name)
            .map(|item| item.status == "approved")
            .unwrap_or(false)
    }
}

impl std::str::FromStr for AllowedAlgorithm {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Self::from_canonical_name(s).ok_or(())
    }
}

#[derive(Debug, Clone, Deserialize)]
pub struct CatalogItem {
    pub name: String,
    pub status: String,
    pub category: String,
    pub priority: u32,
    #[serde(default)]
    pub suppresses: Vec<String>,
}

#[derive(Debug, Clone, Deserialize)]
struct CatalogDoc {
    pub algorithm: Vec<CatalogItem>,
}

pub fn get_catalog() -> &'static [CatalogItem] {
    static CATALOG: std::sync::OnceLock<Vec<CatalogItem>> = std::sync::OnceLock::new();
    CATALOG.get_or_init(|| {
        let raw = include_str!("catalog.toml");
        let doc: CatalogDoc = toml::from_str(raw).expect("Failed to parse catalog.toml");
        doc.algorithm
    })
}

pub fn select_labels(
    detected: &[AllowedAlgorithm],
    source: &str,
    require_approved: bool,
) -> Vec<AllowedAlgorithm> {
    let mut current: std::collections::HashSet<AllowedAlgorithm> = if require_approved {
        detected
            .iter()
            .filter(|algo| algo.is_approved())
            .copied()
            .collect()
    } else {
        detected.iter().copied().collect()
    };

    // 1. Most specific wins (suppression rules)
    // Tree DP suppresses Dynamic Programming and DFS
    if current.contains(&AllowedAlgorithm::TreeDp) {
        current.remove(&AllowedAlgorithm::DynamicProgramming);
        current.remove(&AllowedAlgorithm::Dfs);
        current.remove(&AllowedAlgorithm::KadanesAlgorithm);
    }

    // Bitmask DP suppresses Dynamic Programming
    if current.contains(&AllowedAlgorithm::BitmaskDp) {
        current.remove(&AllowedAlgorithm::DynamicProgramming);
    }

    // Interval DP suppresses Dynamic Programming
    if current.contains(&AllowedAlgorithm::IntervalDp) {
        current.remove(&AllowedAlgorithm::DynamicProgramming);
    }

    // Knapsack DP suppresses Dynamic Programming
    if current.contains(&AllowedAlgorithm::KnapsackDp) {
        current.remove(&AllowedAlgorithm::DynamicProgramming);
    }

    // 2D DP suppresses Dynamic Programming
    if current.contains(&AllowedAlgorithm::TwoDDp) {
        current.remove(&AllowedAlgorithm::DynamicProgramming);
    }

    // 1D DP suppresses Dynamic Programming
    if current.contains(&AllowedAlgorithm::OneDDp) {
        current.remove(&AllowedAlgorithm::DynamicProgramming);
    }

    // Dijkstra suppresses BFS and Heap / Priority Queue
    if current.contains(&AllowedAlgorithm::Dijkstra) {
        current.remove(&AllowedAlgorithm::Bfs);
        current.remove(&AllowedAlgorithm::HeapPriorityQueue);
    }

    // Topological Sort suppresses BFS and DFS
    if current.contains(&AllowedAlgorithm::TopologicalSort) {
        current.remove(&AllowedAlgorithm::Bfs);
        current.remove(&AllowedAlgorithm::Dfs);
    }

    // Strongly Connected Components suppresses DFS
    if current.contains(&AllowedAlgorithm::StronglyConnectedComponents) {
        current.remove(&AllowedAlgorithm::Dfs);
    }

    // Bridges and Articulation Points suppresses DFS
    if current.contains(&AllowedAlgorithm::BridgesAndArticulationPoints) {
        current.remove(&AllowedAlgorithm::Dfs);
    }

    // Eulerian Path suppresses DFS
    if current.contains(&AllowedAlgorithm::EulerianPath) {
        current.remove(&AllowedAlgorithm::Dfs);
    }

    // Binary Search on Answer suppresses Binary Search
    if current.contains(&AllowedAlgorithm::BinarySearchOnAnswer) {
        current.remove(&AllowedAlgorithm::BinarySearch);
    }

    // Sliding Window suppresses Two Pointers
    if current.contains(&AllowedAlgorithm::SlidingWindow) {
        current.remove(&AllowedAlgorithm::TwoPointers);
    }

    // Top K and Two Heaps suppress Heap / Priority Queue
    if current.contains(&AllowedAlgorithm::TopK) || current.contains(&AllowedAlgorithm::TwoHeaps) {
        current.remove(&AllowedAlgorithm::HeapPriorityQueue);
    }

    // Heap / Priority Queue suppresses Sorting
    if current.contains(&AllowedAlgorithm::HeapPriorityQueue) {
        current.remove(&AllowedAlgorithm::Sorting);
    }

    // Monotonic Stack suppresses Stack
    if current.contains(&AllowedAlgorithm::MonotonicStack) {
        current.remove(&AllowedAlgorithm::Stack);
    }

    // Monotonic Queue suppresses Queue and Stack
    if current.contains(&AllowedAlgorithm::MonotonicQueue) {
        current.remove(&AllowedAlgorithm::Queue);
        current.remove(&AllowedAlgorithm::Stack);
    }

    // Dijkstra suppresses Queue
    if current.contains(&AllowedAlgorithm::Dijkstra) {
        current.remove(&AllowedAlgorithm::Queue);
    }

    // KMP suppresses Stack
    if current.contains(&AllowedAlgorithm::Kmp) {
        current.remove(&AllowedAlgorithm::Stack);
    }

    // Fenwick Tree and Segment Tree suppress Difference Array
    if current.contains(&AllowedAlgorithm::FenwickTree)
        || current.contains(&AllowedAlgorithm::SegmentTree)
    {
        current.remove(&AllowedAlgorithm::DifferenceArray);
    }

    // Lazy Segment Tree suppresses Segment Tree
    if current.contains(&AllowedAlgorithm::LazySegmentTree) {
        current.remove(&AllowedAlgorithm::SegmentTree);
    }

    // Fenwick Tree and Segment Tree suppress Prefix Sum only when the prefix sums are computed through the tree
    if (current.contains(&AllowedAlgorithm::FenwickTree)
        || current.contains(&AllowedAlgorithm::SegmentTree)
        || current.contains(&AllowedAlgorithm::LazySegmentTree))
        && !source.contains("pref[")
        && !source.contains("prefix[")
    {
        current.remove(&AllowedAlgorithm::PrefixSum);
    }

    // Memoization suppresses Dynamic Programming
    if current.contains(&AllowedAlgorithm::Memoization) {
        current.remove(&AllowedAlgorithm::DynamicProgramming);
    }

    // Dijkstra suppresses Shortest Path
    if current.contains(&AllowedAlgorithm::Dijkstra) {
        current.remove(&AllowedAlgorithm::ShortestPath);
    }

    // Shortest Path suppresses BFS and Queue
    if current.contains(&AllowedAlgorithm::ShortestPath) {
        current.remove(&AllowedAlgorithm::Bfs);
        current.remove(&AllowedAlgorithm::Queue);
    }

    // Sparse Table suppresses Bit Manipulation
    if current.contains(&AllowedAlgorithm::SparseTable) {
        current.remove(&AllowedAlgorithm::BitManipulation);
    }

    // Sliding Window suppresses Frequency Counting
    if current.contains(&AllowedAlgorithm::SlidingWindow) {
        current.remove(&AllowedAlgorithm::FrequencyCounting);
    }

    // LCM suppresses GCD
    if current.contains(&AllowedAlgorithm::Lcm) {
        current.remove(&AllowedAlgorithm::Gcd);
    }

    // Fast Exponentiation suppresses Modular Arithmetic
    if current.contains(&AllowedAlgorithm::FastExponentiation) {
        current.remove(&AllowedAlgorithm::ModularArithmetic);
    }

    // Combinatorics suppresses Modular Arithmetic
    if current.contains(&AllowedAlgorithm::Combinatorics) {
        current.remove(&AllowedAlgorithm::ModularArithmetic);
    }

    // Frequency Counting suppresses HashMap
    if current.contains(&AllowedAlgorithm::FrequencyCounting) {
        current.remove(&AllowedAlgorithm::HashMap);
    }

    // Backtracking suppresses DFS
    if current.contains(&AllowedAlgorithm::Backtracking) {
        current.remove(&AllowedAlgorithm::Dfs);
    }

    // Binary Search Tree suppresses DFS
    if current.contains(&AllowedAlgorithm::BinarySearchTree) {
        current.remove(&AllowedAlgorithm::Dfs);
    }

    let mut result: Vec<AllowedAlgorithm> = current.into_iter().collect();

    // Deterministic priority ordering: lower priority number = higher precedence
    result.sort_by_key(|a| a.priority());

    // Keep at most 3 labels with the highest priority
    if result.len() > 3 {
        result.truncate(3);
    }

    result
}

pub fn apply_selection_rules(detected: &[AllowedAlgorithm], source: &str) -> Vec<AllowedAlgorithm> {
    select_labels(detected, source, true)
}

fn has_sieve_structure(source: &str) -> bool {
    let mut rest = source;
    while let Some(for_pos) = rest.find("for") {
        let after_for = &rest[for_pos + 3..];
        if let Some(open_paren) = after_for.find('(') {
            let for_hdr = &after_for[open_paren + 1..];
            if let Some(close_paren) = for_hdr.find(')') {
                let hdr = for_hdr[..close_paren].trim();
                let parts: Vec<&str> = hdr.split(';').collect();
                if parts.len() == 3 {
                    let init_part = parts[0].trim();
                    let v_init = init_part.split('=').next().unwrap_or("").trim();
                    let outer_var = v_init
                        .split_whitespace()
                        .last()
                        .unwrap_or("")
                        .trim_matches(|c: char| !c.is_alphanumeric() && c != '_');
                    if !outer_var.is_empty() {
                        let body_slice = &for_hdr[close_paren + 1..];
                        let mut inner_rest = body_slice;
                        while let Some(inner_for_pos) = inner_rest.find("for") {
                            let after_inner = &inner_rest[inner_for_pos + 3..];
                            if let Some(inner_open) = after_inner.find('(') {
                                let inner_hdr_slice = &after_inner[inner_open + 1..];
                                if let Some(inner_close) = inner_hdr_slice.find(')') {
                                    let inner_hdr = inner_hdr_slice[..inner_close].trim();
                                    let inner_parts: Vec<&str> = inner_hdr.split(';').collect();
                                    if inner_parts.len() == 3 {
                                        let inner_step = inner_parts[2].trim();
                                        let step1 = format!("+= {outer_var}");
                                        let step2 = format!("+={outer_var}");
                                        if inner_step.contains(&step1)
                                            || inner_step.contains(&step2)
                                        {
                                            let body_candidate = inner_hdr_slice[inner_close + 1..].trim_start();
                                            let inner_body = if body_candidate.starts_with('{') {
                                                let mut depth = 0;
                                                let mut end_idx = body_candidate.len();
                                                for (i, c) in body_candidate.char_indices() {
                                                    if c == '{' {
                                                        depth += 1;
                                                    } else if c == '}' {
                                                        depth -= 1;
                                                        if depth == 0 {
                                                            end_idx = i + 1;
                                                            break;
                                                        }
                                                    }
                                                }
                                                &body_candidate[..end_idx]
                                            } else if let Some(semi) = body_candidate.find(';') {
                                                &body_candidate[..=semi]
                                            } else {
                                                body_candidate
                                            };
                                            let has_mark = inner_body.contains('[')
                                                && (inner_body.contains("= false")
                                                    || inner_body.contains("=false")
                                                    || inner_body.contains("= 0")
                                                    || inner_body.contains("=0")
                                                    || inner_body.contains("= true")
                                                    || inner_body.contains("= 1"));
                                            if has_mark {
                                                return true;
                                            }
                                        }
                                    }
                                }
                            }
                            inner_rest = &after_inner[1..];
                        }
                    }
                }
            }
        }
        rest = &after_for[1..];
    }
    false
}

fn has_two_pointers_structure(source: &str) -> bool {
    let mut rest = source;
    while let Some(while_pos) = rest.find("while") {
        let after_while = &rest[while_pos + 5..];
        if let Some(open_paren) = after_while.find('(') {
            let cond_start = &after_while[open_paren + 1..];
            if let Some(close_paren) = cond_start.find(')') {
                let cond = cond_start[..close_paren].trim();
                let parts: Vec<&str> = if cond.contains("<=") {
                    cond.split("<=").collect()
                } else if cond.contains('<') {
                    cond.split('<').collect()
                } else {
                    Vec::new()
                };
                if parts.len() == 2 {
                    let v1 = parts[0]
                        .trim()
                        .trim_matches(|c: char| !c.is_alphanumeric() && c != '_');
                    let v2 = parts[1]
                        .trim()
                        .trim_matches(|c: char| !c.is_alphanumeric() && c != '_');
                    if !v1.is_empty() && !v2.is_empty() && v1 != v2 {
                        let body_slice = &cond_start[close_paren + 1..];
                        let has_v1_inc = body_slice.contains(&format!("{v1}++"))
                            || body_slice.contains(&format!("{v1} += 1"))
                            || body_slice.contains(&format!("{v1} += 1;"))
                            || body_slice.contains(&format!("{v1}+=1"))
                            || body_slice.contains(&format!("++{v1}"));
                        let has_v2_dec = body_slice.contains(&format!("{v2}--"))
                            || body_slice.contains(&format!("{v2} -= 1"))
                            || body_slice.contains(&format!("{v2} -= 1;"))
                            || body_slice.contains(&format!("{v2}-=1"))
                            || body_slice.contains(&format!("--{v2}"));
                        if has_v1_inc && has_v2_dec {
                            return true;
                        }
                    }
                }
            }
        }
        rest = &after_while[1..];
    }
    false
}

fn has_binary_search_structure(source: &str) -> bool {
    let mut rest = source;
    while let Some(while_pos) = rest.find("while") {
        let after_while = &rest[while_pos + 5..];
        if let Some(open_paren) = after_while.find('(') {
            let cond_start = &after_while[open_paren + 1..];
            if let Some(close_paren) = cond_start.find(')') {
                let cond = cond_start[..close_paren].trim();
                let parts: Vec<&str> = if cond.contains("<=") {
                    cond.split("<=").collect()
                } else if cond.contains('<') {
                    cond.split('<').collect()
                } else {
                    Vec::new()
                };
                if parts.len() == 2 {
                    let v1 = parts[0]
                        .trim()
                        .trim_matches(|c: char| !c.is_alphanumeric() && c != '_');
                    let v2 = parts[1]
                        .trim()
                        .trim_matches(|c: char| !c.is_alphanumeric() && c != '_');
                    if !v1.is_empty() && !v2.is_empty() && v1 != v2 {
                        let body_slice = &cond_start[close_paren + 1..];
                        let has_halving = body_slice.contains("/ 2")
                            || body_slice.contains("/2")
                            || body_slice.contains(">> 1")
                            || body_slice.contains(">>1");
                        let has_v1_update = body_slice.contains(&format!("{v1} ="))
                            || body_slice.contains(&format!("{v1}="));
                        let has_v2_update = body_slice.contains(&format!("{v2} ="))
                            || body_slice.contains(&format!("{v2}="));
                        if has_halving && has_v1_update && has_v2_update {
                            return true;
                        }
                    }
                }
            }
        }
        rest = &after_while[1..];
    }
    false
}

fn has_monotonic_stack_structure(source: &str) -> bool {
    let has_stack_type = source.contains("stack<")
        || source.contains("Stack<")
        || source.contains("ArrayDeque")
        || source.contains("Deque<")
        || source.contains("stack")
        || source.contains("Stack");

    let mut rest = source;
    while let Some(while_pos) = rest.find("while") {
        let after_while = &rest[while_pos + 5..];
        if let Some(open_paren) = after_while.find('(') {
            let cond_start = &after_while[open_paren + 1..];
            if let Some(close_paren) = cond_start.find(')') {
                let cond = &cond_start[..close_paren];
                let has_empty_check = cond.contains(".empty")
                    || cond.contains(".isEmpty")
                    || cond.contains(".size()")
                    || cond.contains(".size >")
                    || cond.contains(".size() >");
                let has_cmp = cond.contains('<') || cond.contains('>');
                let body_slice = &cond_start[close_paren + 1..];
                let window = if body_slice.len() > 400 {
                    &body_slice[..400]
                } else {
                    body_slice
                };
                let has_pop = window.contains(".pop()")
                    || window.contains(".pop();")
                    || window.contains(".pollLast()");
                if has_empty_check && has_cmp && has_pop && has_stack_type {
                    return true;
                }
            }
        }
        rest = &after_while[1..];
    }
    false
}

#[inline]
pub(crate) fn contains_any(source: &str, patterns: &[&str]) -> bool {
    patterns.iter().any(|&p| source.contains(p))
}


pub struct AlgorithmDetector;

impl AlgorithmDetector {
    pub fn detect(source: &str) -> Vec<AllowedAlgorithm> {
        apply_selection_rules(&Self::detect_raw(source), source)
    }

    pub fn detect_raw(source: &str) -> Vec<AllowedAlgorithm> {
        let mut detected = Vec::new();

        // 1. Sieve
        let has_prime_ident = contains_any(
            source,
            &[
                "p * p", "p*p", "i * i", "i*i", "d * d", "d*d", "isPrime", "is_prime",
                "primes", "prime", "sieve", "seive", "composite", "isComp", "not_prime",
            ],
        );
        let has_sieve_step = contains_any(
            source,
            &[
                "+= p", "+=p", "+= i", "+=i", "+= j", "+=j", "+= d", "+=d", "+= prime",
            ],
        );
        if (has_prime_ident && has_sieve_step)
            || has_sieve_structure(source)
            || contains_any(source, &["void sieve", "sieve("])
        {
            detected.push(AllowedAlgorithm::Sieve);
        }

        // 2. Segment Tree
        if contains_any(source, &["4 * n", "4*n", "2 * node", "2*node"])
            && contains_any(source, &["mid", "update", "query"])
        {
            detected.push(AllowedAlgorithm::SegmentTree);
        }

        // 3. Fenwick Tree
        let has_lowbit = contains_any(source, &["& -", "&-"]);
        if (has_lowbit || contains_any(source, &["Fenwick", "BinaryIndexedTree"]))
            && !detected.contains(&AllowedAlgorithm::SegmentTree)
            && (contains_any(source, &["Fenwick", "BinaryIndexedTree"])
                || (contains_any(source, &["add(", "update(", "add ", "update "])
                    && contains_any(source, &["query(", "query ", "sumRange", "sum("])))
        {
            detected.push(AllowedAlgorithm::FenwickTree);
        }

        // 4. Sparse Table
        if contains_any(
            source,
            &[
                "st[",
                "st.",
                " st(",
                "\nst(",
                "SparseTable",
                "sparse_table",
            ],
        ) && contains_any(
            source,
            &[
                "1 << j",
                "1<<j",
                "31 - __builtin_clz",
                "numberOfLeadingZeros",
            ],
        ) {
            detected.push(AllowedAlgorithm::SparseTable);
        }

        // 5. DSU & MST
        let has_dsu = ((source.contains("find(") || source.contains("find ("))
            && (source.contains("unite(")
                || source.contains("union(")
                || source.contains("unite (")
                || source.contains("union (")))
            || ((source.contains("parent")
                || source.contains("parent[")
                || source.contains("root")
                || source.contains("dsu.")
                || source.contains("dsu->")
                || source.contains("DSU")
                || source.contains("DisjointSet"))
                && (source.contains("find(")
                    || source.contains("unite(")
                    || source.contains("union(")));

        if (has_dsu
            && (source.contains("weight")
                || source.contains("cost")
                || source.contains("Edge")
                || source.contains("edge"))
            && (source.contains("sort")
                || source.contains("Sort")
                || source.contains("mst")
                || source.contains("MST")
                || source.contains("Kruskal")
                || source.contains("kruskal")))
            || (source.contains("prim(")
                || source.contains("Prim(")
                || source.contains("prims(")
                || source.contains("Prims(")
                || source.contains("prim_mst")
                || source.contains("kruskal_mst"))
        {
            detected.push(AllowedAlgorithm::Mst);
        } else if has_dsu {
            detected.push(AllowedAlgorithm::Dsu);
        }

        // 6. Binary Lifting & LCA
        let has_binary_lifting =
            (source.contains("up[") || source.contains("ancestor[") || source.contains("jump["))
                && (source.contains("1 <<")
                    || source.contains("1<<")
                    || source.contains("LOG")
                    || source.contains("LOGN")
                    || source.contains("20"));
        let has_tree_lca = source.contains("lowestCommonAncestor")
            || source.contains("LCA(")
            || source.contains("lca(")
            || (source.contains(".left")
                && source.contains(".right")
                && source.contains("== p")
                && source.contains("== q"));
        if (has_binary_lifting
            && (source.contains("lca(")
                || source.contains("LCA")
                || source.contains("depth[")
                || source.contains("tin[")))
            || has_tree_lca
        {
            detected.push(AllowedAlgorithm::Lca);
            if has_binary_lifting {
                detected.push(AllowedAlgorithm::BinaryLifting);
            }
        } else if has_binary_lifting {
            detected.push(AllowedAlgorithm::BinaryLifting);
        }

        // 7. Z Algorithm
        if source.contains("z_algorithm")
            || source.contains("zAlgorithm")
            || source.contains("z_box")
            || ((source.contains("z[") || source.contains("z."))
                && (source.contains("r - i + 1")
                    || (source.contains("l = i") && source.contains("r = "))
                    || source.contains("z[k]")))
        {
            detected.push(AllowedAlgorithm::ZAlgorithm);
        }

        // 8. Rolling Hash
        if (source.contains("hash") || source.contains("Hash") || source.contains("poly_hash"))
            && (source.contains("p_pow")
                || source.contains("power[")
                || source.contains("base")
                || source.contains("BASE"))
            && (source.contains("%") || source.contains("MOD"))
        {
            detected.push(AllowedAlgorithm::RollingHash);
        }

        // 9. Dijkstra
        if (source.contains("priority_queue") || source.contains("PriorityQueue"))
            && (source.contains("dist[") || source.contains("dist.") || source.contains("weight"))
        {
            detected.push(AllowedAlgorithm::Dijkstra);
        }

        // 10. Topological Sort
        if (source.contains("in_degree")
            || source.contains("inDegree")
            || source.contains("indegree"))
            && (source.contains("queue")
                || source.contains("Queue")
                || source.contains("q.push")
                || source.contains("q.add"))
        {
            detected.push(AllowedAlgorithm::TopologicalSort);
        }

        // 11. BFS
        if (source.contains("queue")
            || source.contains("Queue")
            || source.contains("LinkedList")
            || source.contains("deque")
            || source.contains("Deque")
            || source.contains("popleft")
            || source.contains("bfs(")
            || source.contains("bfs (")
            || source.contains("def bfs")
            || source.contains("void bfs"))
            && (source.contains("vis[")
                || source.contains("visited")
                || source.contains("vis.")
                || source.contains("dist[")
                || source.contains("dist.")
                || source.contains("grid[")
                || source.contains("grid.")
                || source.contains("board[")
                || source.contains("matrix[")
                || source.contains("steps")
                || source.contains("depth")
                || source.contains("level"))
            && !detected.contains(&AllowedAlgorithm::TopologicalSort)
            && !detected.contains(&AllowedAlgorithm::Dijkstra)
        {
            detected.push(AllowedAlgorithm::Bfs);
        }

        // 12. Tree DP
        let has_tree_par_dp = (source.contains("!= p")
            || source.contains("p !=")
            || source.contains("!= parent")
            || source.contains("parent !=")
            || source.contains("!= par"))
            && (source.contains("dp[") || source.contains("sz[") || source.contains("sz."));
        let has_binary_tree_dp = (source.contains("TreeNode")
            || source.contains("root->left")
            || source.contains("root.left"))
            && (source.contains("left") && source.contains("right"))
            && (source.contains("max(") || source.contains("Math.max("))
            && (source.contains("gain") || source.contains("Gain") || source.contains("diameter") || source.contains("Diameter") || source.contains("path") || source.contains("price") || source.contains("rob") || source.contains("dp"));
        if has_tree_par_dp || has_binary_tree_dp {
            detected.push(AllowedAlgorithm::TreeDp);
        }

        // 13. DFS
        if !detected.contains(&AllowedAlgorithm::TreeDp)
            && (source.contains("dfs(") || source.contains("dfs (") || source.contains("dfs "))
            && (source.contains("vis[")
                || source.contains("vis.")
                || source.contains("visited")
                || source.contains("adj[")
                || source.contains("adj.")
                || source.contains("grid[")
                || source.contains("grid.")
                || source.contains("board[")
                || source.contains("matrix[")
                || source.contains("path")
                || source.contains("start")
                || source.contains("idx")
                || source.contains("dfs(grid")
                || source.contains("dfs (grid")
                || source.contains("dfs(r")
                || source.contains("dfs(i"))
        {
            detected.push(AllowedAlgorithm::Dfs);
        }

        // 14. Bitmask DP
        if ((source.contains("1 << n")
            || source.contains("1<<n")
            || source.contains("1 << ")
            || source.contains("1<<")
            || source.contains("& mask")
            || source.contains("&mask")
            || source.contains("& sub")
            || source.contains("bitCount"))
            && (source.contains("mask") || source.contains("dp[") || source.contains("dp =")))
            || source.contains("bitmask")
            || source.contains("Bitmask")
        {
            detected.push(AllowedAlgorithm::BitmaskDp);
        }

        // 15. Monotonic Stack
        let has_stack = source.contains("stack<")
            || source.contains("Stack<")
            || source.contains("ArrayDeque")
            || source.contains("Deque<")
            || source.contains("st.push")
            || source.contains("st.pop")
            || source.contains("stk.push")
            || source.contains("stk.pop")
            || source.contains("s.push")
            || source.contains("s.pop")
            || source.contains("stack.push")
            || source.contains("stack.pop");
        let has_mono_loop = (source.contains("while (!st.empty()")
            || source.contains("while (!st.isEmpty()")
            || source.contains("while (!stk.empty()")
            || source.contains("while (!stk.isEmpty()")
            || source.contains("while (!s.empty()")
            || source.contains("while (!s.isEmpty()")
            || source.contains("while (!stack.empty()")
            || source.contains("while (!stack.isEmpty()")
            || source.contains("while (st.size()")
            || source.contains("while (stk.size()")
            || source.contains("while (stack.size()")
            || source.contains("while (!st.empty")
            || source.contains("while (!stack.empty"))
            && (source.contains("<") || source.contains(">"));
        if (has_stack && has_mono_loop) || has_monotonic_stack_structure(source) {
            detected.push(AllowedAlgorithm::MonotonicStack);
        }

        // 16. Monotonic Queue
        if (source.contains("deque<") || source.contains("Deque") || source.contains("ArrayDeque"))
            && (source.contains("pop_front") || source.contains("pollFirst"))
            && (source.contains("pop_back") || source.contains("pollLast"))
        {
            detected.push(AllowedAlgorithm::MonotonicQueue);
        }

        // 17. Prefix Sum
        let has_prefix_expr = source.contains("pref[i - 1]")
            || source.contains("pref[i-1]")
            || source.contains("pref[i + 1]")
            || source.contains("pref[i+1]")
            || source.contains("prefix[i - 1]")
            || source.contains("prefix[i-1]")
            || source.contains("prefix[i + 1]")
            || source.contains("prefix[i+1]")
            || source.contains("prefixSum[i - 1]")
            || source.contains("prefixSum[i-1]")
            || source.contains("pre[i - 1]")
            || source.contains("pre[i-1]")
            || source.contains("sum[i - 1]")
            || source.contains("sum[i-1]")
            || source.contains("psum[i - 1]")
            || source.contains("psum[i-1]")
            || (source.contains("pref[")
                && (source.contains("- pref[")
                    || source.contains("+ nums[")
                    || source.contains("+ a[")))
            || (source.contains("prefix[")
                && (source.contains("- prefix[")
                    || source.contains("+ nums[")
                    || source.contains("+ a[")));
        if has_prefix_expr && !detected.contains(&AllowedAlgorithm::FenwickTree) {
            detected.push(AllowedAlgorithm::PrefixSum);
        }

        // 18. Binary Search on Answer & 19. Binary Search
        let has_bs_bounds = source.contains("low <= high")
            || source.contains("low < high")
            || source.contains("l <= r")
            || source.contains("l < r")
            || source.contains("left <= right")
            || source.contains("left < right")
            || source.contains("lo <= hi")
            || source.contains("lo < hi")
            || source.contains("start <= end")
            || source.contains("start < end");

        let has_bs_mid = (source.contains("mid =")
            || source.contains("mid=")
            || source.contains("int mid")
            || source.contains("long mid")
            || source.contains("auto mid")
            || source.contains("mid :=")
            || source.contains(" m =")
            || source.contains(" m=")
            || source.contains("\nm =")
            || source.contains("\nm="))
            && (source.contains("/ 2")
                || source.contains("/2")
                || source.contains(">> 1")
                || source.contains(">>1"));

        let has_bs_update = (source.contains("high =")
            || source.contains("high=")
            || source.contains("r =")
            || source.contains("r=")
            || source.contains("right =")
            || source.contains("right=")
            || source.contains("hi =")
            || source.contains("hi=")
            || source.contains("end =")
            || source.contains("end="))
            && (source.contains("low =")
                || source.contains("low=")
                || source.contains("l =")
                || source.contains("l=")
                || source.contains("left =")
                || source.contains("left=")
                || source.contains("lo =")
                || source.contains("lo=")
                || source.contains("start =")
                || source.contains("start="));

        let is_binary_search = ((has_bs_bounds && has_bs_mid && has_bs_update)
            || has_binary_search_structure(source))
            && !detected.contains(&AllowedAlgorithm::SegmentTree);

        let has_bs_answer_predicate = source.contains("check(")
            || source.contains("check (")
            || source.contains("isPossible(")
            || source.contains("isPossible (")
            || source.contains("isValid(")
            || source.contains("isValid (")
            || source.contains("can(")
            || source.contains("can (")
            || source.contains("feasible(")
            || source.contains("good(")
            || source.contains("ok(");

        let has_inner_loop_in_bs = if is_binary_search {
            let mut in_while = false;
            let mut found_inner_loop = false;
            for line in source.lines() {
                let trimmed = line.trim();
                if trimmed.starts_with("while")
                    && (trimmed.contains("low")
                        || trimmed.contains("l <")
                        || trimmed.contains("l <=")
                        || trimmed.contains("left")
                        || trimmed.contains("lo")
                        || trimmed.contains("start"))
                {
                    in_while = true;
                } else if in_while
                    && (trimmed.starts_with("for ")
                        || trimmed.starts_with("for(")
                        || trimmed.starts_with("for:"))
                {
                    found_inner_loop = true;
                    break;
                } else if in_while && trimmed.starts_with("return ") {
                    in_while = false;
                }
            }
            found_inner_loop
        } else {
            false
        };

        if is_binary_search && (has_bs_answer_predicate || has_inner_loop_in_bs) {
            detected.push(AllowedAlgorithm::BinarySearchOnAnswer);
        } else if is_binary_search {
            detected.push(AllowedAlgorithm::BinarySearch);
        }

        // 20. Two Pointers
        let has_two_pointers_bounds = source.contains("l < r")
            || source.contains("l <= r")
            || source.contains("left < right")
            || source.contains("left <= right")
            || source.contains("low < high")
            || source.contains("low <= high")
            || source.contains("lo < hi")
            || source.contains("lo <= hi")
            || source.contains("start < end")
            || source.contains("start <= end")
            || source.contains("i < j")
            || source.contains("i <= j");
        let has_two_pointers_adv = (source.contains("l++")
            || source.contains("left++")
            || source.contains("low++")
            || source.contains("lo++")
            || source.contains("start++")
            || source.contains("i++"))
            && (source.contains("r--")
                || source.contains("right--")
                || source.contains("high--")
                || source.contains("hi--")
                || source.contains("end--")
                || source.contains("j--"));
        let is_two_pointers = ((has_two_pointers_bounds && has_two_pointers_adv)
            || has_two_pointers_structure(source))
            && !is_binary_search;
        if is_two_pointers {
            detected.push(AllowedAlgorithm::TwoPointers);
        }

        // 21. Sliding Window
        let has_sliding_window = (source.contains("for (int r = 0")
            || source.contains("for (int right = 0")
            || source.contains("for (int j = 0")
            || source.contains("for (int end = 0")
            || source.contains("r++")
            || source.contains("right++"))
            && (source.contains("while (") || source.contains("while("))
            && (source.contains("l++") || source.contains("left++") || source.contains("start++"));
        if has_sliding_window
            && !detected.contains(&AllowedAlgorithm::TwoPointers)
            && !is_binary_search
        {
            detected.push(AllowedAlgorithm::SlidingWindow);
        }

        // 22. KMP
        if (source.contains("pi[")
            || source.contains("pi.")
            || source.contains("pi(")
            || source.contains("lps[")
            || source.contains("lps.")
            || source.contains("lps"))
            && (source.contains("pattern")
                || source.contains("needle")
                || source.contains("match")
                || source.contains("pi[i - 1]"))
        {
            detected.push(AllowedAlgorithm::Kmp);
        }

        // 23. Trie
        if source.contains("child[26]")
            || source.contains("Node[26]")
            || source.contains("child[2]")
            || source.contains("Node[2]")
            || source.contains("is_end")
            || source.contains("isEnd")
            || (source.contains("TrieNode") && (source.contains("child") || source.contains("children")))
        {
            detected.push(AllowedAlgorithm::Trie);
        }

        // 24. Sorting (only when main technique)
        if (source.contains("std::sort")
            || source.contains("Arrays.sort")
            || source.contains("Collections.sort"))
            && detected.is_empty()
        {
            detected.push(AllowedAlgorithm::Sorting);
        }

        // 25. Kadane's Algorithm
        let has_kadane_reset = (source.contains("< 0") || source.contains("<= 0"))
            && (source.contains("= 0;")
                || source.contains("= 0\n")
                || source.contains("= 0 }")
                || source.contains("= 0}")
                || source.contains("=0;"))
            && (source.contains("+=") || source.contains("+ ="));
        let has_kadane_max_choice = (source.contains("max(") || source.contains("Math.max("))
            && (source.contains("max(0,")
                || source.contains("max(0LL,")
                || source.contains("Math.max(0,")
                || source.contains("cur +")
                || source.contains("cur_max +")
                || source.contains("curr +")
                || source.contains("curr_max +")
                || source.contains("sum +")
                || source.contains("current +")
                || source.contains("current_sum +")
                || source.contains("running +")
                || source.contains("running_sum +")
                || source.contains("dp[i - 1] +")
                || source.contains("dp[i-1] +")
                || source.contains("best +")
                || source.contains("ans +"));
        let tracks_global_max = source.contains("max(")
            || source.contains("Math.max(")
            || (source.contains("if")
                && (source.contains(" > ")
                    || source.contains(">")
                    || source.contains(" < ")
                    || source.contains("<")));
        let not_sliding_window = !source.contains("l++") && !source.contains("left++");

        if (has_kadane_reset || has_kadane_max_choice)
            && tracks_global_max
            && not_sliding_window
            && !detected.contains(&AllowedAlgorithm::TwoPointers)
            && !detected.contains(&AllowedAlgorithm::BinarySearchOnAnswer)
            && !detected.contains(&AllowedAlgorithm::BinarySearch)
        {
            detected.push(AllowedAlgorithm::KadanesAlgorithm);
        }

        // 26. Fast and Slow Pointers
        let has_fast_slow = (source.contains("->next->next") || source.contains(".next.next"))
            && (source.contains("->next") || source.contains(".next"));
        if has_fast_slow && !detected.contains(&AllowedAlgorithm::TwoPointers) {
            detected.push(AllowedAlgorithm::FastAndSlowPointers);
        }

        // 27. Difference Array
        let has_diff_ops = (source.contains("+=") || source.contains("++"))
            && (source.contains("-=") || source.contains("--"))
            && (source.contains("+ 1]") || source.contains("+1]"));
        if has_diff_ops
            && (source.contains("diff")
                || source.contains("d[")
                || source.contains("delta")
                || (source.contains("[r + 1]") || source.contains("[r+1]")))
        {
            detected.push(AllowedAlgorithm::DifferenceArray);
        }

        // 28. Coordinate Compression
        let has_coord_comp = (source.contains("unique(") || source.contains("std::unique"))
            && (source.contains("lower_bound") || source.contains("binary_search"));
        if has_coord_comp {
            detected.push(AllowedAlgorithm::CoordinateCompression);
        }

        // 29. Intervals
        let has_intervals = (source.contains("interval")
            || source.contains("Interval")
            || source.contains("[0]")
            || source.contains(".start"))
            && (source.contains("[1]") || source.contains(".end"))
            && (source.contains("sort") || source.contains("Sort"))
            && (source.contains("max(") || source.contains("Math.max("));
        if has_intervals
            && !detected.contains(&AllowedAlgorithm::TwoPointers)
            && !detected.contains(&AllowedAlgorithm::KadanesAlgorithm)
        {
            detected.push(AllowedAlgorithm::Intervals);
        }

        // 30. Matrix / Grid
        let has_grid = (source.contains("grid[")
            || source.contains("matrix[")
            || source.contains("board[")
            || (source.contains("dr") && source.contains("dc"))
            || (source.contains("dx") && source.contains("dy")))
            && (source.contains("< R")
                || source.contains("< m")
                || source.contains("< n")
                || source.contains("< rows")
                || source.contains("grid.length")
                || source.contains("grid.size()"));
        if has_grid
            && !detected.contains(&AllowedAlgorithm::Bfs)
            && !detected.contains(&AllowedAlgorithm::Dfs)
        {
            detected.push(AllowedAlgorithm::MatrixGrid);
        }

        // 31. Two Heaps
        let has_two_heaps = (source.contains("max_heap") || source.contains("maxHeap"))
            && (source.contains("min_heap") || source.contains("minHeap"));
        if has_two_heaps {
            detected.push(AllowedAlgorithm::TwoHeaps);
        }

        // 32. Top K
        let has_heap_base = source.contains("priority_queue")
            || source.contains("PriorityQueue")
            || source.contains("heapq");
        let has_top_k = has_heap_base
            && (source.contains(".size() > k")
                || source.contains(".size() > K")
                || source.contains(".size() == k")
                || source.contains(".size() == K")
                || source.contains(".size() >= k"));
        if has_top_k && !has_two_heaps {
            detected.push(AllowedAlgorithm::TopK);
        }

        // 33. Heap / Priority Queue
        if has_heap_base
            && !has_two_heaps
            && !detected.contains(&AllowedAlgorithm::Dijkstra)
        {
            detected.push(AllowedAlgorithm::HeapPriorityQueue);
        }

        // 34. Stack
        let has_vector_stack = (source.contains(".push_back(")
            || source.contains(".emplace_back("))
            && (source.contains(".pop_back()") || source.contains(".back()"))
            && !source.contains("vector<vector<");
        if (has_stack || has_vector_stack)
            && !detected.contains(&AllowedAlgorithm::MonotonicStack)
            && (!source.contains("Queue<")
                || source.contains("Stack<")
                || source.contains("stack<"))
        {
            detected.push(AllowedAlgorithm::Stack);
        }

        // 35. Queue
        let has_queue_base = source.contains("queue<")
            || source.contains("Queue<")
            || (source.contains("ArrayDeque")
                && (source.contains(".add(")
                    || source.contains(".offer(")
                    || source.contains(".remove(")
                    || source.contains(".poll(")))
            || (source.contains("LinkedList<")
                && (source.contains(".offer(") || source.contains(".poll(")));
        if has_queue_base
            && !detected.contains(&AllowedAlgorithm::Bfs)
            && !detected.contains(&AllowedAlgorithm::TopologicalSort)
            && !detected.contains(&AllowedAlgorithm::MonotonicQueue)
            && !detected.contains(&AllowedAlgorithm::MonotonicStack)
            && (!detected.contains(&AllowedAlgorithm::Stack)
                || source.contains("Queue<")
                || source.contains("queue<"))
        {
            detected.push(AllowedAlgorithm::Queue);
        }

        // 36. Linked List Reversal
        let has_reverse_list = (source.contains("prev = null")
            || source.contains("prev = nullptr")
            || source.contains("prev = NULL"))
            && (source.contains(".next = prev")
                || source.contains("->next = prev")
                || source.contains("curr.next = prev")
                || source.contains("curr->next = prev"));
        if has_reverse_list {
            detected.push(AllowedAlgorithm::LinkedListReversal);
        }

        // 37. Cycle Detection
        let has_cycle = source.contains("hasCycle")
            || source.contains("detectCycle")
            || source.contains("isCycle")
            || source.contains("tortoise != hare")
            || source.contains("tortoise == hare")
            || source.contains("slow == fast")
            || (source.contains("vis[") && (source.contains("== 1") || source.contains("== 2")));
        if has_cycle {
            detected.push(AllowedAlgorithm::CycleDetection);
        }

        // 38. Merge Linked Lists
        let has_merge_lists = source.contains("mergeTwoLists")
            || source.contains("mergeKLists")
            || ((source.contains(".next") || source.contains("->next"))
                && (source.contains("l1.val < l2.val")
                    || source.contains("list1->val < list2->val")
                    || source.contains("list1.val <= list2.val")));
        if has_merge_lists {
            detected.push(AllowedAlgorithm::MergeLinkedLists);
        }

        // 39. Linked List
        let has_linked_list = (source.contains("ListNode")
            || source.contains("Node*")
            || source.contains("class Node")
            || source.contains("struct Node"))
            && (source.contains(".next") || source.contains("->next") || source.contains("next;"));
        if has_linked_list
            && !has_reverse_list
            && !has_merge_lists
            && !has_cycle
            && !detected.contains(&AllowedAlgorithm::FastAndSlowPointers)
        {
            detected.push(AllowedAlgorithm::LinkedList);
        }

        // 40. Lazy Segment Tree
        let has_lazy_seg = (source.contains("lazy[")
            || source.contains("lazy.")
            || source.contains("lazy")
            || source.contains("push_down")
            || source.contains("pushDown")
            || source.contains("push("))
            && (source.contains("tree[")
                || source.contains("seg[")
                || source.contains("tree.")
                || source.contains("tree")
                || source.contains("2 * node")
                || source.contains("2*node")
                || source.contains("<< 1")
                || source.contains("LazySeg")
                || source.contains("LazySegment"));
        if has_lazy_seg {
            detected.push(AllowedAlgorithm::LazySegmentTree);
        }

        // 41. Binary Search Tree
        let has_bst_structure = (source.contains(".left") || source.contains("->left"))
            && (source.contains(".right") || source.contains("->right"))
            && (source.contains(".val")
                || source.contains("->val")
                || source.contains("val <")
                || source.contains("val >")
                || source.contains("< val")
                || source.contains("> val")
                || source.contains("root->val")
                || source.contains("root.val"));
        let has_bst_name = source.contains("BST")
            || source.contains("bst_")
            || source.contains("_bst")
            || source.contains("searchBST")
            || source.contains("isValidBST")
            || source.contains("insertIntoBST");
        if (has_bst_structure || has_bst_name)
            && !detected.contains(&AllowedAlgorithm::SegmentTree)
            && !detected.contains(&AllowedAlgorithm::BinarySearch)
        {
            detected.push(AllowedAlgorithm::BinarySearchTree);
        }

        // 42. Shortest Path (Bellman-Ford, Floyd-Warshall, 0-1 BFS)
        let has_bellman_ford = (source.contains("dist[v] > dist[u]")
            || source.contains("dist[to] > dist[v]")
            || source.contains("d[v] > d[u]"))
            && (source.contains("edges") || source.contains("edge") || source.contains("Edge"));
        let has_floyd_warshall = (source.contains("dist[i][k] + dist[k][j]")
            || source.contains("d[i][k] + d[k][j]")
            || source.contains("dp[i][k] + dp[k][j]"))
            || (source.contains("floyd")
                || source.contains("Floyd")
                || source.contains("bellman")
                || source.contains("Bellman"));
        let has_zero_one_bfs = (source.contains("push_front") || source.contains("addFirst"))
            && (source.contains("push_back") || source.contains("addLast"))
            && (source.contains("dist[") || source.contains("dist."));
        if (has_bellman_ford || has_floyd_warshall || has_zero_one_bfs)
            && !detected.contains(&AllowedAlgorithm::Dijkstra)
        {
            detected.push(AllowedAlgorithm::ShortestPath);
        }

        // 43. Strongly Connected Components
        let has_tarjan_scc = (source.contains("low[") || source.contains("lowlink["))
            && (source.contains("dfn[") || source.contains("tin[") || source.contains("disc["))
            && (source.contains("in_stack")
                || source.contains("inStack")
                || source.contains("onStack")
                || source.contains("on_stack")
                || source.contains("stack.push")
                || source.contains("st.push")
                || source.contains("stk.push"));
        let has_kosaraju = (source.contains("adjRev")
            || source.contains("rev_adj")
            || source.contains("radj")
            || source.contains("g_rev"))
            && (source.contains("dfs") || source.contains("DFS"));
        if has_tarjan_scc
            || has_kosaraju
            || source.contains("scc")
            || source.contains("SCC")
            || source.contains("tarjan")
            || source.contains("kosaraju")
        {
            detected.push(AllowedAlgorithm::StronglyConnectedComponents);
        }

        // 44. Bridges and Articulation Points
        let has_bridges_ap = ((source.contains("low[")
            && (source.contains("tin[") || source.contains("disc[") || source.contains("dfn[")))
            && (source.contains("low[to] > tin[v]")
                || source.contains("low[v] > tin[u]")
                || source.contains("low[to] >= tin[v]")
                || source.contains("low[v] >= tin[u]")
                || source.contains("is_cut")
                || source.contains("isCut")
                || source.contains("bridges")))
            || source.contains("articulation");
        if has_bridges_ap && !detected.contains(&AllowedAlgorithm::StronglyConnectedComponents) {
            detected.push(AllowedAlgorithm::BridgesAndArticulationPoints);
        }

        // 45. Eulerian Path
        let has_eulerian = (source.contains("hierholzer")
            || source.contains("Hierholzer")
            || source.contains("eulerian")
            || source.contains("Eulerian")
            || source.contains("euler")
            || source.contains("Euler"))
            || ((source.contains("out_degree") || source.contains("outdegree"))
                && (source.contains("in_degree") || source.contains("indegree"))
                && source.contains("== 1"));
        if has_eulerian {
            detected.push(AllowedAlgorithm::EulerianPath);
        }

        // 46. GCD
        let has_gcd_loop = (source.contains("%")
            && (source.contains("b == 0")
                || source.contains("b != 0")
                || source.contains("== 0")
                || source.contains("!= 0")))
            && (source.contains("a % b")
                || source.contains("b % a")
                || source.contains("% b")
                || source.contains("% a"));
        let has_gcd_name = source.contains("gcd(")
            || source.contains("gcd (")
            || source.contains("__gcd")
            || source.contains("GCD");
        if has_gcd_loop || has_gcd_name {
            detected.push(AllowedAlgorithm::Gcd);
        }

        // 47. LCM
        let has_lcm_formula = (source.contains("*")
            && source.contains("/")
            && (source.contains("gcd") || source.contains("GCD") || source.contains("__gcd")))
            || source.contains("lcm(")
            || source.contains("lcm (")
            || source.contains("LCM");
        if has_lcm_formula {
            detected.push(AllowedAlgorithm::Lcm);
        }

        // 48. Fast Exponentiation
        let has_fast_pow = (source.contains(">> 1")
            || source.contains(">>= 1")
            || source.contains("/ 2")
            || source.contains("/= 2"))
            && (source.contains("& 1") || source.contains("% 2") || source.contains("% 2 == 1"))
            && (source.contains("*") && (source.contains("%") || source.contains("MOD")));
        let has_pow_name = source.contains("binpow")
            || source.contains("fastPow")
            || source.contains("quickPow")
            || source.contains("modPow")
            || source.contains("power(");
        if has_fast_pow || has_pow_name {
            detected.push(AllowedAlgorithm::FastExponentiation);
        }

        // 49. Modular Arithmetic
        let has_mod_inv = source.contains("modInverse")
            || source.contains("extgcd")
            || source.contains("MOD - 2")
            || source.contains("mod - 2")
            || source.contains("1000000007")
            || source.contains("998244353");
        let has_mod_ops =
            source.contains("% MOD") || source.contains("% mod") || source.contains("% m");
        if has_mod_inv
            || ((has_mod_ops || source.contains("% 1000000007"))
                && !detected.contains(&AllowedAlgorithm::RollingHash)
                && !detected.contains(&AllowedAlgorithm::FastExponentiation))
        {
            detected.push(AllowedAlgorithm::ModularArithmetic);
        }

        // 50. Prime Factorization
        let has_prime_factors = (source.contains("*")
            && (source.contains("<=") || source.contains("<"))
            && source.contains("%")
            && (source.contains("/=") || source.contains("/ =")))
            || (source.contains("d * d <= n")
                || source.contains("i * i <= n")
                || source.contains("i * i <= num")
                || source.contains("d * d <= num"));
        let has_factors_name = source.contains("primeFactors")
            || source.contains("prime_factors")
            || source.contains("getFactors");
        if has_prime_factors || has_factors_name {
            detected.push(AllowedAlgorithm::PrimeFactorization);
        }

        // 51. Combinatorics
        let has_ncr = source.contains("nCr")
            || source.contains("ncr")
            || source.contains("nPr")
            || source.contains("npr")
            || source.contains("comb(")
            || source.contains("combinations")
            || source.contains("C(n, r)")
            || source.contains("C(n, k)");
        let has_fact_inv = (source.contains("fact[") || source.contains("factorial["))
            && (source.contains("invFact[")
                || source.contains("inv[")
                || source.contains("ifact["));
        let has_pascal = source.contains("pascal")
            || (source.contains("c[i][j]")
                && (source.contains("c[i-1][j-1]") || source.contains("c[i - 1][j - 1]")))
            || (source.contains("[j - 1] +") || source.contains("[j-1] +"));
        if has_ncr || has_fact_inv || has_pascal {
            detected.push(AllowedAlgorithm::Combinatorics);
        }

        // 52. Hash Map
        let has_hash_map = source.contains("unordered_map")
            || source.contains("HashMap")
            || (source.contains("Map<") && !source.contains("TreeMap"))
            || source.contains("map<");
        if has_hash_map {
            detected.push(AllowedAlgorithm::HashMap);
        }

        // 53. Hash Set
        let has_hash_set = source.contains("unordered_set")
            || source.contains("HashSet")
            || (source.contains("Set<") && !source.contains("TreeSet"))
            || source.contains("set<");
        if has_hash_set {
            detected.push(AllowedAlgorithm::HashSet);
        }

        // 54. Frequency Counting
        let has_freq = (source.contains("count[")
            || source.contains("cnt[")
            || source.contains("freq[")
            || source.contains("frequency["))
            && (source.contains("++") || source.contains("+= 1") || source.contains("+=1"))
            || (source.contains(".put(") && source.contains("getOrDefault("));
        if has_freq {
            detected.push(AllowedAlgorithm::FrequencyCounting);
        }

        // 55. Knapsack DP
        let has_knapsack = (source.contains("weights")
            || source.contains("wt[")
            || source.contains("weight")
            || source.contains("cost[")
            || source.contains("val[")
            || source.contains("values"))
            && (source.contains("dp[w]")
                || source.contains("dp[j]")
                || source.contains("dp[i][w]")
                || source.contains("dp[i][j]"))
            && (source.contains("- weight") || source.contains("- wt[") || source.contains("- w["));
        if has_knapsack {
            detected.push(AllowedAlgorithm::KnapsackDp);
        }

        // 56. Interval DP
        let has_interval_dp = (source.contains("[i][j]") || source.contains("[r][c]"))
            && (source.contains("[i][k]")
                || source.contains("[k+1][j]")
                || source.contains("[k + 1][j]")
                || source.contains("[k - 1]"))
            && ((source.contains("[i][k]")
                && (source.contains("[k+1][j]") || source.contains("[k + 1][j]")))
                || source.contains("len =")
                || source.contains("length =")
                || source.contains("len<=")
                || source.contains("length<="));
        if has_interval_dp {
            detected.push(AllowedAlgorithm::IntervalDp);
        }

        // 57. Memoization
        let has_memo = (source.contains("memo[")
            || source.contains("cache[")
            || source.contains("dp[")
            || source.contains("memo."))
            && (source.contains("!= -1")
                || source.contains("!= null")
                || source.contains("!= 0")
                || source.contains("contains("))
            && (source.contains("return memo")
                || source.contains("return cache")
                || source.contains("return dp["));
        if has_memo && !has_interval_dp && !has_knapsack {
            detected.push(AllowedAlgorithm::Memoization);
        }

        // 58. 2D DP
        let has_2d_dp = (source.contains("dp[i][j]")
            || source.contains("dp[r][c]")
            || source.contains("f[i][j]"))
            && (source.contains("dp[i - 1][j]")
                || source.contains("dp[i-1][j]")
                || source.contains("dp[i][j - 1]")
                || source.contains("dp[i][j-1]")
                || source.contains("dp[i - 1][j - 1]")
                || source.contains("dp[i-1][j-1]")
                || source.contains("dp[r - 1][c]")
                || source.contains("dp[r-1][c]")
                || source.contains("dp[r][c - 1]")
                || source.contains("dp[r][c-1]")
                || source.contains("dp[r - 1][c - 1]")
                || source.contains("dp[r-1][c-1]"));
        if has_2d_dp && !has_knapsack && !has_interval_dp {
            detected.push(AllowedAlgorithm::TwoDDp);
        }

        // 59. 1D DP
        let has_1d_dp = (source.contains("dp[i]") || source.contains("f[i]"))
            && (source.contains("dp[i - 1]")
                || source.contains("dp[i-1]")
                || source.contains("dp[i - 2]")
                || source.contains("dp[i-2]")
                || source.contains("f[i - 1]")
                || source.contains("f[i-1]")
                || source.contains("f[i - 2]")
                || source.contains("f[i-2]"))
            && !detected.contains(&AllowedAlgorithm::KadanesAlgorithm)
            && !has_knapsack;
        if has_1d_dp {
            detected.push(AllowedAlgorithm::OneDDp);
        }

        // 60. Dynamic Programming general fallback
        if contains_any(
            source,
            &[
                "dp[",
                "int[] dp",
                "int[][] dp",
                "dp = new",
                "vector<int> dp",
                "vector<vector<int>> dp",
            ],
        ) && !detected.contains(&AllowedAlgorithm::OneDDp)
            && !detected.contains(&AllowedAlgorithm::TwoDDp)
            && !detected.contains(&AllowedAlgorithm::KnapsackDp)
            && !detected.contains(&AllowedAlgorithm::IntervalDp)
            && !detected.contains(&AllowedAlgorithm::BitmaskDp)
            && !detected.contains(&AllowedAlgorithm::TreeDp)
            && !detected.contains(&AllowedAlgorithm::Memoization)
            && !detected.contains(&AllowedAlgorithm::KadanesAlgorithm)
        {
            detected.push(AllowedAlgorithm::DynamicProgramming);
        }

        // 61. Backtracking
        let has_board_undo = contains_any(source, &["board[", "grid["])
            && contains_any(source, &["solve(", "backtrack(", "dfs("])
            && contains_any(source, &[" = '.'", " = ' '", " = 0", " = false"]);
        let has_backtrack = (contains_any(source, &[".push_back(", ".add(", ".append("])
            && contains_any(
                source,
                &[
                    ".pop_back()",
                    ".remove(path.size() - 1)",
                    ".remove(",
                    ".pop()",
                ],
            )
            && contains_any(source, &["backtrack", "dfs", "solve", "helper", "search"]))
            || has_board_undo;
        if has_backtrack && !detected.contains(&AllowedAlgorithm::MonotonicStack) {
            detected.push(AllowedAlgorithm::Backtracking);
        }

        // 62. Divide and Conquer
        let has_divide_conquer = contains_any(
            source,
            &[
                "(left, mid)",
                "(l, mid)",
                "(start, mid)",
                "start, mid",
                "low, mid",
                "(low, mid)",
                "l, mid",
            ],
        ) && contains_any(
            source,
            &[
                "(mid + 1, right)",
                "(mid + 1, r)",
                "(mid + 1, end)",
                "(mid + 1, high)",
                "mid + 1, end",
                "mid + 1, high",
                "mid + 1, right",
                "mid + 1, r",
            ],
        ) && contains_any(
            source,
            &["merge", "combine", "conquer", "solve", "divide", "sort"],
        );
        if has_divide_conquer && !detected.contains(&AllowedAlgorithm::SegmentTree) {
            detected.push(AllowedAlgorithm::DivideAndConquer);
        }

        // 63. Greedy
        let has_greedy = contains_any(source, &["sort", "Sort"])
            && contains_any(source, &["greedy", "ans++", "res++", "count++"])
            && !detected.contains(&AllowedAlgorithm::Intervals)
            && !detected.contains(&AllowedAlgorithm::TwoPointers)
            && !detected.contains(&AllowedAlgorithm::Mst)
            && !detected.contains(&AllowedAlgorithm::CoordinateCompression);
        if has_greedy || contains_any(source, &["greedy", "Greedy"]) {
            detected.push(AllowedAlgorithm::Greedy);
        }

        // 64. Bit Manipulation
        let has_bit_manip = contains_any(
            source,
            &[
                "__builtin_popcount",
                "Integer.bitCount",
                "__builtin_clz",
                "Integer.numberOfLeadingZeros",
                "x & (x - 1)",
                "n & (n - 1)",
            ],
        ) || (source.contains("^=")
            && contains_any(source, &["singleNumber", "unique"]));
        if has_bit_manip
            && !detected.contains(&AllowedAlgorithm::FenwickTree)
            && !detected.contains(&AllowedAlgorithm::BitmaskDp)
        {
            detected.push(AllowedAlgorithm::BitManipulation);
        }

        // 65. Meet in the Middle
        let has_mitm = contains_any(source, &["meet_in_the_middle", "meetInTheMiddle"])
            || (contains_any(source, &["n / 2", "n/2", "len / 2", "len/2"])
                && contains_any(
                    source,
                    &[
                        "first_half",
                        "second_half",
                        "left_half",
                        "right_half",
                        "part1",
                        "part2",
                    ],
                )
                && contains_any(
                    source,
                    &["lower_bound", "binary_search", "HashMap", "unordered_map"],
                ));
        if has_mitm {
            detected.push(AllowedAlgorithm::MeetInTheMiddle);
        }

        // 66. Sweep Line
        let has_sweep_line = contains_any(source, &["events", "Event", "points", "endpoints"])
            && contains_any(source, &["sort", "Sort"])
            && contains_any(source, &["+1", "-1", "START", "END", "type", "delta"]);
        if (has_sweep_line
            || contains_any(source, &["sweepLine", "sweep_line", "SweepLine"]))
            && !detected.contains(&AllowedAlgorithm::Intervals)
        {
            detected.push(AllowedAlgorithm::SweepLine);
        }

        detected
    }
}
