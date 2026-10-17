use kiteo_engine::algorithms::{AlgorithmDetector, AllowedAlgorithm};

// ============================================================================
// BATCH 1: ARRAYS, SEARCHING, TWO POINTERS & HASHING (5-7 VARIATIONS EACH)
// ============================================================================

// 1. TWO POINTERS (7 variations)
#[test]
fn test_two_pointers_variations() {
    // Var 1: Canonical C++ inward l/r
    let v1 = r#"
    int l = 0, r = n - 1;
    while (l < r) {
        if (a[l] + a[r] == target) return true;
        else if (a[l] + a[r] < target) l++;
        else r--;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::TwoPointers));

    // Var 2: Arbitrary friend variable names (rahul & rohit)
    let v2 = r#"
    int rahul = 0, rohit = len - 1;
    while (rahul <= rohit) {
        if (arr[rahul] + arr[rohit] == k) return true;
        rahul++; rohit--;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::TwoPointers));

    // Var 3: Java while loop with start/end
    let v3 = r#"
    int start = 0, end = nums.length - 1;
    while (start < end) {
        int sum = nums[start] + nums[end];
        if (sum == target) return new int[]{start, end};
        if (sum < target) start++;
        else end--;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::TwoPointers));

    // Var 4: low/high pointers with inverted conditions
    let v4 = r#"
    int low = 0, high = n - 1;
    while (low < high) {
        if (arr[low] + arr[high] > target) high--;
        else low++;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::TwoPointers));

    // Var 5: Palindrome verification with i and j
    let v5 = r#"
    int i = 0, j = s.length() - 1;
    while (i < j) {
        if (s.charAt(i) != s.charAt(j)) return false;
        i++; j--;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::TwoPointers));

    // Var 6: Pre-increment ++head and --tail
    let v6 = r#"
    int head = 0, tail = n - 1;
    while (head < tail) {
        if (a[head] == a[tail]) { ++head; --tail; }
        else ++head;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v6).contains(&AllowedAlgorithm::TwoPointers));

    // Var 7 (Negative): Nested loops without convergence
    let neg = r#"
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] + a[j] == target) return true;
        }
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::TwoPointers));
}

// 2. FAST AND SLOW POINTERS (6 variations)
#[test]
fn test_fast_and_slow_pointers_variations() {
    // Var 1: Canonical cycle detection in linked list
    let v1 = r#"
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::FastAndSlowPointers));

    // Var 2: C++ pointer arrow syntax
    let v2 = r#"
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::FastAndSlowPointers));

    // Var 3: Finding middle of linked list
    let v3 = r#"
    ListNode* s = head;
    ListNode* f = head;
    while (f && f->next) {
        s = s->next;
        f = f->next->next;
    }
    return s;
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::FastAndSlowPointers));

    // Var 4: Friend variable names (turtle & hare)
    let v4 = r#"
    Node turtle = head, hare = head;
    while (hare != null && hare.next != null) {
        turtle = turtle.next;
        hare = hare.next.next;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::FastAndSlowPointers));

    // Var 5: Helper method encapsulation
    let v5 = r#"
    boolean hasCycle(ListNode node) {
        ListNode p1 = node, p2 = node;
        while (p2 != null && p2.next != null) {
            p1 = p1.next;
            p2 = p2.next.next;
        }
        return false;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::FastAndSlowPointers));

    // Var 6 (Negative): Standard single-pointer list traversal
    let neg = r#"
    ListNode curr = head;
    while (curr != null) {
        curr = curr.next;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::FastAndSlowPointers));
}

// 3. SLIDING WINDOW (6 variations)
#[test]
fn test_sliding_window_variations() {
    // Var 1: Classic expand right, shrink left
    let v1 = r#"
    int l = 0;
    for (int r = 0; r < n; r++) {
        sum += a[r];
        while (sum > k) {
            sum -= a[l];
            l++;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::SlidingWindow));

    // Var 2: Full word identifiers (left / right)
    let v2 = r#"
    int left = 0;
    for (int right = 0; right < n; right++) {
        sum += nums[right];
        while (sum >= target) {
            left++;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::SlidingWindow));

    // Var 3: Character count window shrink
    let v3 = r#"
    int start = 0;
    for (int end = 0; end < s.length(); end++) {
        freq[s.charAt(end)]++;
        while (freq[s.charAt(end)] > 1) {
            freq[s.charAt(start)]--;
            start++;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::SlidingWindow));

    // Var 4: Java Solution class style
    let v4 = r#"
    class Solution {
        public int minSubArrayLen(int target, int[] nums) {
            int left = 0, cur = 0;
            for (int r = 0; r < nums.length; r++) {
                cur += nums[r];
                while (cur >= target) {
                    left++;
                }
            }
            return 0;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::SlidingWindow));

    // Var 5: While loop with j outer pointer
    let v5 = r#"
    int l = 0;
    for (int j = 0; j < n; j++) {
        while (window_invalid()) {
            l++;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::SlidingWindow));

    // Var 6 (Negative): Pure non-window nested for loops
    let neg = r#"
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            sum += matrix[i][j];
        }
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::SlidingWindow));
}

// 4. PREFIX SUM (6 variations)
#[test]
fn test_prefix_sum_variations() {
    // Var 1: 0-indexed pref[i - 1]
    let v1 = r#"
    vector<int> pref(n);
    pref[0] = a[0];
    for (int i = 1; i < n; i++) {
        pref[i] = pref[i - 1] + a[i];
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::PrefixSum));

    // Var 2: 1-indexed pref[i + 1] = pref[i] + nums[i]
    let v2 = r#"
    int[] pref = new int[n + 1];
    for (int i = 0; i < n; i++) {
        pref[i + 1] = pref[i] + nums[i];
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::PrefixSum));

    // Var 3: prefixSum naming with spacing
    let v3 = r#"
    for (int i = 1; i < n; i++) {
        prefixSum[i] = prefixSum[i-1] + val[i];
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::PrefixSum));

    // Var 4: Array query range difference pref[r+1] - pref[l]
    let v4 = r#"
    int query(int l, int r) {
        return pref[r + 1] - pref[l];
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::PrefixSum));

    // Var 5: In-place cumulative prefix sum
    let v5 = r#"
    for (int i = 1; i < n; i++) {
        pre[i] = pre[i - 1] + arr[i];
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::PrefixSum));

    // Var 6 (Negative): Running total scalar accumulator
    let neg = r#"
    int total = 0;
    for (int x : nums) {
        total += x;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::PrefixSum));
}

// 5. DIFFERENCE ARRAY (6 variations)
#[test]
fn test_difference_array_variations() {
    // Var 1: diff[l] += x; diff[r + 1] -= x;
    let v1 = r#"
    vector<int> diff(n + 2, 0);
    for (auto& q : queries) {
        diff[q.l] += q.x;
        diff[q.r + 1] -= q.x;
    }
    for (int i = 1; i <= n; i++) diff[i] += diff[i - 1];
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::DifferenceArray));

    // Var 2: d[a]++ and d[b+1]--
    let v2 = r#"
    int[] d = new int[n + 2];
    for (int[] range : intervals) {
        d[range[0]]++;
        d[range[1] + 1]--;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::DifferenceArray));

    // Var 3: Delta array variable naming
    let v3 = r#"
    vector<int> delta(n + 1, 0);
    delta[start] += val;
    delta[end + 1] -= val;
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::DifferenceArray));

    // Var 4: Java solution class style
    let v4 = r#"
    class Solution {
        public int[] corpFlightBookings(int[][] bookings, int n) {
            int[] diff = new int[n + 2];
            for (int[] b : bookings) {
                diff[b[0]] += b[2];
                diff[b[1] + 1] -= b[2];
            }
            return diff;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::DifferenceArray));

    // Var 5: 0-indexed spacing format [r+1]
    let v5 = r#"
    diff[l] += val;
    diff[r+1] -= val;
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::DifferenceArray));

    // Var 6 (Negative): Independent array increments without decrement
    let neg = r#"
    for (int i = 0; i < n; i++) {
        count[a[i]]++;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::DifferenceArray));
}

// 6. BINARY SEARCH (7 variations)
#[test]
fn test_binary_search_variations() {
    // Var 1: Canonical left/right interval halving
    let v1 = r#"
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (a[mid] == target) return mid;
        else if (a[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::BinarySearch));

    // Var 2: Arbitrary friend variable names (amit, sumit, vikram)
    let v2 = r#"
    int amit = 0, sumit = n - 1;
    while (amit <= sumit) {
        int vikram = (amit + sumit) / 2;
        if (arr[vikram] < val) amit = vikram + 1;
        else sumit = vikram - 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::BinarySearch));

    // Var 3: Bitwise right shift midpoint
    let v3 = r#"
    int l = 0, r = n - 1;
    while (l <= r) {
        int mid = (l + r) >> 1;
        if (nums[mid] == target) return mid;
        if (nums[mid] < target) l = mid + 1;
        else r = mid - 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::BinarySearch));

    // Var 4: Java Solution class
    let v4 = r#"
    class Solution {
        public int search(int[] nums, int target) {
            int low = 0, high = nums.length - 1;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (nums[mid] == target) return mid;
                else if (nums[mid] < target) low = mid + 1;
                else high = mid - 1;
            }
            return -1;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::BinarySearch));

    // Var 5: Lower bound / upper bound style
    let v5 = r#"
    int start = 0, end = n - 1;
    while (start <= end) {
        int mid = start + (end - start) / 2;
        if (a[mid] >= target) end = mid - 1;
        else start = mid + 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::BinarySearch));

    // Var 6: Single-letter variables (l, r, m)
    let v6 = r#"
    int l = 0, r = n - 1;
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (a[m] < target) l = m + 1;
        else r = m - 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v6).contains(&AllowedAlgorithm::BinarySearch));

    // Var 7 (Negative): Loop halving bounds without midpoint index
    let neg = r#"
    int n = 100;
    while (n > 0) {
        n /= 2;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::BinarySearch));
}

// 7. KADANE'S ALGORITHM (7 variations)
#[test]
fn test_kadanes_algorithm_variations() {
    // Var 1: Canonical max(nums[i], cur_max + nums[i])
    let v1 = r#"
    int maxSubArray(vector<int>& nums) {
        int max_so_far = nums[0], cur_max = nums[0];
        for (size_t i = 1; i < nums.size(); ++i) {
            cur_max = max(nums[i], cur_max + nums[i]);
            max_so_far = max(max_so_far, cur_max);
        }
        return max_so_far;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::KadanesAlgorithm));

    // Var 2: User's branch reset style (if sum < 0 sum = 0)
    let v2 = r#"
    int max = Integer.MIN_VALUE, sum = 0;
    for (int i = 0; i < n.length; ++i) {
        sum += n[i];
        if (sum > max) max = sum;
        if (sum < 0) sum = 0;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::KadanesAlgorithm));

    // Var 3: Arbitrary friend variable names (alice, bob, charlie)
    let v3 = r#"
    int alice = -99999, bob = 0;
    for (int i = 0; i < charlie.length; i++) {
        bob += charlie[i];
        if (bob > alice) alice = bob;
        if (bob < 0) bob = 0;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::KadanesAlgorithm));

    // Var 4: Java Math.max(0, sum) style
    let v4 = r#"
    int maxSoFar = nums[0], cur = 0;
    for (int x : nums) {
        cur += x;
        maxSoFar = Math.max(maxSoFar, cur);
        cur = Math.max(0, cur);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::KadanesAlgorithm));

    // Var 5: DP array formulation dp[i] = max(a[i], dp[i-1] + a[i])
    let v5 = r#"
    vector<int> dp(n);
    dp[0] = a[0];
    int ans = dp[0];
    for (int i = 1; i < n; i++) {
        dp[i] = max(a[i], dp[i - 1] + a[i]);
        ans = max(ans, dp[i]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::KadanesAlgorithm));

    // Var 6: C++ max ending here naming
    let v6 = r#"
    int max_so_far = INT_MIN, max_ending_here = 0;
    for (int i = 0; i < n; i++) {
        max_ending_here += a[i];
        if (max_so_far < max_ending_here) max_so_far = max_ending_here;
        if (max_ending_here < 0) max_ending_here = 0;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v6).contains(&AllowedAlgorithm::KadanesAlgorithm));

    // Var 7 (Negative): Pure array maximum search
    let neg = r#"
    int max_val = a[0];
    for (int i = 1; i < n; i++) {
        max_val = max(max_val, a[i]);
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::KadanesAlgorithm));
}

// 8. COORDINATE COMPRESSION (5 variations)
#[test]
fn test_coordinate_compression_variations() {
    // Var 1: std::unique + lower_bound
    let v1 = r#"
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    int id = lower_bound(vals.begin(), vals.end(), x) - vals.begin();
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::CoordinateCompression));

    // Var 2: Fully qualified std::unique
    let v2 = r#"
    std::sort(coords.begin(), coords.end());
    coords.erase(std::unique(coords.begin(), coords.end()), coords.end());
    int rank = lower_bound(coords.begin(), coords.end(), val) - coords.begin();
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::CoordinateCompression));

    // Var 3: Arrays compression in function
    let v3 = r#"
    void compress(vector<int>& a) {
        vector<int> b = a;
        sort(b.begin(), b.end());
        b.resize(unique(b.begin(), b.end()) - b.begin());
        for (int& x : a) x = lower_bound(b.begin(), b.end(), x) - b.begin();
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::CoordinateCompression));

    // Var 4: With binary_search query
    let v4 = r#"
    unique(all.begin(), all.end());
    bool ok = binary_search(all.begin(), all.end(), target);
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::CoordinateCompression));

    // Var 5 (Negative): Standard sorting without uniqueness ranking
    let neg = r#"
    sort(a.begin(), a.end());
    return a[0];
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::CoordinateCompression));
}

// 9. INTERVALS (5 variations)
#[test]
fn test_intervals_variations() {
    // Var 1: LeetCode 56 Merge Intervals
    let v1 = r#"
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> merged;
    for (auto& interval : intervals) {
        if (merged.empty() || merged.back()[1] < interval[0]) merged.push_back(interval);
        else merged.back()[1] = max(merged.back()[1], interval[1]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Intervals));

    // Var 2: Java Interval Object with start and end
    let v2 = r#"
    Collections.sort(intervals, (a, b) -> a.start - b.start);
    int end = intervals.get(0).end;
    for (Interval i : intervals) {
        end = Math.max(end, i.end);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Intervals));

    // Var 3: Non-overlapping intervals count
    let v3 = r#"
    Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
    int end = intervals[0][1];
    for (int[] interval : intervals) {
        end = Math.max(end, interval[1]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Intervals));

    // Var 4: Custom structure Interval
    let v4 = r#"
    struct Interval { int start, end; };
    sort(intervals.begin(), intervals.end(), cmp);
    int max_end = max(intervals[0].end, next.end);
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Intervals));

    // Var 5 (Negative): Standard 2D array sort without interval overlap logic
    let neg = r#"
    sort(points.begin(), points.end());
    int total = points[0][0] + points[0][1];
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Intervals));
}

// 10. MATRIX / GRID (5 variations)
#[test]
fn test_matrix_grid_variations() {
    // Var 1: Direction arrays dr/dc with bounds check
    let v1 = r#"
    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};
    for (int d = 0; d < 4; d++) {
        int nr = r + dr[d], nc = c + dc[d];
        if (nr >= 0 && nr < R && nc >= 0 && nc < C) {
            grid[nr][nc] = 1;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::MatrixGrid));

    // Var 2: dx/dy direction vectors
    let v2 = r#"
    int dx[] = {0, 0, 1, -1};
    int dy[] = {1, -1, 0, 0};
    int m = matrix.length, n = matrix[0].length;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            matrix[i][j] = 0;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::MatrixGrid));

    // Var 3: Board matrix search
    let v3 = r#"
    int rows = board.length;
    for (int r = 0; r < rows; r++) {
        board[r][0] = 'X';
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::MatrixGrid));

    // Var 4: 2D Grid dimension check
    let v4 = r#"
    int R = grid.size();
    for (int r = 0; r < R; r++) {
        grid[r][0] = 42;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::MatrixGrid));

    // Var 5 (Negative): 1D array traversal
    let neg = r#"
    for (int i = 0; i < n; i++) {
        a[i] = 0;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::MatrixGrid));
}

// ============================================================================
// BATCH 2: STACK, QUEUE, HEAP & LINKED LISTS (5-7 VARIATIONS EACH)
// ============================================================================

// 11. MONOTONIC STACK (6 variations)
#[test]
fn test_monotonic_stack_variations() {
    // Var 1: Canonical next greater element C++
    let v1 = r#"
    stack<int> st;
    for (int i = 0; i < n; i++) {
        while (!st.empty() && a[st.top()] < a[i]) st.pop();
        st.push(i);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::MonotonicStack));

    // Var 2: Java Stack with peek() and pop()
    let v2 = r#"
    Stack<Integer> stk = new Stack<>();
    for (int x : nums) {
        while (!stk.isEmpty() && stk.peek() > x) {
            stk.pop();
        }
        stk.push(x);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::MonotonicStack));

    // Var 3: Friend variable names (mono, s)
    let v3 = r#"
    stack<int> s;
    for (int i = 0; i < n; i++) {
        while (!s.empty() && arr[s.top()] <= arr[i]) s.pop();
        s.push(i);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::MonotonicStack));

    // Var 4: Java ArrayDeque as stack
    let v4 = r#"
    ArrayDeque<Integer> stack = new ArrayDeque<>();
    for (int i = 0; i < n; i++) {
        while (stack.size() > 0 && nums[stack.peek()] < nums[i]) {
            stack.pop();
        }
        stack.push(i);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::MonotonicStack));

    // Var 5: Deque monotonic stack C++
    let v5 = r#"
    deque<int> st;
    for (int i = 0; i < n; i++) {
        while (st.size() && a[st.back()] < a[i]) st.pop_back();
        st.push_back(i);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::MonotonicStack));

    // Var 6 (Negative): Plain stack parenthesis matching
    let neg = r#"
    stack<char> st;
    for (char c : s) {
        if (c == '(') st.push(c);
        else if (!st.empty()) st.pop();
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::MonotonicStack));
}

// 12. HEAP / PRIORITY QUEUE (5 variations)
#[test]
fn test_heap_priority_queue_variations() {
    // Var 1: C++ default max-heap
    let v1 = r#"
    priority_queue<int> pq;
    for (int x : nums) pq.push(x);
    int largest = pq.top();
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::HeapPriorityQueue));

    // Var 2: C++ min-heap with greater<>
    let v2 = r#"
    priority_queue<int, vector<int>, greater<int>> min_pq;
    min_pq.push(42);
    int top = min_pq.top();
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::HeapPriorityQueue));

    // Var 3: Java PriorityQueue
    let v3 = r#"
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    for (int val : a) pq.add(val);
    int head = pq.poll();
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::HeapPriorityQueue));

    // Var 4: Java custom comparator PriorityQueue
    let v4 = r#"
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    pq.offer(new int[]{1, 2});
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::HeapPriorityQueue));

    // Var 5 (Negative): Standard Vector without heap
    let neg = r#"
    vector<int> list;
    list.push_back(10);
    int front = list.front();
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::HeapPriorityQueue));
}

// 13. TOP K (5 variations)
#[test]
fn test_top_k_variations() {
    // Var 1: Top K largest elements with min-heap size > k
    let v1 = r#"
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int x : nums) {
        pq.push(x);
        if (pq.size() > k) pq.pop();
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::TopK));

    // Var 2: Java Top K with PriorityQueue size > k
    let v2 = r#"
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    for (int num : nums) {
        pq.add(num);
        if (pq.size() > k) pq.poll();
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::TopK));

    // Var 3: Capitalized K parameter
    let v3 = r#"
    priority_queue<int> pq;
    for (int x : a) {
        pq.push(x);
        if (pq.size() > K) pq.pop();
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::TopK));

    // Var 4: Fixed size == k check
    let v4 = r#"
    priority_queue<pair<int, int>> pq;
    for (auto& p : items) {
        pq.push(p);
        if (pq.size() >= k) pq.pop();
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::TopK));

    // Var 5 (Negative): Heap without size limit
    let neg = r#"
    priority_queue<int> pq;
    for (int x : nums) pq.push(x);
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::TopK));
}

// 14. TWO HEAPS (5 variations)
#[test]
fn test_two_heaps_variations() {
    // Var 1: Running median with maxHeap and minHeap
    let v1 = r#"
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    void addNum(int num) {
        if (maxHeap.empty() || num < maxHeap.top()) maxHeap.push(num);
        else minHeap.push(num);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::TwoHeaps));

    // Var 2: Snake case naming max_heap and min_heap
    let v2 = r#"
    priority_queue<int> max_heap;
    priority_queue<int, vector<int>, greater<int>> min_heap;
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::TwoHeaps));

    // Var 3: Java MedianFinder
    let v3 = r#"
    class MedianFinder {
        PriorityQueue<Integer> maxHeap;
        PriorityQueue<Integer> minHeap;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::TwoHeaps));

    // Var 4: Java snake case fields
    let v4 = r#"
    PriorityQueue<Integer> max_heap = new PriorityQueue<>(Collections.reverseOrder());
    PriorityQueue<Integer> min_heap = new PriorityQueue<>();
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::TwoHeaps));

    // Var 5 (Negative): Single priority queue
    let neg = r#"
    PriorityQueue<Integer> min_heap = new PriorityQueue<>();
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::TwoHeaps));
}

// 15. LINKED LIST REVERSAL (5 variations)
#[test]
fn test_linked_list_reversal_variations() {
    // Var 1: Canonical iterative reverse C++
    let v1 = r#"
    ListNode* prev = nullptr;
    ListNode* curr = head;
    while (curr) {
        ListNode* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::LinkedListReversal));

    // Var 2: Java Solution style
    let v2 = r#"
    ListNode prev = null;
    ListNode curr = head;
    while (curr != null) {
        ListNode nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::LinkedListReversal));

    // Var 3: C++ NULL pointer
    let v3 = r#"
    Node* prev = NULL;
    while (head) {
        Node* nxt = head->next;
        head->next = prev;
        prev = head;
        head = nxt;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::LinkedListReversal));

    // Var 4: Reverse linked list helper function
    let v4 = r#"
    ListNode reverse(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::LinkedListReversal));

    // Var 5 (Negative): Straight forward traversal without reversal
    let neg = r#"
    ListNode curr = head;
    while (curr != null) {
        curr = curr.next;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::LinkedListReversal));
}

// 16. MERGE LINKED LISTS (5 variations)
#[test]
fn test_merge_linked_lists_variations() {
    // Var 1: mergeTwoLists function name
    let v1 = r#"
    ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        return dummy.next;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::MergeLinkedLists));

    // Var 2: mergeKLists function name
    let v2 = r#"
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        return nullptr;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::MergeLinkedLists));

    // Var 3: Pointer value comparison l1.val < l2.val
    let v3 = r#"
    while (l1 != null && l2 != null) {
        if (l1.val < l2.val) {
            curr.next = l1;
            l1 = l1.next;
        } else {
            curr.next = l2;
            l2 = l2.next;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::MergeLinkedLists));

    // Var 4: C++ arrow syntax value comparison
    let v4 = r#"
    if (list1->val < list2->val) {
        tail->next = list1;
        list1 = list1->next;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::MergeLinkedLists));

    // Var 5 (Negative): Single list sum
    let neg = r#"
    int sum = 0;
    while (head != null) {
        sum += head.val;
        head = head.next;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::MergeLinkedLists));
}

// ============================================================================
// BATCH 2 CONTINUED: STACK, QUEUE, LINKED LIST & CYCLE DETECTION
// ============================================================================

// 17. STACK (6 variations)
#[test]
fn test_stack_variations() {
    // Var 1: C++ STL stack with friend var name
    let v1 = r#"
    stack<int> rohit;
    rohit.push(10);
    rohit.push(20);
    int top_val = rohit.top();
    rohit.pop();
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Stack));

    // Var 2: Java Stack with push/pop
    let v2 = r#"
    Stack<Integer> amit = new Stack<>();
    amit.push(42);
    if (!amit.isEmpty()) {
        int x = amit.pop();
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Stack));

    // Var 3: Java Deque as stack
    let v3 = r#"
    Deque<Character> priya = new ArrayDeque<>();
    priya.push('a');
    char c = priya.pop();
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Stack));

    // Var 4: C++ vector simulating stack with push_back and pop_back
    let v4 = r#"
    vector<int> charlie;
    charlie.push_back(100);
    int last = charlie.back();
    charlie.pop_back();
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Stack));

    // Var 5: Pointer stack helper
    let v5 = r#"
    Stack<String> history = new Stack<>();
    history.push("home");
    String prev = history.peek();
    history.pop();
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Stack));

    // Var 6 (Negative): Plain vector without stack pop operations
    let neg = r#"
    vector<int> nums = {1, 2, 3};
    for (int x : nums) {
        sum += x;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Stack));
}

// 18. QUEUE (6 variations)
#[test]
fn test_queue_variations() {
    // Var 1: C++ queue push/pop
    let v1 = r#"
    queue<int> vikram;
    vikram.push(1);
    vikram.push(2);
    int front = vikram.front();
    vikram.pop();
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Queue));

    // Var 2: Java Queue LinkedList offer/poll
    let v2 = r#"
    Queue<Integer> ananya = new LinkedList<>();
    ananya.offer(5);
    int val = ananya.poll();
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Queue));

    // Var 3: Java ArrayDeque as queue
    let v3 = r#"
    Queue<String> tasks = new ArrayDeque<>();
    tasks.add("job1");
    String job = tasks.remove();
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Queue));

    // Var 4: C++ queue with pair
    let v4 = r#"
    queue<pair<int, int>> q;
    q.push({r, c});
    auto p = q.front();
    q.pop();
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Queue));

    // Var 5: Java Queue with peek and poll
    let v5 = r#"
    Queue<TreeNode> line = new LinkedList<>();
    line.offer(root);
    if (!line.isEmpty()) {
        TreeNode curr = line.poll();
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Queue));

    // Var 6 (Negative): Stack operations
    let neg = r#"
    stack<int> s;
    s.push(1);
    s.pop();
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Queue));
}

// 19. LINKED LIST (6 variations)
#[test]
fn test_linked_list_variations() {
    // Var 1: C++ ListNode pointer traversal
    let v1 = r#"
    ListNode* curr = head;
    while (curr != nullptr) {
        cout << curr->val << endl;
        curr = curr->next;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::LinkedList));

    // Var 2: Java ListNode traversal with friend var
    let v2 = r#"
    ListNode rohit = head;
    int count = 0;
    while (rohit != null) {
        count++;
        rohit = rohit.next;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::LinkedList));

    // Var 3: Custom Node class structure
    let v3 = r#"
    class Node {
        int data;
        Node next;
        Node(int d) { data = d; next = null; }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::LinkedList));

    // Var 4: C++ struct Node traversal
    let v4 = r#"
    Node* temp = head;
    while (temp) {
        val_sum += temp->val;
        temp = temp->next;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::LinkedList));

    // Var 5: Insertion at head
    let v5 = r#"
    ListNode newNode = new ListNode(val);
    newNode.next = head;
    head = newNode;
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::LinkedList));

    // Var 6 (Negative): Plain array iteration
    let neg = r#"
    for (int i = 0; i < n; i++) {
        total += arr[i];
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::LinkedList));
}

// 20. CYCLE DETECTION (6 variations)
#[test]
fn test_cycle_detection_variations() {
    // Var 1: hasCycle method name
    let v1 = r#"
    public boolean hasCycle(ListNode head) {
        ListNode s = head, f = head;
        while (f != null && f.next != null) {
            s = s.next;
            f = f.next.next;
            if (s == f) return true;
        }
        return false;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::CycleDetection));

    // Var 2: detectCycle in linked list
    let v2 = r#"
    ListNode *detectCycle(ListNode *head) {
        return nullptr;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::CycleDetection));

    // Var 3: Tortoise and hare with custom names
    let v3 = r#"
    while (tortoise != hare) {
        tortoise = tortoise.next;
        hare = hare.next.next;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::CycleDetection));

    // Var 4: Directed graph cycle check with 3-color states
    let v4 = r#"
    bool isCycle(int u) {
        vis[u] = 1;
        for (int v : adj[u]) {
            if (vis[v] == 1) return true;
        }
        vis[u] = 2;
        return false;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::CycleDetection));

    // Var 5: C++ cycle check function
    let v5 = r#"
    bool hasCycle = false;
    if (slow == fast) {
        hasCycle = true;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::CycleDetection));

    // Var 6 (Negative): Simple linear traversal without cycle check
    let neg = r#"
    ListNode* curr = head;
    while (curr) {
        curr = curr->next;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::CycleDetection));
}

// ============================================================================
// BATCH 3: TREES & GRAPHS (5-7 VARIATIONS EACH)
// ============================================================================

// 21. BINARY SEARCH TREE (6 variations)
#[test]
fn test_binary_search_tree_variations() {
    // Var 1: Search BST with pointer comparisons
    let v1 = r#"
    TreeNode* searchBST(TreeNode* root, int val) {
        if (!root || root->val == val) return root;
        if (val < root->val) return searchBST(root->left, val);
        return searchBST(root->right, val);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::BinarySearchTree));

    // Var 2: Insert into BST with friend variables
    let v2 = r#"
    TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);
        if (val < root.val) root.left = insertIntoBST(root.left, val);
        else root.right = insertIntoBST(root.right, val);
        return root;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::BinarySearchTree));

    // Var 3: Iterative BST traversal
    let v3 = r#"
    TreeNode curr = root;
    while (curr != null) {
        if (target < curr.val) curr = curr.left;
        else if (target > curr.val) curr = curr.right;
        else return curr;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::BinarySearchTree));

    // Var 4: Validate BST (isValidBST)
    let v4 = r#"
    bool isValidBST(TreeNode* root) {
        return check(root, LLONG_MIN, LLONG_MAX);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::BinarySearchTree));

    // Var 5: C++ BST node structure
    let v5 = r#"
    struct BSTNode {
        int val;
        BSTNode *left, *right;
    };
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::BinarySearchTree));

    // Var 6 (Negative): General binary tree max depth
    let neg = r#"
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::BinarySearchTree));
}

// 22. LCA (6 variations)
#[test]
fn test_lca_variations() {
    // Var 1: lowestCommonAncestor canonical recursive
    let v1 = r#"
    TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root;
        return left != null ? left : right;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Lca));

    // Var 2: C++ lowestCommonAncestor with arrow pointers
    let v2 = r#"
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root || root == p || root == q) return root;
        TreeNode* l = lowestCommonAncestor(root->left, p, q);
        TreeNode* r = lowestCommonAncestor(root->right, p, q);
        return l && r ? root : (l ? l : r);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Lca));

    // Var 3: BST LCA condition
    let v3 = r#"
    if (root.val > p.val && root.val > q.val) return lowestCommonAncestor(root.left, p, q);
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Lca));

    // Var 4: Tree LCA with binary lifting query
    let v4 = r#"
    int lca(int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        for (int i = 20; i >= 0; i--) {
            if (depth[u] - (1 << i) >= depth[v]) u = up[u][i];
        }
        return u;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Lca));

    // Var 5: LCA with tin and tout discovery times
    let v5 = r#"
    int get_lca(int u, int v) {
        if (tin[u] <= tin[v]) return u;
        return LCA(u, v);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Lca));

    // Var 6 (Negative): Single node lookup
    let neg = r#"
    TreeNode findNode(TreeNode root, int val) {
        if (root == null || root.val == val) return root;
        return findNode(root.left, val);
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Lca));
}

// 23. BINARY LIFTING (6 variations)
#[test]
fn test_binary_lifting_variations() {
    // Var 1: 2D up array jump preprocessing
    let v1 = r#"
    for (int j = 1; j < LOGN; j++) {
        for (int i = 1; i <= n; i++) {
            up[i][j] = up[up[i][j - 1]][j - 1];
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::BinaryLifting));

    // Var 2: ancestor table with bit shift
    let v2 = r#"
    for (int j = 1; (1 << j) <= n; j++) {
        for (int u = 0; u < n; u++) {
            ancestor[u][j] = ancestor[ancestor[u][j - 1]][j - 1];
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::BinaryLifting));

    // Var 3: jump table with 1 << 20
    let v3 = r#"
    int jump[N][20];
    void precompute() {
        for (int j = 1; j < 20; j++) {
            for (int i = 0; i < n; i++) {
                jump[i][j] = jump[jump[i][j - 1]][j - 1];
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::BinaryLifting));

    // Var 4: Kth ancestor query
    let v4 = r#"
    int getKthAncestor(int node, int k) {
        for (int i = 0; i < 20; i++) {
            if ((k & (1 << i)) != 0) {
                node = up[node][i];
            }
        }
        return node;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::BinaryLifting));

    // Var 5: C++ 2D vector for binary lifting
    let v5 = r#"
    vector<vector<int>> up(n, vector<int>(LOG));
    for (int j = 1; j < LOG; j++) {
        up[u][j] = up[up[u][j - 1]][j - 1];
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::BinaryLifting));

    // Var 6 (Negative): Plain 2D grid matrix
    let neg = r#"
    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) matrix[i][j] = 0;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::BinaryLifting));
}

// 24. TREE DP (6 variations)
#[test]
fn test_tree_dp_variations() {
    // Var 1: Subtree size DP
    let v1 = r#"
    void dfs(int u, int p) {
        sz[u] = 1;
        for (int v : adj[u]) {
            if (v != p) {
                dfs(v, u);
                sz[u] += sz[v];
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::TreeDp));

    // Var 2: In-and-out DP on trees
    let v2 = r#"
    void dfs(int u, int p) {
        dp[u] = 0;
        for (int v : tree[u]) {
            if (p != v) {
                dfs(v, u);
                dp[u] += dp[v] + 1;
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::TreeDp));

    // Var 3: Maximum independent set on tree
    let v3 = r#"
    void dfs(int u, int parent) {
        dp[u][1] = 1;
        for (int v : g[u]) {
            if (v != parent) {
                dfs(v, u);
                dp[u][0] += max(dp[v][0], dp[v][1]);
                dp[u][1] += dp[v][0];
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::TreeDp));

    // Var 4: Java style tree DP
    let v4 = r#"
    void dfs(int u, int p) {
        dp[u] = val[u];
        for (int v : adj.get(u)) {
            if (v != p) {
                dfs(v, u);
                dp[u] = Math.max(dp[u], dp[u] + dp[v]);
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::TreeDp));

    // Var 5: Rerooting DP
    let v5 = r#"
    for (int to : adj[v]) {
        if (to != p) {
            dp[to] = dp[v] + (n - 2 * sz[to]);
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::TreeDp));

    // Var 6 (Negative): Standard grid DFS
    let neg = r#"
    void dfs(int r, int c) {
        vis[r][c] = true;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::TreeDp));
}

// 25. DSU (6 variations)
#[test]
fn test_dsu_variations() {
    // Var 1: Canonical DSU struct
    let v1 = r#"
    struct DSU {
        vector<int> parent;
        int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]);
        }
        void unite(int i, int j) {
            int root_i = find(i), root_j = find(j);
            if (root_i != root_j) parent[root_i] = root_j;
        }
    };
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Dsu));

    // Var 2: Java DisjointSetUnion class
    let v2 = r#"
    class DisjointSet {
        int[] parent;
        int find(int x) {
            if (parent[x] == x) return x;
            return parent[x] = find(parent[x]);
        }
        void union(int x, int y) {
            int rx = find(x), ry = find(y);
            if (rx != ry) parent[rx] = ry;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Dsu));

    // Var 3: Arbitrary friend var names (rohit & amit)
    let v3 = r#"
    int rohit = find(u);
    int amit = find(v);
    if (rohit != amit) parent[rohit] = amit;
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Dsu));

    // Var 4: Path compression with root
    let v4 = r#"
    int find(int i) {
        while (root[i] != i) i = root[i];
        return i;
    }
    void union(int a, int b) {
        int ra = find(a), rb = find(b);
        root[ra] = rb;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Dsu));

    // Var 5: DSU rank array
    let v5 = r#"
    int find(int x) { return parent[x] == x ? x : parent[x] = find(parent[x]); }
    void unite(int x, int y) {
        x = find(x); y = find(y);
        if (x != y) parent[x] = y;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Dsu));

    // Var 6 (Negative): Plain array assignment
    let neg = r#"
    for (int i = 0; i < n; i++) arr[i] = i;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Dsu));
}

// 26. DIJKSTRA (6 variations)
#[test]
fn test_dijkstra_variations() {
    // Var 1: Priority queue with distance relaxation
    let v1 = r#"
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    dist[start] = 0;
    pq.push({0, start});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, weight] : g[u]) {
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Dijkstra));

    // Var 2: Java PriorityQueue with Node class
    let v2 = r#"
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
    dist[src] = 0;
    pq.offer(new int[]{src, 0});
    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int u = curr[0];
        for (int[] edge : adj.get(u)) {
            int v = edge[0], weight = edge[1];
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.offer(new int[]{v, dist[v]});
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Dijkstra));

    // Var 3: Dijkstra with friend variable names
    let v3 = r#"
    PriorityQueue<Pair> rohit = new PriorityQueue<>();
    rohit.add(new Pair(0, start));
    while (!rohit.isEmpty()) {
        Pair amit = rohit.poll();
        if (dist[amit.node] < amit.cost) continue;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Dijkstra));

    // Var 4: C++ Dijkstra function
    let v4 = r#"
    vector<int> dist(n, INF);
    priority_queue<pair<int, int>> pq;
    dist[0] = 0;
    pq.push({0, 0});
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Dijkstra));

    // Var 5: Dijkstra on grid with weights
    let v5 = r#"
    priority_queue<tuple<int, int, int>> pq;
    dist[0][0] = 0;
    pq.push({0, 0, 0});
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Dijkstra));

    // Var 6 (Negative): Plain BFS with unweighted queue
    let neg = r#"
    queue<int> q;
    q.push(start);
    while (!q.empty()) {
        int u = q.front(); q.pop();
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Dijkstra));
}

// 27. MST (6 variations)
#[test]
fn test_mst_variations() {
    // Var 1: Kruskal's algorithm with edge sorting and DSU
    let v1 = r#"
    struct Edge { int u, v, weight; };
    sort(edges.begin(), edges.end(), [](Edge a, Edge b) { return a.weight < b.weight; });
    int mst_cost = 0;
    for (auto& e : edges) {
        if (dsu.find(e.u) != dsu.find(e.v)) {
            dsu.unite(e.u, e.v);
            mst_cost += e.weight;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Mst));

    // Var 2: Kruskal with Kruskal function name
    let v2 = r#"
    int kruskal_mst(vector<Edge>& edges, int n) {
        sort(edges.begin(), edges.end());
        return 0;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Mst));

    // Var 3: Prim's algorithm
    let v3 = r#"
    int prim(int start) {
        priority_queue<pair<int, int>> pq;
        return 0;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Mst));

    // Var 4: Java Kruskal with cost sorting
    let v4 = r#"
    Arrays.sort(edges, (a, b) -> Integer.compare(a.cost, b.cost));
    int totalMST = 0;
    for (Edge edge : edges) {
        if (find(edge.u) != find(edge.v)) {
            union(edge.u, edge.v);
            totalMST += edge.cost;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Mst));

    // Var 5: Prim MST function
    let v5 = r#"
    int prims(vector<vector<int>>& graph) {
        return mst_weight;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Mst));

    // Var 6 (Negative): Plain edge printing
    let neg = r#"
    for (Edge e : edges) {
        System.out.println(e.u + " " + e.v);
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Mst));
}

// 28. TOPOLOGICAL SORT (6 variations)
#[test]
fn test_topological_sort_variations() {
    // Var 1: Kahn's algorithm with in_degree and queue
    let v1 = r#"
    vector<int> in_degree(n, 0);
    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (in_degree[i] == 0) q.push(i);
    }
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (--in_degree[v] == 0) q.push(v);
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::TopologicalSort));

    // Var 2: Java Kahn's inDegree
    let v2 = r#"
    int[] inDegree = new int[numCourses];
    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < numCourses; i++) {
        if (inDegree[i] == 0) queue.add(i);
    }
    while (!queue.isEmpty()) {
        int curr = queue.poll();
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::TopologicalSort));

    // Var 3: indegree with friend variable names
    let v3 = r#"
    int[] indegree = new int[n];
    Queue<Integer> rohit = new ArrayDeque<>();
    rohit.add(0);
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::TopologicalSort));

    // Var 4: C++ queue push on zero in_degree
    let v4 = r#"
    for (int x : in_degree) {
        if (x == 0) q.push(x);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::TopologicalSort));

    // Var 5: Java indegree decrement
    let v5 = r#"
    if (--indegree[next] == 0) {
        q.add(next);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::TopologicalSort));

    // Var 6 (Negative): Plain BFS without in_degree
    let neg = r#"
    queue<int> q;
    q.push(0);
    while (!q.empty()) {
        int u = q.front(); q.pop();
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::TopologicalSort));
}

// 29. SHORTEST PATH (6 variations)
#[test]
fn test_shortest_path_variations() {
    // Var 1: Bellman-Ford edge relaxation
    let v1 = r#"
    for (int i = 0; i < n - 1; i++) {
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            if (dist[u] != INF && dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::ShortestPath));

    // Var 2: Floyd-Warshall all pairs
    let v2 = r#"
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::ShortestPath));

    // Var 3: 0-1 BFS with deque
    let v3 = r#"
    deque<int> dq;
    dist[src] = 0;
    dq.push_back(src);
    while (!dq.empty()) {
        int u = dq.front(); dq.pop_front();
        if (w == 0) dq.push_front(v);
        else dq.push_back(v);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::ShortestPath));

    // Var 4: Java Floyd-Warshall
    let v4 = r#"
    void floyd(int[][] graph) {
        for (int k = 0; k < V; k++) {
            for (int i = 0; i < V; i++) {
                for (int j = 0; j < V; j++) {
                    d[i][j] = Math.min(d[i][j], d[i][k] + d[k][j]);
                }
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::ShortestPath));

    // Var 5: Bellman-Ford function name
    let v5 = r#"
    bool bellman(int src) {
        return has_negative_cycle;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::ShortestPath));

    // Var 6 (Negative): Plain matrix addition
    let neg = r#"
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            c[i][j] = a[i][j] + b[i][j];
        }
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::ShortestPath));
}

// 30. STRONGLY CONNECTED COMPONENTS (6 variations)
#[test]
fn test_scc_variations() {
    // Var 1: Tarjan SCC with dfn, low, in_stack
    let v1 = r#"
    void tarjan(int u) {
        dfn[u] = low[u] = ++timer;
        stk.push(u);
        in_stack[u] = true;
        for (int v : adj[u]) {
            if (!dfn[v]) {
                tarjan(v);
                low[u] = min(low[u], low[v]);
            } else if (in_stack[v]) {
                low[u] = min(low[u], dfn[v]);
            }
        }
    }
    "#;
    assert!(
        AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::StronglyConnectedComponents)
    );

    // Var 2: Kosaraju algorithm with reversed graph
    let v2 = r#"
    void dfs1(int u) {
        vis[u] = true;
        for (int v : adj[u]) if (!vis[v]) dfs1(v);
        order.push(u);
    }
    void dfs2(int u) {
        vis[u] = true;
        for (int v : adjRev[u]) if (!vis[v]) dfs2(v);
    }
    "#;
    assert!(
        AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::StronglyConnectedComponents)
    );

    // Var 3: SCC naming convention
    let v3 = r#"
    vector<vector<int>> getSCC(int n) {
        return scc_components;
    }
    "#;
    assert!(
        AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::StronglyConnectedComponents)
    );

    // Var 4: Java Tarjan with onStack
    let v4 = r#"
    low[u] = Math.min(low[u], disc[v]);
    if (onStack[v]) {
        stack.push(u);
    }
    "#;
    assert!(
        AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::StronglyConnectedComponents)
    );

    // Var 5: Kosaraju function call
    let v5 = r#"
    int count = kosaraju(g);
    "#;
    assert!(
        AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::StronglyConnectedComponents)
    );

    // Var 6 (Negative): Plain graph DFS
    let neg = r#"
    void dfs(int u) {
        vis[u] = true;
        for (int v : adj[u]) if (!vis[v]) dfs(v);
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg)
        .contains(&AllowedAlgorithm::StronglyConnectedComponents));
}

// 31. BRIDGES AND ARTICULATION POINTS (6 variations)
#[test]
fn test_bridges_and_articulation_points_variations() {
    // Var 1: Bridge detection low[to] > tin[v]
    let v1 = r#"
    void dfs(int v, int p = -1) {
        tin[v] = low[v] = ++timer;
        for (int to : adj[v]) {
            if (to == p) continue;
            if (tin[to]) {
                low[v] = min(low[v], tin[to]);
            } else {
                dfs(to, v);
                low[v] = min(low[v], low[to]);
                if (low[to] > tin[v]) {
                    bridges.push_back({v, to});
                }
            }
        }
    }
    "#;
    assert!(
        AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::BridgesAndArticulationPoints)
    );

    // Var 2: Articulation point condition low[to] >= tin[v]
    let v2 = r#"
    if (p != -1 && low[to] >= tin[v]) {
        is_cut[v] = true;
    }
    "#;
    assert!(
        AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::BridgesAndArticulationPoints)
    );

    // Var 3: Java Critical Connections in a Network
    let v3 = r#"
    disc[u] = low[u] = time++;
    if (low[v] > disc[u]) {
        bridges.add(Arrays.asList(u, v));
    }
    "#;
    assert!(
        AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::BridgesAndArticulationPoints)
    );

    // Var 4: articulation points finder
    let v4 = r#"
    void find_articulation_points() {
        for (int i = 0; i < n; i++) if (!tin[i]) dfs(i);
    }
    "#;
    assert!(
        AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::BridgesAndArticulationPoints)
    );

    // Var 5: Cut vertices logic
    let v5 = r#"
    if (low[v] >= tin[u]) isCut[u] = true;
    "#;
    assert!(
        AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::BridgesAndArticulationPoints)
    );

    // Var 6 (Negative): Standard tree traversal
    let neg = r#"
    void dfs(int u, int p) {
        for (int v : tree[u]) if (v != p) dfs(v, u);
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg)
        .contains(&AllowedAlgorithm::BridgesAndArticulationPoints));
}

// 32. EULERIAN PATH (6 variations)
#[test]
fn test_eulerian_path_variations() {
    // Var 1: Hierholzer algorithm
    let v1 = r#"
    void hierholzer(int u) {
        while (!adj[u].empty()) {
            int v = adj[u].back();
            adj[u].pop_back();
            hierholzer(v);
        }
        path.push_back(u);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::EulerianPath));

    // Var 2: In-degree and Out-degree balance for Eulerian trail
    let v2 = r#"
    int start = 0, end = 0;
    for (int i = 0; i < n; i++) {
        if (out_degree[i] - in_degree[i] == 1) start++;
        else if (in_degree[i] - out_degree[i] == 1) end++;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::EulerianPath));

    // Var 3: Eulerian circuit check
    let v3 = r#"
    bool isEulerian() {
        return check_connected() && odd_degree_count == 0;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::EulerianPath));

    // Var 4: Eulerian trail function
    let v4 = r#"
    vector<int> findEulerianPath(vector<vector<int>>& graph) {
        return res;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::EulerianPath));

    // Var 5: Hierholzer path reversal
    let v5 = r#"
    List<String> Hierholzer() {
        return itinerary;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::EulerianPath));

    // Var 6 (Negative): Hamiltonian path / cycle check
    let neg = r#"
    bool hamiltonian(int mask, int u) {
        if (mask == (1 << n) - 1) return true;
        return false;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::EulerianPath));
}

// 33. BFS (6 variations)
#[test]
fn test_bfs_variations() {
    // Var 1: Canonical graph BFS with queue and visited array
    let v1 = r#"
    queue<int> q;
    vector<bool> vis(n, false);
    q.push(start);
    vis[start] = true;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (!vis[v]) {
                vis[v] = true;
                q.push(v);
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Bfs));

    // Var 2: Grid BFS with 4-directional moves
    let v2 = r#"
    Queue<int[]> queue = new LinkedList<>();
    queue.offer(new int[]{r, c});
    grid[r][c] = 0;
    while (!queue.isEmpty()) {
        int[] curr = queue.poll();
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Bfs));

    // Var 3: BFS function name
    let v3 = r#"
    void bfs(int start, vector<vector<int>>& grid) {
        visited[start] = true;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Bfs));

    // Var 4: Deque BFS with matrix visited check
    let v4 = r#"
    Deque<Pair> rohit = new ArrayDeque<>();
    rohit.add(new Pair(0, 0));
    matrix[0][0] = -1;
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Bfs));

    // Var 5: Level-order traversal
    let v5 = r#"
    queue<int> q;
    q.push(root);
    vis[root] = 1;
    while (!q.empty()) {
        int sz = q.size();
        while (sz--) {
            int u = q.front(); q.pop();
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Bfs));

    // Var 6 (Negative): Plain for loop
    let neg = r#"
    for (int i = 0; i < n; i++) sum += a[i];
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Bfs));
}

// 34. DFS (6 variations)
#[test]
fn test_dfs_variations() {
    // Var 1: Canonical recursive DFS with visited
    let v1 = r#"
    void dfs(int u) {
        vis[u] = true;
        for (int v : adj[u]) {
            if (!vis[v]) dfs(v);
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Dfs));

    // Var 2: Grid DFS with boundary checks
    let v2 = r#"
    void dfs(int r, int c, vector<vector<char>>& grid) {
        if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || grid[r][c] == '0') return;
        grid[r][c] = '0';
        dfs(r + 1, c, grid);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Dfs));

    // Var 3: Java DFS on matrix
    let v3 = r#"
    void dfs(int[][] matrix, int r, int c) {
        visited[r][c] = true;
        dfs(matrix, r + 1, c);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Dfs));

    // Var 4: Connected components DFS
    let v4 = r#"
    int components = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i);
            components++;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Dfs));

    // Var 5: Board DFS
    let v5 = r#"
    void dfs(int i, int j) {
        board[i][j] = 'X';
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Dfs));

    // Var 6 (Negative): Binary search
    let neg = r#"
    int l = 0, r = n - 1;
    while (l <= r) {
        int m = l + (r - l) / 2;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Dfs));
}

// ============================================================================
// BATCH 4: MATH, STRINGS & ADVANCED STRUCTURES (5-7 VARIATIONS EACH)
// ============================================================================

// 35. GCD (6 variations)
#[test]
fn test_gcd_variations() {
    // Var 1: Euclidean algorithm with modulo while loop
    let v1 = r#"
    int gcd(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Gcd));

    // Var 2: Recursive ternary GCD
    let v2 = r#"
    long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Gcd));

    // Var 3: Friend variable names (rohit & amit)
    let v3 = r#"
    int rohit = num1, amit = num2;
    while (amit != 0) {
        int rem = rohit % amit;
        rohit = amit;
        amit = rem;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Gcd));

    // Var 4: C++ std::__gcd builtin
    let v4 = r#"
    int g = __gcd(x, y);
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Gcd));

    // Var 5: Java BigInteger or GCD helper call
    let v5 = r#"
    int common = GCD(len1, len2);
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Gcd));

    // Var 6 (Negative): Plain modulo check for even/odd
    let neg = r#"
    if (n % 2 == 0) return true;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Gcd));
}

// 36. LCM (6 variations)
#[test]
fn test_lcm_variations() {
    // Var 1: Canonical (a * b) / gcd(a, b)
    let v1 = r#"
    long long lcm(long long a, long long b) {
        return (a * b) / gcd(a, b);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Lcm));

    // Var 2: Overflow-safe (a / gcd) * b
    let v2 = r#"
    long lcm(long a, long b) {
        return (a / gcd(a, b)) * b;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Lcm));

    // Var 3: Using __gcd
    let v3 = r#"
    int ans = (x * y) / __gcd(x, y);
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Lcm));

    // Var 4: LCM function name with friend vars
    let v4 = r#"
    long rohit = lcm(a, b);
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Lcm));

    // Var 5: LCM uppercase
    let v5 = r#"
    int val = LCM(u, v);
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Lcm));

    // Var 6 (Negative): Plain multiplication
    let neg = r#"
    long area = length * width;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Lcm));
}

// 37. FAST EXPONENTIATION (6 variations)
#[test]
fn test_fast_exponentiation_variations() {
    // Var 1: Canonical binpow with bit shift
    let v1 = r#"
    long long binpow(long long a, long long b, long long m) {
        long long res = 1;
        while (b > 0) {
            if (b & 1) res = (res * a) % m;
            a = (a * a) % m;
            b >>= 1;
        }
        return res;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::FastExponentiation));

    // Var 2: Java modPow style with % 2
    let v2 = r#"
    long power(long base, long exp) {
        long res = 1;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::FastExponentiation));

    // Var 3: Friend variable names (amit & rohit)
    let v3 = r#"
    long rohit = 1;
    while (amit > 0) {
        if ((amit & 1) != 0) rohit = (rohit * val) % mod;
        val = (val * val) % mod;
        amit >>= 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::FastExponentiation));

    // Var 4: fastPow naming
    let v4 = r#"
    long long fastPow(long long n, long long k) {
        return k == 0 ? 1 : 0;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::FastExponentiation));

    // Var 5: quickPow naming
    let v5 = r#"
    long quickPow(long x, long y) {
        return ans;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::FastExponentiation));

    // Var 6 (Negative): Linear power computation
    let neg = r#"
    long res = 1;
    for (int i = 0; i < n; i++) res *= a;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::FastExponentiation));
}

// 38. MODULAR ARITHMETIC (6 variations)
#[test]
fn test_modular_arithmetic_variations() {
    // Var 1: Fermat's Little Theorem modular inverse
    let v1 = r#"
    long long modInverse(long long n, long long p) {
        return power(n, p - 2, p);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::ModularArithmetic));

    // Var 2: Extended Euclidean algorithm extgcd
    let v2 = r#"
    int extgcd(int a, int b, int &x, int &y) {
        if (b == 0) { x = 1; y = 0; return a; }
        return 0;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::ModularArithmetic));

    // Var 3: Constant MOD 1000000007 operations
    let v3 = r#"
    long long ans = (a + b) % 1000000007;
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::ModularArithmetic));

    // Var 4: Constant MOD 998244353 operations
    let v4 = r#"
    int MOD = 998244353;
    long total = (x * y) % MOD;
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::ModularArithmetic));

    // Var 5: Subtraction with modulo
    let v5 = r#"
    int diff = (a - b + mod) % mod;
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::ModularArithmetic));

    // Var 6 (Negative): Plain addition
    let neg = r#"
    int sum = a + b;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::ModularArithmetic));
}

// 39. PRIME FACTORIZATION (6 variations)
#[test]
fn test_prime_factorization_variations() {
    // Var 1: Trial division up to d * d <= n
    let v1 = r#"
    vector<int> prime_factors(int n) {
        vector<int> factors;
        for (int d = 2; d * d <= n; d++) {
            while (n % d == 0) {
                factors.push_back(d);
                n /= d;
            }
        }
        if (n > 1) factors.push_back(n);
        return factors;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::PrimeFactorization));

    // Var 2: Java style prime factors
    let v2 = r#"
    List<Integer> primeFactors(int num) {
        List<Integer> res = new ArrayList<>();
        for (int i = 2; i * i <= num; i++) {
            while (num % i == 0) {
                res.add(i);
                num /= i;
            }
        }
        return res;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::PrimeFactorization));

    // Var 3: getFactors method name
    let v3 = r#"
    void getFactors(int n) {
        while (n % 2 == 0) n /= 2;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::PrimeFactorization));

    // Var 4: Friend variable name (rohit)
    let v4 = r#"
    int rohit = n;
    for (int p = 2; p * p <= rohit; p++) {
        while (rohit % p == 0) rohit /= p;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::PrimeFactorization));

    // Var 5: Counting prime exponents
    let v5 = r#"
    for (int d = 2; d * d <= n; d++) {
        int cnt = 0;
        while (n % d == 0) {
            cnt++;
            n /= d;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::PrimeFactorization));

    // Var 6 (Negative): Checking single division
    let neg = r#"
    if (n % 2 == 0) n /= 2;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::PrimeFactorization));
}

// 40. COMBINATORICS (6 variations)
#[test]
fn test_combinatorics_variations() {
    // Var 1: Precomputed factorials and inverse factorials
    let v1 = r#"
    long long nCr(int n, int r) {
        if (r < 0 || r > n) return 0;
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Combinatorics));

    // Var 2: Pascal's triangle C(n, k)
    let v2 = r#"
    for (int i = 0; i <= n; i++) {
        c[i][0] = 1;
        for (int j = 1; j <= i; j++) {
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Combinatorics));

    // Var 3: combinations method call
    let v3 = r#"
    long ways = combinations(n, k);
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Combinatorics));

    // Var 4: Permutations nPr
    let v4 = r#"
    long nPr(int n, int r) {
        return factorial[n] * ifact[n - r];
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Combinatorics));

    // Var 5: Pascal function name
    let v5 = r#"
    List<List<Integer>> generate_pascal(int numRows) {
        return result;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Combinatorics));

    // Var 6 (Negative): Simple array addition
    let neg = r#"
    int sum = a + b;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Combinatorics));
}

// 41. KMP (6 variations)
#[test]
fn test_kmp_variations() {
    // Var 1: Canonical pi array prefix function
    let v1 = r#"
    vector<int> compute_lps(string pattern) {
        int m = pattern.size();
        vector<int> pi(m, 0);
        for (int i = 1; i < m; i++) {
            int j = pi[i - 1];
            while (j > 0 && pattern[i] != pattern[j]) j = pi[j - 1];
            if (pattern[i] == pattern[j]) j++;
            pi[i] = j;
        }
        return pi;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Kmp));

    // Var 2: Needle in haystack search with LPS
    let v2 = r#"
    int lps[n];
    string needle = "abc";
    string haystack = "aababc";
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Kmp));

    // Var 3: pi array pattern matching
    let v3 = r#"
    vector<int> pi(n);
    if (pattern[i] == pattern[len]) len++;
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Kmp));

    // Var 4: Java KMP search
    let v4 = r#"
    int[] lps = new int[needle.length()];
    for (int i = 0; i < match; i++) {}
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Kmp));

    // Var 5: C++ KMP string match
    let v5 = r#"
    pi[0] = 0;
    for (int i = 1; i < pattern.length(); i++) {}
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Kmp));

    // Var 6 (Negative): Simple brute force substring search
    let neg = r#"
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (s[i + j] != t[j]) break;
        }
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Kmp));
}

// 42. Z ALGORITHM (6 variations)
#[test]
fn test_z_algorithm_variations() {
    // Var 1: Canonical z array with [l, r] window box
    let v1 = r#"
    vector<int> z_function(string s) {
        int n = s.size();
        vector<int> z(n);
        int l = 0, r = 0;
        for (int i = 1; i < n; i++) {
            if (i <= r) z[i] = min(r - i + 1, z[i - l]);
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
            if (i + z[i] - 1 > r) { l = i; r = i + z[i] - 1; }
        }
        return z;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::ZAlgorithm));

    // Var 2: zAlgorithm function name
    let v2 = r#"
    int[] zAlgorithm(String s) {
        int[] z = new int[s.length()];
        return z;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::ZAlgorithm));

    // Var 3: z_box name
    let v3 = r#"
    void z_box(string s) {
        int l = 0, r = 0;
        z[k] = 0;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::ZAlgorithm));

    // Var 4: C++ z array update
    let v4 = r#"
    if (i <= r) z[i] = min(r - i + 1, z[i - l]);
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::ZAlgorithm));

    // Var 5: z_algorithm name
    let v5 = r#"
    vector<int> z_algorithm(const string& str) {
        vector<int> z(str.length());
        return z;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::ZAlgorithm));

    // Var 6 (Negative): Plain string equality
    let neg = r#"
    if (s == t) return true;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::ZAlgorithm));
}

// 43. ROLLING HASH (6 variations)
#[test]
fn test_rolling_hash_variations() {
    // Var 1: Polynomial rolling hash with p_pow and MOD
    let v1 = r#"
    long long poly_hash(string const& s) {
        const int p = 31;
        const int m = 1e9 + 9;
        long long hash_value = 0;
        long long p_pow = 1;
        for (char c : s) {
            hash_value = (hash_value + (c - 'a' + 1) * p_pow) % m;
            p_pow = (p_pow * p) % m;
        }
        return hash_value;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::RollingHash));

    // Var 2: Power array with BASE and MOD
    let v2 = r#"
    long[] power = new long[n];
    power[0] = 1;
    for (int i = 1; i < n; i++) {
        power[i] = (power[i - 1] * BASE) % MOD;
    }
    long hash = 0;
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::RollingHash));

    // Var 3: Rabin-Karp rolling hash subtraction and shift
    let v3 = r#"
    long hashVal = (curr_hash - old_char * p_pow) % MOD;
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::RollingHash));

    // Var 4: Double hash prefix computation
    let v4 = r#"
    vector<long long> Hash(n + 1, 0);
    for (int i = 0; i < n; i++) {
        Hash[i + 1] = (Hash[i] * base + s[i]) % MOD;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::RollingHash));

    // Var 5: Java string rolling hash
    let v5 = r#"
    long hash = 0;
    long base = 256;
    for (int i = 0; i < s.length(); i++) {
        hash = (hash * base + s.charAt(i)) % 1000000007;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::RollingHash));

    // Var 6 (Negative): Plain checksum XOR
    let neg = r#"
    int xor_sum = 0;
    for (char c : s) xor_sum ^= c;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::RollingHash));
}

// 44. TRIE (6 variations)
#[test]
fn test_trie_variations() {
    // Var 1: Node with child[26] array and is_end flag
    let v1 = r#"
    struct TrieNode {
        TrieNode* child[26];
        bool is_end = false;
        TrieNode() {
            for (int i = 0; i < 26; i++) child[i] = nullptr;
        }
    };
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Trie));

    // Var 2: Java Node with Node[26] and isEnd
    let v2 = r#"
    class Node {
        Node[] children = new Node[26];
        boolean isEnd = false;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Trie));

    // Var 3: Insert with is_end update
    let v3 = r#"
    void insert(string word) {
        Node* curr = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!curr->child[idx]) curr->child[idx] = new Node();
            curr = curr->child[idx];
        }
        curr->is_end = true;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Trie));

    // Var 4: Friend variable names in Trie traversal
    let v4 = r#"
    Node rohit = root;
    rohit.isEnd = true;
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Trie));

    // Var 5: C++ child array of size 26
    let v5 = r#"
    Node* child[26];
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Trie));

    // Var 6 (Negative): Frequency array of size 26
    let neg = r#"
    int count[26] = {0};
    for (char c : s) count[c - 'a']++;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Trie));
}

// 45. SEGMENT TREE (6 variations)
#[test]
fn test_segment_tree_variations() {
    // Var 1: 4 * n tree allocation with mid and update
    let v1 = r#"
    vector<int> tree(4 * n);
    void update(int node, int start, int end, int idx, int val) {
        if (start == end) { tree[node] = val; return; }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::SegmentTree));

    // Var 2: 4*n tree with query
    let v2 = r#"
    int query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return 0;
        int mid = (l + r) / 2;
        return query(2*node, l, mid, ql, qr) + query(2*node + 1, mid + 1, r, ql, qr);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::SegmentTree));

    // Var 3: Java SegmentTree class
    let v3 = r#"
    class SegmentTree {
        int[] tree;
        SegmentTree(int n) { tree = new int[4 * n]; }
        void update(int node, int mid) {}
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::SegmentTree));

    // Var 4: Friend variable name in node index
    let v4 = r#"
    int rohit = 2 * node;
    int amit = 2 * node + 1;
    int mid = (l + r) / 2;
    update(rohit, l, mid);
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::SegmentTree));

    // Var 5: C++ 4*n tree array with query
    let v5 = r#"
    int tree[4 * n];
    int query(int node) { return mid; }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::SegmentTree));

    // Var 6 (Negative): Plain array multiplication
    let neg = r#"
    for (int i = 0; i < n; i++) a[i] *= 4;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::SegmentTree));
}

// 46. LAZY SEGMENT TREE (6 variations)
#[test]
fn test_lazy_segment_tree_variations() {
    // Var 1: Segment tree with lazy array and push_down
    let v1 = r#"
    vector<int> tree(4 * n), lazy(4 * n);
    void push_down(int node, int start, int end) {
        if (lazy[node] != 0) {
            tree[2 * node] += lazy[node];
            tree[2 * node + 1] += lazy[node];
            lazy[2 * node] += lazy[node];
            lazy[2 * node + 1] += lazy[node];
            lazy[node] = 0;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::LazySegmentTree));

    // Var 2: Java pushDown function
    let v2 = r#"
    void pushDown(int node) {
        if (lazy[node] != 0) {
            tree[2 * node] += lazy[node];
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::LazySegmentTree));

    // Var 3: Bit shift << 1 child propagation
    let v3 = r#"
    void push(int node) {
        lazy[node << 1] += lazy[node];
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::LazySegmentTree));

    // Var 4: seg tree with lazy array
    let v4 = r#"
    int seg[4 * N], lazy[4 * N];
    void push_down(int node) {
        seg[2*node] += lazy[node];
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::LazySegmentTree));

    // Var 5: Lazy propagation struct
    let v5 = r#"
    struct LazySeg {
        vector<int> tree, lazy;
        void push(int node) {}
    };
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::LazySegmentTree));

    // Var 6 (Negative): Plain segment tree without lazy tag
    let neg = r#"
    void update(int node, int l, int r) {
        tree[2 * node] += val;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::LazySegmentTree));
}

// 47. FENWICK TREE (6 variations)
#[test]
fn test_fenwick_tree_variations() {
    // Var 1: Canonical BIT with i += i & -i and i -= i & -i
    let v1 = r#"
    struct Fenwick {
        vector<int> tree;
        void add(int i, int delta) {
            for (; i < tree.size(); i += i & -i) tree[i] += delta;
        }
        int query(int i) {
            int sum = 0;
            for (; i > 0; i -= i & -i) sum += tree[i];
            return sum;
        }
    };
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::FenwickTree));

    // Var 2: Binary Indexed Tree with update and query
    let v2 = r#"
    void update(int idx, int val) {
        while (idx <= n) {
            bit[idx] += val;
            idx += idx & -idx;
        }
    }
    int query(int idx) {
        int sum = 0;
        while (idx > 0) {
            sum += bit[idx];
            idx -= idx & -idx;
        }
        return sum;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::FenwickTree));

    // Var 3: x & -x with Fenwick naming
    let v3 = r#"
    class FenwickTree {
        int lowbit(int x) { return x & -x; }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::FenwickTree));

    // Var 4: Friend variable name in Fenwick loop
    let v4 = r#"
    Fenwick bit;
    for (int rohit = idx; rohit <= n; rohit += rohit & -rohit) {
        tree[rohit] += val;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::FenwickTree));

    // Var 5: C++ Fenwick prefix sum
    let v5 = r#"
    int query(int i) {
        int res = 0;
        for (; i > 0; i -= i & -i) res += f[i];
        return res;
    }
    void add(int i, int delta) {
        for (; i <= n; i += i & -i) f[i] += delta;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::FenwickTree));

    // Var 6 (Negative): Plain bitwise AND check
    let neg = r#"
    if ((x & 1) == 0) return true;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::FenwickTree));
}

// 48. SPARSE TABLE (6 variations)
#[test]
fn test_sparse_table_variations() {
    // Var 1: 2D jump table with 1 << j
    let v1 = r#"
    for (int j = 1; (1 << j) <= n; j++) {
        for (int i = 0; i + (1 << j) <= n; i++) {
            st[i][j] = min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::SparseTable));

    // Var 2: RMQ query with 31 - __builtin_clz
    let v2 = r#"
    int query(int l, int r) {
        int j = 31 - __builtin_clz(r - l + 1);
        return min(st[l][j], st[r - (1 << j) + 1][j]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::SparseTable));

    // Var 3: SparseTable class name
    let v3 = r#"
    class SparseTable {
        int[][] st;
        int query(int l, int r) {
            int k = 31 - Integer.numberOfLeadingZeros(r - l + 1);
            return 0;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::SparseTable));

    // Var 4: 1<<j with st array
    let v4 = r#"
    st[i][j] = min(st[i][j - 1], st[i + (1<<j)][j - 1]);
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::SparseTable));

    // Var 5: Sparse Table power of two jumps
    let v5 = r#"
    vector<vector<int>> st(n, vector<int>(20));
    int len = 1 << j;
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::SparseTable));

    // Var 6 (Negative): Plain 2D array matrix multiplication
    let neg = r#"
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) c[i][j] = 0;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::SparseTable));
}

// 49. SIEVE (6 variations)
#[test]
fn test_sieve_variations() {
    // Var 1: Canonical Sieve with is_prime and += p
    let v1 = r#"
    vector<bool> is_prime(n + 1, true);
    for (int p = 2; p * p <= n; p++) {
        if (is_prime[p]) {
            for (int i = p * p; i <= n; i += p) is_prime[i] = false;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Sieve));

    // Var 2: Sieve with friend variable names (rahul & rohit)
    let v2 = r#"
    vector<bool> rohit(n + 1, true);
    for (int rahul = 2; rahul * rahul <= n; rahul++) {
        if (rohit[rahul]) {
            for (int k = rahul * rahul; k <= n; k += rahul) {
                rohit[k] = false;
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Sieve));

    // Var 3: Sieve function name
    let v3 = r#"
    void sieve(int n) {
        primes.push_back(2);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Sieve));

    // Var 4: Java Sieve with isPrime array
    let v4 = r#"
    boolean[] isPrime = new boolean[n + 1];
    Arrays.fill(isPrime, true);
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) isPrime[j] = false;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Sieve));

    // Var 5: Composite marker array
    let v5 = r#"
    vector<int> composite(n + 1, 0);
    for (int i = 2; i * i <= n; i++) {
        for (int j = i * i; j <= n; j += i) composite[j] = 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Sieve));

    // Var 6 (Negative): Single prime test loop
    let neg = r#"
    bool check(int n) {
        for (int i = 2; i < n; i++) if (n % i == 0) return false;
        return true;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Sieve));
}

// ============================================================================
// BATCH 5: DP, HASHING & GENERAL PARADIGMS (5-7 VARIATIONS EACH)
// ============================================================================

// 50. BINARY SEARCH ON ANSWER (6 variations)
#[test]
fn test_binary_search_on_answer_variations() {
    // Var 1: isPossible predicate with low <= high
    let v1 = r#"
    bool isPossible(int mid, vector<int>& nums) { return true; }
    int low = 1, high = max_val;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (isPossible(mid, nums)) high = mid - 1;
        else low = mid + 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::BinarySearchOnAnswer));

    // Var 2: Koko eating bananas with inner verification loop
    let v2 = r#"
    int low = 1, high = max_val;
    while (low < high) {
        int mid = low + (high - low) / 2;
        long total = 0;
        for (int p : piles) {
            total += (p + mid - 1) / mid;
        }
        if (total <= h) high = mid;
        else low = mid + 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::BinarySearchOnAnswer));

    // Var 3: check() helper with friend variable names (rohit & amit)
    let v3 = r#"
    bool check(int val) { return true; }
    int rohit = 0, amit = 1e9;
    while (rohit < amit) {
        int mid = rohit + (amit - rohit) / 2;
        if (check(mid)) amit = mid;
        else rohit = mid + 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::BinarySearchOnAnswer));

    // Var 4: Java isValid condition
    let v4 = r#"
    boolean isValid(int target) { return false; }
    int l = 0, r = Integer.MAX_VALUE;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (isValid(mid)) l = mid + 1;
        else r = mid - 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::BinarySearchOnAnswer));

    // Var 5: can() helper function
    let v5 = r#"
    bool can(int k) { return true; }
    int start = 1, end = n;
    while (start <= end) {
        int mid = (start + end) / 2;
        if (can(mid)) end = mid - 1;
        else start = mid + 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::BinarySearchOnAnswer));

    // Var 6 (Negative): Plain array binary search without answer predicate
    let neg = r#"
    int l = 0, r = n - 1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (a[mid] == target) return mid;
        else if (a[mid] < target) l = mid + 1;
        else r = mid - 1;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::BinarySearchOnAnswer));
}

// 51. SORTING (6 variations)
#[test]
fn test_sorting_variations() {
    // Var 1: std::sort
    let v1 = r#"
    std::sort(nums.begin(), nums.end());
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Sorting));

    // Var 2: Arrays.sort in Java
    let v2 = r#"
    Arrays.sort(arr);
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Sorting));

    // Var 3: Collections.sort in Java
    let v3 = r#"
    Collections.sort(list);
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Sorting));

    // Var 4: Custom comparator sort
    let v4 = r#"
    std::sort(vec.begin(), vec.end(), greater<int>());
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Sorting));

    // Var 5: Java 2D array sort
    let v5 = r#"
    Arrays.sort(pairs, (a, b) -> Integer.compare(a[0], b[0]));
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Sorting));

    // Var 6 (Negative): Linear iteration
    let neg = r#"
    for (int i = 0; i < n; i++) sum += a[i];
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Sorting));
}

// 52. HASH MAP (6 variations)
#[test]
fn test_hash_map_variations() {
    // Var 1: unordered_map
    let v1 = r#"
    unordered_map<int, int> mp;
    mp[key] = value;
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::HashMap));

    // Var 2: Java HashMap
    let v2 = r#"
    HashMap<String, Integer> map = new HashMap<>();
    map.put("key", 1);
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::HashMap));

    // Var 3: Java Map interface
    let v3 = r#"
    Map<Integer, String> lookup = new HashMap<>();
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::HashMap));

    // Var 4: C++ std::map
    let v4 = r#"
    map<int, string> dict;
    dict[1] = "one";
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::HashMap));

    // Var 5: Friend variable names with unordered_map
    let v5 = r#"
    unordered_map<char, int> rohit;
    rohit['a'] = 10;
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::HashMap));

    // Var 6 (Negative): Plain array indexing
    let neg = r#"
    int arr[10];
    arr[0] = 5;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::HashMap));
}

// 53. HASH SET (6 variations)
#[test]
fn test_hash_set_variations() {
    // Var 1: unordered_set
    let v1 = r#"
    unordered_set<int> seen;
    seen.insert(x);
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::HashSet));

    // Var 2: Java HashSet
    let v2 = r#"
    HashSet<String> set = new HashSet<>();
    set.add("item");
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::HashSet));

    // Var 3: Java Set interface
    let v3 = r#"
    Set<Integer> unique = new HashSet<>();
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::HashSet));

    // Var 4: C++ set
    let v4 = r#"
    set<int> visited;
    visited.insert(42);
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::HashSet));

    // Var 5: Friend variable names with unordered_set
    let v5 = r#"
    unordered_set<long> amit;
    amit.insert(100LL);
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::HashSet));

    // Var 6 (Negative): Plain vector push
    let neg = r#"
    vector<int> v;
    v.push_back(1);
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::HashSet));
}

// 54. FREQUENCY COUNTING (6 variations)
#[test]
fn test_frequency_counting_variations() {
    // Var 1: Array count increment
    let v1 = r#"
    int count[26] = {0};
    for (char c : s) count[c - 'a']++;
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::FrequencyCounting));

    // Var 2: cnt array increment
    let v2 = r#"
    for (int x : nums) cnt[x]++;
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::FrequencyCounting));

    // Var 3: Java getOrDefault frequency counting
    let v3 = r#"
    Map<Integer, Integer> map = new HashMap<>();
    map.put(num, map.getOrDefault(num, 0) + 1);
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::FrequencyCounting));

    // Var 4: freq array += 1
    let v4 = r#"
    freq[val] += 1;
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::FrequencyCounting));

    // Var 5: frequency array with friend variable
    let v5 = r#"
    frequency[rohit]++;
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::FrequencyCounting));

    // Var 6 (Negative): Plain array assignment
    let neg = r#"
    for (int i = 0; i < n; i++) arr[i] = 0;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::FrequencyCounting));
}

// 55. MONOTONIC QUEUE (6 variations)
#[test]
fn test_monotonic_queue_variations() {
    // Var 1: Deque sliding window maximum with pop_front and pop_back
    let v1 = r#"
    deque<int> dq;
    for (int i = 0; i < n; i++) {
        if (!dq.empty() && dq.front() == i - k) dq.pop_front();
        while (!dq.empty() && a[dq.back()] < a[i]) dq.pop_back();
        dq.push_back(i);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::MonotonicQueue));

    // Var 2: Java ArrayDeque with pollFirst and pollLast
    let v2 = r#"
    Deque<Integer> dq = new ArrayDeque<>();
    while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i]) {
        dq.pollLast();
    }
    if (!dq.isEmpty() && dq.peekFirst() <= i - k) {
        dq.pollFirst();
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::MonotonicQueue));

    // Var 3: Friend variable names with deque
    let v3 = r#"
    deque<int> rohit;
    rohit.pop_front();
    rohit.pop_back();
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::MonotonicQueue));

    // Var 4: Deque interface with pop_front and pop_back
    let v4 = r#"
    Deque<Integer> window = new LinkedList<>();
    window.pollFirst();
    window.pollLast();
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::MonotonicQueue));

    // Var 5: C++ deque sliding min
    let v5 = r#"
    deque<int> q;
    while (!q.empty() && nums[q.back()] > nums[i]) q.pop_back();
    if (!q.empty() && q.front() < i - k + 1) q.pop_front();
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::MonotonicQueue));

    // Var 6 (Negative): Plain queue with only pop_front
    let neg = r#"
    queue<int> q;
    q.pop();
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::MonotonicQueue));
}

// 56. DYNAMIC PROGRAMMING (6 variations)
#[test]
fn test_dynamic_programming_variations() {
    // Var 1: C++ vector dp allocation
    let v1 = r#"
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= n; i++) dp[i] = dp[i - 1] * 2;
    "#;
    assert!(
        AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::DynamicProgramming)
            || AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::OneDDp)
    );

    // Var 2: Java int[] dp array
    let v2 = r#"
    int[] dp = new int[n + 1];
    dp[0] = 0;
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::DynamicProgramming));

    // Var 3: 2D dp vector allocation
    let v3 = r#"
    vector<vector<int>> dp(m, vector<int>(n, 0));
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::DynamicProgramming));

    // Var 4: General dp array usage
    let v4 = r#"
    int dp[N];
    dp[1] = 1;
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::DynamicProgramming));

    // Var 5: Java 2D dp
    let v5 = r#"
    int[][] dp = new int[n][m];
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::DynamicProgramming));

    // Var 6 (Negative): Plain array without dp naming
    let neg = r#"
    int arr[10];
    for (int i = 0; i < 10; i++) arr[i] = i;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::DynamicProgramming));
}

// 57. MEMOIZATION (6 variations)
#[test]
fn test_memoization_variations() {
    // Var 1: memo array with != -1 check
    let v1 = r#"
    int solve(int i) {
        if (memo[i] != -1) return memo[i];
        return memo[i] = solve(i - 1) + 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Memoization));

    // Var 2: 2D memo table
    let v2 = r#"
    int helper(int i, int j) {
        if (memo[i][j] != -1) return memo[i][j];
        return memo[i][j] = 0;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Memoization));

    // Var 3: cache array with != 0 check
    let v3 = r#"
    int rec(int n) {
        if (cache[n] != 0) return cache[n];
        return cache[n] = rec(n - 1) + rec(n - 2);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Memoization));

    // Var 4: dp table lookup with return dp[
    let v4 = r#"
    int dfs(int u) {
        if (dp[u] != -1) return dp[u];
        return dp[u] = 1;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Memoization));

    // Var 5: Java memo array with null check
    let v5 = r#"
    Integer memo[] = new Integer[n];
    int topDown(int i) {
        if (memo[i] != null) return memo[i];
        return memo[i] = 42;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Memoization));

    // Var 6 (Negative): Plain recursive Fibonacci without memo
    let neg = r#"
    int fib(int n) {
        if (n <= 1) return n;
        return fib(n - 1) + fib(n - 2);
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Memoization));
}

// 58. 1D DP (6 variations)
#[test]
fn test_one_d_dp_variations() {
    // Var 1: Climbing stairs recurrence dp[i] = dp[i-1] + dp[i-2]
    let v1 = r#"
    dp[0] = 1; dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::OneDDp));

    // Var 2: House robber recurrence with max
    let v2 = r#"
    for (int i = 2; i < n; i++) {
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::OneDDp));

    // Var 3: f array recurrence
    let v3 = r#"
    for (int i = 1; i <= n; i++) {
        f[i] = f[i - 1] * 2;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::OneDDp));

    // Var 4: Min cost climbing stairs
    let v4 = r#"
    for (int i = 2; i <= n; i++) {
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::OneDDp));

    // Var 5: Java 1D DP recurrence
    let v5 = r#"
    for (int i = 1; i < nums.length; i++) {
        dp[i] = Math.max(dp[i - 1], nums[i]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::OneDDp));

    // Var 6 (Negative): Plain array assignment
    let neg = r#"
    for (int i = 0; i < n; i++) a[i] = i * 2;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::OneDDp));
}

// 59. 2D DP (6 variations)
#[test]
fn test_two_d_dp_variations() {
    // Var 1: Grid unique paths dp[i][j] = dp[i-1][j] + dp[i][j-1]
    let v1 = r#"
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::TwoDDp));

    // Var 2: Longest Common Subsequence (LCS)
    let v2 = r#"
    if (s1[i-1] == s2[j-1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
    } else {
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::TwoDDp));

    // Var 3: Edit distance
    let v3 = r#"
    dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::TwoDDp));

    // Var 4: 2D row/col dp with dp[r][c]
    let v4 = r#"
    dp[r][c] = dp[r - 1][c] + dp[r][c - 1];
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::TwoDDp));

    // Var 5: Java 2D DP with Math.min
    let v5 = r#"
    dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::TwoDDp));

    // Var 6 (Negative): 2D matrix multiplication
    let neg = r#"
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) c[i][j] = a[i][j] + b[i][j];
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::TwoDDp));
}

// 60. KNAPSACK DP (6 variations)
#[test]
fn test_knapsack_dp_variations() {
    // Var 1: 0-1 Knapsack 1D backwards loop
    let v1 = r#"
    for (int i = 0; i < n; i++) {
        for (int w = W; w >= weight[i]; w--) {
            dp[w] = max(dp[w], dp[w - weight[i]] + val[i]);
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::KnapsackDp));

    // Var 2: 2D 0-1 Knapsack
    let v2 = r#"
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (wt[i - 1] <= w) {
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt[i - 1]] + val[i - 1]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::KnapsackDp));

    // Var 3: Unbounded Knapsack / Coin Change
    let v3 = r#"
    for (int w = weight; w <= W; w++) {
        dp[w] = max(dp[w], dp[w - weight] + cost[i]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::KnapsackDp));

    // Var 4: Java 0-1 knapsack with weights array
    let v4 = r#"
    for (int j = maxWeight; j >= weights[i]; j--) {
        dp[j] = Math.max(dp[j], dp[j - weights[i]] + values[i]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::KnapsackDp));

    // Var 5: Knapsack with w array
    let v5 = r#"
    dp[w] = max(dp[w], dp[w - w[i]] + val[i]);
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::KnapsackDp));

    // Var 6 (Negative): Plain array maximum
    let neg = r#"
    int max_val = 0;
    for (int x : nums) max_val = max(max_val, x);
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::KnapsackDp));
}

// 61. BITMASK DP (6 variations)
#[test]
fn test_bitmask_dp_variations() {
    // Var 1: TSP mask loop with 1 << n
    let v1 = r#"
    for (int mask = 0; mask < (1 << n); mask++) {
        for (int u = 0; u < n; u++) {
            if (!(mask & (1 << u))) continue;
            for (int v = 0; v < n; v++) {
                if (!(mask & (1 << v))) {
                    dp[mask | (1 << v)] = min(dp[mask | (1 << v)], dp[mask] + cost[u][v]);
                }
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::BitmaskDp));

    // Var 2: SOS DP (Sum Over Subsets)
    let v2 = r#"
    for (int i = 0; i < n; i++) {
        for (int mask = 0; mask < (1 << n); mask++) {
            if (mask & (1 << i)) dp[mask] += dp[mask ^ (1 << i)];
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::BitmaskDp));

    // Var 3: Matching bitmask DP
    let v3 = r#"
    vector<int> dp(1 << n, 0);
    for (int mask = 0; mask < (1<<n); mask++) {}
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::BitmaskDp));

    // Var 4: Java bitmask DP
    let v4 = r#"
    int[] dp = new int[1 << n];
    for (int mask = 0; mask < (1 << n); mask++) {
        int count = Integer.bitCount(mask);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::BitmaskDp));

    // Var 5: Bitmask subset iteration
    let v5 = r#"
    for (int sub = mask; sub > 0; sub = (sub - 1) & mask) {
        dp[mask] = min(dp[mask], dp[sub] + cost[mask ^ sub]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::BitmaskDp));

    // Var 6 (Negative): Plain bitwise check
    let neg = r#"
    bool is_set = (flags & (1 << 3)) != 0;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::BitmaskDp));
}

// 62. INTERVAL DP (6 variations)
#[test]
fn test_interval_dp_variations() {
    // Var 1: Matrix Chain Multiplication (MCM) loop by length
    let v1 = r#"
    for (int len = 2; len <= n; len++) {
        for (int i = 1; i <= n - len + 1; i++) {
            int j = i + len - 1;
            for (int k = i; k < j; k++) {
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + cost[i][k][j]);
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::IntervalDp));

    // Var 2: Burst Balloons interval DP
    let v2 = r#"
    for (int len = 1; len <= n; len++) {
        for (int i = 1; i <= n - len + 1; i++) {
            int j = i + len - 1;
            for (int k = i; k <= j; k++) {
                dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1]);
            }
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::IntervalDp));

    // Var 3: length = 2 loop condition
    let v3 = r#"
    for (int length = 2; length <= n; length++) {
        int j = i + length - 1;
        cost[i][j] = min(cost[i][j], cost[i][k] + cost[k+1][j]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::IntervalDp));

    // Var 4: Java Interval DP
    let v4 = r#"
    for (int len = 2; len <= N; len++) {
        for (int i = 0; i <= N - len; i++) {
            int j = i + len - 1;
            dp[i][j] = dp[i][k] + dp[k + 1][j];
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::IntervalDp));

    // Var 5: C++ interval DP recurrence
    let v5 = r#"
    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + sum);
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::IntervalDp));

    // Var 6 (Negative): Plain 2D array iteration
    let neg = r#"
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) a[i][j] = 0;
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::IntervalDp));
}

// 63. GREEDY (6 variations)
#[test]
fn test_greedy_variations() {
    // Var 1: Activity selection / Interval scheduling with greedy count
    let v1 = r#"
    sort(intervals.begin(), intervals.end());
    int ans = 0, last_end = -1;
    for (auto& item : intervals) {
        if (item.start >= last_end) {
            ans++;
            last_end = item.end;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Greedy));

    // Var 2: Greedy jump game
    let v2 = r#"
    int greedy_reach = 0;
    for (int i = 0; i < n; i++) {
        if (i > greedy_reach) return false;
        greedy_reach = max(greedy_reach, i + nums[i]);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Greedy));

    // Var 3: Java greedy choice with Arrays.sort
    let v3 = r#"
    Arrays.sort(tasks);
    int count = 0;
    for (int t : tasks) {
        count++;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Greedy));

    // Var 4: Fractional knapsack greedy sort
    let v4 = r#"
    sort(items.begin(), items.end(), compare);
    double res = 0;
    for (auto& it : items) {
        res++;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Greedy));

    // Var 5: Greedy algorithm function naming
    let v5 = r#"
    int greedySolve() {
        return ans;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Greedy));

    // Var 6 (Negative): Binary search
    let neg = r#"
    int l = 0, r = n - 1;
    while (l <= r) int m = (l + r) / 2;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Greedy));
}

// 64. BACKTRACKING (6 variations)
#[test]
fn test_backtracking_variations() {
    // Var 1: Permutations choice -> explore -> unchoose
    let v1 = r#"
    void backtrack(vector<int>& path, vector<bool>& used) {
        if (path.size() == n) { res.push_back(path); return; }
        for (int i = 0; i < n; i++) {
            if (used[i]) continue;
            used[i] = true;
            path.push_back(nums[i]);
            backtrack(path, used);
            path.pop_back();
            used[i] = false;
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::Backtracking));

    // Var 2: Java combinations backtracking
    let v2 = r#"
    void backtrack(List<Integer> path, int start) {
        if (path.size() == k) { result.add(new ArrayList<>(path)); return; }
        for (int i = start; i <= n; i++) {
            path.add(i);
            backtrack(path, i + 1);
            path.remove(path.size() - 1);
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::Backtracking));

    // Var 3: N-Queens search with undo
    let v3 = r#"
    void solve(int row, vector<string>& board) {
        if (row == n) { ans.push_back(board); return; }
        for (int col = 0; col < n; col++) {
            board[row][col] = 'Q';
            solve(row + 1, board);
            board[row][col] = '.';
        }
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::Backtracking));

    // Var 4: Subset generation with helper
    let v4 = r#"
    void helper(int idx, vector<int>& current) {
        current.push_back(nums[idx]);
        helper(idx + 1, current);
        current.pop_back();
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::Backtracking));

    // Var 5: DFS with path push and pop
    let v5 = r#"
    void dfs(int u) {
        path.push_back(u);
        dfs(v);
        path.pop_back();
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::Backtracking));

    // Var 6 (Negative): Plain recursion without state undo
    let neg = r#"
    int factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::Backtracking));
}

// 65. DIVIDE AND CONQUER (6 variations)
#[test]
fn test_divide_and_conquer_variations() {
    // Var 1: Merge Sort divide and conquer
    let v1 = r#"
    void merge_sort(int left, int right) {
        if (left >= right) return;
        int mid = left + (right - left) / 2;
        merge_sort(left, mid);
        merge_sort(mid + 1, right);
        merge(left, mid, right);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::DivideAndConquer));

    // Var 2: Quick Sort partition divide and conquer
    let v2 = r#"
    void divide(int l, int r) {
        if (l >= r) return;
        int mid = (l + r) / 2;
        divide(l, mid);
        divide(mid + 1, r);
        conquer(l, r);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::DivideAndConquer));

    // Var 3: Java style divide and conquer
    let v3 = r#"
    void sort(int[] a, int start, int end) {
        int mid = (start + end) / 2;
        sort(a, start, mid);
        sort(a, mid + 1, end);
        merge(a, start, mid, end);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::DivideAndConquer));

    // Var 4: Closest pair of points
    let v4 = r#"
    double solve(int low, int high) {
        int mid = (low + high) / 2;
        double d1 = solve(low, mid);
        double d2 = solve(mid + 1, high);
        return combine(d1, d2);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::DivideAndConquer));

    // Var 5: Maximum subarray divide and conquer
    let v5 = r#"
    int maxSub(int l, int r) {
        int mid = (l + r) / 2;
        int left_sum = maxSub(l, mid);
        int right_sum = maxSub(mid + 1, r);
        return merge(left_sum, right_sum);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::DivideAndConquer));

    // Var 6 (Negative): Linear traversal
    let neg = r#"
    for (int i = 0; i < n; i++) sum += a[i];
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::DivideAndConquer));
}

// 66. BIT MANIPULATION (6 variations)
#[test]
fn test_bit_manipulation_variations() {
    // Var 1: __builtin_popcount
    let v1 = r#"
    int bits = __builtin_popcount(mask);
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::BitManipulation));

    // Var 2: Brian Kernighan bit trick x & (x - 1)
    let v2 = r#"
    int count = 0;
    while (x > 0) {
        x = x & (x - 1);
        count++;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::BitManipulation));

    // Var 3: Java Integer.bitCount
    let v3 = r#"
    int ones = Integer.bitCount(num);
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::BitManipulation));

    // Var 4: Single Number XOR trick
    let v4 = r#"
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int x : nums) ans ^= x;
        return ans;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::BitManipulation));

    // Var 5: Leading zeros builtin
    let v5 = r#"
    int lz = __builtin_clz(val);
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::BitManipulation));

    // Var 6 (Negative): Plain arithmetic addition
    let neg = r#"
    int total = a + b;
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::BitManipulation));
}

// 67. MEET IN THE MIDDLE (6 variations)
#[test]
fn test_meet_in_the_middle_variations() {
    // Var 1: Partitioning array into first_half and second_half
    let v1 = r#"
    int mid = n / 2;
    vector<long long> first_half, second_half;
    sort(second_half.begin(), second_half.end());
    for (long long s : first_half) {
        auto it = lower_bound(second_half.begin(), second_half.end(), target - s);
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::MeetInTheMiddle));

    // Var 2: Meet in the middle naming
    let v2 = r#"
    long meet_in_the_middle(vector<int>& nums, int target) {
        return ans;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::MeetInTheMiddle));

    // Var 3: Two subsets part1 and part2 with binary search
    let v3 = r#"
    int half = len / 2;
    vector<int> part1, part2;
    binary_search(part2.begin(), part2.end(), val);
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::MeetInTheMiddle));

    // Var 4: Java meet in the middle with HashMap
    let v4 = r#"
    int mid = n / 2;
    HashMap<Long, Integer> left_half = new HashMap<>();
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::MeetInTheMiddle));

    // Var 5: C++ meetInTheMiddle method
    let v5 = r#"
    void meetInTheMiddle() {}
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::MeetInTheMiddle));

    // Var 6 (Negative): Single array binary search
    let neg = r#"
    int idx = lower_bound(a.begin(), a.end(), target) - a.begin();
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::MeetInTheMiddle));
}

// 68. SWEEP LINE (6 variations)
#[test]
fn test_sweep_line_variations() {
    // Var 1: Event sorting with START and END markers
    let v1 = r#"
    struct Event { int x, type; };
    vector<Event> events;
    sort(events.begin(), events.end(), [](auto& a, auto& b) { return a.x < b.x; });
    int active = 0;
    for (auto& e : events) {
        if (e.type == START) active++;
        else active--;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v1).contains(&AllowedAlgorithm::SweepLine));

    // Var 2: Coordinate endpoints +1 and -1 sweep
    let v2 = r#"
    vector<pair<int, int>> points;
    sort(points.begin(), points.end());
    for (auto& p : points) {
        int delta = p.second;
        curr += delta;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v2).contains(&AllowedAlgorithm::SweepLine));

    // Var 3: sweep_line function name
    let v3 = r#"
    int sweep_line(vector<vector<int>>& intervals) {
        return max_overlap;
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v3).contains(&AllowedAlgorithm::SweepLine));

    // Var 4: SweepLine class name
    let v4 = r#"
    class SweepLine {
        void process() {}
    }
    "#;
    assert!(AlgorithmDetector::detect_raw(v4).contains(&AllowedAlgorithm::SweepLine));

    // Var 5: Event point sorting with sweepLine
    let v5 = r#"
    sort(events.begin(), events.end());
    int sweepLine = 0;
    "#;
    assert!(AlgorithmDetector::detect_raw(v5).contains(&AllowedAlgorithm::SweepLine));

    // Var 6 (Negative): Plain array sort
    let neg = r#"
    sort(nums.begin(), nums.end());
    "#;
    assert!(!AlgorithmDetector::detect_raw(neg).contains(&AllowedAlgorithm::SweepLine));
}
