use kiteo_engine::analyze;

// --- EXAMPLES FROM KIT ---

#[test]
fn test_example_two_sum_brute_cpp() {
    let brute_cpp = r#"
    class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            int n = nums.size();
            for (int i = 0; i < n; i++)
                for (int j = i + 1; j < n; j++)
                    if (nums[i] + nums[j] == target) return {i, j};
            return {};
        }
    };
    "#;
    let res = analyze(brute_cpp, "cpp");
    assert_eq!(
        res.tc, "O(n^2)",
        "Brute C++ should have O(n^2) time complexity"
    );
    assert_eq!(
        res.sc, "O(1)",
        "Brute C++ auxiliary space should be O(1) (return value excluded)"
    );
}

#[test]
fn test_example_two_sum_optimal_cpp() {
    let optimal_cpp = r#"
    class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int,int> seen;
            for (int i = 0; i < (int)nums.size(); i++) {
                auto it = seen.find(target - nums[i]);
                if (it != seen.end()) return {it->second, i};
                seen[nums[i]] = i;
            }
            return {};
        }
    };
    "#;
    let res = analyze(optimal_cpp, "cpp");
    assert_eq!(
        res.tc, "O(n)",
        "Optimal C++ should have O(n) time complexity"
    );
    assert_eq!(
        res.sc, "O(n)",
        "Optimal C++ auxiliary space should be O(n) due to unordered_map"
    );
}

#[test]
fn test_example_two_sum_optimal_java() {
    let optimal_java = r#"
    class Solution {
        public int[] twoSum(int[] nums, int target) {
            java.util.HashMap<Integer, Integer> seen = new java.util.HashMap<>();
            for (int i = 0; i < nums.length; i++) {
                Integer j = seen.get(target - nums[i]);
                if (j != null) return new int[]{j, i};
                seen.put(nums[i], i);
            }
            return new int[0];
        }
    }
    "#;
    let res = analyze(optimal_java, "java");
    assert_eq!(
        res.tc, "O(n)",
        "Optimal Java should have O(n) time complexity"
    );
    assert_eq!(
        res.sc, "O(n)",
        "Optimal Java auxiliary space should be O(n) due to HashMap"
    );
}

// --- CUSTOM TEST FIXTURES (CLEARLY MARKED AS TEST FIXTURES, NOT DATASET RECORDS) ---

#[test]
fn test_fixture_string_length_traversal_cpp() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    let code = r#"
    class Solution {
    public:
        int countVowels(string s) {
            int count = 0;
            for (int i = 0; i < (int)s.length(); i++) {
                if (s[i] == 'a') count++;
            }
            return count;
        }
    };
    "#;
    let res = analyze(code, "cpp");
    assert_eq!(res.tc, "O(n)");
    assert_eq!(res.sc, "O(1)");
}

#[test]
fn test_fixture_2d_grid_traversal_cpp() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    let code = r#"
    class Solution {
    public:
        int countZeros(vector<vector<int>>& grid) {
            int m = grid.size();
            int n = grid[0].size();
            int zeros = 0;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (grid[i][j] == 0) zeros++;
                }
            }
            return zeros;
        }
    };
    "#;
    let res = analyze(code, "cpp");
    assert_eq!(res.tc, "O(n m)");
    assert_eq!(res.sc, "O(1)");
}

#[test]
fn test_fixture_listnode_traversal_java() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    let code = r#"
    class Solution {
        public int getLength(ListNode head) {
            int len = 0;
            ListNode curr = head;
            while (curr != null) {
                len++;
                curr = curr.next;
            }
            return len;
        }
    }
    "#;
    let res = analyze(code, "java");
    assert_eq!(res.tc, "O(n)");
    assert_eq!(res.sc, "O(1)");
}

#[test]
fn test_fixture_helper_reachability_cpp() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    let code = r#"
    class Solution {
        int helper(const vector<int>& a) {
            int s = 0;
            for (int i = 0; i < (int)a.size(); i++) s += a[i];
            return s;
        }
    public:
        int solve(vector<int>& nums) {
            return helper(nums);
        }
    };
    "#;
    let res = analyze(code, "cpp");
    assert_eq!(res.tc, "O(n)");
    assert_eq!(res.sc, "O(1)");
}

#[test]
fn test_fixture_scalar_k_bound_java() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    let code = r#"
    class Solution {
        public int repeatSum(int k) {
            int total = 0;
            for (int i = 0; i < k; i++) {
                total += i;
            }
            return total;
        }
    }
    "#;
    let res = analyze(code, "java");
    assert_eq!(res.tc, "O(k)");
    assert_eq!(res.sc, "O(1)");
}

#[test]
fn test_fixture_halving_while_loop_cpp() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    let code = r#"
    class Solution {
    public:
        int reduceToZero(int n) {
            int steps = 0;
            while (n > 0) {
                n /= 2;
                steps++;
            }
            return steps;
        }
    };
    "#;
    let res = analyze(code, "cpp");
    assert_eq!(res.tc, "O(log n)");
    assert_eq!(res.sc, "O(1)");
}

#[test]
fn test_fixture_auxiliary_hashset_java() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    let code = r#"
    class Solution {
        public boolean hasDuplicates(int[] nums) {
            java.util.HashSet<Integer> set = new java.util.HashSet<>();
            for (int i = 0; i < nums.length; i++) {
                if (set.contains(nums[i])) return true;
                set.add(nums[i]);
            }
            return false;
        }
    }
    "#;
    let res = analyze(code, "java");
    assert_eq!(res.tc, "O(n)");
    assert_eq!(res.sc, "O(n)");
}

#[test]
fn test_fixture_auxiliary_vector_cpp() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    let code = r#"
    class Solution {
    public:
        int sumSquared(vector<int>& nums) {
            int n = nums.size();
            vector<int> squares(n);
            for (int i = 0; i < n; i++) {
                squares[i] = nums[i] * nums[i];
            }
            int sum = 0;
            for (int i = 0; i < n; i++) sum += squares[i];
            return sum;
        }
    };
    "#;
    let res = analyze(code, "cpp");
    assert_eq!(res.tc, "O(n)");
    assert_eq!(res.sc, "O(n)");
}

// --- NEGATIVE LOOK-ALIKES (TEST FIXTURES, NOT DATASET RECORDS) ---

#[test]
fn test_fixture_negative_lookalike_constant_bounds_cpp() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    // Nested loops with constant literal bounds must evaluate to O(1), not O(n^2)
    let code = r#"
    class Solution {
    public:
        int fixedBoardTraversal() {
            int sum = 0;
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    sum += (i ^ j);
                }
            }
            return sum;
        }
    };
    "#;
    let res = analyze(code, "cpp");
    assert_eq!(res.tc, "O(1)");
    assert_eq!(res.sc, "O(1)");
}

#[test]
fn test_fixture_negative_lookalike_unreachable_helper_java() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    // Private helper has nested O(n^2) loop, but is NOT called by public entry method
    let code = r#"
    class Solution {
        private int unusedHeavyHelper(int[] nums) {
            int cnt = 0;
            for (int i = 0; i < nums.length; i++) {
                for (int j = 0; j < nums.length; j++) {
                    cnt++;
                }
            }
            return cnt;
        }
        public int solve(int[] nums) {
            int sum = 0;
            for (int i = 0; i < nums.length; i++) {
                sum += nums[i];
            }
            return sum;
        }
    }
    "#;
    let res = analyze(code, "java");
    assert_eq!(
        res.tc, "O(n)",
        "Must ignore unreachable helper method complexity"
    );
    assert_eq!(res.sc, "O(1)");
}

#[test]
fn test_fixture_negative_lookalike_no_public_entry_cpp() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    // Solution class with only private methods and no public entry point
    let code = r#"
    class Solution {
    private:
        void hiddenMethod(int n) {
            for (int i = 0; i < n; i++) {}
        }
    };
    "#;
    let res = analyze(code, "cpp");
    assert_eq!(
        res.tc, "Unknown",
        "Must return Unknown when entry point cannot be determined"
    );
    assert_eq!(
        res.sc, "Unknown",
        "Must return Unknown when entry point cannot be determined"
    );
}

#[test]
fn test_fixture_negative_lookalike_unknown_while_condition_cpp() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    // While loop with unresolvable/unmodeled termination condition
    let code = r#"
    extern bool hasWork();
    class Solution {
    public:
        void processStream() {
            while (hasWork()) {
                int dummy = 1;
            }
        }
    };
    "#;
    let res = analyze(code, "cpp");
    assert_eq!(
        res.tc, "Unknown",
        "Must return Unknown when condition cannot be bound"
    );
}

#[test]
fn test_fixture_negative_lookalike_empty_solution_cpp() {
    // [TEST FIXTURE - NOT A DATASET RECORD]
    // Solution class with no methods at all
    let code = r#"
    class Solution {
    };
    "#;
    let res = analyze(code, "cpp");
    assert_eq!(res.tc, "Unknown");
    assert_eq!(res.sc, "Unknown");
}

#[test]
fn test_increasing_triplet_enhanced_for_java() {
    let code = r#"
    class Solution {
        public boolean increasingTriplet(int[] nums) {
            int s = Integer.MAX_VALUE;
            int m = Integer.MAX_VALUE;

            for(int i : nums){
                if(i <= s) s = i;
                else if(i <= m) m = i;
                else return true;
            }
            return false;
        }
    }
    "#;
    let res = analyze(code, "java");
    assert_eq!(res.tc, "O(n)");
    assert_eq!(res.sc, "O(1)");
}

#[test]
fn test_increasing_triplet_range_for_cpp() {
    let code = r#"
    class Solution {
    public:
        bool increasingTriplet(vector<int>& nums) {
            int s = 2147483647, m = 2147483647;
            for (int x : nums) {
                if (x <= s) s = x;
                else if (x <= m) m = x;
                else return true;
            }
            return false;
        }
    };
    "#;
    let res = analyze(code, "cpp");
    assert_eq!(res.tc, "O(n)");
    assert_eq!(res.sc, "O(1)");
}

#[test]
fn test_do_while_java_and_cpp() {
    let java_code = r#"
    class Solution {
        public int solve(int n) {
            int i = 0, count = 0;
            do {
                count++;
                i++;
            } while (i < n);
            return count;
        }
    }
    "#;
    let res_j = analyze(java_code, "java");
    assert_eq!(res_j.tc, "O(n)");
    assert_eq!(res_j.sc, "O(1)");

    let cpp_code = r#"
    class Solution {
    public:
        int solve(int n) {
            int i = 0, count = 0;
            do {
                count++;
                i++;
            } while (i < n);
            return count;
        }
    };
    "#;
    let res_c = analyze(cpp_code, "cpp");
    assert_eq!(res_c.tc, "O(n)");
    assert_eq!(res_c.sc, "O(1)");
}

#[test]
fn test_enhanced_for_to_char_array_java() {
    let code = r#"
    class Solution {
        public int countVowels(String s) {
            int cnt = 0;
            for (char c : s.toCharArray()) {
                if (c == 'a' || c == 'e') cnt++;
            }
            return cnt;
        }
    }
    "#;
    let res = analyze(code, "java");
    assert_eq!(res.tc, "O(n)");
}

#[test]
fn test_while_k_decrement_bound() {
    let code = r#"
    class Solution {
        public int reduce(int k) {
            int count = 0;
            while (k > 0) {
                count++;
                k--;
            }
            return count;
        }
    }
    "#;
    let res = analyze(code, "java");
    assert_eq!(res.tc, "O(k)");
}

#[test]
fn test_2d_grid_enhanced_for_java() {
    let code = r#"
    class Solution {
        public int sumMatrix(int[][] grid) {
            int sum = 0;
            for (int[] row : grid) {
                for (int val : row) {
                    sum += val;
                }
            }
            return sum;
        }
    }
    "#;
    let res = analyze(code, "java");
    assert_eq!(res.tc, "O(n m)");
}

#[test]
fn test_amount_target_dp_space() {
    let code = r#"
    class Solution {
        public int coinChange(int[] coins, int amount) {
            int[] dp = new int[amount + 1];
            return dp[amount];
        }
    }
    "#;
    let res = analyze(code, "java");
    assert_eq!(res.sc, "O(A)");
}

#[test]
fn test_comma_expr_two_pointer_cpp() {
    let code = r#"
    class Solution {
    public:
        void reverseString(vector<char>& s) {
            int n = s.size();
            for (int i = 0, j = n - 1; i < j; i++, j--) {
                swap(s[i], s[j]);
            }
        }
    };
    "#;
    let res = analyze(code, "cpp");
    assert_eq!(res.tc, "O(n)");
    assert_eq!(res.sc, "O(1)");
}

