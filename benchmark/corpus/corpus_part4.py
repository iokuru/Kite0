# corpus_part4.py: Problems 196 to 250 (55 problems = 110 cases)
PART4_CASES = []

def add_prob(pid, name, tc, sc, algos, rating, tags, cpp_code, java_code):
    PART4_CASES.append({
        "id": f"{pid}_cpp",
        "name": f"{name} (C++)",
        "language": "cpp",
        "rating": rating,
        "tags": tags,
        "expected_tc": tc,
        "expected_sc": sc,
        "expected_algorithms": algos,
        "code": cpp_code
    })
    PART4_CASES.append({
        "id": f"{pid}_java",
        "name": f"{name} (Java)",
        "language": "java",
        "rating": rating,
        "tags": tags,
        "expected_tc": tc,
        "expected_sc": sc,
        "expected_algorithms": algos,
        "code": java_code
    })

# oa_196_path_minimum_effort
add_prob(
    "oa_196_path_minimum_effort", "Path with Minimum Effort", "O((V + E) log V)", "O(V + E)", ["Dijkstra"], "Medium", ["dijkstra", "graph"],
    '''#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        vector<vector<int>> dist(m, vector<int>(n, 1e9));
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        dist[0][0] = 0;
        pq.push({0, 0, 0});
        int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();
            int d = curr[0], r = curr[1], c = curr[2];
            if (d > dist[r][c]) continue;
            if (r == m - 1 && c == n - 1) return d;
            for (auto& dir : dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int weight = max(d, abs(heights[r][c] - heights[nr][nc]));
                    if (weight < dist[nr][nc]) {
                        dist[nr][nc] = weight;
                        pq.push({weight, nr, nc});
                    }
                }
            }
        }
        return 0;
    }
};''',
    '''import java.util.*;
class Solution {
    public int minimumEffortPath(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        int[][] dist = new int[m][n];
        for (int[] row : dist) Arrays.fill(row, 1000000000);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        dist[0][0] = 0;
        pq.offer(new int[]{0, 0, 0});
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int d = curr[0], r = curr[1], c = curr[2];
            if (d > dist[r][c]) continue;
            if (r == m - 1 && c == n - 1) return d;
            for (int[] dir : dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int weight = Math.max(d, Math.abs(heights[r][c] - heights[nr][nc]));
                    if (weight < dist[nr][nc]) {
                        dist[nr][nc] = weight;
                        pq.offer(new int[]{weight, nr, nc});
                    }
                }
            }
        }
        return 0;
    }
}'''
)

# oa_197_swim_in_rising_water
add_prob(
    "oa_197_swim_in_rising_water", "Swim in Rising Water", "O((V + E) log V)", "O(V + E)", ["Dijkstra"], "Hard", ["dijkstra", "graph"],
    '''#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> dist(n, vector<int>(n, 1e9));
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        dist[0][0] = grid[0][0];
        pq.push({grid[0][0], 0, 0});
        int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();
            int t = curr[0], r = curr[1], c = curr[2];
            if (t > dist[r][c]) continue;
            if (r == n - 1 && c == n - 1) return t;
            for (auto& dir : dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                    int weight = max(t, grid[nr][nc]);
                    if (weight < dist[nr][nc]) {
                        dist[nr][nc] = weight;
                        pq.push({weight, nr, nc});
                    }
                }
            }
        }
        return 0;
    }
};''',
    '''import java.util.*;
class Solution {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        int[][] dist = new int[n][n];
        for (int[] row : dist) Arrays.fill(row, 1000000000);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        dist[0][0] = grid[0][0];
        pq.offer(new int[]{grid[0][0], 0, 0});
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int t = curr[0], r = curr[1], c = curr[2];
            if (t > dist[r][c]) continue;
            if (r == n - 1 && c == n - 1) return t;
            for (int[] dir : dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                    int weight = Math.max(t, grid[nr][nc]);
                    if (weight < dist[nr][nc]) {
                        dist[nr][nc] = weight;
                        pq.offer(new int[]{weight, nr, nc});
                    }
                }
            }
        }
        return 0;
    }
}'''
)

# oa_198_network_delay_time
add_prob(
    "oa_198_network_delay_time", "Network Delay Time", "O((V + E) log V)", "O(V + E)", ["Dijkstra"], "Medium", ["dijkstra", "graph"],
    '''#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> adj(n + 1);
        for (auto& t : times) adj[t[0]].push_back({t[1], t[2]});
        vector<int> dist(n + 1, 1e9);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        dist[k] = 0;
        pq.push({0, k});
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (d > dist[u]) continue;
            for (auto& [v, weight] : adj[u]) {
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    pq.push({dist[v], v});
                }
            }
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) ans = max(ans, dist[i]);
        return ans == 1e9 ? -1 : ans;
    }
};''',
    '''import java.util.*;
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for (int[] t : times) adj.get(t[0]).add(new int[]{t[1], t[2]});
        int[] dist = new int[n + 1];
        Arrays.fill(dist, 1000000000);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        dist[k] = 0;
        pq.offer(new int[]{0, k});
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int d = curr[0], u = curr[1];
            if (d > dist[u]) continue;
            for (int[] edge : adj.get(u)) {
                int v = edge[0], weight = edge[1];
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    pq.offer(new int[]{dist[v], v});
                }
            }
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) ans = Math.max(ans, dist[i]);
        return ans == 1000000000 ? -1 : ans;
    }
}'''
)

# oa_199_cheapest_flights_k_stops
add_prob(
    "oa_199_cheapest_flights_k_stops", "Cheapest Flights Within K Stops", "O((V + E) log V)", "O(V + E)", ["Dijkstra"], "Medium", ["dijkstra", "graph"],
    '''#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<pair<int, int>>> adj(n);
        for (auto& f : flights) adj[f[0]].push_back({f[1], f[2]});
        vector<int> dist(n, 1e9);
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        dist[src] = 0;
        pq.push({0, src, 0});
        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();
            int cost = curr[0], u = curr[1], stops = curr[2];
            if (u == dst) return cost;
            if (stops > k) continue;
            for (auto& [v, weight] : adj[u]) {
                if (cost + weight < dist[v]) {
                    dist[v] = cost + weight;
                    pq.push({cost + weight, v, stops + 1});
                }
            }
        }
        return -1;
    }
};''',
    '''import java.util.*;
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] f : flights) adj.get(f[0]).add(new int[]{f[1], f[2]});
        int[] dist = new int[n];
        Arrays.fill(dist, 1000000000);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        dist[src] = 0;
        pq.offer(new int[]{0, src, 0});
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int cost = curr[0], u = curr[1], stops = curr[2];
            if (u == dst) return cost;
            if (stops > k) continue;
            for (int[] edge : adj.get(u)) {
                int v = edge[0], weight = edge[1];
                if (cost + weight < dist[v]) {
                    dist[v] = cost + weight;
                    pq.offer(new int[]{cost + weight, v, stops + 1});
                }
            }
        }
        return -1;
    }
}'''
)

# oa_200_max_probability_path
add_prob(
    "oa_200_max_probability_path", "Path with Maximum Probability", "O((V + E) log V)", "O(V + E)", ["Dijkstra"], "Medium", ["dijkstra", "graph"],
    '''#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        vector<vector<pair<int, double>>> adj(n);
        for (int i = 0; i < (int)edges.size(); i++) {
            adj[edges[i][0]].push_back({edges[i][1], succProb[i]});
            adj[edges[i][1]].push_back({edges[i][0], succProb[i]});
        }
        vector<double> dist(n, 0.0);
        priority_queue<pair<double, int>> pq;
        dist[start_node] = 1.0;
        pq.push({1.0, start_node});
        while (!pq.empty()) {
            auto [prob, u] = pq.top();
            pq.pop();
            if (u == end_node) return prob;
            if (prob < dist[u]) continue;
            for (auto& [v, weight] : adj[u]) {
                if (dist[u] * weight > dist[v]) {
                    dist[v] = dist[u] * weight;
                    pq.push({dist[v], v});
                }
            }
        }
        return 0.0;
    }
};''',
    '''import java.util.*;
class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        List<List<double[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < edges.length; i++) {
            adj.get(edges[i][0]).add(new double[]{edges[i][1], succProb[i]});
            adj.get(edges[i][1]).add(new double[]{edges[i][0], succProb[i]});
        }
        double[] dist = new double[n];
        PriorityQueue<double[]> pq = new PriorityQueue<>((a, b) -> Double.compare(b[0], a[0]));
        dist[start_node] = 1.0;
        pq.offer(new double[]{1.0, start_node});
        while (!pq.isEmpty()) {
            double[] curr = pq.poll();
            double prob = curr[0];
            int u = (int)curr[1];
            if (u == end_node) return prob;
            if (prob < dist[u]) continue;
            for (double[] edge : adj.get(u)) {
                int v = (int)edge[0];
                double weight = edge[1];
                if (dist[u] * weight > dist[v]) {
                    dist[v] = dist[u] * weight;
                    pq.offer(new double[]{dist[v], v});
                }
            }
        }
        return 0.0;
    }
}'''
)

# oa_201_second_minimum_time
add_prob(
    "oa_201_second_minimum_time", "Second Minimum Time Destination", "O((V + E) log V)", "O(V + E)", ["Dijkstra"], "Hard", ["dijkstra", "graph"],
    '''#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        vector<vector<int>> adj(n + 1);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vector<vector<int>> dist(n + 1, vector<int>(2, 1e9));
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        dist[1][0] = 0;
        pq.push({0, 1});
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (d > dist[u][1]) continue;
            int weight = d;
            if ((weight / change) % 2 == 1) weight = ((weight / change) + 1) * change;
            weight += time;
            for (int v : adj[u]) {
                if (weight < dist[v][0]) {
                    dist[v][1] = dist[v][0];
                    dist[v][0] = weight;
                    pq.push({weight, v});
                } else if (weight > dist[v][0] && weight < dist[v][1]) {
                    dist[v][1] = weight;
                    pq.push({weight, v});
                }
            }
        }
        return dist[n][1];
    }
};''',
    '''import java.util.*;
class Solution {
    public int secondMinimum(int n, int[][] edges, int time, int change) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        int[][] dist = new int[n + 1][2];
        for (int[] row : dist) Arrays.fill(row, 1000000000);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        dist[1][0] = 0;
        pq.offer(new int[]{0, 1});
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int d = curr[0], u = curr[1];
            if (d > dist[u][1]) continue;
            int weight = d;
            if ((weight / change) % 2 == 1) weight = ((weight / change) + 1) * change;
            weight += time;
            for (int v : adj.get(u)) {
                if (weight < dist[v][0]) {
                    dist[v][1] = dist[v][0];
                    dist[v][0] = weight;
                    pq.offer(new int[]{weight, v});
                } else if (weight > dist[v][0] && weight < dist[v][1]) {
                    dist[v][1] = weight;
                    pq.offer(new int[]{weight, v});
                }
            }
        }
        return dist[n][1];
    }
}'''
)

# oa_202_ways_arrive_destination
add_prob(
    "oa_202_ways_arrive_destination", "Ways to Arrive at Destination", "O((V + E) log V)", "O(V + E)", ["Dijkstra"], "Medium", ["dijkstra", "graph"],
    '''#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        vector<vector<pair<int, int>>> adj(n);
        for (auto& r : roads) {
            adj[r[0]].push_back({r[1], r[2]});
            adj[r[1]].push_back({r[0], r[2]});
        }
        vector<long long> dist(n, 1e18);
        vector<long long> ways(n, 0);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        dist[0] = 0;
        ways[0] = 1;
        pq.push({0, 0});
        int MOD = 1e9 + 7;
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (d > dist[u]) continue;
            for (auto& [v, weight] : adj[u]) {
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    ways[v] = ways[u];
                    pq.push({dist[v], v});
                } else if (dist[u] + weight == dist[v]) {
                    ways[v] = (ways[v] + ways[u]) % MOD;
                }
            }
        }
        return ways[n - 1];
    }
};''',
    '''import java.util.*;
class Solution {
    public int countPaths(int n, int[][] roads) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] r : roads) {
            adj.get(r[0]).add(new int[]{r[1], r[2]});
            adj.get(r[1]).add(new int[]{r[0], r[2]});
        }
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        long[] ways = new long[n];
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        dist[0] = 0;
        ways[0] = 1;
        pq.offer(new long[]{0, 0});
        int MOD = 1000000007;
        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            long d = curr[0];
            int u = (int)curr[1];
            if (d > dist[u]) continue;
            for (int[] edge : adj.get(u)) {
                int v = edge[0], weight = edge[1];
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    ways[v] = ways[u];
                    pq.offer(new long[]{dist[v], v});
                } else if (dist[u] + weight == dist[v]) {
                    ways[v] = (ways[v] + ways[u]) % MOD;
                }
            }
        }
        return (int)ways[n - 1];
    }
}'''
)

# oa_203_permutations
add_prob(
    "oa_203_permutations", "Permutations", "O(V + E)", "O(V + E)", ["DFS"], "Medium", ["dfs", "backtracking"],
    '''#include <vector>
using namespace std;
class Solution {
    vector<vector<int>> res;
    void dfs(vector<int>& nums, vector<int>& path, vector<bool>& vis) {
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < (int)nums.size(); i++) {
            if (vis[i]) continue;
            vis[i] = true;
            path.push_back(nums[i]);
            dfs(nums, path, vis);
            path.pop_back();
            vis[i] = false;
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> path;
        vector<bool> vis(nums.size(), false);
        dfs(nums, path, vis);
        return res;
    }
};''',
    '''import java.util.*;
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    void dfs(int[] nums, List<Integer> path, boolean[] vis) {
        if (path.size() == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (vis[i]) continue;
            vis[i] = true;
            path.add(nums[i]);
            dfs(nums, path, vis);
            path.remove(path.size() - 1);
            vis[i] = false;
        }
    }
    public List<List<Integer>> permute(int[] nums) {
        dfs(nums, new ArrayList<>(), new boolean[nums.length]);
        return res;
    }
}'''
)

# oa_204_permutations_ii
add_prob(
    "oa_204_permutations_ii", "Permutations II", "O(V + E)", "O(V + E)", ["DFS"], "Medium", ["dfs", "backtracking"],
    '''#include <vector>
#include <algorithm>
using namespace std;
class Solution {
    vector<vector<int>> res;
    void dfs(vector<int>& nums, vector<int>& path, vector<bool>& vis) {
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < (int)nums.size(); i++) {
            if (vis[i] || (i > 0 && nums[i] == nums[i - 1] && !vis[i - 1])) continue;
            vis[i] = true;
            path.push_back(nums[i]);
            dfs(nums, path, vis);
            path.pop_back();
            vis[i] = false;
        }
    }
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> path;
        vector<bool> vis(nums.size(), false);
        dfs(nums, path, vis);
        return res;
    }
};''',
    '''import java.util.*;
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    void dfs(int[] nums, List<Integer> path, boolean[] vis) {
        if (path.size() == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (vis[i] || (i > 0 && nums[i] == nums[i - 1] && !vis[i - 1])) continue;
            vis[i] = true;
            path.add(nums[i]);
            dfs(nums, path, vis);
            path.remove(path.size() - 1);
            vis[i] = false;
        }
    }
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        dfs(nums, new ArrayList<>(), new boolean[nums.length]);
        return res;
    }
}'''
)

# oa_205_combinations
add_prob(
    "oa_205_combinations", "Combinations", "O(V + E)", "O(V + E)", ["DFS"], "Medium", ["dfs", "backtracking"],
    '''#include <vector>
using namespace std;
class Solution {
    vector<vector<int>> res;
    void dfs(int start, int n, int k, vector<int>& path) {
        if ((int)path.size() == k) {
            res.push_back(path);
            return;
        }
        for (int i = start; i <= n; i++) {
            path.push_back(i);
            dfs(i + 1, n, k, path);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> path;
        dfs(1, n, k, path);
        return res;
    }
};''',
    '''import java.util.*;
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    void dfs(int start, int n, int k, List<Integer> path) {
        if (path.size() == k) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i <= n; i++) {
            path.add(i);
            dfs(i + 1, n, k, path);
            path.remove(path.size() - 1);
        }
    }
    public List<List<Integer>> combine(int n, int k) {
        dfs(1, n, k, new ArrayList<>());
        return res;
    }
}'''
)

# oa_206_combination_sum
add_prob(
    "oa_206_combination_sum", "Combination Sum", "O(V + E)", "O(V + E)", ["DFS"], "Medium", ["dfs", "backtracking"],
    '''#include <vector>
using namespace std;
class Solution {
    vector<vector<int>> res;
    void dfs(vector<int>& candidates, int target, int start, vector<int>& path) {
        if (target == 0) {
            res.push_back(path);
            return;
        }
        if (target < 0) return;
        for (int i = start; i < (int)candidates.size(); i++) {
            path.push_back(candidates[i]);
            dfs(candidates, target - candidates[i], i, path);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> path;
        dfs(candidates, target, 0, path);
        return res;
    }
};''',
    '''import java.util.*;
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    void dfs(int[] candidates, int target, int start, List<Integer> path) {
        if (target == 0) {
            res.add(new ArrayList<>(path));
            return;
        }
        if (target < 0) return;
        for (int i = start; i < candidates.length; i++) {
            path.add(candidates[i]);
            dfs(candidates, target - candidates[i], i, path);
            path.remove(path.size() - 1);
        }
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        dfs(candidates, target, 0, new ArrayList<>());
        return res;
    }
}'''
)

# oa_207_combination_sum_ii
add_prob(
    "oa_207_combination_sum_ii", "Combination Sum II", "O(V + E)", "O(V + E)", ["DFS"], "Medium", ["dfs", "backtracking"],
    '''#include <vector>
#include <algorithm>
using namespace std;
class Solution {
    vector<vector<int>> res;
    void dfs(vector<int>& candidates, int target, int start, vector<int>& path) {
        if (target == 0) {
            res.push_back(path);
            return;
        }
        for (int i = start; i < (int)candidates.size(); i++) {
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            if (candidates[i] > target) break;
            path.push_back(candidates[i]);
            dfs(candidates, target - candidates[i], i + 1, path);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> path;
        dfs(candidates, target, 0, path);
        return res;
    }
};''',
    '''import java.util.*;
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    void dfs(int[] candidates, int target, int start, List<Integer> path) {
        if (target == 0) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            if (candidates[i] > target) break;
            path.add(candidates[i]);
            dfs(candidates, target - candidates[i], i + 1, path);
            path.remove(path.size() - 1);
        }
    }
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        dfs(candidates, target, 0, new ArrayList<>());
        return res;
    }
}'''
)

# oa_208_combination_sum_iii
add_prob(
    "oa_208_combination_sum_iii", "Combination Sum III", "O(V + E)", "O(V + E)", ["DFS"], "Medium", ["dfs", "backtracking"],
    '''#include <vector>
using namespace std;
class Solution {
    vector<vector<int>> res;
    void dfs(int start, int k, int n, vector<int>& path) {
        if ((int)path.size() == k && n == 0) {
            res.push_back(path);
            return;
        }
        if ((int)path.size() > k || n < 0) return;
        for (int i = start; i <= 9; i++) {
            path.push_back(i);
            dfs(i + 1, k, n - i, path);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> path;
        dfs(1, k, n, path);
        return res;
    }
};''',
    '''import java.util.*;
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    void dfs(int start, int k, int n, List<Integer> path) {
        if (path.size() == k && n == 0) {
            res.add(new ArrayList<>(path));
            return;
        }
        if (path.size() > k || n < 0) return;
        for (int i = start; i <= 9; i++) {
            path.add(i);
            dfs(i + 1, k, n - i, path);
            path.remove(path.size() - 1);
        }
    }
    public List<List<Integer>> combinationSum3(int k, int n) {
        dfs(1, k, n, new ArrayList<>());
        return res;
    }
}'''
)

# oa_209_letter_combinations
add_prob(
    "oa_209_letter_combinations", "Letter Combinations Phone Number", "O(V + E)", "O(V + E)", ["DFS"], "Medium", ["dfs", "backtracking", "string"],
    '''#include <vector>
#include <string>
using namespace std;
class Solution {
    vector<string> res;
    vector<string> pad = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    void dfs(string& digits, int idx, string path) {
        if (idx == (int)digits.size()) {
            res.push_back(path);
            return;
        }
        for (char c : pad[digits[idx] - '0']) {
            dfs(digits, idx + 1, path + c);
        }
    }
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        dfs(digits, 0, "");
        return res;
    }
};''',
    '''import java.util.*;
class Solution {
    List<String> res = new ArrayList<>();
    String[] pad = new String[]{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    void dfs(String digits, int idx, StringBuilder path) {
        if (idx == digits.length()) {
            res.add(path.toString());
            return;
        }
        for (char c : pad[digits.charAt(idx) - '0'].toCharArray()) {
            path.append(c);
            dfs(digits, idx + 1, path);
            path.deleteCharAt(path.length() - 1);
        }
    }
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) return res;
        dfs(digits, 0, new StringBuilder());
        return res;
    }
}'''
)

# oa_210_n_queens
add_prob(
    "oa_210_n_queens", "N-Queens", "O(V + E)", "O(V + E)", ["DFS"], "Hard", ["dfs", "backtracking"],
    '''#include <vector>
#include <string>
using namespace std;
class Solution {
    vector<vector<string>> res;
    bool isValid(vector<string>& board, int row, int col, int n) {
        for (int i = 0; i < row; i++) if (board[i][col] == 'Q') return false;
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) if (board[i][j] == 'Q') return false;
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) if (board[i][j] == 'Q') return false;
        return true;
    }
    void dfs(vector<string>& board, int row, int n) {
        if (row == n) {
            res.push_back(board);
            return;
        }
        for (int col = 0; col < n; col++) {
            if (isValid(board, row, col, n)) {
                board[row][col] = 'Q';
                dfs(board, row + 1, n);
                board[row][col] = '.';
            }
        }
    }
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        dfs(board, 0, n);
        return res;
    }
};''',
    '''import java.util.*;
class Solution {
    List<List<String>> res = new ArrayList<>();
    boolean isValid(char[][] board, int row, int col, int n) {
        for (int i = 0; i < row; i++) if (board[i][col] == 'Q') return false;
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) if (board[i][j] == 'Q') return false;
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) if (board[i][j] == 'Q') return false;
        return true;
    }
    void dfs(char[][] board, int row, int n) {
        if (row == n) {
            List<String> b = new ArrayList<>();
            for (char[] r : board) b.add(new String(r));
            res.add(b);
            return;
        }
        for (int col = 0; col < n; col++) {
            if (isValid(board, row, col, n)) {
                board[row][col] = 'Q';
                dfs(board, row + 1, n);
                board[row][col] = '.';
            }
        }
    }
    public List<List<String>> solveNQueens(int n) {
        char[][] board = new char[n][n];
        for (char[] r : board) Arrays.fill(r, '.');
        dfs(board, 0, n);
        return res;
    }
}'''
)

# oa_211_n_queens_ii
add_prob(
    "oa_211_n_queens_ii", "N-Queens II", "O(V + E)", "O(V + E)", ["DFS"], "Hard", ["dfs", "backtracking"],
    '''#include <vector>
using namespace std;
class Solution {
    int count = 0;
    bool cols[20] = {0}, diag1[40] = {0}, diag2[40] = {0};
    void dfs(int row, int n) {
        if (row == n) {
            count++;
            return;
        }
        for (int col = 0; col < n; col++) {
            if (cols[col] || diag1[row + col] || diag2[row - col + n]) continue;
            cols[col] = diag1[row + col] = diag2[row - col + n] = true;
            dfs(row + 1, n);
            cols[col] = diag1[row + col] = diag2[row - col + n] = false;
        }
    }
public:
    int totalNQueens(int n) {
        dfs(0, n);
        return count;
    }
};''',
    '''class Solution {
    int count = 0;
    boolean[] cols = new boolean[20];
    boolean[] diag1 = new boolean[40];
    boolean[] diag2 = new boolean[40];
    void dfs(int row, int n) {
        if (row == n) {
            count++;
            return;
        }
        for (int col = 0; col < n; col++) {
            if (cols[col] || diag1[row + col] || diag2[row - col + n]) continue;
            cols[col] = diag1[row + col] = diag2[row - col + n] = true;
            dfs(row + 1, n);
            cols[col] = diag1[row + col] = diag2[row - col + n] = false;
        }
    }
    public int totalNQueens(int n) {
        dfs(0, n);
        return count;
    }
}'''
)

# oa_212_word_search
add_prob(
    "oa_212_word_search", "Word Search", "O(V + E)", "O(V + E)", ["DFS"], "Medium", ["dfs", "backtracking"],
    '''#include <vector>
#include <string>
using namespace std;
class Solution {
    bool dfs(vector<vector<char>>& board, string& word, int idx, int r, int c) {
        if (idx == (int)word.size()) return true;
        if (r < 0 || r >= (int)board.size() || c < 0 || c >= (int)board[0].size() || board[r][c] != word[idx]) return false;
        char temp = board[r][c];
        board[r][c] = '#';
        bool found = dfs(board, word, idx + 1, r + 1, c) ||
                     dfs(board, word, idx + 1, r - 1, c) ||
                     dfs(board, word, idx + 1, r, c + 1) ||
                     dfs(board, word, idx + 1, r, c - 1);
        board[r][c] = temp;
        return found;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size(), n = board[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, word, 0, i, j)) return true;
            }
        }
        return false;
    }
};''',
    '''class Solution {
    boolean dfs(char[][] board, String word, int idx, int r, int c) {
        if (idx == word.length()) return true;
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(idx)) return false;
        char temp = board[r][c];
        board[r][c] = '#';
        boolean found = dfs(board, word, idx + 1, r + 1, c) ||
                        dfs(board, word, idx + 1, r - 1, c) ||
                        dfs(board, word, idx + 1, r, c + 1) ||
                        dfs(board, word, idx + 1, r, c - 1);
        board[r][c] = temp;
        return found;
    }
    public boolean exist(char[][] board, String word) {
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, word, 0, i, j)) return true;
            }
        }
        return false;
    }
}'''
)

# oa_213_palindrome_partitioning
add_prob(
    "oa_213_palindrome_partitioning", "Palindrome Partitioning", "O(V + E)", "O(V + E)", ["DFS", "Two Pointers"], "Medium", ["dfs", "backtracking", "string"],
    '''#include <vector>
#include <string>
using namespace std;
class Solution {
    vector<vector<string>> res;
    bool isPalindrome(string& s, int l, int r) {
        while (l < r) if (s[l++] != s[r--]) return false;
        return true;
    }
    void dfs(string& s, int start, vector<string>& path) {
        if (start == (int)s.size()) {
            res.push_back(path);
            return;
        }
        for (int i = start; i < (int)s.size(); i++) {
            if (isPalindrome(s, start, i)) {
                path.push_back(s.substr(start, i - start + 1));
                dfs(s, i + 1, path);
                path.pop_back();
            }
        }
    }
public:
    vector<vector<string>> partition(string s) {
        vector<string> path;
        dfs(s, 0, path);
        return res;
    }
};''',
    '''import java.util.*;
class Solution {
    List<List<String>> res = new ArrayList<>();
    boolean isPalindrome(String s, int l, int r) {
        while (l < r) if (s.charAt(l++) != s.charAt(r--)) return false;
        return true;
    }
    void dfs(String s, int start, List<String> path) {
        if (start == s.length()) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < s.length(); i++) {
            if (isPalindrome(s, start, i)) {
                path.add(s.substring(start, i + 1));
                dfs(s, i + 1, path);
                path.remove(path.size() - 1);
            }
        }
    }
    public List<List<String>> partition(String s) {
        dfs(s, 0, new ArrayList<>());
        return res;
    }
}'''
)

# oa_214_restore_ip_addresses
add_prob(
    "oa_214_restore_ip_addresses", "Restore IP Addresses", "O(V + E)", "O(V + E)", ["DFS"], "Medium", ["dfs", "backtracking", "string"],
    '''#include <vector>
#include <string>
using namespace std;
class Solution {
    vector<string> res;
    void dfs(string& s, int idx, int segment, string path) {
        if (idx == (int)s.size() && segment == 4) {
            path.pop_back();
            res.push_back(path);
            return;
        }
        if (idx == (int)s.size() || segment == 4) return;
        for (int len = 1; len <= 3 && idx + len <= (int)s.size(); len++) {
            string part = s.substr(idx, len);
            if ((part[0] == '0' && len > 1) || stoi(part) > 255) break;
            dfs(s, idx + len, segment + 1, path + part + ".");
        }
    }
public:
    vector<string> restoreIpAddresses(string s) {
        dfs(s, 0, 0, "");
        return res;
    }
};''',
    '''import java.util.*;
class Solution {
    List<String> res = new ArrayList<>();
    void dfs(String s, int idx, int segment, StringBuilder path) {
        if (idx == s.length() && segment == 4) {
            res.add(path.substring(0, path.length() - 1));
            return;
        }
        if (idx == s.length() || segment == 4) return;
        for (int len = 1; len <= 3 && idx + len <= s.length(); len++) {
            String part = s.substring(idx, idx + len);
            if ((part.charAt(0) == '0' && len > 1) || Integer.parseInt(part) > 255) break;
            int prevLen = path.length();
            path.append(part).append(".");
            dfs(s, idx + len, segment + 1, path);
            path.setLength(prevLen);
        }
    }
    public List<String> restoreIpAddresses(String s) {
        dfs(s, 0, 0, new StringBuilder());
        return res;
    }
}'''
)

# oa_215_generate_parentheses
add_prob(
    "oa_215_generate_parentheses", "Generate Parentheses", "O(V + E)", "O(V + E)", ["DFS"], "Medium", ["dfs", "backtracking", "string"],
    '''#include <vector>
#include <string>
using namespace std;
class Solution {
    vector<string> res;
    void dfs(int open, int close, int n, string path) {
        if ((int)path.size() == 2 * n) {
            res.push_back(path);
            return;
        }
        if (open < n) dfs(open + 1, close, n, path + "(");
        if (close < open) dfs(open, close + 1, n, path + ")");
    }
public:
    vector<string> generateParenthesis(int n) {
        dfs(0, 0, n, "");
        return res;
    }
};''',
    '''import java.util.*;
class Solution {
    List<String> res = new ArrayList<>();
    void dfs(int open, int close, int n, StringBuilder path) {
        if (path.length() == 2 * n) {
            res.add(path.toString());
            return;
        }
        if (open < n) {
            path.append("(");
            dfs(open + 1, close, n, path);
            path.deleteCharAt(path.length() - 1);
        }
        if (close < open) {
            path.append(")");
            dfs(open, close + 1, n, path);
            path.deleteCharAt(path.length() - 1);
        }
    }
    public List<String> generateParenthesis(int n) {
        dfs(0, 0, n, new StringBuilder());
        return res;
    }
}'''
)

# oa_216_climbing_stairs
add_prob(
    "oa_216_climbing_stairs", "Climbing Stairs", "O(n)", "O(n)", [], "Easy", ["dp"],
    '''#include <vector>
using namespace std;
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        vector<int> dp(n + 1);
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) dp[i] = dp[i - 1] + dp[i - 2];
        return dp[n];
    }
};''',
    '''class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) dp[i] = dp[i - 1] + dp[i - 2];
        return dp[n];
    }
}'''
)

# oa_217_house_robber
add_prob(
    "oa_217_house_robber", "House Robber", "O(n)", "O(n)", [], "Medium", ["dp"],
    '''#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        vector<int> dp(n);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        for (int i = 2; i < n; i++) dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
        return dp[n - 1];
    }
};''',
    '''class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        int[] dp = new int[n];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        for (int i = 2; i < n; i++) dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
        return dp[n - 1];
    }
}'''
)

# oa_218_house_robber_ii
add_prob(
    "oa_218_house_robber_ii", "House Robber II", "O(n)", "O(n)", [], "Medium", ["dp"],
    '''#include <vector>
#include <algorithm>
using namespace std;
class Solution {
    int robRange(vector<int>& nums, int start, int end) {
        int n = end - start + 1;
        if (n == 1) return nums[start];
        vector<int> dp(n);
        dp[0] = nums[start];
        dp[1] = max(nums[start], nums[start + 1]);
        for (int i = 2; i < n; i++) dp[i] = max(dp[i - 1], dp[i - 2] + nums[start + i]);
        return dp[n - 1];
    }
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        return max(robRange(nums, 0, n - 2), robRange(nums, 1, n - 1));
    }
};''',
    '''class Solution {
    int robRange(int[] nums, int start, int end) {
        int n = end - start + 1;
        if (n == 1) return nums[start];
        int[] dp = new int[n];
        dp[0] = nums[start];
        dp[1] = Math.max(nums[start], nums[start + 1]);
        for (int i = 2; i < n; i++) dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[start + i]);
        return dp[n - 1];
    }
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        return Math.max(robRange(nums, 0, n - 2), robRange(nums, 1, n - 1));
    }
}'''
)

# oa_219_coin_change
add_prob(
    "oa_219_coin_change", "Coin Change", "O(n)", "O(n)", [], "Medium", ["dp"],
    '''#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int coinChange(vector<int>& coins, int n) {
        vector<int> dp(n + 1, 1e9);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int c : coins) {
                if (i - c >= 0) dp[i] = min(dp[i], dp[i - c] + 1);
            }
        }
        return dp[n] == 1e9 ? -1 : dp[n];
    }
};''',
    '''import java.util.*;
class Solution {
    public int coinChange(int[] coins, int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, 1000000000);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int c : coins) {
                if (i - c >= 0) dp[i] = Math.min(dp[i], dp[i - c] + 1);
            }
        }
        return dp[n] == 1000000000 ? -1 : dp[n];
    }
}'''
)

# oa_220_coin_change_ii
add_prob(
    "oa_220_coin_change_ii", "Coin Change II", "O(n)", "O(n)", [], "Medium", ["dp"],
    '''#include <vector>
using namespace std;
class Solution {
public:
    int change(int n, vector<int>& coins) {
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            dp[i] += dp[i - 1];
        }
        return dp[n];
    }
};''',
    '''class Solution {
    public int change(int n, int[] coins) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            dp[i] += dp[i - 1];
        }
        return dp[n];
    }
}'''
)

# oa_221_integer_break
add_prob(
    "oa_221_integer_break", "Integer Break", "O(n^2)", "O(n)", [], "Medium", ["dp"],
    '''#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int integerBreak(int n) {
        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]));
            }
        }
        return dp[n];
    }
};''',
    '''class Solution {
    public int integerBreak(int n) {
        int[] dp = new int[n + 1];
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                dp[i] = Math.max(dp[i], Math.max(j * (i - j), j * dp[i - j]));
            }
        }
        return dp[n];
    }
}'''
)

# oa_222_word_break
add_prob(
    "oa_222_word_break", "Word Break", "O(n^2)", "O(n)", [], "Medium", ["dp", "string"],
    '''#include <vector>
#include <string>
#include <unordered_set>
using namespace std;
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        int n = s.size();
        vector<bool> dp(n + 1, false);
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && dict.count(s.substr(j, i - j))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
};''',
    '''import java.util.*;
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && dict.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}'''
)

# oa_223_unique_paths
add_prob(
    "oa_223_unique_paths", "Unique Paths", "O(n m)", "O(n)", [], "Medium", ["dp"],
    '''#include <vector>
using namespace std;
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j - 1];
            }
        }
        return dp[n - 1];
    }
};''',
    '''import java.util.*;
class Solution {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j - 1];
            }
        }
        return dp[n - 1];
    }
}'''
)

# oa_224_minimum_path_sum
add_prob(
    "oa_224_minimum_path_sum", "Minimum Path Sum", "O(n m)", "O(n)", [], "Medium", ["dp"],
    '''#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<int> dp(n, 1e9);
        dp[0] = 0;
        for (int i = 0; i < m; i++) {
            dp[0] += grid[i][0];
            for (int j = 1; j < n; j++) {
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j];
            }
        }
        return dp[n - 1];
    }
};''',
    '''import java.util.*;
class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1000000000);
        dp[0] = 0;
        for (int i = 0; i < m; i++) {
            dp[0] += grid[i][0];
            for (int j = 1; j < n; j++) {
                dp[j] = Math.min(dp[j], dp[j - 1]) + grid[i][j];
            }
        }
        return dp[n - 1];
    }
}'''
)

# oa_225_maximal_square
add_prob(
    "oa_225_maximal_square", "Maximal Square", "O(n m)", "O(n)", [], "Medium", ["dp"],
    '''#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<int> dp(n + 1, 0);
        int max_len = 0, prev = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (matrix[i - 1][j - 1] == '1') {
                    dp[j] = min(min(dp[j], dp[j - 1]), prev) + 1;
                    max_len = max(max_len, dp[j]);
                } else {
                    dp[j] = 0;
                }
                prev = temp;
            }
        }
        return max_len * max_len;
    }
};''',
    '''import java.util.*;
class Solution {
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int[] dp = new int[n + 1];
        int maxLen = 0, prev = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (matrix[i - 1][j - 1] == '1') {
                    dp[j] = Math.min(Math.min(dp[j], dp[j - 1]), prev) + 1;
                    maxLen = Math.max(maxLen, dp[j]);
                } else {
                    dp[j] = 0;
                }
                prev = temp;
            }
        }
        return maxLen * maxLen;
    }
}'''
)

# oa_226_longest_common_subsequence
add_prob(
    "oa_226_longest_common_subsequence", "Longest Common Subsequence", "O(n m)", "O(n)", [], "Medium", ["dp", "string"],
    '''#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.size(), n = text2.size();
        vector<int> dp(n + 1, 0);
        for (int i = 1; i <= m; i++) {
            int prev = 0;
            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (text1[i - 1] == text2[j - 1]) dp[j] = prev + 1;
                else dp[j] = max(dp[j], dp[j - 1]);
                prev = temp;
            }
        }
        return dp[n];
    }
};''',
    '''class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[] dp = new int[n + 1];
        for (int i = 1; i <= m; i++) {
            int prev = 0;
            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) dp[j] = prev + 1;
                else dp[j] = Math.max(dp[j], dp[j - 1]);
                prev = temp;
            }
        }
        return dp[n];
    }
}'''
)

# oa_227_edit_distance
add_prob(
    "oa_227_edit_distance", "Edit Distance", "O(n m)", "O(n)", [], "Medium", ["dp", "string"],
    '''#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<int> dp(n + 1);
        for (int j = 0; j <= n; j++) dp[j] = j;
        for (int i = 1; i <= m; i++) {
            int prev = dp[0];
            dp[0] = i;
            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (word1[i - 1] == word2[j - 1]) dp[j] = prev;
                else dp[j] = min(min(dp[j - 1], dp[j]), prev) + 1;
                prev = temp;
            }
        }
        return dp[n];
    }
};''',
    '''class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[] dp = new int[n + 1];
        for (int j = 0; j <= n; j++) dp[j] = j;
        for (int i = 1; i <= m; i++) {
            int prev = dp[0];
            dp[0] = i;
            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) dp[j] = prev;
                else dp[j] = Math.min(Math.min(dp[j - 1], dp[j]), prev) + 1;
                prev = temp;
            }
        }
        return dp[n];
    }
}'''
)

# oa_228_longest_palindromic_subsequence
add_prob(
    "oa_228_longest_palindromic_subsequence", "Longest Palindromic Subsequence", "O(n^2)", "O(n)", [], "Medium", ["dp", "string"],
    '''#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        vector<int> dp(n, 1);
        for (int i = n - 2; i >= 0; i--) {
            int prev = 0;
            for (int j = i + 1; j < n; j++) {
                int temp = dp[j];
                if (s[i] == s[j]) dp[j] = prev + 2;
                else dp[j] = max(dp[j], dp[j - 1]);
                prev = temp;
            }
        }
        return dp[n - 1];
    }
};''',
    '''class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = n - 2; i >= 0; i--) {
            int prev = 0;
            for (int j = i + 1; j < n; j++) {
                int temp = dp[j];
                if (s.charAt(i) == s.charAt(j)) dp[j] = prev + 2;
                else dp[j] = Math.max(dp[j], dp[j - 1]);
                prev = temp;
            }
        }
        return dp[n - 1];
    }
}'''
)

# oa_229_distinct_subsequences
add_prob(
    "oa_229_distinct_subsequences", "Distinct Subsequences", "O(n m)", "O(n)", [], "Hard", ["dp", "string"],
    '''#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.size(), n = t.size();
        vector<unsigned long long> dp(n + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= m; i++) {
            for (int j = n; j >= 1; j--) {
                if (s[i - 1] == t[j - 1]) dp[j] += dp[j - 1];
            }
        }
        return dp[n];
    }
};''',
    '''class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        long[] dp = new long[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= m; i++) {
            for (int j = n; j >= 1; j--) {
                if (s.charAt(i - 1) == t.charAt(j - 1)) dp[j] += dp[j - 1];
            }
        }
        return (int)dp[n];
    }
}'''
)

# oa_230_house_robber_iii
add_prob(
    "oa_230_house_robber_iii", "House Robber III", "O(n)", "O(n)", ["Tree DP"], "Medium", ["tree_dp", "dp", "tree"],
    '''#include <vector>
#include <algorithm>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
class Solution {
    pair<int, int> dfs(TreeNode* root) {
        if (!root) return {0, 0};
        auto left = dfs(root->left);
        auto right = dfs(root->right);
        int rob_this = root->val + left.second + right.second;
        int not_rob = max(left.first, left.second) + max(right.first, right.second);
        return {rob_this, not_rob};
    }
public:
    int rob(TreeNode* root) {
        auto p = dfs(root);
        return max(p.first, p.second);
    }
};''',
    '''import java.util.*;
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}
class Solution {
    int[] dfs(TreeNode root) {
        if (root == null) return new int[]{0, 0};
        int[] left = dfs(root.left);
        int[] right = dfs(root.right);
        int robThis = root.val + left[1] + right[1];
        int notRob = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return new int[]{robThis, notRob};
    }
    public int rob(TreeNode root) {
        int[] p = dfs(root);
        return Math.max(p[0], p[1]);
    }
}'''
)

# oa_231_diameter_binary_tree
add_prob(
    "oa_231_diameter_binary_tree", "Diameter of Binary Tree", "O(n)", "O(n)", ["Tree DP"], "Easy", ["tree_dp", "tree"],
    '''#include <algorithm>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
class Solution {
    int max_diameter = 0;
    int dfs(TreeNode* root) {
        if (!root) return 0;
        int left_gain = dfs(root->left);
        int right_gain = dfs(root->right);
        max_diameter = max(max_diameter, left_gain + right_gain);
        return 1 + max(left_gain, right_gain);
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root);
        return max_diameter;
    }
};''',
    '''class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}
class Solution {
    int maxDiameter = 0;
    int dfs(TreeNode root) {
        if (root == null) return 0;
        int leftGain = dfs(root.left);
        int rightGain = dfs(root.right);
        maxDiameter = Math.max(maxDiameter, leftGain + rightGain);
        return 1 + Math.max(leftGain, rightGain);
    }
    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return maxDiameter;
    }
}'''
)

# oa_232_binary_tree_max_path_sum
add_prob(
    "oa_232_binary_tree_max_path_sum", "Binary Tree Maximum Path Sum", "O(n)", "O(n)", ["Tree DP"], "Hard", ["tree_dp", "tree"],
    '''#include <algorithm>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
class Solution {
    int max_sum = -1e9;
    int max_gain(TreeNode* root) {
        if (!root) return 0;
        int left_gain = max(0, max_gain(root->left));
        int right_gain = max(0, max_gain(root->right));
        max_sum = max(max_sum, root->val + left_gain + right_gain);
        return root->val + max(left_gain, right_gain);
    }
public:
    int maxPathSum(TreeNode* root) {
        max_gain(root);
        return max_sum;
    }
};''',
    '''class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}
class Solution {
    int maxSum = -1000000000;
    int maxGain(TreeNode root) {
        if (root == null) return 0;
        int leftGain = Math.max(0, maxGain(root.left));
        int rightGain = Math.max(0, maxGain(root.right));
        maxSum = Math.max(maxSum, root.val + leftGain + rightGain);
        return root.val + Math.max(leftGain, rightGain);
    }
    public int maxPathSum(TreeNode root) {
        maxGain(root);
        return maxSum;
    }
}'''
)

# oa_233_shortest_path_all_nodes
add_prob(
    "oa_233_shortest_path_all_nodes", "Shortest Path Visiting All Nodes", "O(2^n * n)", "O(2^n * n)", ["Bitmask DP"], "Hard", ["bitmask_dp", "dp"],
    '''#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int shortestPathLength(vector<vector<int>>& graph) {
        int n = graph.size();
        int full_mask = (1 << n) - 1;
        vector<vector<int>> dp(1 << n, vector<int>(n, 1e9));
        for (int i = 0; i < n; i++) dp[1 << i][i] = 0;
        for (int mask = 1; mask <= full_mask; mask++) {
            for (int u = 0; u < n; u++) {
                if (dp[mask][u] == 1e9) continue;
                for (int v : graph[u]) {
                    int next_mask = mask | (1 << v);
                    dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + 1);
                }
            }
        }
        int ans = 1e9;
        for (int i = 0; i < n; i++) ans = min(ans, dp[full_mask][i]);
        return ans;
    }
};''',
    '''import java.util.*;
class Solution {
    public int shortestPathLength(int[][] graph) {
        int n = graph.length;
        int fullMask = (1 << n) - 1;
        int[][] dp = new int[1 << n][n];
        for (int[] row : dp) Arrays.fill(row, 1000000000);
        for (int i = 0; i < n; i++) dp[1 << i][i] = 0;
        for (int mask = 1; mask <= fullMask; mask++) {
            for (int u = 0; u < n; u++) {
                if (dp[mask][u] == 1000000000) continue;
                for (int v : graph[u]) {
                    int nextMask = mask | (1 << v);
                    dp[nextMask][v] = Math.min(dp[nextMask][v], dp[mask][u] + 1);
                }
            }
        }
        int ans = 1000000000;
        for (int i = 0; i < n; i++) ans = Math.min(ans, dp[fullMask][i]);
        return ans;
    }
}'''
)

# oa_234_partition_k_subsets
add_prob(
    "oa_234_partition_k_subsets", "Partition to K Equal Sum Subsets", "O(2^n * n)", "O(2^n * n)", ["Bitmask DP"], "Medium", ["bitmask_dp", "dp"],
    '''#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;
class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int n = nums.size();
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % k != 0) return false;
        int target = sum / k;
        vector<int> dp(1 << n, -1);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] == -1) continue;
            for (int i = 0; i < n; i++) {
                if (!(mask & (1 << i)) && dp[mask] + nums[i] <= target) {
                    dp[mask | (1 << i)] = (dp[mask] + nums[i]) % target;
                }
            }
        }
        return dp[(1 << n) - 1] == 0;
    }
};''',
    '''import java.util.*;
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int n = nums.length;
        int sum = 0;
        for (int x : nums) sum += x;
        if (sum % k != 0) return false;
        int target = sum / k;
        int[] dp = new int[1 << n];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] == -1) continue;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) == 0 && dp[mask] + nums[i] <= target) {
                    dp[mask | (1 << i)] = (dp[mask] + nums[i]) % target;
                }
            }
        }
        return dp[(1 << n) - 1] == 0;
    }
}'''
)

# oa_235_burst_balloons
add_prob(
    "oa_235_burst_balloons", "Burst Balloons", "O(n^3)", "O(n)", [], "Hard", ["interval_dp", "dp"],
    '''#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<int> a(n + 2, 1);
        for (int i = 0; i < n; i++) a[i + 1] = nums[i];
        vector<int> dp(n + 2, 0);
        for (int len = 1; len <= n; len++) {
            for (int left = 1; left <= n - len + 1; left++) {
                int right = left + len - 1;
                for (int k = left; k <= right; k++) {
                    dp[left] = max(dp[left], a[left - 1] * a[k] * a[right + 1]);
                }
            }
        }
        return dp[1];
    }
};''',
    '''class Solution {
    public int maxCoins(int[] nums) {
        int n = nums.length;
        int[] a = new int[n + 2];
        a[0] = a[n + 1] = 1;
        for (int i = 0; i < n; i++) a[i + 1] = nums[i];
        int[] dp = new int[n + 2];
        for (int len = 1; len <= n; len++) {
            for (int left = 1; left <= n - len + 1; left++) {
                int right = left + len - 1;
                for (int k = left; k <= right; k++) {
                    dp[left] = Math.max(dp[left], a[left - 1] * a[k] * a[right + 1]);
                }
            }
        }
        return dp[1];
    }
}'''
)

# oa_236_implement_trie
add_prob(
    "oa_236_implement_trie", "Implement Trie (Prefix Tree)", "O(n)", "O(n)", ["Trie"], "Medium", ["trie", "string"],
    '''#include <string>
#include <vector>
using namespace std;
class TrieNode {
public:
    TrieNode* child[26];
    bool is_end;
    TrieNode() {
        for (int i = 0; i < 26; i++) child[i] = nullptr;
        is_end = false;
    }
};
class Trie {
    TrieNode* root;
public:
    Trie() { root = new TrieNode(); }
    void insert(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (!curr->child[c - 'a']) curr->child[c - 'a'] = new TrieNode();
            curr = curr->child[c - 'a'];
        }
        curr->is_end = true;
    }
};''',
    '''class TrieNode {
    TrieNode[] child = new TrieNode[26];
    boolean isEnd = false;
}
class Trie {
    TrieNode root = new TrieNode();
    public void insert(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            if (curr.child[c - 'a'] == null) curr.child[c - 'a'] = new TrieNode();
            curr = curr.child[c - 'a'];
        }
        curr.isEnd = true;
    }
}'''
)

# oa_237_max_xor_binary_trie
add_prob(
    "oa_237_max_xor_binary_trie", "Maximum XOR Array (Binary Trie)", "O(n)", "O(n)", ["Trie"], "Medium", ["trie", "bit_manipulation"],
    '''#include <vector>
#include <algorithm>
using namespace std;
struct Node {
    Node* child[2];
    Node() { child[0] = child[1] = nullptr; }
};
class Solution {
    Node* root = new Node();
    void insert(int num) {
        Node* curr = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (!curr->child[bit]) curr->child[bit] = new Node();
            curr = curr->child[bit];
        }
    }
public:
    int findMaximumXOR(vector<int>& nums) {
        for (int x : nums) insert(x);
        return 0;
    }
};''',
    '''class Node {
    Node[] child = new Node[2];
}
class Solution {
    Node root = new Node();
    void insert(int num) {
        Node curr = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.child[bit] == null) curr.child[bit] = new Node();
            curr = curr.child[bit];
        }
    }
    public int findMaximumXOR(int[] nums) {
        for (int x : nums) insert(x);
        return 0;
    }
}'''
)

# oa_238_fenwick_tree_range_sum
add_prob(
    "oa_238_fenwick_tree_range_sum", "Range Sum Query (Fenwick Tree)", "O(q log n)", "O(n)", ["Fenwick Tree"], "Medium", ["fenwick", "range_query"],
    '''#include <vector>
using namespace std;
class NumArray {
    vector<int> bit;
    int n;
public:
    NumArray(vector<int>& nums) {
        n = nums.size();
        bit.assign(n + 1, 0);
    }
    void update(int index, int val) {
        for (int i = index + 1; i <= n; i += i & -i) bit[i] += val;
    }
    int sumRange(int left, int right) {
        int sum = 0;
        for (int i = right + 1; i > 0; i -= i & -i) sum += bit[i];
        for (int i = left; i > 0; i -= i & -i) sum -= bit[i];
        return sum;
    }
};''',
    '''class NumArray {
    int[] bit;
    int n;
    public NumArray(int[] nums) {
        n = nums.length;
        bit = new int[n + 1];
    }
    public void update(int index, int val) {
        for (int i = index + 1; i <= n; i += i & -i) bit[i] += val;
    }
    public int sumRange(int left, int right) {
        int sum = 0;
        for (int i = right + 1; i > 0; i -= i & -i) sum += bit[i];
        for (int i = left; i > 0; i -= i & -i) sum -= bit[i];
        return sum;
    }
}'''
)

# oa_239_segment_tree_range_sum
add_prob(
    "oa_239_segment_tree_range_sum", "Range Sum Query (Segment Tree)", "O(n + q log n)", "O(n)", ["Segment Tree"], "Medium", ["segment_tree", "range_query"],
    '''#include <vector>
using namespace std;
class NumArray {
    vector<int> tree;
    int n;
    void buildTree(vector<int>& nums, int node, int start, int end) {
        if (start == end) { tree[node] = nums[start]; return; }
        int mid = (start + end) / 2;
        buildTree(nums, 2 * node, start, mid);
        buildTree(nums, 2 * node + 1, mid + 1, end);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
public:
    NumArray(vector<int>& nums) {
        n = nums.size();
        tree.assign(4 * n, 0);
        buildTree(nums, 1, 0, n - 1);
    }
    void update(int index, int val) {}
};''',
    '''class NumArray {
    int[] tree;
    int n;
    void buildTree(int[] nums, int node, int start, int end) {
        if (start == end) { tree[node] = nums[start]; return; }
        int mid = (start + end) / 2;
        buildTree(nums, 2 * node, start, mid);
        buildTree(nums, 2 * node + 1, mid + 1, end);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
    public NumArray(int[] nums) {
        n = nums.length;
        tree = new int[4 * n];
        buildTree(nums, 1, 0, n - 1);
    }
    public void update(int index, int val) {}
}'''
)

# oa_240_sparse_table_rmq
add_prob(
    "oa_240_sparse_table_rmq", "Range Minimum Query (Sparse Table)", "O(n log n + q)", "O(n log n)", ["Sparse Table"], "Hard", ["sparse_table", "range_query"],
    '''#include <vector>
#include <algorithm>
using namespace std;
class SparseTable {
    vector<vector<int>> st;
public:
    SparseTable(vector<int>& arr) {
        int n = arr.size();
        st.assign(n, vector<int>(20, 0));
        for (int i = 0; i < n; i++) st[i][0] = arr[i];
        for (int j = 1; (1 << j) <= n; j++) {
            for (int i = 0; i + (1 << j) <= n; i++) {
                st[i][j] = min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
            }
        }
    }
};''',
    '''import java.util.*;
class SparseTable {
    int[][] st;
    public SparseTable(int[] arr) {
        int n = arr.length;
        st = new int[n][20];
        for (int i = 0; i < n; i++) st[i][0] = arr[i];
        for (int j = 1; (1 << j) <= n; j++) {
            for (int i = 0; i + (1 << j) <= n; i++) {
                st[i][j] = Math.min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
            }
        }
    }
}'''
)

# oa_241_kmp_pattern_matching
add_prob(
    "oa_241_kmp_pattern_matching", "KMP Pattern Matching", "O(n + m)", "O(m)", ["KMP"], "Medium", ["kmp", "string"],
    '''#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.size(), m = needle.size();
        if (m == 0) return 0;
        vector<int> pi(m, 0);
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && needle[i] != needle[j]) j = pi[j - 1];
            if (needle[i] == needle[j]) j++;
            pi[i] = j;
        }
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && haystack[i] != needle[j]) j = pi[j - 1];
            if (haystack[i] == needle[j]) j++;
            if (j == m) return i - m + 1;
        }
        return -1;
    }
};''',
    '''class Solution {
    public int strStr(String haystack, String needle) {
        int n = haystack.length(), m = needle.length();
        if (m == 0) return 0;
        int[] pi = new int[m];
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && needle.charAt(i) != needle.charAt(j)) j = pi[j - 1];
            if (needle.charAt(i) == needle.charAt(j)) j++;
            pi[i] = j;
        }
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && haystack.charAt(i) != needle.charAt(j)) j = pi[j - 1];
            if (haystack.charAt(i) == needle.charAt(j)) j++;
            if (j == m) return i - m + 1;
        }
        return -1;
    }
}'''
)

# oa_242_rolling_hash_rabin_karp
add_prob(
    "oa_242_rolling_hash_rabin_karp", "Rolling Hash (Rabin-Karp)", "O(n)", "O(n)", ["Rolling Hash"], "Medium", ["rolling_hash", "string"],
    '''#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    int rabinKarp(string s, string pattern) {
        int n = s.size(), m = pattern.size();
        long long BASE = 31, MOD = 1e9 + 7;
        vector<long long> p_pow(max(n, m) + 1, 1);
        for (int i = 1; i <= max(n, m); i++) p_pow[i] = (p_pow[i - 1] * BASE) % MOD;
        long long pattern_hash = 0;
        for (int i = 0; i < m; i++) pattern_hash = (pattern_hash * BASE + pattern[i]) % MOD;
        return 0;
    }
};''',
    '''class Solution {
    public int rabinKarp(String s, String pattern) {
        int n = s.length(), m = pattern.length();
        long BASE = 31, MOD = 1000000007;
        long[] p_pow = new long[Math.max(n, m) + 1];
        p_pow[0] = 1;
        for (int i = 1; i <= Math.max(n, m); i++) p_pow[i] = (p_pow[i - 1] * BASE) % MOD;
        long patternHash = 0;
        for (int i = 0; i < m; i++) patternHash = (patternHash * BASE + pattern.charAt(i)) % MOD;
        return 0;
    }
}'''
)

# oa_243_z_algorithm
add_prob(
    "oa_243_z_algorithm", "Z-Algorithm String Matching", "O(n)", "O(n)", ["Z Algorithm"], "Medium", ["z_algorithm", "string"],
    '''#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> z_algorithm(string s) {
        int n = s.size();
        vector<int> z(n, 0);
        int l = 0, r = 0;
        for (int i = 1; i < n; i++) {
            if (i <= r) z[i] = min(r - i + 1, z[i - l]);
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        return z;
    }
};''',
    '''class Solution {
    public int[] z_algorithm(String s) {
        int n = s.length();
        int[] z = new int[n];
        int l = 0, r = 0;
        for (int i = 1; i < n; i++) {
            if (i <= r) z[i] = Math.min(r - i + 1, z[i - l]);
            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i])) z[i]++;
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        return z;
    }
}'''
)

# oa_244_critical_connections_bridges
add_prob(
    "oa_244_critical_connections_bridges", "Critical Connections (Bridges)", "O(V + E)", "O(V + E)", ["DFS"], "Hard", ["dfs", "graph", "bridges"],
    '''#include <vector>
#include <algorithm>
using namespace std;
class Solution {
    vector<vector<int>> res;
    vector<vector<int>> adj;
    vector<int> tin, low;
    int timer = 0;
    void dfs(int v, int p) {
        tin[v] = low[v] = ++timer;
        for (int to : adj[v]) {
            if (to == p) continue;
            if (tin[to]) {
                low[v] = min(low[v], tin[to]);
            } else {
                dfs(to, v);
                low[v] = min(low[v], low[to]);
                if (low[to] > tin[v]) res.push_back({v, to});
            }
        }
    }
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        adj.resize(n);
        tin.assign(n, 0);
        low.assign(n, 0);
        for (auto& c : connections) {
            adj[c[0]].push_back(c[1]);
            adj[c[1]].push_back(c[0]);
        }
        dfs(0, -1);
        return res;
    }
};''',
    '''import java.util.*;
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    List<List<Integer>> adj = new ArrayList<>();
    int[] tin, low;
    int timer = 0;
    void dfs(int v, int p) {
        tin[v] = low[v] = ++timer;
        for (int to : adj.get(v)) {
            if (to == p) continue;
            if (tin[to] > 0) {
                low[v] = Math.min(low[v], tin[to]);
            } else {
                dfs(to, v);
                low[v] = Math.min(low[v], low[to]);
                if (low[to] > tin[v]) res.add(Arrays.asList(v, to));
            }
        }
    }
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        tin = new int[n];
        low = new int[n];
        for (List<Integer> c : connections) {
            adj.get(c.get(0)).add(c.get(1));
            adj.get(c.get(1)).add(c.get(0));
        }
        dfs(0, -1);
        return res;
    }
}'''
)

# oa_245_reconstruct_itinerary
add_prob(
    "oa_245_reconstruct_itinerary", "Reconstruct Itinerary", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Hard", ["dfs", "graph", "eulerian", "heap"],
    '''#include <vector>
#include <string>
#include <unordered_map>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
    unordered_map<string, priority_queue<string, vector<string>, greater<string>>> targets;
    vector<string> route;
    void dfs(string airport) {
        while (!targets[airport].empty()) {
            string next = targets[airport].top();
            targets[airport].pop();
            dfs(next);
        }
        route.push_back(airport);
    }
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for (auto& ticket : tickets) targets[ticket[0]].push(ticket[1]);
        dfs("JFK");
        reverse(route.begin(), route.end());
        return route;
    }
};''',
    '''import java.util.*;
class Solution {
    Map<String, PriorityQueue<String>> targets = new HashMap<>();
    List<String> route = new ArrayList<>();
    void dfs(String airport) {
        while (targets.containsKey(airport) && !targets.get(airport).isEmpty()) {
            dfs(targets.get(airport).poll());
        }
        route.add(0, airport);
    }
    public List<String> findItinerary(List<List<String>> tickets) {
        for (List<String> ticket : tickets) {
            targets.computeIfAbsent(ticket.get(0), k -> new PriorityQueue<>()).add(ticket.get(1));
        }
        dfs("JFK");
        return route;
    }
}'''
)

# oa_246_number_of_1_bits
add_prob(
    "oa_246_number_of_1_bits", "Number of 1 Bits", "O(n)", "O(1)", [], "Easy", ["bit_manipulation", "math"],
    '''class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    }
};''',
    '''class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    }
}'''
)

# oa_247_counting_bits
add_prob(
    "oa_247_counting_bits", "Counting Bits", "O(n)", "O(n)", [], "Easy", ["bit_manipulation", "dp"],
    '''#include <vector>
using namespace std;
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i >> 1] + (i & 1);
        }
        return dp;
    }
};''',
    '''class Solution {
    public int[] countBits(int n) {
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i >> 1] + (i & 1);
        }
        return dp;
    }
}'''
)

# oa_248_single_number
add_prob(
    "oa_248_single_number", "Single Number", "O(n)", "O(1)", [], "Easy", ["bit_manipulation"],
    '''#include <vector>
using namespace std;
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) ans ^= nums[i];
        return ans;
    }
};''',
    '''class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.length; i++) ans ^= nums[i];
        return ans;
    }
}'''
)

# oa_249_count_primes_sieve
add_prob(
    "oa_249_count_primes_sieve", "Count Primes (Sieve)", "O(n log log n)", "O(n)", ["Sieve"], "Medium", ["sieve", "math"],
    '''#include <vector>
using namespace std;
class Solution {
public:
    int countPrimes(int n) {
        if (n <= 2) return 0;
        vector<bool> is_prime(n, true);
        is_prime[0] = is_prime[1] = false;
        for (int p = 2; p * p < n; p++) {
            if (is_prime[p]) {
                for (int i = p * p; i < n; i += p) is_prime[i] = false;
            }
        }
        int count = 0;
        for (int i = 2; i < n; i++) if (is_prime[i]) count++;
        return count;
    }
};''',
    '''import java.util.*;
class Solution {
    public int countPrimes(int n) {
        if (n <= 2) return 0;
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        for (int p = 2; p * p < n; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i < n; i += p) isPrime[i] = false;
            }
        }
        int count = 0;
        for (int i = 2; i < n; i++) if (isPrime[i]) count++;
        return count;
    }
}'''
)

# oa_250_fast_power_pow_x_n
add_prob(
    "oa_250_fast_power_pow_x_n", "Fast Modular Exponentiation Pow(x, n)", "O(log n)", "O(1)", [], "Medium", ["math", "binary_search"],
    '''class Solution {
public:
    double myPow(double x, int n) {
        long long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        double ans = 1;
        double current_product = x;
        while (N > 0) {
            if (N % 2 == 1) ans *= current_product;
            current_product *= current_product;
            N >>= 1;
        }
        return ans;
    }
};''',
    '''class Solution {
    public double myPow(double x, int n) {
        long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        double ans = 1;
        double currentProduct = x;
        while (N > 0) {
            if (N % 2 == 1) ans *= currentProduct;
            currentProduct *= currentProduct;
            N >>= 1;
        }
        return ans;
    }
}'''
)

print(f'Part 4 loaded with {len(PART4_CASES)} cases ({len(PART4_CASES)//2} problems: 196 to 250).')
