use kiteo_engine::space::SpaceAnalyzer;

#[test]
fn test_fixed_size_value_indexed_array_yields_a() {
    let code = r#"
    void solve(int n, const vector<int>& a) {
        int freq[1000005] = {};
        for (int i = 0; i < n; i++) {
            freq[a[i]]++;
        }
    }
    "#;

    let sc = SpaceAnalyzer::analyze_source(code);
    assert_eq!(sc.to_string(), "O(A)");
}

#[test]
fn test_fixed_size_input_indexed_array_yields_n() {
    let code = r#"
    void solve(int n) {
        vector<int> dp(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i - 1] + 1;
        }
    }
    "#;

    let sc = SpaceAnalyzer::analyze_source(code);
    assert_eq!(sc.to_string(), "O(n)");
}

#[test]
fn test_in_place_algorithm_yields_o1() {
    let code = r#"
    int sum(int n, const int* a) {
        int s = 0;
        for (int i = 0; i < n; i++) s += a[i];
        return s;
    }
    "#;

    let sc = SpaceAnalyzer::analyze_source(code);
    assert_eq!(sc.to_string(), "O(1)");
}

#[test]
fn test_constant_size_local_cpp_and_java() {
    let cpp_dp = r#"
    void solve() {
        vector<int> dp(3);
    }
    "#;
    assert_eq!(SpaceAnalyzer::analyze_source(cpp_dp).to_string(), "O(1)");

    let cpp_arr = r#"
    void solve() {
        int count[26];
    }
    "#;
    assert_eq!(SpaceAnalyzer::analyze_source(cpp_arr).to_string(), "O(1)");

    let java_arr = r#"
    class Solution {
        public void solve() {
            int[] count = new int[26];
        }
    }
    "#;
    assert_eq!(SpaceAnalyzer::analyze_source(java_arr).to_string(), "O(1)");
}

#[test]
fn test_local_sized_by_k_cpp_and_java() {
    let cpp_k = r#"
    void solve(int k) {
        vector<int> arr(k);
    }
    "#;
    assert_eq!(SpaceAnalyzer::analyze_source(cpp_k).to_string(), "O(k)");

    let java_k = r#"
    class Solution {
        public void solve(int k) {
            int[] arr = new int[k];
        }
    }
    "#;
    assert_eq!(SpaceAnalyzer::analyze_source(java_k).to_string(), "O(k)");
}

#[test]
fn test_comments_and_strings_ignored_cpp_and_java() {
    let cpp_code = r#"
    void solve() {
        // vector<int> big(n);
        /* int count[1000005]; */
        string s = "vector<int> dp(n); new int[n];";
        int sum = 0;
    }
    "#;
    assert_eq!(SpaceAnalyzer::analyze_source(cpp_code).to_string(), "O(1)");

    let java_code = r#"
    class Solution {
        public void solve() {
            // int[] big = new int[n];
            /* Map<Integer, Integer> map = new HashMap<>(); */
            String s = "new int[n]; HashMap";
            int sum = 0;
        }
    }
    "#;
    assert_eq!(SpaceAnalyzer::analyze_source(java_code).to_string(), "O(1)");
}

#[test]
fn test_local_containers_growing_with_n_cpp_and_java() {
    let cpp_vector_n = r#"
    void solve(int n) {
        vector<int> big(n);
    }
    "#;
    assert_eq!(
        SpaceAnalyzer::analyze_source(cpp_vector_n).to_string(),
        "O(n)"
    );

    let cpp_map = r#"
    void solve() {
        unordered_map<int, int> mp;
    }
    "#;
    assert_eq!(SpaceAnalyzer::analyze_source(cpp_map).to_string(), "O(n)");

    let java_array_n = r#"
    class Solution {
        public void solve(int n) {
            int[] big = new int[n];
        }
    }
    "#;
    assert_eq!(
        SpaceAnalyzer::analyze_source(java_array_n).to_string(),
        "O(n)"
    );

    let java_hashmap = r#"
    class Solution {
        public void solve() {
            Map<Integer, Integer> map = new HashMap<>();
        }
    }
    "#;
    assert_eq!(
        SpaceAnalyzer::analyze_source(java_hashmap).to_string(),
        "O(n)"
    );
}

#[test]
fn test_unknown_size_allocation_yields_unknown() {
    let cpp_unknown = r#"
    void solve() {
        vector<int> custom(mystery_dim);
    }
    "#;
    assert_eq!(
        SpaceAnalyzer::analyze_source(cpp_unknown).to_string(),
        "Unknown"
    );

    let java_unknown = r#"
    class Solution {
        public void solve() {
            int[] custom = new int[mystery_dim];
        }
    }
    "#;
    assert_eq!(
        SpaceAnalyzer::analyze_source(java_unknown).to_string(),
        "Unknown"
    );
}
