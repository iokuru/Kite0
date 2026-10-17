import json
import os

TOUGH_BENCHMARK_CASES = [
    {
        "id": "tough_dijkstra_network_delay_cpp",
        "name": "Network Delay Time (C++ Dijkstra)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "graph",
            "dijkstra",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O((V + E) log V)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "Dijkstra"
        ],
        "code": "#include <vector>\n#include <queue>\nusing namespace std;\nclass Solution {\npublic:\n    int networkDelayTime(vector<vector<int>>& times, int n, int k) {\n        vector<vector<pair<int, int>>> adj(n + 1);\n        for (const auto& edge : times) {\n            adj[edge[0]].push_back({edge[1], edge[2]});\n        }\n        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;\n        vector<int> dist(n + 1, 1e9);\n        dist[k] = 0;\n        pq.push({0, k});\n        while (!pq.empty()) {\n            auto [d, u] = pq.top();\n            pq.pop();\n            if (d > dist[u]) continue;\n            for (auto [v, w] : adj[u]) {\n                if (dist[u] + w < dist[v]) {\n                    dist[v] = dist[u] + w;\n                    pq.push({dist[v], v});\n                }\n            }\n        }\n        int ans = 0;\n        for (int i = 1; i <= n; i++) {\n            if (dist[i] == 1e9) return -1;\n            ans = max(ans, dist[i]);\n        }\n        return ans;\n    }\n};"
    },
    {
        "id": "tough_dijkstra_network_delay_java",
        "name": "Network Delay Time (Java Dijkstra)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "graph",
            "dijkstra",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O((V + E) log V)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "Dijkstra"
        ],
        "code": "import java.util.*;\nclass Solution {\n    public int networkDelayTime(int[][] times, int n, int k) {\n        List<List<int[]>> adj = new ArrayList<>();\n        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());\n        for (int[] edge : times) {\n            adj.get(edge[0]).add(new int[]{edge[1], edge[2]});\n        }\n        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);\n        int[] dist = new int[n + 1];\n        Arrays.fill(dist, 1000000000);\n        dist[k] = 0;\n        pq.add(new int[]{0, k});\n        while (!pq.isEmpty()) {\n            int[] cur = pq.poll();\n            int d = cur[0], u = cur[1];\n            if (d > dist[u]) continue;\n            for (int[] next : adj.get(u)) {\n                int v = next[0], w = next[1];\n                if (dist[u] + w < dist[v]) {\n                    dist[v] = dist[u] + w;\n                    pq.add(new int[]{dist[v], v});\n                }\n            }\n        }\n        int ans = 0;\n        for (int i = 1; i <= n; i++) {\n            if (dist[i] == 1000000000) return -1;\n            ans = Math.max(ans, dist[i]);\n        }\n        return ans;\n    }\n}"
    },
    {
        "id": "tough_kruskal_mst_cpp",
        "name": "Kruskal Minimum Spanning Tree (C++ DSU)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "graph",
            "mst",
            "dsu",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(E log V)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "MST"
        ],
        "code": "#include <vector>\n#include <algorithm>\n#include <numeric>\nusing namespace std;\nstruct DSU {\n    vector<int> parent;\n    DSU(int n) : parent(n) {\n        iota(parent.begin(), parent.end(), 0);\n    }\n    int find(int i) {\n        if (parent[i] == i)\n            return i;\n        return parent[i] = find(parent[i]);\n    }\n    bool unite(int i, int j) {\n        int root_i = find(i);\n        int root_j = find(j);\n        if (root_i != root_j) {\n            parent[root_i] = root_j;\n            return true;\n        }\n        return false;\n    }\n};\nclass Solution {\npublic:\n    int minCostConnectPoints(vector<vector<int>>& edges, int n) {\n        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {\n            return a[2] < b[2];\n        });\n        DSU dsu(n);\n        int cost = 0, count = 0;\n        for (const auto& e : edges) {\n            if (dsu.unite(e[0], e[1])) {\n                cost += e[2];\n                if (++count == n - 1) break;\n            }\n        }\n        return cost;\n    }\n};"
    },
    {
        "id": "tough_kruskal_mst_java",
        "name": "Kruskal Minimum Spanning Tree (Java DSU)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "graph",
            "mst",
            "dsu",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(E log V)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "MST"
        ],
        "code": "import java.util.*;\nclass Solution {\n    static class DSU {\n        int[] parent;\n        DSU(int n) {\n            parent = new int[n];\n            for (int i = 0; i < n; i++) parent[i] = i;\n        }\n        int find(int i) {\n            if (parent[i] == i) return i;\n            return parent[i] = find(parent[i]);\n        }\n        boolean unite(int i, int j) {\n            int root_i = find(i);\n            int root_j = find(j);\n            if (root_i != root_j) {\n                parent[root_i] = root_j;\n                return true;\n            }\n            return false;\n        }\n    }\n    public int minCostConnectPoints(int[][] edges, int n) {\n        Arrays.sort(edges, (a, b) -> Integer.compare(a[2], b[2]));\n        DSU dsu = new DSU(n);\n        int cost = 0, count = 0;\n        for (int[] e : edges) {\n            if (dsu.unite(e[0], e[1])) {\n                cost += e[2];\n                if (++count == n - 1) break;\n            }\n        }\n        return cost;\n    }\n}"
    },
    {
        "id": "tough_topo_sort_kahn_cpp",
        "name": "Course Schedule II (C++ Kahn Topological Sort)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "graph",
            "topological_sort",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(V + E)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "Topological Sort"
        ],
        "code": "#include <vector>\n#include <queue>\nusing namespace std;\nclass Solution {\npublic:\n    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {\n        vector<vector<int>> adj(numCourses);\n        vector<int> indegree(numCourses, 0);\n        for (const auto& pre : prerequisites) {\n            adj[pre[1]].push_back(pre[0]);\n            indegree[pre[0]]++;\n        }\n        queue<int> q;\n        for (int i = 0; i < numCourses; i++) {\n            if (indegree[i] == 0) q.push(i);\n        }\n        vector<int> order;\n        while (!q.empty()) {\n            int curr = q.front();\n            q.pop();\n            order.push_back(curr);\n            for (int neighbor : adj[curr]) {\n                indegree[neighbor]--;\n                if (indegree[neighbor] == 0) q.push(neighbor);\n            }\n        }\n        if (order.size() == numCourses) return order;\n        return {};\n    }\n};"
    },
    {
        "id": "tough_topo_sort_kahn_java",
        "name": "Course Schedule II (Java Kahn Topological Sort)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "graph",
            "topological_sort",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(V + E)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "Topological Sort"
        ],
        "code": "import java.util.*;\nclass Solution {\n    public int[] findOrder(int numCourses, int[][] prerequisites) {\n        List<List<Integer>> adj = new ArrayList<>();\n        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());\n        int[] indegree = new int[numCourses];\n        for (int[] pre : prerequisites) {\n            adj.get(pre[1]).add(pre[0]);\n            indegree[pre[0]]++;\n        }\n        Queue<Integer> q = new LinkedList<>();\n        for (int i = 0; i < numCourses; i++) {\n            if (indegree[i] == 0) q.add(i);\n        }\n        int[] order = new int[numCourses];\n        int idx = 0;\n        while (!q.isEmpty()) {\n            int curr = q.poll();\n            order[idx++] = curr;\n            for (int neighbor : adj.get(curr)) {\n                indegree[neighbor]--;\n                if (indegree[neighbor] == 0) q.add(neighbor);\n            }\n        }\n        return idx == numCourses ? order : new int[0];\n    }\n}"
    },
    {
        "id": "tough_segment_tree_cpp",
        "name": "Range Sum Query Mutable (C++ Segment Tree)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "data_structure",
            "segment_tree",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n + q log n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Segment Tree"
        ],
        "code": "#include <vector>\nusing namespace std;\nclass NumArray {\n    vector<int> tree;\n    int n;\n    void buildTree(const vector<int>& nums, int node, int start, int end) {\n        if (start == end) {\n            tree[node] = nums[start];\n        } else {\n            int mid = start + (end - start) / 2;\n            buildTree(nums, 2 * node, start, mid);\n            buildTree(nums, 2 * node + 1, mid + 1, end);\n            tree[node] = tree[2 * node] + tree[2 * node + 1];\n        }\n    }\npublic:\n    NumArray(vector<int>& nums) {\n        n = nums.size();\n        tree.resize(4 * n, 0);\n        if (n > 0) buildTree(nums, 1, 0, n - 1);\n    }\n    void update(int index, int val, int node, int start, int end) {\n        if (start == end) {\n            tree[node] = val;\n            return;\n        }\n        int mid = start + (end - start) / 2;\n        if (index <= mid) update(index, val, 2 * node, start, mid);\n        else update(index, val, 2 * node + 1, mid + 1, end);\n        tree[node] = tree[2 * node] + tree[2 * node + 1];\n    }\n    int sumRange(int left, int right, int node, int start, int end) {\n        if (left <= start && end <= right) return tree[node];\n        int mid = start + (end - start) / 2;\n        int sum = 0;\n        if (left <= mid) sum += sumRange(left, right, 2 * node, start, mid);\n        if (right > mid) sum += sumRange(left, right, 2 * node + 1, mid + 1, end);\n        return sum;\n    }\n};"
    },
    {
        "id": "tough_segment_tree_java",
        "name": "Range Sum Query Mutable (Java Segment Tree)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "data_structure",
            "segment_tree",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n + q log n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Segment Tree"
        ],
        "code": "class NumArray {\n    int[] tree;\n    int n;\n    void build(int[] nums, int node, int start, int end) {\n        if (start == end) {\n            tree[node] = nums[start];\n        } else {\n            int mid = start + (end - start) / 2;\n            build(nums, 2 * node, start, mid);\n            build(nums, 2 * node + 1, mid + 1, end);\n            tree[node] = tree[2 * node] + tree[2 * node + 1];\n        }\n    }\n    public NumArray(int[] nums) {\n        n = nums.length;\n        tree = new int[4 * n];\n        if (n > 0) build(nums, 1, 0, n - 1);\n    }\n    public void update(int index, int val, int node, int start, int end) {\n        if (start == end) {\n            tree[node] = val;\n            return;\n        }\n        int mid = start + (end - start) / 2;\n        if (index <= mid) update(index, val, 2 * node, start, mid);\n        else update(index, val, 2 * node + 1, mid + 1, end);\n        tree[node] = tree[2 * node] + tree[2 * node + 1];\n    }\n    public int sumRange(int left, int right, int node, int start, int end) {\n        if (left <= start && end <= right) return tree[node];\n        int mid = start + (end - start) / 2;\n        int sum = 0;\n        if (left <= mid) sum += sumRange(left, right, 2 * node, start, mid);\n        if (right > mid) sum += sumRange(left, right, 2 * node + 1, mid + 1, end);\n        return sum;\n    }\n}"
    },
    {
        "id": "tough_fenwick_tree_cpp",
        "name": "Fenwick Tree Inversion Count (C++ BIT)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "data_structure",
            "fenwick_tree",
            "leetcode",
            "hard"
        ],
        "expected_tc": "O(q log n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Fenwick Tree"
        ],
        "code": "#include <vector>\nusing namespace std;\nstruct Fenwick {\n    int n;\n    vector<int> bit;\n    Fenwick(int n) : n(n), bit(n + 1, 0) {}\n    void add(int idx, int val) {\n        for (; idx <= n; idx += idx & -idx)\n            bit[idx] += val;\n    }\n    int query(int idx) {\n        int sum = 0;\n        for (; idx > 0; idx -= idx & -idx)\n            sum += bit[idx];\n        return sum;\n    }\n};\nclass Solution {\npublic:\n    int countInversions(vector<int>& nums) {\n        int n = nums.size();\n        Fenwick ft(n);\n        int ans = 0;\n        for (int i = 0; i < n; i++) {\n            ans += ft.query(n) - ft.query(nums[i]);\n            ft.add(nums[i], 1);\n        }\n        return ans;\n    }\n};"
    },
    {
        "id": "tough_fenwick_tree_java",
        "name": "Fenwick Tree Inversion Count (Java BIT)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "data_structure",
            "fenwick_tree",
            "leetcode",
            "hard"
        ],
        "expected_tc": "O(q log n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Fenwick Tree"
        ],
        "code": "class Solution {\n    static class Fenwick {\n        int n;\n        int[] bit;\n        Fenwick(int n) {\n            this.n = n;\n            bit = new int[n + 1];\n        }\n        void add(int idx, int val) {\n            for (; idx <= n; idx += idx & -idx)\n                bit[idx] += val;\n        }\n        int query(int idx) {\n            int sum = 0;\n            for (; idx > 0; idx -= idx & -idx)\n                sum += bit[idx];\n            return sum;\n        }\n    }\n    public int countInversions(int[] nums) {\n        int n = nums.length;\n        Fenwick ft = new Fenwick(n);\n        int ans = 0;\n        for (int i = 0; i < n; i++) {\n            ans += ft.query(n) - ft.query(nums[i]);\n            ft.add(nums[i], 1);\n        }\n        return ans;\n    }\n}"
    },
    {
        "id": "tough_monotonic_stack_histogram_cpp",
        "name": "Largest Rectangle in Histogram (C++ Monotonic Stack)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "monotonic_stack",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Monotonic Stack"
        ],
        "code": "#include <vector>\n#include <stack>\n#include <algorithm>\nusing namespace std;\nclass Solution {\npublic:\n    int largestRectangleArea(vector<int>& heights) {\n        int n = heights.size();\n        stack<int> st;\n        int max_area = 0;\n        for (int i = 0; i <= n; i++) {\n            int h = (i == n) ? 0 : heights[i];\n            while (!st.empty() && heights[st.top()] >= h) {\n                int height = heights[st.top()];\n                st.pop();\n                int width = st.empty() ? i : i - st.top() - 1;\n                max_area = max(max_area, height * width);\n            }\n            st.push(i);\n        }\n        return max_area;\n    }\n};"
    },
    {
        "id": "tough_monotonic_stack_histogram_java",
        "name": "Largest Rectangle in Histogram (Java Monotonic Stack)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "monotonic_stack",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Monotonic Stack"
        ],
        "code": "import java.util.*;\nclass Solution {\n    public int largestRectangleArea(int[] heights) {\n        int n = heights.length;\n        Stack<Integer> st = new Stack<>();\n        int maxArea = 0;\n        for (int i = 0; i <= n; i++) {\n            int h = (i == n) ? 0 : heights[i];\n            while (!st.isEmpty() && heights[st.peek()] >= h) {\n                int height = heights[st.pop()];\n                int width = st.isEmpty() ? i : i - st.peek() - 1;\n                maxArea = Math.max(maxArea, height * width);\n            }\n            st.push(i);\n        }\n        return maxArea;\n    }\n}"
    },
    {
        "id": "tough_monotonic_queue_max_cpp",
        "name": "Sliding Window Maximum (C++ Monotonic Queue)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "monotonic_queue",
            "sliding_window",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(k)",
        "expected_algorithms": [
            "Monotonic Queue"
        ],
        "code": "#include <vector>\n#include <deque>\nusing namespace std;\nclass Solution {\npublic:\n    vector<int> maxSlidingWindow(vector<int>& nums, int k) {\n        int n = nums.size();\n        deque<int> dq;\n        vector<int> res;\n        for (int i = 0; i < n; i++) {\n            while (!dq.empty() && dq.front() <= i - k) {\n                dq.pop_front();\n            }\n            while (!dq.empty() && nums[dq.back()] <= nums[i]) {\n                dq.pop_back();\n            }\n            dq.push_back(i);\n            if (i >= k - 1) {\n                res.push_back(nums[dq.front()]);\n            }\n        }\n        return res;\n    }\n};"
    },
    {
        "id": "tough_monotonic_queue_max_java",
        "name": "Sliding Window Maximum (Java Monotonic Queue)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "monotonic_queue",
            "sliding_window",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(k)",
        "expected_algorithms": [
            "Monotonic Queue"
        ],
        "code": "import java.util.*;\nclass Solution {\n    public int[] maxSlidingWindow(int[] nums, int k) {\n        int n = nums.length;\n        Deque<Integer> dq = new ArrayDeque<>();\n        int[] res = new int[n - k + 1];\n        int idx = 0;\n        for (int i = 0; i < n; i++) {\n            while (!dq.isEmpty() && dq.peekFirst() <= i - k) {\n                dq.pollFirst();\n            }\n            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) {\n                dq.pollLast();\n            }\n            dq.addLast(i);\n            if (i >= k - 1) {\n                res[idx++] = nums[dq.peekFirst()];\n            }\n        }\n        return res;\n    }\n}"
    },
    {
        "id": "tough_bs_on_answer_packages_cpp",
        "name": "Capacity to Ship Packages (C++ Binary Search on Answer)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "binary_search_on_answer",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n log A)",
        "expected_sc": "O(1)",
        "expected_algorithms": [
            "Binary Search on Answer"
        ],
        "code": "#include <vector>\n#include <numeric>\n#include <algorithm>\nusing namespace std;\nclass Solution {\n    bool check(const vector<int>& weights, int cap, int days) {\n        int needed = 1, cur = 0;\n        for (int w : weights) {\n            if (cur + w > cap) {\n                needed++;\n                cur = 0;\n            }\n            cur += w;\n        }\n        return needed <= days;\n    }\npublic:\n    int shipWithinDays(vector<int>& weights, int days) {\n        int low = *max_element(weights.begin(), weights.end());\n        int high = accumulate(weights.begin(), weights.end(), 0);\n        int ans = high;\n        while (low <= high) {\n            int mid = low + (high - low) / 2;\n            if (check(weights, mid, days)) {\n                ans = mid;\n                high = mid - 1;\n            } else {\n                low = mid + 1;\n            }\n        }\n        return ans;\n    }\n};"
    },
    {
        "id": "tough_bs_on_answer_packages_java",
        "name": "Capacity to Ship Packages (Java Binary Search on Answer)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "binary_search_on_answer",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n log A)",
        "expected_sc": "O(1)",
        "expected_algorithms": [
            "Binary Search on Answer"
        ],
        "code": "class Solution {\n    boolean check(int[] weights, int cap, int days) {\n        int needed = 1, cur = 0;\n        for (int w : weights) {\n            if (cur + w > cap) {\n                needed++;\n                cur = 0;\n            }\n            cur += w;\n        }\n        return needed <= days;\n    }\n    public int shipWithinDays(int[] weights, int days) {\n        int low = 0, high = 0;\n        for (int w : weights) {\n            low = Math.max(low, w);\n            high += w;\n        }\n        int ans = high;\n        while (low <= high) {\n            int mid = low + (high - low) / 2;\n            if (check(weights, mid, days)) {\n                ans = mid;\n                high = mid - 1;\n            } else {\n                low = mid + 1;\n            }\n        }\n        return ans;\n    }\n}"
    },
    {
        "id": "tough_sliding_window_min_sub_cpp",
        "name": "Minimum Window Substring (C++ Sliding Window)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "sliding_window",
            "two_pointers",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(1)",
        "expected_algorithms": [
            "Sliding Window"
        ],
        "code": "#include <string>\n#include <vector>\nusing namespace std;\nclass Solution {\npublic:\n    string minWindow(string s, string t) {\n        vector<int> target(128, 0);\n        for (char c : t) target[c]++;\n        int required = t.size();\n        int left = 0, right = 0;\n        int min_len = 1e9, start_idx = 0;\n        while (right < s.size()) {\n            if (target[s[right]] > 0) required--;\n            target[s[right]]--;\n            right++;\n            while (required == 0) {\n                if (right - left < min_len) {\n                    min_len = right - left;\n                    start_idx = left;\n                }\n                target[s[left]]++;\n                if (target[s[left]] > 0) required++;\n                left++;\n            }\n        }\n        return min_len == 1e9 ? \"\" : s.substr(start_idx, min_len);\n    }\n};"
    },
    {
        "id": "tough_sliding_window_min_sub_java",
        "name": "Minimum Window Substring (Java Sliding Window)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "sliding_window",
            "two_pointers",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(1)",
        "expected_algorithms": [
            "Sliding Window"
        ],
        "code": "class Solution {\n    public String minWindow(String s, String t) {\n        int[] target = new int[128];\n        for (char c : t.toCharArray()) target[c]++;\n        int required = t.length();\n        int left = 0, right = 0;\n        int minLen = 1000000000, startIdx = 0;\n        while (right < s.length()) {\n            char c = s.charAt(right);\n            if (target[c] > 0) required--;\n            target[c]++;\n            right++;\n            while (required == 0) {\n                if (right - left < minLen) {\n                    minLen = right - left;\n                    startIdx = left;\n                }\n                char lc = s.charAt(left);\n                target[lc]++;\n                if (target[lc] > 0) required++;\n                left++;\n            }\n        }\n        return minLen == 1000000000 ? \"\" : s.substring(startIdx, startIdx + minLen);\n    }\n}"
    },
    {
        "id": "tough_tree_dp_max_path_cpp",
        "name": "Binary Tree Maximum Path Sum (C++ Tree DP)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "tree",
            "tree_dp",
            "dfs",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Tree DP"
        ],
        "code": "#include <algorithm>\nusing namespace std;\nstruct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n};\nclass Solution {\n    int max_sum = -1e9;\n    int dfs(TreeNode* root) {\n        if (!root) return 0;\n        int left_gain = max(dfs(root->left), 0);\n        int right_gain = max(dfs(root->right), 0);\n        int price_newpath = root->val + left_gain + right_gain;\n        max_sum = max(max_sum, price_newpath);\n        return root->val + max(left_gain, right_gain);\n    }\npublic:\n    int maxPathSum(TreeNode* root) {\n        dfs(root);\n        return max_sum;\n    }\n};"
    },
    {
        "id": "tough_tree_dp_max_path_java",
        "name": "Binary Tree Maximum Path Sum (Java Tree DP)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "tree",
            "tree_dp",
            "dfs",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Tree DP"
        ],
        "code": "class TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n}\nclass Solution {\n    int maxSum = -1000000000;\n    int dfs(TreeNode root) {\n        if (root == null) return 0;\n        int leftGain = Math.max(dfs(root.left), 0);\n        int rightGain = Math.max(dfs(root.right), 0);\n        int pathSum = root.val + leftGain + rightGain;\n        maxSum = Math.max(maxSum, pathSum);\n        return root.val + Math.max(leftGain, rightGain);\n    }\n    public int maxPathSum(TreeNode root) {\n        dfs(root);\n        return maxSum;\n    }\n}"
    },
    {
        "id": "tough_binary_lifting_lca_cpp",
        "name": "Tree Ancestor Binary Lifting (C++)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "tree",
            "binary_lifting",
            "lca",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n log n + q log n)",
        "expected_sc": "O(n log n)",
        "expected_algorithms": [
            "Binary Lifting"
        ],
        "code": "#include <vector>\nusing namespace std;\nclass TreeAncestor {\n    vector<vector<int>> up;\npublic:\n    TreeAncestor(int n, vector<int>& parent) {\n        up.assign(n, vector<int>(20, -1));\n        for (int i = 0; i < n; i++) {\n            up[i][0] = parent[i];\n        }\n        for (int j = 1; j < 20; j++) {\n            for (int i = 0; i < n; i++) {\n                if (up[i][j - 1] != -1) {\n                    up[i][j] = up[up[i][j - 1]][j - 1];\n                }\n            }\n        }\n    }\n    int getKthAncestor(int node, int k) {\n        for (int j = 0; j < 20; j++) {\n            if ((k >> j) & 1) {\n                node = up[node][j];\n                if (node == -1) break;\n            }\n        }\n        return node;\n    }\n};"
    },
    {
        "id": "tough_binary_lifting_lca_java",
        "name": "Tree Ancestor Binary Lifting (Java)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "tree",
            "binary_lifting",
            "lca",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n log n + q log n)",
        "expected_sc": "O(n log n)",
        "expected_algorithms": [
            "Binary Lifting"
        ],
        "code": "class TreeAncestor {\n    int[][] up;\n    public TreeAncestor(int n, int[] parent) {\n        up = new int[n][20];\n        for (int i = 0; i < n; i++) {\n            up[i][0] = parent[i];\n        }\n        for (int j = 1; j < 20; j++) {\n            for (int i = 0; i < n; i++) {\n                if (up[i][j - 1] != -1) {\n                    up[i][j] = up[up[i][j - 1]][j - 1];\n                } else {\n                    up[i][j] = -1;\n                }\n            }\n        }\n    }\n    public int getKthAncestor(int node, int k) {\n        for (int j = 0; j < 20; j++) {\n            if (((k >> j) & 1) == 1) {\n                node = up[node][j];\n                if (node == -1) break;\n            }\n        }\n        return node;\n    }\n}"
    },
    {
        "id": "tough_2d_dp_edit_distance_cpp",
        "name": "Edit Distance (C++ 2D DP)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "dp",
            "two_d_dp",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n m)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\nclass Solution {\npublic:\n    int minDistance(string word1, string word2) {\n        int m = word1.size(), n = word2.size();\n        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));\n        for (int i = 0; i <= m; i++) dp[i][0] = i;\n        for (int j = 0; j <= n; j++) dp[0][j] = j;\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (word1[i - 1] == word2[j - 1]) {\n                    dp[i][j] = dp[i - 1][j - 1];\n                } else {\n                    dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});\n                }\n            }\n        }\n        return dp[m][n];\n    }\n};"
    },
    {
        "id": "tough_2d_dp_edit_distance_java",
        "name": "Edit Distance (Java 2D DP)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "dp",
            "two_d_dp",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n m)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "class Solution {\n    public int minDistance(String word1, String word2) {\n        int m = word1.length(), n = word2.length();\n        int[][] dp = new int[m + 1][n + 1];\n        for (int i = 0; i <= m; i++) dp[i][0] = i;\n        for (int j = 0; j <= n; j++) dp[0][j] = j;\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {\n                    dp[i][j] = dp[i - 1][j - 1];\n                } else {\n                    dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1]));\n                }\n            }\n        }\n        return dp[m][n];\n    }\n}"
    },
    {
        "id": "tough_bitmask_dp_tsp_cpp",
        "name": "Traveling Salesperson Problem (C++ Bitmask DP)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "dp",
            "bitmask_dp",
            "hard",
            "cf"
        ],
        "expected_tc": "O(2^n * n)",
        "expected_sc": "O(2^n * n)",
        "expected_algorithms": [
            "Bitmask DP"
        ],
        "code": "#include <vector>\n#include <algorithm>\nusing namespace std;\nclass Solution {\npublic:\n    int shortestPathLength(vector<vector<int>>& dist, int n) {\n        vector<vector<int>> dp(1 << n, vector<int>(n, 1e9));\n        for (int i = 0; i < n; i++) dp[1 << i][i] = 0;\n        for (int mask = 1; mask < (1 << n); mask++) {\n            for (int u = 0; u < n; u++) {\n                if (!(mask & (1 << u))) continue;\n                for (int v = 0; v < n; v++) {\n                    if (mask & (1 << v)) continue;\n                    int next_mask = mask | (1 << v);\n                    dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + dist[u][v]);\n                }\n            }\n        }\n        int ans = 1e9;\n        for (int u = 0; u < n; u++) ans = min(ans, dp[(1 << n) - 1][u]);\n        return ans;\n    }\n};"
    },
    {
        "id": "tough_bitmask_dp_tsp_java",
        "name": "Traveling Salesperson Problem (Java Bitmask DP)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "dp",
            "bitmask_dp",
            "hard",
            "cf"
        ],
        "expected_tc": "O(2^n * n)",
        "expected_sc": "O(2^n * n)",
        "expected_algorithms": [
            "Bitmask DP"
        ],
        "code": "import java.util.*;\nclass Solution {\n    public int shortestPathLength(int[][] dist, int n) {\n        int[][] dp = new int[1 << n][n];\n        for (int i = 0; i < (1 << n); i++) Arrays.fill(dp[i], 1000000000);\n        for (int i = 0; i < n; i++) dp[1 << i][i] = 0;\n        for (int mask = 1; mask < (1 << n); mask++) {\n            for (int u = 0; u < n; u++) {\n                if ((mask & (1 << u)) == 0) continue;\n                for (int v = 0; v < n; v++) {\n                    if ((mask & (1 << v)) != 0) continue;\n                    int nextMask = mask | (1 << v);\n                    dp[nextMask][v] = Math.min(dp[nextMask][v], dp[mask][u] + dist[u][v]);\n                }\n            }\n        }\n        int ans = 1000000000;\n        for (int u = 0; u < n; u++) ans = Math.min(ans, dp[(1 << n) - 1][u]);\n        return ans;\n    }\n}"
    },
    {
        "id": "tough_kmp_search_cpp",
        "name": "KMP Pattern Matcher (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "string",
            "kmp",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n + m)",
        "expected_sc": "O(m)",
        "expected_algorithms": [
            "KMP"
        ],
        "code": "#include <string>\n#include <vector>\nusing namespace std;\nclass Solution {\npublic:\n    int strStr(string haystack, string needle) {\n        int m = needle.size(), n = haystack.size();\n        if (m == 0) return 0;\n        vector<int> pi(m, 0);\n        for (int i = 1, j = 0; i < m; i++) {\n            while (j > 0 && needle[i] != needle[j]) j = pi[j - 1];\n            if (needle[i] == needle[j]) j++;\n            pi[i] = j;\n        }\n        for (int i = 0, j = 0; i < n; i++) {\n            while (j > 0 && haystack[i] != needle[j]) j = pi[j - 1];\n            if (haystack[i] == needle[j]) j++;\n            if (j == m) return i - m + 1;\n        }\n        return -1;\n    }\n};"
    },
    {
        "id": "tough_kmp_search_java",
        "name": "KMP Pattern Matcher (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "string",
            "kmp",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n + m)",
        "expected_sc": "O(m)",
        "expected_algorithms": [
            "KMP"
        ],
        "code": "class Solution {\n    public int strStr(String haystack, String needle) {\n        int m = needle.length(), n = haystack.length();\n        if (m == 0) return 0;\n        int[] pi = new int[m];\n        for (int i = 1, j = 0; i < m; i++) {\n            while (j > 0 && needle.charAt(i) != needle.charAt(j)) j = pi[j - 1];\n            if (needle.charAt(i) == needle.charAt(j)) j++;\n            pi[i] = j;\n        }\n        for (int i = 0, j = 0; i < n; i++) {\n            while (j > 0 && haystack.charAt(i) != needle.charAt(j)) j = pi[j - 1];\n            if (haystack.charAt(i) == needle.charAt(j)) j++;\n            if (j == m) return i - m + 1;\n        }\n        return -1;\n    }\n}"
    },
    {
        "id": "tough_trie_prefix_tree_cpp",
        "name": "Implement Trie Prefix Tree (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "data_structure",
            "trie",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Trie"
        ],
        "code": "#include <string>\n#include <vector>\nusing namespace std;\nclass Trie {\n    struct Node {\n        Node* child[26] = {nullptr};\n        bool is_word = false;\n    };\n    Node* root;\npublic:\n    Trie() { root = new Node(); }\n    void insert(string word) {\n        Node* curr = root;\n        for (char c : word) {\n            int idx = c - 'a';\n            if (!curr->child[idx]) curr->child[idx] = new Node();\n            curr = curr->child[idx];\n        }\n        curr->is_word = true;\n    }\n    bool search(string word) {\n        Node* curr = root;\n        for (char c : word) {\n            int idx = c - 'a';\n            if (!curr->child[idx]) return false;\n            curr = curr->child[idx];\n        }\n        return curr->is_word;\n    }\n};"
    },
    {
        "id": "tough_trie_prefix_tree_java",
        "name": "Implement Trie Prefix Tree (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "data_structure",
            "trie",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Trie"
        ],
        "code": "class Trie {\n    static class Node {\n        Node[] child = new Node[26];\n        bool isWord = false;\n    }\n    Node root;\n    public Trie() { root = new Node(); }\n    public void insert(String word) {\n        Node curr = root;\n        for (char c : word.toCharArray()) {\n            int idx = c - 'a';\n            if (curr.child[idx] == null) curr.child[idx] = new Node();\n            curr = curr.child[idx];\n        }\n        curr.isWord = true;\n    }\n    public boolean search(String word) {\n        Node curr = root;\n        for (char c : word.toCharArray()) {\n            int idx = c - 'a';\n            if (curr.child[idx] == null) return false;\n            curr = curr.child[idx];\n        }\n        return curr.isWord;\n    }\n}"
    },
    {
        "id": "tough_sieve_primes_cpp",
        "name": "Count Primes Sieve of Eratosthenes (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "math",
            "sieve",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n log log n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Sieve"
        ],
        "code": "#include <vector>\nusing namespace std;\nclass Solution {\npublic:\n    int countPrimes(int n) {\n        if (n <= 2) return 0;\n        vector<bool> is_prime(n, true);\n        is_prime[0] = is_prime[1] = false;\n        for (int p = 2; p * p < n; p++) {\n            if (is_prime[p]) {\n                for (int i = p * p; i < n; i += p) {\n                    is_prime[i] = false;\n                }\n            }\n        }\n        int count = 0;\n        for (int i = 2; i < n; i++) {\n            if (is_prime[i]) count++;\n        }\n        return count;\n    }\n};"
    },
    {
        "id": "tough_sieve_primes_java",
        "name": "Count Primes Sieve of Eratosthenes (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "math",
            "sieve",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n log log n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Sieve"
        ],
        "code": "import java.util.*;\nclass Solution {\n    public int countPrimes(int n) {\n        if (n <= 2) return 0;\n        boolean[] isPrime = new boolean[n];\n        Arrays.fill(isPrime, true);\n        isPrime[0] = isPrime[1] = false;\n        for (int p = 2; p * p < n; p++) {\n            if (isPrime[p]) {\n                for (int i = p * p; i < n; i += p) {\n                    isPrime[i] = false;\n                }\n            }\n        }\n        int count = 0;\n        for (int i = 2; i < n; i++) {\n            if (isPrime[i]) count++;\n        }\n        return count;\n    }\n}"
    },
    {
        "id": "tough_z_algorithm_cpp",
        "name": "Z-Algorithm String Matching (C++)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "string",
            "z_algorithm",
            "hard",
            "cf"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Z Algorithm"
        ],
        "code": "#include <string>\n#include <vector>\nusing namespace std;\nvector<int> z_function(string s) {\n    int n = s.length();\n    vector<int> z(n, 0);\n    int l = 0, r = 0;\n    for (int i = 1; i < n; i++) {\n        if (i <= r) z[i] = min(r - i + 1, z[i - l]);\n        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;\n        if (i + z[i] - 1 > r) {\n            l = i;\n            r = i + z[i] - 1;\n        }\n    }\n    return z;\n}"
    },
    {
        "id": "tough_z_algorithm_java",
        "name": "Z-Algorithm String Matching (Java)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "string",
            "z_algorithm",
            "hard",
            "cf"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Z Algorithm"
        ],
        "code": "class Solution {\n    public int[] zFunction(String s) {\n        int n = s.length();\n        int[] z = new int[n];\n        int l = 0, r = 0;\n        for (int i = 1; i < n; i++) {\n            if (i <= r) z[i] = Math.min(r - i + 1, z[i - l]);\n            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i])) z[i]++;\n            if (i + z[i] - 1 > r) {\n                l = i;\n                r = i + z[i] - 1;\n            }\n        }\n        return z;\n    }\n}"
    },
    {
        "id": "tough_rolling_hash_cpp",
        "name": "Rabin-Karp Rolling Hash (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "string",
            "rolling_hash",
            "medium",
            "cf"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Rolling Hash"
        ],
        "code": "#include <string>\nusing namespace std;\nclass Solution {\npublic:\n    int rabinKarp(string s, string p) {\n        long long mod = 1e9 + 7, base = 31;\n        long long p_hash = 0, s_hash = 0, power = 1;\n        int m = p.size(), n = s.size();\n        for (int i = 0; i < m; i++) {\n            p_hash = (p_hash * base + p[i]) % mod;\n            s_hash = (s_hash * base + s[i]) % mod;\n            if (i > 0) power = (power * base) % mod;\n        }\n        for (int i = 0; i <= n - m; i++) {\n            if (p_hash == s_hash && s.substr(i, m) == p) return i;\n            if (i < n - m) {\n                s_hash = ((s_hash - s[i] * power % mod + mod) * base + s[i + m]) % mod;\n            }\n        }\n        return -1;\n    }\n};"
    },
    {
        "id": "tough_rolling_hash_java",
        "name": "Rabin-Karp Rolling Hash (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "string",
            "rolling_hash",
            "medium",
            "cf"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Rolling Hash"
        ],
        "code": "class Solution {\n    public int rabinKarp(String s, String p) {\n        long mod = 1000000007, base = 31;\n        long pHash = 0, sHash = 0, power = 1;\n        int m = p.length(), n = s.length();\n        for (int i = 0; i < m; i++) {\n            pHash = (pHash * base + p.charAt(i)) % mod;\n            sHash = (sHash * base + s.charAt(i)) % mod;\n            if (i > 0) power = (power * base) % mod;\n        }\n        for (int i = 0; i <= n - m; i++) {\n            if (pHash == sHash && s.substring(i, i + m).equals(p)) return i;\n            if (i < n - m) {\n                sHash = ((sHash - s.charAt(i) * power % mod + mod) * base + s.charAt(i + m)) % mod;\n            }\n        }\n        return -1;\n    }\n}"
    },
    {
        "id": "tough_sparse_table_rmq_cpp",
        "name": "Sparse Table Range Minimum Query (C++)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "data_structure",
            "sparse_table",
            "hard",
            "cf"
        ],
        "expected_tc": "O(n log n + q)",
        "expected_sc": "O(n log n)",
        "expected_algorithms": [
            "Sparse Table"
        ],
        "code": "#include <vector>\n#include <algorithm>\nusing namespace std;\nstruct SparseTable {\n    vector<vector<int>> st;\n    vector<int> lg;\n    SparseTable(const vector<int>& a) {\n        int n = a.size();\n        lg.assign(n + 1, 0);\n        for (int i = 2; i <= n; i++) lg[i] = lg[i / 2] + 1;\n        int k = lg[n] + 1;\n        st.assign(n, vector<int>(k));\n        for (int i = 0; i < n; i++) st[i][0] = a[i];\n        for (int j = 1; j < k; j++) {\n            for (int i = 0; i + (1 << j) <= n; i++) {\n                st[i][j] = min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);\n            }\n        }\n    }\n    int query(int L, int R) {\n        int j = lg[R - L + 1];\n        return min(st[L][j], st[R - (1 << j) + 1][j]);\n    }\n};"
    },
    {
        "id": "tough_sparse_table_rmq_java",
        "name": "Sparse Table Range Minimum Query (Java)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "data_structure",
            "sparse_table",
            "hard",
            "cf"
        ],
        "expected_tc": "O(n log n + q)",
        "expected_sc": "O(n log n)",
        "expected_algorithms": [
            "Sparse Table"
        ],
        "code": "class SparseTable {\n    int[][] st;\n    int[] lg;\n    SparseTable(int[] a) {\n        int n = a.length;\n        lg = new int[n + 1];\n        for (int i = 2; i <= n; i++) lg[i] = lg[i / 2] + 1;\n        int k = lg[n] + 1;\n        st = new int[n][k];\n        for (int i = 0; i < n; i++) st[i][0] = a[i];\n        for (int j = 1; j < k; j++) {\n            for (int i = 0; i + (1 << j) <= n; i++) {\n                st[i][j] = Math.min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);\n            }\n        }\n    }\n    int query(int L, int R) {\n        int j = lg[R - L + 1];\n        return Math.min(st[L][j], st[R - (1 << j) + 1][j]);\n    }\n}"
    },
    {
        "id": "tough_kadane_max_sub_cpp",
        "name": "Maximum Subarray (C++ Kadane)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "kadanes_algorithm",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(1)",
        "expected_algorithms": [
            "Kadane's Algorithm"
        ],
        "code": "#include <vector>\n#include <algorithm>\nusing namespace std;\nclass Solution {\npublic:\n    int maxSubArray(vector<int>& nums) {\n        int max_so_far = nums[0];\n        int curr_max = nums[0];\n        for (size_t i = 1; i < nums.size(); ++i) {\n            curr_max = max(nums[i], curr_max + nums[i]);\n            max_so_far = max(max_so_far, curr_max);\n        }\n        return max_so_far;\n    }\n};"
    },
    {
        "id": "tough_kadane_max_sub_java",
        "name": "Maximum Subarray (Java Kadane)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "kadanes_algorithm",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(1)",
        "expected_algorithms": [
            "Kadane's Algorithm"
        ],
        "code": "class Solution {\n    public int maxSubArray(int[] nums) {\n        int max_so_far = nums[0];\n        int curr_max = nums[0];\n        for (int i = 1; i < nums.length; ++i) {\n            curr_max = Math.max(nums[i], curr_max + nums[i]);\n            max_so_far = Math.max(max_so_far, curr_max);\n        }\n        return max_so_far;\n    }\n}"
    },
    {
        "id": "tough_grid_bfs_rotting_oranges_cpp",
        "name": "Rotting Oranges Multi-source BFS (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "graph",
            "bfs",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(V + E)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "BFS"
        ],
        "code": "#include <vector>\n#include <queue>\nusing namespace std;\nclass Solution {\npublic:\n    int orangesRotting(vector<vector<int>>& grid) {\n        int m = grid.size(), n = grid[0].size();\n        queue<pair<int, int>> q;\n        int fresh = 0;\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (grid[i][j] == 2) q.push({i, j});\n                else if (grid[i][j] == 1) fresh++;\n            }\n        }\n        int minutes = 0;\n        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};\n        while (!q.empty() && fresh > 0) {\n            int sz = q.size();\n            for (int k = 0; k < sz; k++) {\n                auto [r, c] = q.front();\n                q.pop();\n                for (auto& d : dirs) {\n                    int nr = r + d[0], nc = c + d[1];\n                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {\n                        grid[nr][nc] = 2;\n                        fresh--;\n                        q.push({nr, nc});\n                    }\n                }\n            }\n            minutes++;\n        }\n        return fresh == 0 ? minutes : -1;\n    }\n};"
    },
    {
        "id": "tough_grid_bfs_rotting_oranges_java",
        "name": "Rotting Oranges Multi-source BFS (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "graph",
            "bfs",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(V + E)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "BFS"
        ],
        "code": "import java.util.*;\nclass Solution {\n    public int orangesRotting(int[][] grid) {\n        int m = grid.length, n = grid[0].length;\n        Queue<int[]> q = new LinkedList<>();\n        int fresh = 0;\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (grid[i][j] == 2) q.add(new int[]{i, j});\n                else if (grid[i][j] == 1) fresh++;\n            }\n        }\n        int minutes = 0;\n        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};\n        while (!q.isEmpty() && fresh > 0) {\n            int sz = q.size();\n            for (int k = 0; k < sz; k++) {\n                int[] cur = q.poll();\n                int r = cur[0], c = cur[1];\n                for (int[] d : dirs) {\n                    int nr = r + d[0], nc = c + d[1];\n                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {\n                        grid[nr][nc] = 2;\n                        fresh--;\n                        q.add(new int[]{nr, nc});\n                    }\n                }\n            }\n            minutes++;\n        }\n        return fresh == 0 ? minutes : -1;\n    }\n}"
    },
    {
        "id": "tough_bulb_switcher_sim_java",
        "name": "Bulb Switcher II State Simulation (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "simulation",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(k)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "import java.util.*;\nclass Solution {\n    public int flipLights(int n, int k) {\n        n = Math.min(6, n);\n        Set<String> set = new HashSet<>();\n        set.add(\"1\".repeat(n));\n        for(int i = 0; i < k; ++i){\n            Set<String> temp = new HashSet<>();\n            for(String s: set){\n                StringBuilder x = new StringBuilder(s);\n                for(int j = 0; j < n; ++j){\n                    if(x.charAt(j) == '0') x.setCharAt(j, '1');\n                    else x.setCharAt(j, '0');\n                }\n                temp.add(x.toString());\n                x = new StringBuilder(s);\n                for(int j = 0; j < n; j += 2){\n                    if(x.charAt(j) == '0') x.setCharAt(j, '1');\n                    else x.setCharAt(j, '0');\n                }\n                temp.add(x.toString());\n            }\n            set = temp;\n        }\n        return set.size();\n    }\n}"
    },
    {
        "id": "tough_bulb_switcher_sim_cpp",
        "name": "Bulb Switcher II State Simulation (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "simulation",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(k)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "#include <string>\n#include <unordered_set>\n#include <algorithm>\nusing namespace std;\nclass Solution {\npublic:\n    int flipLights(int n, int k) {\n        n = min(6, n);\n        unordered_set<string> states;\n        states.insert(string(n, '1'));\n        for (int i = 0; i < k; ++i) {\n            unordered_set<string> temp;\n            for (const string& s : states) {\n                string x = s;\n                for (int j = 0; j < n; ++j) {\n                    x[j] = (x[j] == '0' ? '1' : '0');\n                }\n                temp.insert(x);\n                x = s;\n                for (int j = 0; j < n; j += 2) {\n                    x[j] = (x[j] == '0' ? '1' : '0');\n                }\n                temp.insert(x);\n            }\n            states = temp;\n        }\n        return states.size();\n    }\n};"
    },
    {
        "id": "tough_harmonic_divisor_sieve_cpp",
        "name": "Sum of Divisors Harmonic Loop (C++)",
        "language": "cpp",
        "rating": "1600",
        "tags": [
            "math",
            "cf",
            "1600"
        ],
        "expected_tc": "O(n log n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "#include <iostream>\n#include <vector>\nusing namespace std;\nint main() {\n    int n;\n    if (!(cin >> n)) return 0;\n    vector<long long> div_sum(n + 1, 0);\n    for (int i = 1; i <= n; i++) {\n        for (int j = i; j <= n; j += i) {\n            div_sum[j] += i;\n        }\n    }\n    long long total = 0;\n    for (int i = 1; i <= n; i++) total += div_sum[i];\n    cout << total << \"\\n\";\n    return 0;\n}"
    },
    {
        "id": "tough_harmonic_divisor_sieve_java",
        "name": "Sum of Divisors Harmonic Loop (Java)",
        "language": "java",
        "rating": "1600",
        "tags": [
            "math",
            "cf",
            "1600"
        ],
        "expected_tc": "O(n log n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "import java.util.Scanner;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            long[] divSum = new long[n + 1];\n            for (int i = 1; i <= n; i++) {\n                for (int j = i; j <= n; j += i) {\n                    divSum[j] += i;\n                }\n            }\n            long total = 0;\n            for (int i = 1; i <= n; i++) total += divSum[i];\n            System.out.println(total);\n        }\n    }\n}"
    },
    {
        "id": "tough_2d_prefix_sum_cpp",
        "name": "2D Prefix Sum Matrix (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "prefix_sum",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Prefix Sum"
        ],
        "code": "#include <vector>\nusing namespace std;\nclass NumMatrix {\n    vector<vector<int>> pref;\npublic:\n    NumMatrix(vector<vector<int>>& matrix) {\n        int m = matrix.size(), n = matrix[0].size();\n        pref.assign(m + 1, vector<int>(n + 1, 0));\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                pref[i + 1][j + 1] = matrix[i][j] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j];\n            }\n        }\n    }\n    int sumRegion(int row1, int col1, int row2, int col2) {\n        return pref[row2 + 1][col2 + 1] - pref[row1][col2 + 1] - pref[row2 + 1][col1] + pref[row1][col1];\n    }\n};"
    },
    {
        "id": "tough_2d_prefix_sum_java",
        "name": "2D Prefix Sum Matrix (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "prefix_sum",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Prefix Sum"
        ],
        "code": "class NumMatrix {\n    int[][] pref;\n    public NumMatrix(int[][] matrix) {\n        int m = matrix.length, n = matrix[0].length;\n        pref = new int[m + 1][n + 1];\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                pref[i + 1][j + 1] = matrix[i][j] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j];\n            }\n        }\n    }\n    public int sumRegion(int row1, int col1, int row2, int col2) {\n        return pref[row2 + 1][col2 + 1] - pref[row1][col2 + 1] - pref[row2 + 1][col1] + pref[row1][col1];\n    }\n}"
    },
    {
        "id": "tough_3sum_two_pointers_cpp",
        "name": "3Sum (C++ Two Pointers + Sorting)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "two_pointers",
            "sorting",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n^2)",
        "expected_sc": "O(1)",
        "expected_algorithms": [
            "Two Pointers"
        ],
        "code": "#include <vector>\n#include <algorithm>\nusing namespace std;\nclass Solution {\npublic:\n    vector<vector<int>> threeSum(vector<int>& nums) {\n        sort(nums.begin(), nums.end());\n        int n = nums.size();\n        vector<vector<int>> res;\n        for (int i = 0; i < n; i++) {\n            if (i > 0 && nums[i] == nums[i - 1]) continue;\n            int l = i + 1, r = n - 1;\n            while (l < r) {\n                int sum = nums[i] + nums[l] + nums[r];\n                if (sum == 0) {\n                    res.push_back({nums[i], nums[l], nums[r]});\n                    while (l < r && nums[l] == nums[l + 1]) l++;\n                    while (l < r && nums[r] == nums[r - 1]) r--;\n                    l++;\n                    r--;\n                } else if (sum < 0) {\n                    l++;\n                } else {\n                    r--;\n                }\n            }\n        }\n        return res;\n    }\n};"
    },
    {
        "id": "tough_3sum_two_pointers_java",
        "name": "3Sum (Java Two Pointers + Sorting)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "two_pointers",
            "sorting",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n^2)",
        "expected_sc": "O(1)",
        "expected_algorithms": [
            "Two Pointers"
        ],
        "code": "import java.util.*;\nclass Solution {\n    public List<List<Integer>> threeSum(int[] nums) {\n        Arrays.sort(nums);\n        int n = nums.length;\n        List<List<Integer>> res = new ArrayList<>();\n        for (int i = 0; i < n; i++) {\n            if (i > 0 && nums[i] == nums[i - 1]) continue;\n            int l = i + 1, r = n - 1;\n            while (l < r) {\n                int sum = nums[i] + nums[l] + nums[r];\n                if (sum == 0) {\n                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));\n                    while (l < r && nums[l] == nums[l + 1]) l++;\n                    while (l < r && nums[r] == nums[r - 1]) r--;\n                    l++;\n                    r--;\n                } else if (sum < 0) {\n                    l++;\n                } else {\n                    r--;\n                }\n            }\n        }\n        return res;\n    }\n}"
    },
    {
        "id": "tough_bs_rotated_sorted_cpp",
        "name": "Search in Rotated Sorted Array (C++ Binary Search)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "binary_search",
            "leetcode",
            "medium"
        ],
        "code": "#include <vector>\nusing namespace std;\nclass Solution {\npublic:\n    int search(vector<int>& nums, int target) {\n        int left = 0, right = (int)nums.size() - 1;\n        while (left <= right) {\n            int mid = left + (right - left) / 2;\n            if (nums[mid] == target) return mid;\n            if (nums[left] <= nums[mid]) {\n                if (nums[left] <= target && target < nums[mid]) right = mid - 1;\n                else left = mid + 1;\n            } else {\n                if (nums[mid] < target && target <= nums[right]) left = mid + 1;\n                else right = mid - 1;\n            }\n        }\n        return -1;\n    }\n};",
        "expected_tc": "O(log n)",
        "expected_sc": "O(1)",
        "expected_algorithms": [
            "Binary Search"
        ]
    },
    {
        "id": "tough_bs_rotated_sorted_java",
        "name": "Search in Rotated Sorted Array (Java Binary Search)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "binary_search",
            "leetcode",
            "medium"
        ],
        "code": "class Solution {\n    public int search(int[] nums, int target) {\n        int left = 0, right = nums.length - 1;\n        while (left <= right) {\n            int mid = left + (right - left) / 2;\n            if (nums[mid] == target) return mid;\n            if (nums[left] <= nums[mid]) {\n                if (nums[left] <= target && target < nums[mid]) right = mid - 1;\n                else left = mid + 1;\n            } else {\n                if (nums[mid] < target && target <= nums[right]) left = mid + 1;\n                else right = mid - 1;\n            }\n        }\n        return -1;\n    }\n}",
        "expected_tc": "O(log n)",
        "expected_sc": "O(1)",
        "expected_algorithms": [
            "Binary Search"
        ]
    },
    {
        "id": "tough_zero_one_bfs_cpp",
        "name": "0-1 BFS Shortest Path (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "graph",
            "bfs",
            "medium",
            "leetcode"
        ],
        "code": "#include <vector>\n#include <deque>\nusing namespace std;\nclass Solution {\npublic:\n    int minCost(vector<vector<pair<int, int>>>& adj, int n, int src, int dst) {\n        vector<int> dist(n, 1e9);\n        deque<int> dq;\n        dist[src] = 0;\n        dq.push_back(src);\n        while (!dq.empty()) {\n            int u = dq.front();\n            dq.pop_front();\n            for (auto& edge : adj[u]) {\n                int v = edge.first, w = edge.second;\n                if (dist[u] + w < dist[v]) {\n                    dist[v] = dist[u] + w;\n                    if (w == 1) dq.push_back(v);\n                    else dq.push_front(v);\n                }\n            }\n        }\n        return dist[dst] == 1e9 ? -1 : dist[dst];\n    }\n};",
        "expected_tc": "O(V + E)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "BFS"
        ]
    },
    {
        "id": "tough_zero_one_bfs_java",
        "name": "0-1 BFS Shortest Path (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "graph",
            "bfs",
            "medium",
            "leetcode"
        ],
        "code": "import java.util.*;\nclass Solution {\n    public int minCost(List<List<int[]>> adj, int n, int src, int dst) {\n        int[] dist = new int[n];\n        Arrays.fill(dist, 1000000000);\n        Deque<Integer> dq = new ArrayDeque<>();\n        dist[src] = 0;\n        dq.addLast(src);\n        while (!dq.isEmpty()) {\n            int u = dq.pollFirst();\n            for (int[] edge : adj.get(u)) {\n                int v = edge[0], w = edge[1];\n                if (dist[u] + w < dist[v]) {\n                    dist[v] = dist[u] + w;\n                    if (w == 1) dq.addLast(v);\n                    else dq.addFirst(v);\n                }\n            }\n        }\n        return dist[dst] == 1000000000 ? -1 : dist[dst];\n    }\n}",
        "expected_tc": "O(V + E)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "BFS"
        ]
    },
    {
        "id": "tough_tarjan_bridges_cpp",
        "name": "Tarjan Critical Connections (C++ DFS)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "graph",
            "dfs",
            "hard",
            "leetcode"
        ],
        "code": "#include <vector>\n#include <algorithm>\nusing namespace std;\nclass Solution {\n    int timer = 1;\n    void dfs(int u, int p, vector<vector<int>>& adj, vector<int>& tin, vector<int>& low, vector<vector<int>>& bridges) {\n        tin[u] = low[u] = timer++;\n        for (int v : adj[u]) {\n            if (v == p) continue;\n            if (tin[v]) {\n                low[u] = min(low[u], tin[v]);\n            } else {\n                dfs(v, u, adj, tin, low, bridges);\n                low[u] = min(low[u], low[v]);\n                if (low[v] > tin[u]) {\n                    bridges.push_back({u, v});\n                }\n            }\n        }\n    }\npublic:\n    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {\n        vector<vector<int>> adj(n);\n        for (auto& e : connections) {\n            adj[e[0]].push_back(e[1]);\n            adj[e[1]].push_back(e[0]);\n        }\n        vector<int> tin(n, 0), low(n, 0);\n        vector<vector<int>> bridges;\n        dfs(0, -1, adj, tin, low, bridges);\n        return bridges;\n    }\n};",
        "expected_tc": "O(V + E)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "DFS"
        ]
    },
    {
        "id": "tough_tarjan_bridges_java",
        "name": "Tarjan Critical Connections (Java DFS)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "graph",
            "dfs",
            "hard",
            "leetcode"
        ],
        "code": "import java.util.*;\nclass Solution {\n    int timer = 1;\n    void dfs(int u, int p, List<List<Integer>> adj, int[] tin, int[] low, List<List<Integer>> bridges) {\n        tin[u] = low[u] = timer++;\n        for (int v : adj.get(u)) {\n            if (v == p) continue;\n            if (tin[v] > 0) {\n                low[u] = Math.min(low[u], tin[v]);\n            } else {\n                dfs(v, u, adj, tin, low, bridges);\n                low[u] = Math.min(low[u], low[v]);\n                if (low[v] > tin[u]) {\n                    bridges.add(Arrays.asList(u, v));\n                }\n            }\n        }\n    }\n    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {\n        List<List<Integer>> adj = new ArrayList<>();\n        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());\n        for (List<Integer> e : connections) {\n            adj.get(e.get(0)).add(e.get(1));\n            adj.get(e.get(1)).add(e.get(0));\n        }\n        int[] tin = new int[n], low = new int[n];\n        List<List<Integer>> bridges = new ArrayList<>();\n        dfs(0, -1, adj, tin, low, bridges);\n        return bridges;\n    }\n}",
        "expected_tc": "O(V + E)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "DFS"
        ]
    },
    {
        "id": "tough_hierholzer_eulerian_cpp",
        "name": "Reconstruct Itinerary Eulerian Path (C++)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "graph",
            "dfs",
            "hard",
            "leetcode"
        ],
        "code": "#include <vector>\n#include <string>\n#include <unordered_map>\n#include <queue>\n#include <algorithm>\nusing namespace std;\nclass Solution {\n    unordered_map<string, priority_queue<string, vector<string>, greater<string>>> adj;\n    vector<string> route;\n    void dfs(string u) {\n        auto& pq = adj[u];\n        while (!pq.empty()) {\n            string v = pq.top();\n            pq.pop();\n            dfs(v);\n        }\n        route.push_back(u);\n    }\npublic:\n    vector<string> findItinerary(vector<vector<string>>& tickets) {\n        for (auto& t : tickets) adj[t[0]].push(t[1]);\n        dfs(\"JFK\");\n        reverse(route.begin(), route.end());\n        return route;\n    }\n};",
        "expected_tc": "O(V + E)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "DFS"
        ]
    },
    {
        "id": "tough_hierholzer_eulerian_java",
        "name": "Reconstruct Itinerary Eulerian Path (Java)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "graph",
            "dfs",
            "hard",
            "leetcode"
        ],
        "code": "import java.util.*;\nclass Solution {\n    Map<String, PriorityQueue<String>> adj = new HashMap<>();\n    List<String> route = new LinkedList<>();\n    void dfs(String u) {\n        PriorityQueue<String> pq = adj.get(u);\n        while (pq != null && !pq.isEmpty()) {\n            dfs(pq.poll());\n        }\n        route.add(0, u);\n    }\n    public List<String> findItinerary(List<List<String>> tickets) {\n        for (List<String> t : tickets) {\n            adj.computeIfAbsent(t.get(0), k -> new PriorityQueue<>()).add(t.get(1));\n        }\n        dfs(\"JFK\");\n        return route;\n    }\n}",
        "expected_tc": "O(V + E)",
        "expected_sc": "O(V + E)",
        "expected_algorithms": [
            "DFS"
        ]
    },
    {
        "id": "tough_brian_kernighan_bits_cpp",
        "name": "Counting Bits Brian Kernighan (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "bit_manipulation",
            "leetcode",
            "medium"
        ],
        "code": "#include <vector>\nusing namespace std;\nclass Solution {\npublic:\n    vector<int> countBits(int n) {\n        vector<int> ans(n + 1, 0);\n        for (int i = 1; i <= n; i++) {\n            ans[i] = ans[i & (i - 1)] + 1;\n        }\n        return ans;\n    }\n};",
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": []
    },
    {
        "id": "tough_brian_kernighan_bits_java",
        "name": "Counting Bits Brian Kernighan (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "bit_manipulation",
            "leetcode",
            "medium"
        ],
        "code": "class Solution {\n    public int[] countBits(int n) {\n        int[] ans = new int[n + 1];\n        for (int i = 1; i <= n; i++) {\n            ans[i] = ans[i & (i - 1)] + 1;\n        }\n        return ans;\n    }\n}",
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": []
    },
    {
        "id": "tough_binary_trie_xor_cpp",
        "name": "Maximum XOR of Two Numbers (C++ Binary Trie)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "trie",
            "bit_manipulation",
            "medium",
            "leetcode"
        ],
        "code": "#include <vector>\n#include <algorithm>\nusing namespace std;\nstruct TrieNode {\n    TrieNode* child[2] = {nullptr, nullptr};\n};\nclass Solution {\n    TrieNode* root = new TrieNode();\n    void insert(int num) {\n        TrieNode* cur = root;\n        for (int i = 31; i >= 0; i--) {\n            int bit = (num >> i) & 1;\n            if (!cur->child[bit]) cur->child[bit] = new TrieNode();\n            cur = cur->child[bit];\n        }\n    }\n    int query(int num) {\n        TrieNode* cur = root;\n        int max_xor = 0;\n        for (int i = 31; i >= 0; i--) {\n            int bit = (num >> i) & 1;\n            if (cur->child[1 - bit]) {\n                max_xor |= (1 << i);\n                cur = cur->child[1 - bit];\n            } else {\n                cur = cur->child[bit];\n            }\n        }\n        return max_xor;\n    }\npublic:\n    int findMaximumXOR(vector<int>& nums) {\n        for (int x : nums) insert(x);\n        int ans = 0;\n        for (int x : nums) ans = max(ans, query(x));\n        return ans;\n    }\n};",
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Trie"
        ]
    },
    {
        "id": "tough_binary_trie_xor_java",
        "name": "Maximum XOR of Two Numbers (Java Binary Trie)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "trie",
            "bit_manipulation",
            "medium",
            "leetcode"
        ],
        "code": "class Solution {\n    static class TrieNode {\n        TrieNode[] child = new TrieNode[2];\n    }\n    TrieNode root = new TrieNode();\n    void insert(int num) {\n        TrieNode cur = root;\n        for (int i = 31; i >= 0; i--) {\n            int bit = (num >> i) & 1;\n            if (cur.child[bit] == null) cur.child[bit] = new TrieNode();\n            cur = cur.child[bit];\n        }\n    }\n    int query(int num) {\n        TrieNode cur = root;\n        int max_xor = 0;\n        for (int i = 31; i >= 0; i--) {\n            int bit = (num >> i) & 1;\n            if (cur.child[1 - bit] != null) {\n                max_xor |= (1 << i);\n                cur = cur.child[1 - bit];\n            } else {\n                cur = cur.child[bit];\n            }\n        }\n        return max_xor;\n    }\n    public int findMaximumXOR(int[] nums) {\n        for (int x : nums) insert(x);\n        int ans = 0;\n        for (int x : nums) ans = Math.max(ans, query(x));\n        return ans;\n    }\n}",
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [
            "Trie"
        ]
    },
    {
        "id": "tough_fast_pow_gcd_cpp",
        "name": "Fast Modular Exponentiation & GCD (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "math",
            "leetcode",
            "medium"
        ],
        "code": "class Solution {\npublic:\n    long long modPow(long long base, long long exp, long long mod) {\n        long long res = 1;\n        base %= mod;\n        while (exp > 0) {\n            if (exp & 1) res = (res * base) % mod;\n            base = (base * base) % mod;\n            exp >>= 1;\n        }\n        return res;\n    }\n};",
        "expected_tc": "O(log n)",
        "expected_sc": "O(1)",
        "expected_algorithms": []
    },
    {
        "id": "tough_fast_pow_gcd_java",
        "name": "Fast Modular Exponentiation & GCD (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "math",
            "leetcode",
            "medium"
        ],
        "code": "class Solution {\n    public long modPow(long base, long exp, long mod) {\n        long res = 1;\n        base %= mod;\n        while (exp > 0) {\n            if ((exp & 1) == 1) res = (res * base) % mod;\n            base = (base * base) % mod;\n            exp >>= 1;\n        }\n        return res;\n    }\n}",
        "expected_tc": "O(log n)",
        "expected_sc": "O(1)",
        "expected_algorithms": []
    },
    {
        "id": "tough_diff_array_flights_cpp",
        "name": "Corporate Flight Bookings Difference Array (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "prefix_sum",
            "difference_array",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "#include <vector>\nusing namespace std;\nclass Solution {\npublic:\n    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {\n        vector<int> diff(n + 2, 0);\n        for (const auto& b : bookings) {\n            diff[b[0]] += b[2];\n            diff[b[1] + 1] -= b[2];\n        }\n        vector<int> ans(n);\n        int cur = 0;\n        for (int i = 1; i <= n; i++) {\n            cur += diff[i];\n            ans[i - 1] = cur;\n        }\n        return ans;\n    }\n};"
    },
    {
        "id": "tough_diff_array_flights_java",
        "name": "Corporate Flight Bookings Difference Array (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "prefix_sum",
            "difference_array",
            "leetcode",
            "medium"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "class Solution {\n    public int[] corpFlightBookings(int[][] bookings, int n) {\n        int[] diff = new int[n + 2];\n        for (int[] b : bookings) {\n            diff[b[0]] += b[2];\n            diff[b[1] + 1] -= b[2];\n        }\n        int[] ans = new int[n];\n        int cur = 0;\n        for (int i = 1; i <= n; i++) {\n            cur += diff[i];\n            ans[i - 1] = cur;\n        }\n        return ans;\n    }\n}"
    },
    {
        "id": "tough_interval_dp_balloons_cpp",
        "name": "Burst Balloons Interval DP (C++)",
        "language": "cpp",
        "rating": "Hard",
        "tags": [
            "dp",
            "interval_dp",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n^3)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "#include <vector>\n#include <algorithm>\nusing namespace std;\nclass Solution {\npublic:\n    int maxCoins(vector<int>& nums) {\n        int n = nums.size();\n        vector<int> val(n + 2, 1);\n        for (int i = 0; i < n; i++) val[i + 1] = nums[i];\n        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));\n        for (int len = 1; len <= n; len++) {\n            for (int i = 1; i <= n - len + 1; i++) {\n                int j = i + len - 1;\n                for (int k = i; k <= j; k++) {\n                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + val[i - 1] * val[k] * val[j + 1]);\n                }\n            }\n        }\n        return dp[1][n];\n    }\n};"
    },
    {
        "id": "tough_interval_dp_balloons_java",
        "name": "Burst Balloons Interval DP (Java)",
        "language": "java",
        "rating": "Hard",
        "tags": [
            "dp",
            "interval_dp",
            "hard",
            "leetcode"
        ],
        "expected_tc": "O(n^3)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "class Solution {\n    public int maxCoins(int[] nums) {\n        int n = nums.length;\n        int[] val = new int[n + 2];\n        val[0] = val[n + 1] = 1;\n        for (int i = 0; i < n; i++) val[i + 1] = nums[i];\n        int[][] dp = new int[n + 2][n + 2];\n        for (int len = 1; len <= n; len++) {\n            for (int i = 1; i <= n - len + 1; i++) {\n                int j = i + len - 1;\n                for (int k = i; k <= j; k++) {\n                    dp[i][j] = Math.max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + val[i - 1] * val[k] * val[j + 1]);\n                }\n            }\n        }\n        return dp[1][n];\n    }\n}"
    },
    {
        "id": "tough_floyd_warshall_cpp",
        "name": "Floyd-Warshall All-Pairs Shortest Paths (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "graph",
            "medium",
            "leetcode"
        ],
        "expected_tc": "O(n^3)",
        "expected_sc": "O(1)",
        "expected_algorithms": [],
        "code": "#include <algorithm>\nusing namespace std;\nclass Solution {\npublic:\n    void floydWarshall(int dist[100][100], int n) {\n        for (int k = 0; k < n; k++) {\n            for (int i = 0; i < n; i++) {\n                for (int j = 0; j < n; j++) {\n                    if (dist[i][k] != 1e9 && dist[k][j] != 1e9) {\n                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);\n                    }\n                }\n            }\n        }\n    }\n};"
    },
    {
        "id": "tough_floyd_warshall_java",
        "name": "Floyd-Warshall All-Pairs Shortest Paths (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "graph",
            "medium",
            "leetcode"
        ],
        "expected_tc": "O(n^3)",
        "expected_sc": "O(1)",
        "expected_algorithms": [],
        "code": "class Solution {\n    public void floydWarshall(int[][] dist, int n) {\n        for (int k = 0; k < n; k++) {\n            for (int i = 0; i < n; i++) {\n                for (int j = 0; j < n; j++) {\n                    if (dist[i][k] != 1000000000 && dist[k][j] != 1000000000) {\n                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);\n                    }\n                }\n            }\n        }\n    }\n}"
    },
    {
        "id": "tough_grid_dp_unique_paths_cpp",
        "name": "Unique Paths II Grid DP (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "dp",
            "grid",
            "medium",
            "leetcode"
        ],
        "expected_tc": "O(n m)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "#include <vector>\nusing namespace std;\nclass Solution {\npublic:\n    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {\n        int m = obstacleGrid.size(), n = obstacleGrid[0].size();\n        vector<long long> dp(n, 0);\n        dp[0] = obstacleGrid[0][0] == 0 ? 1 : 0;\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (obstacleGrid[i][j] == 1) {\n                    dp[j] = 0;\n                } else if (j > 0) {\n                    dp[j] += dp[j - 1];\n                }\n            }\n        }\n        return dp[n - 1];\n    }\n};"
    },
    {
        "id": "tough_grid_dp_unique_paths_java",
        "name": "Unique Paths II Grid DP (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "dp",
            "grid",
            "medium",
            "leetcode"
        ],
        "expected_tc": "O(n m)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "class Solution {\n    public int uniquePathsWithObstacles(int[][] obstacleGrid) {\n        int m = obstacleGrid.length, n = obstacleGrid[0].length;\n        int[] dp = new int[n];\n        dp[0] = obstacleGrid[0][0] == 0 ? 1 : 0;\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (obstacleGrid[i][j] == 1) {\n                    dp[j] = 0;\n                } else if (j > 0) {\n                    dp[j] += dp[j - 1];\n                }\n            }\n        }\n        return dp[n - 1];\n    }\n}"
    },
    {
        "id": "tough_quickselect_kth_cpp",
        "name": "Quickselect Kth Largest (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "sorting",
            "quickselect",
            "medium",
            "leetcode"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(1)",
        "expected_algorithms": [],
        "code": "#include <vector>\n#include <algorithm>\nusing namespace std;\nclass Solution {\n    int partition(vector<int>& nums, int left, int right) {\n        int pivot = nums[right], i = left;\n        for (int j = left; j < right; j++) {\n            if (nums[j] <= pivot) {\n                swap(nums[i], nums[j]);\n                i++;\n            }\n        }\n        swap(nums[i], nums[right]);\n        return i;\n    }\npublic:\n    int findKthLargest(vector<int>& nums, int k) {\n        int n = nums.size();\n        int target = n - k, left = 0, right = n - 1;\n        while (left <= right) {\n            int p = partition(nums, left, right);\n            if (p == target) return nums[p];\n            if (p < target) left = p + 1;\n            else right = p - 1;\n        }\n        return nums[left];\n    }\n};"
    },
    {
        "id": "tough_quickselect_kth_java",
        "name": "Quickselect Kth Largest (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "sorting",
            "quickselect",
            "medium",
            "leetcode"
        ],
        "expected_tc": "O(n)",
        "expected_sc": "O(1)",
        "expected_algorithms": [],
        "code": "class Solution {\n    int partition(int[] nums, int left, int right) {\n        int pivot = nums[right], i = left;\n        for (int j = left; j < right; j++) {\n            if (nums[j] <= pivot) {\n                int tmp = nums[i]; nums[i] = nums[j]; nums[j] = tmp;\n                i++;\n            }\n        }\n        int tmp = nums[i]; nums[i] = nums[right]; nums[right] = tmp;\n        return i;\n    }\n    public int findKthLargest(int[] nums, int k) {\n        int n = nums.length;\n        int target = n - k, left = 0, right = n - 1;\n        while (left <= right) {\n            int p = partition(nums, left, right);\n            if (p == target) return nums[p];\n            if (p < target) left = p + 1;\n            else right = p - 1;\n        }\n        return nums[left];\n    }\n}"
    },
    {
        "id": "tough_top_k_frequent_cpp",
        "name": "Top K Frequent Elements (C++ Priority Queue)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "heap",
            "top_k",
            "medium",
            "leetcode"
        ],
        "expected_tc": "O(k)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "#include <vector>\n#include <unordered_map>\n#include <queue>\nusing namespace std;\nclass Solution {\npublic:\n    vector<int> topKFrequent(vector<int>& nums, int k) {\n        unordered_map<int, int> count;\n        for (int x : nums) count[x]++;\n        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;\n        for (auto& p : count) {\n            pq.push({p.second, p.first});\n            if (pq.size() > k) pq.pop();\n        }\n        vector<int> res(k);\n        for (int i = 0; i < k; i++) {\n            res[i] = pq.top().second;\n            pq.pop();\n        }\n        return res;\n    }\n};"
    },
    {
        "id": "tough_top_k_frequent_java",
        "name": "Top K Frequent Elements (Java Priority Queue)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "heap",
            "top_k",
            "medium",
            "leetcode"
        ],
        "expected_tc": "O(k)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "import java.util.*;\nclass Solution {\n    public int[] topKFrequent(int[] nums, int k) {\n        Map<Integer, Integer> count = new HashMap<>();\n        for (int x : nums) count.put(x, count.getOrDefault(x, 0) + 1);\n        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);\n        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {\n            pq.offer(new int[]{entry.getKey(), entry.getValue()});\n            if (pq.size() > k) pq.poll();\n        }\n        int[] res = new int[k];\n        for (int i = 0; i < k; i++) res[i] = pq.poll()[0];\n        return res;\n    }\n}"
    },
    {
        "id": "tough_1d_dp_lis_cpp",
        "name": "Longest Increasing Subsequence 1D DP (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "dp",
            "linear_dp",
            "medium",
            "leetcode"
        ],
        "expected_tc": "O(n^2)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "#include <vector>\n#include <algorithm>\nusing namespace std;\nclass Solution {\npublic:\n    int lengthOfLIS(vector<int>& nums) {\n        int n = nums.size();\n        if (n == 0) return 0;\n        vector<int> dp(n, 1);\n        int max_len = 1;\n        for (int i = 0; i < n; i++) {\n            for (int j = 0; j < i; j++) {\n                if (nums[j] < nums[i]) {\n                    dp[i] = max(dp[i], dp[j] + 1);\n                }\n            }\n            max_len = max(max_len, dp[i]);\n        }\n        return max_len;\n    }\n};"
    },
    {
        "id": "tough_1d_dp_lis_java",
        "name": "Longest Increasing Subsequence 1D DP (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "dp",
            "linear_dp",
            "medium",
            "leetcode"
        ],
        "expected_tc": "O(n^2)",
        "expected_sc": "O(n)",
        "expected_algorithms": [],
        "code": "class Solution {\n    public int lengthOfLIS(int[] nums) {\n        int n = nums.length;\n        if (n == 0) return 0;\n        int[] dp = new int[n];\n        for (int i = 0; i < n; i++) dp[i] = 1;\n        int maxLen = 1;\n        for (int i = 0; i < n; i++) {\n            for (int j = 0; j < i; j++) {\n                if (nums[j] < nums[i]) {\n                    dp[i] = Math.max(dp[i], dp[j] + 1);\n                }\n            }\n            maxLen = Math.max(maxLen, dp[i]);\n        }\n        return maxLen;\n    }\n}"
    },
    {
        "id": "tough_backtracking_subsets_cpp",
        "name": "Subsets Backtracking (C++)",
        "language": "cpp",
        "rating": "Medium",
        "tags": [
            "backtracking",
            "dfs",
            "medium",
            "leetcode"
        ],
        "expected_tc": "O(n^2)",
        "expected_sc": "O(1)",
        "expected_algorithms": [],
        "code": "#include <vector>\nusing namespace std;\nclass Solution {\n    vector<vector<int>> res;\n    vector<int> curr;\n    void backtrack(vector<int>& nums, int start) {\n        res.push_back(curr);\n        for (int i = start; i < nums.size(); i++) {\n            curr.push_back(nums[i]);\n            backtrack(nums, i + 1);\n            curr.pop_back();\n        }\n    }\npublic:\n    vector<vector<int>> subsets(vector<int>& nums) {\n        backtrack(nums, 0);\n        return res;\n    }\n};"
    },
    {
        "id": "tough_backtracking_subsets_java",
        "name": "Subsets Backtracking (Java)",
        "language": "java",
        "rating": "Medium",
        "tags": [
            "backtracking",
            "dfs",
            "medium",
            "leetcode"
        ],
        "expected_tc": "O(n^2)",
        "expected_sc": "O(1)",
        "expected_algorithms": [],
        "code": "import java.util.*;\nclass Solution {\n    List<List<Integer>> res = new ArrayList<>();\n    List<Integer> curr = new ArrayList<>();\n    void backtrack(int[] nums, int start) {\n        res.add(new ArrayList<>(curr));\n        for (int i = start; i < nums.length; i++) {\n            curr.add(nums[i]);\n            backtrack(nums, i + 1);\n            curr.remove(curr.size() - 1);\n        }\n    }\n    public List<List<Integer>> subsets(int[] nums) {\n        backtrack(nums, 0);\n        return res;\n    }\n}"
    }
]

def main():
    out_dir = os.path.join(os.path.dirname(__file__))
    out_file = os.path.join(out_dir, "tough_benchmark.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(TOUGH_BENCHMARK_CASES, f, indent=2)
    print(f"Generated {out_file} with {len(TOUGH_BENCHMARK_CASES)} cases successfully.")

if __name__ == "__main__":
    main()
