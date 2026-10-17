# generate_part3.py: generates corpus_part3.py (Problems 146 to 195 = 50 problems, 100 cases)
import json

code_entries = []

def add_prob(pid, name, tc, sc, algos, rating, tags, cpp_code, java_code):
    code_entries.append({
        "id": pid,
        "name": name,
        "tc": tc,
        "sc": sc,
        "algos": algos,
        "rating": rating,
        "tags": tags,
        "cpp": cpp_code,
        "java": java_code
    })

# ==================== MONOTONIC QUEUE (146 - 155) ====================
# 146. Sliding Window Maximum
add_prob(
    "oa_146_sliding_window_max", "Sliding Window Maximum", "O(n)", "O(k)", ["Monotonic Queue"], "Hard", ["monotonic_queue", "sliding_window"],
    """#include <vector>
#include <deque>
using namespace std;
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> res;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (!dq.empty() && dq.front() == i - k) dq.pop_front();
            while (!dq.empty() && nums[dq.back()] < nums[i]) dq.pop_back();
            dq.push_back(i);
            if (i >= k - 1) res.push_back(nums[dq.front()]);
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        int[] res = new int[nums.length - k + 1];
        int idx = 0;
        for (int i = 0; i < nums.length; i++) {
            if (!dq.isEmpty() && dq.peekFirst() == i - k) dq.pollFirst();
            while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i]) dq.pollLast();
            dq.offerLast(i);
            if (i >= k - 1) res[idx++] = nums[dq.peekFirst()];
        }
        return res;
    }
}"""
)

# 147. Constrained Subsequence Sum
add_prob(
    "oa_147_constrained_subsequence_sum", "Constrained Subsequence Sum", "O(n)", "O(k)", ["Kadane's Algorithm", "Monotonic Queue"], "Hard", ["monotonic_queue", "dp"],
    """#include <vector>
#include <deque>
#include <algorithm>
using namespace std;
class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n);
        deque<int> dq;
        int ans = nums[0];
        for (int i = 0; i < n; i++) {
            if (!dq.empty() && dq.front() < i - k) dq.pop_front();
            dp[i] = nums[i] + (!dq.empty() ? max(0, dp[dq.front()]) : 0);
            ans = max(ans, dp[i]);
            while (!dq.empty() && dp[dq.back()] <= dp[i]) dq.pop_back();
            dq.push_back(i);
        }
        return ans;
    }
};""",
    """import java.util.*;
class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
        int n = nums.length;
        int[] dp = new int[n];
        Deque<Integer> dq = new ArrayDeque<>();
        int ans = nums[0];
        for (int i = 0; i < n; i++) {
            if (!dq.isEmpty() && dq.peekFirst() < i - k) dq.pollFirst();
            dp[i] = nums[i] + (!dq.isEmpty() ? Math.max(0, dp[dq.peekFirst()]) : 0);
            ans = Math.max(ans, dp[i]);
            while (!dq.isEmpty() && dp[dq.peekLast()] <= dp[i]) dq.pollLast();
            dq.offerLast(i);
        }
        return ans;
    }
}"""
)

# 148. Shortest Subarray with Sum at Least K
add_prob(
    "oa_148_shortest_subarray_sum_k", "Shortest Subarray with Sum at Least K", "O(n)", "O(k)", ["Monotonic Queue", "Prefix Sum"], "Hard", ["monotonic_queue", "prefix_sum"],
    """#include <vector>
#include <deque>
#include <algorithm>
using namespace std;
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        deque<int> dq;
        int ans = n + 1;
        for (int i = 0; i <= n; i++) {
            while (!dq.empty() && prefix[i] - prefix[dq.front()] >= k) {
                ans = min(ans, i - dq.front());
                dq.pop_front();
            }
            while (!dq.empty() && prefix[i] <= prefix[dq.back()]) dq.pop_back();
            dq.push_back(i);
        }
        return ans <= n ? ans : -1;
    }
};""",
    """import java.util.*;
class Solution {
    public int shortestSubarray(int[] nums, int k) {
        int n = nums.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        Deque<Integer> dq = new ArrayDeque<>();
        int ans = n + 1;
        for (int i = 0; i <= n; i++) {
            while (!dq.isEmpty() && prefix[i] - prefix[dq.peekFirst()] >= k) {
                ans = Math.min(ans, i - dq.pollFirst());
            }
            while (!dq.isEmpty() && prefix[i] <= prefix[dq.peekLast()]) dq.pollLast();
            dq.offerLast(i);
        }
        return ans <= n ? ans : -1;
    }
}"""
)

# 149. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
add_prob(
    "oa_149_longest_continuous_subarray_limit", "Longest Continuous Subarray With Limit", "O(n)", "O(k)", ["Monotonic Queue", "Sliding Window"], "Medium", ["monotonic_queue", "sliding_window"],
    """#include <vector>
#include <deque>
#include <algorithm>
using namespace std;
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        deque<int> max_dq, min_dq;
        int left = 0, ans = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            while (!max_dq.empty() && nums[max_dq.back()] < nums[right]) max_dq.pop_back();
            while (!min_dq.empty() && nums[min_dq.back()] > nums[right]) min_dq.pop_back();
            max_dq.push_back(right);
            min_dq.push_back(right);
            while (nums[max_dq.front()] - nums[min_dq.front()] > limit) {
                if (max_dq.front() == left) max_dq.pop_front();
                if (min_dq.front() == left) min_dq.pop_front();
                left++;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};""",
    """import java.util.*;
class Solution {
    public int longestSubarray(int[] nums, int limit) {
        Deque<Integer> maxDq = new ArrayDeque<>();
        Deque<Integer> minDq = new ArrayDeque<>();
        int left = 0, ans = 0;
        for (int right = 0; right < nums.length; right++) {
            while (!maxDq.isEmpty() && nums[maxDq.peekLast()] < nums[right]) maxDq.pollLast();
            while (!minDq.isEmpty() && nums[minDq.peekLast()] > nums[right]) minDq.pollLast();
            maxDq.offerLast(right);
            minDq.offerLast(right);
            while (nums[maxDq.peekFirst()] - nums[minDq.peekFirst()] > limit) {
                if (maxDq.peekFirst() == left) maxDq.pollFirst();
                if (minDq.peekFirst() == left) minDq.pollFirst();
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}"""
)

# 150. Jump Game VI
add_prob(
    "oa_150_jump_game_vi", "Jump Game VI", "O(n)", "O(k)", ["Monotonic Queue"], "Medium", ["monotonic_queue", "dp"],
    """#include <vector>
#include <deque>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n);
        dp[0] = nums[0];
        deque<int> dq;
        dq.push_back(0);
        for (int i = 1; i < n; i++) {
            if (!dq.empty() && dq.front() < i - k) dq.pop_front();
            dp[i] = nums[i] + dp[dq.front()];
            while (!dq.empty() && dp[dq.back()] <= dp[i]) dq.pop_back();
            dq.push_back(i);
        }
        return dp[n - 1];
    }
};""",
    """import java.util.*;
class Solution {
    public int maxResult(int[] nums, int k) {
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = nums[0];
        Deque<Integer> dq = new ArrayDeque<>();
        dq.offerLast(0);
        for (int i = 1; i < n; i++) {
            if (!dq.isEmpty() && dq.peekFirst() < i - k) dq.pollFirst();
            dp[i] = nums[i] + dp[dq.peekFirst()];
            while (!dq.isEmpty() && dp[dq.peekLast()] <= dp[i]) dq.pollLast();
            dq.offerLast(i);
        }
        return dp[n - 1];
    }
}"""
)

# 151. Max Value of Equation
add_prob(
    "oa_151_max_value_of_equation", "Max Value of Equation", "O(n)", "O(k)", ["Monotonic Queue"], "Hard", ["monotonic_queue"],
    """#include <vector>
#include <deque>
#include <algorithm>
using namespace std;
class Solution {
public:
    int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
        deque<int> dq;
        int ans = -2e9;
        for (int i = 0; i < (int)points.size(); i++) {
            while (!dq.empty() && points[i][0] - points[dq.front()][0] > k) dq.pop_front();
            if (!dq.empty()) {
                ans = max(ans, points[i][0] + points[i][1] + points[dq.front()][1] - points[dq.front()][0]);
            }
            while (!dq.empty() && (points[dq.back()][1] - points[dq.back()][0]) <= (points[i][1] - points[i][0])) {
                dq.pop_back();
            }
            dq.push_back(i);
        }
        return ans;
    }
};""",
    """import java.util.*;
class Solution {
    public int findMaxValueOfEquation(int[][] points, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        int ans = -2000000000;
        for (int i = 0; i < points.length; i++) {
            while (!dq.isEmpty() && points[i][0] - points[dq.peekFirst()][0] > k) dq.pollFirst();
            if (!dq.isEmpty()) {
                ans = Math.max(ans, points[i][0] + points[i][1] + points[dq.peekFirst()][1] - points[dq.peekFirst()][0]);
            }
            while (!dq.isEmpty() && (points[dq.peekLast()][1] - points[dq.peekLast()][0]) <= (points[i][1] - points[i][0])) {
                dq.pollLast();
            }
            dq.offerLast(i);
        }
        return ans;
    }
}"""
)

# 152. Sliding Window Minimum
add_prob(
    "oa_152_sliding_window_min", "Sliding Window Minimum", "O(n)", "O(k)", ["Monotonic Queue"], "Medium", ["monotonic_queue", "sliding_window"],
    """#include <vector>
#include <deque>
using namespace std;
class Solution {
public:
    vector<int> minSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> res;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (!dq.empty() && dq.front() == i - k) dq.pop_front();
            while (!dq.empty() && nums[dq.back()] > nums[i]) dq.pop_back();
            dq.push_back(i);
            if (i >= k - 1) res.push_back(nums[dq.front()]);
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public int[] minSlidingWindow(int[] nums, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        int[] res = new int[nums.length - k + 1];
        int idx = 0;
        for (int i = 0; i < nums.length; i++) {
            if (!dq.isEmpty() && dq.peekFirst() == i - k) dq.pollFirst();
            while (!dq.isEmpty() && nums[dq.peekLast()] > nums[i]) dq.pollLast();
            dq.offerLast(i);
            if (i >= k - 1) res[idx++] = nums[dq.peekFirst()];
        }
        return res;
    }
}"""
)

# 153. Continuous Subarrays
add_prob(
    "oa_153_continuous_subarrays", "Continuous Subarrays", "O(n)", "O(k)", ["Monotonic Queue", "Sliding Window"], "Medium", ["monotonic_queue", "sliding_window"],
    """#include <vector>
#include <deque>
using namespace std;
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        deque<int> max_dq, min_dq;
        int left = 0;
        long long ans = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            while (!max_dq.empty() && nums[max_dq.back()] < nums[right]) max_dq.pop_back();
            while (!min_dq.empty() && nums[min_dq.back()] > nums[right]) min_dq.pop_back();
            max_dq.push_back(right);
            min_dq.push_back(right);
            while (nums[max_dq.front()] - nums[min_dq.front()] > 2) {
                if (max_dq.front() == left) max_dq.pop_front();
                if (min_dq.front() == left) min_dq.pop_front();
                left++;
            }
            ans += (right - left + 1);
        }
        return ans;
    }
};""",
    """import java.util.*;
class Solution {
    public long continuousSubarrays(int[] nums) {
        Deque<Integer> maxDq = new ArrayDeque<>();
        Deque<Integer> minDq = new ArrayDeque<>();
        int left = 0;
        long ans = 0;
        for (int right = 0; right < nums.length; right++) {
            while (!maxDq.isEmpty() && nums[maxDq.peekLast()] < nums[right]) maxDq.pollLast();
            while (!minDq.isEmpty() && nums[minDq.peekLast()] > nums[right]) minDq.pollLast();
            maxDq.offerLast(right);
            minDq.offerLast(right);
            while (nums[maxDq.peekFirst()] - nums[minDq.peekFirst()] > 2) {
                if (maxDq.peekFirst() == left) maxDq.pollFirst();
                if (minDq.peekFirst() == left) minDq.pollFirst();
                left++;
            }
            ans += (right - left + 1);
        }
        return ans;
    }
}"""
)

# 154. Find Longest Subarray With Max-Min Diff
add_prob(
    "oa_154_max_min_diff_subarray", "Subarray With Maximum Difference", "O(n)", "O(k)", ["Monotonic Queue", "Sliding Window"], "Medium", ["monotonic_queue"],
    """#include <vector>
#include <deque>
#include <algorithm>
using namespace std;
class Solution {
public:
    int longestSubarrayDiff(vector<int>& nums, int k) {
        deque<int> max_q, min_q;
        int left = 0, res = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            while (!max_q.empty() && nums[max_q.back()] <= nums[right]) max_q.pop_back();
            while (!min_q.empty() && nums[min_q.back()] >= nums[right]) min_q.pop_back();
            max_q.push_back(right);
            min_q.push_back(right);
            while (nums[max_q.front()] - nums[min_q.front()] > k) {
                if (max_q.front() == left) max_q.pop_front();
                if (min_q.front() == left) min_q.pop_front();
                left++;
            }
            res = max(res, right - left + 1);
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public int longestSubarrayDiff(int[] nums, int k) {
        Deque<Integer> maxQ = new ArrayDeque<>();
        Deque<Integer> minQ = new ArrayDeque<>();
        int left = 0, res = 0;
        for (int right = 0; right < nums.length; right++) {
            while (!maxQ.isEmpty() && nums[maxQ.peekLast()] <= nums[right]) maxQ.pollLast();
            while (!minQ.isEmpty() && nums[minQ.peekLast()] >= nums[right]) minQ.pollLast();
            maxQ.offerLast(right);
            minQ.offerLast(right);
            while (nums[maxQ.peekFirst()] - nums[minQ.peekFirst()] > k) {
                if (maxQ.peekFirst() == left) maxQ.pollFirst();
                if (minQ.peekFirst() == left) minQ.pollFirst();
                left++;
            }
            res = Math.max(res, right - left + 1);
        }
        return res;
    }
}"""
)

# 155. Delimited Sliding Window Max-Min Range
add_prob(
    "oa_155_sliding_window_range", "Sliding Window Range", "O(n)", "O(k)", ["Monotonic Queue"], "Medium", ["monotonic_queue"],
    """#include <vector>
#include <deque>
using namespace std;
class Solution {
public:
    vector<int> windowRange(vector<int>& nums, int k) {
        deque<int> max_dq;
        vector<int> res;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (!max_dq.empty() && max_dq.front() <= i - k) max_dq.pop_front();
            while (!max_dq.empty() && nums[max_dq.back()] <= nums[i]) max_dq.pop_back();
            max_dq.push_back(i);
            if (i >= k - 1) res.push_back(nums[max_dq.front()]);
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public int[] windowRange(int[] nums, int k) {
        Deque<Integer> maxDq = new ArrayDeque<>();
        int[] res = new int[nums.length - k + 1];
        int idx = 0;
        for (int i = 0; i < nums.length; i++) {
            if (!maxDq.isEmpty() && maxDq.peekFirst() <= i - k) maxDq.pollFirst();
            while (!maxDq.isEmpty() && nums[maxDq.peekLast()] <= nums[i]) maxDq.pollLast();
            maxDq.offerLast(i);
            if (i >= k - 1) res[idx++] = nums[maxDq.peekFirst()];
        }
        return res;
    }
}"""
)

# ==================== HEAP / PRIORITY QUEUE (156 - 170) ====================
# 156. Find Median from Data Stream
add_prob(
    "oa_156_find_median_data_stream", "Find Median from Data Stream", "O(n log n)", "O(n)", ["Two Heaps"], "Hard", ["heap", "two_heaps"],
    """#include <queue>
#include <vector>
using namespace std;
class MedianFinder {
    priority_queue<int> max_heap;
    priority_queue<int, vector<int>, greater<int>> min_heap;
public:
    MedianFinder() {}
    void addNum(int num) {
        max_heap.push(num);
        min_heap.push(max_heap.top());
        max_heap.pop();
        if (min_heap.size() > max_heap.size()) {
            max_heap.push(min_heap.top());
            min_heap.pop();
        }
    }
    double findMedian() {
        if (max_heap.size() > min_heap.size()) return max_heap.top();
        return (max_heap.top() + min_heap.top()) / 2.0;
    }
};""",
    """import java.util.*;
class MedianFinder {
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    public MedianFinder() {}
    public void addNum(int num) {
        maxHeap.offer(num);
        minHeap.offer(maxHeap.poll());
        if (minHeap.size() > maxHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
    }
    public double findMedian() {
        if (maxHeap.size() > minHeap.size()) return maxHeap.peek();
        return (maxHeap.peek() + minHeap.peek()) / 2.0;
    }
}"""
)

# 157. Sliding Window Median
add_prob(
    "oa_157_sliding_window_median", "Sliding Window Median", "O(n log n)", "O(n)", ["Two Heaps"], "Hard", ["heap", "two_heaps"],
    """#include <queue>
#include <vector>
using namespace std;
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        priority_queue<int> max_heap;
        priority_queue<int, vector<int>, greater<int>> min_heap;
        vector<double> res;
        for (int i = 0; i < (int)nums.size(); i++) {
            max_heap.push(nums[i]);
            min_heap.push(max_heap.top());
            max_heap.pop();
            if (min_heap.size() > max_heap.size()) {
                max_heap.push(min_heap.top());
                min_heap.pop();
            }
            if (i >= k - 1) {
                res.push_back(max_heap.top());
            }
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        double[] res = new double[nums.length - k + 1];
        int idx = 0;
        for (int i = 0; i < nums.length; i++) {
            maxHeap.offer(nums[i]);
            minHeap.offer(maxHeap.poll());
            if (minHeap.size() > maxHeap.size()) {
                maxHeap.offer(minHeap.poll());
            }
            if (i >= k - 1) {
                res[idx++] = maxHeap.peek();
            }
        }
        return res;
    }
}"""
)

# 158. Top K Frequent Elements
add_prob(
    "oa_158_top_k_frequent", "Top K Frequent Elements", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Medium", ["heap", "hash"],
    """#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int x : nums) count[x]++;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (auto& p : count) {
            pq.push({p.second, p.first});
            if (pq.size() > k) pq.pop();
        }
        vector<int> res;
        while (!pq.empty()) {
            res.push_back(pq.top().second);
            pq.pop();
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int x : nums) count.put(x, count.getOrDefault(x, 0) + 1);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        for (int key : count.keySet()) {
            pq.offer(new int[]{count.get(key), key});
            if (pq.size() > k) pq.poll();
        }
        int[] res = new int[k];
        for (int i = 0; i < k; i++) res[i] = pq.poll()[1];
        return res;
    }
}"""
)

# 159. Top K Frequent Words
add_prob(
    "oa_159_top_k_frequent_words", "Top K Frequent Words", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Medium", ["heap", "string"],
    """#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> count;
        for (auto& w : words) count[w]++;
        auto cmp = [](const pair<int, string>& a, const pair<int, string>& b) {
            return a.first > b.first || (a.first == b.first && a.second < b.second);
        };
        priority_queue<pair<int, string>, vector<pair<int, string>>, decltype(cmp)> pq(cmp);
        for (auto& p : count) {
            pq.push({p.second, p.first});
            if (pq.size() > k) pq.pop();
        }
        vector<string> res(k);
        for (int i = k - 1; i >= 0; i--) {
            res[i] = pq.top().second;
            pq.pop();
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> count = new HashMap<>();
        for (String w : words) count.put(w, count.getOrDefault(w, 0) + 1);
        PriorityQueue<String> pq = new PriorityQueue<>((a, b) -> count.get(a).equals(count.get(b)) ? b.compareTo(a) : count.get(a) - count.get(b));
        for (String w : count.keySet()) {
            pq.offer(w);
            if (pq.size() > k) pq.poll();
        }
        List<String> res = new ArrayList<>();
        while (!pq.isEmpty()) res.add(0, pq.poll());
        return res;
    }
}"""
)

# 160. Merge k Sorted Lists
add_prob(
    "oa_160_merge_k_sorted_lists", "Merge k Sorted Lists", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Hard", ["heap", "linked_list"],
    """#include <vector>
#include <queue>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq(cmp);
        for (auto l : lists) if (l) pq.push(l);
        ListNode dummy(0);
        ListNode* tail = &dummy;
        while (!pq.empty()) {
            ListNode* top = pq.top();
            pq.pop();
            tail->next = top;
            tail = tail->next;
            if (top->next) pq.push(top->next);
        }
        return dummy.next;
    }
};""",
    """import java.util.*;
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
        for (ListNode l : lists) if (l != null) pq.offer(l);
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (!pq.isEmpty()) {
            ListNode top = pq.poll();
            tail.next = top;
            tail = tail.next;
            if (top.next != null) pq.offer(top.next);
        }
        return dummy.next;
    }
}"""
)

# 161. Smallest Range Covering Elements from K Lists
add_prob(
    "oa_161_smallest_range_k_lists", "Smallest Range from K Lists", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Hard", ["heap"],
    """#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        struct Element { int val, r, c; };
        auto cmp = [](const Element& a, const Element& b) { return a.val > b.val; };
        priority_queue<Element, vector<Element>, decltype(cmp)> pq(cmp);
        int max_val = -1e9;
        for (int i = 0; i < (int)nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
            max_val = max(max_val, nums[i][0]);
        }
        int range_start = 0, range_end = 1e9;
        while (pq.size() == nums.size()) {
            Element curr = pq.top();
            pq.pop();
            if (max_val - curr.val < range_end - range_start) {
                range_start = curr.val;
                range_end = max_val;
            }
            if (curr.c + 1 < (int)nums[curr.r].size()) {
                int next_val = nums[curr.r][curr.c + 1];
                pq.push({next_val, curr.r, curr.c + 1});
                max_val = max(max_val, next_val);
            }
        }
        return {range_start, range_end};
    }
};""",
    """import java.util.*;
class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int maxVal = -1000000000;
        for (int i = 0; i < nums.size(); i++) {
            pq.offer(new int[]{nums.get(i).get(0), i, 0});
            maxVal = Math.max(maxVal, nums.get(i).get(0));
        }
        int rangeStart = 0, rangeEnd = 1000000000;
        while (pq.size() == nums.size()) {
            int[] curr = pq.poll();
            if (maxVal - curr[0] < rangeEnd - rangeStart) {
                rangeStart = curr[0];
                rangeEnd = maxVal;
            }
            if (curr[2] + 1 < nums.get(curr[1]).size()) {
                int nextVal = nums.get(curr[1]).get(curr[2] + 1);
                pq.offer(new int[]{nextVal, curr[1], curr[2] + 1});
                maxVal = Math.max(maxVal, nextVal);
            }
        }
        return new int[]{rangeStart, rangeEnd};
    }
}"""
)

# 162. Find K Pairs with Smallest Sums
add_prob(
    "oa_162_k_pairs_smallest_sums", "K Pairs with Smallest Sums", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Medium", ["heap"],
    """#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        auto cmp = [&](const pair<int, int>& a, const pair<int, int>& b) {
            return nums1[a.first] + nums2[a.second] > nums1[b.first] + nums2[b.second];
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);
        for (int i = 0; i < min((int)nums1.size(), k); i++) pq.push({i, 0});
        vector<vector<int>> res;
        while (!pq.empty() && (int)res.size() < k) {
            auto curr = pq.top();
            pq.pop();
            res.push_back({nums1[curr.first], nums2[curr.second]});
            if (curr.second + 1 < (int)nums2.size()) pq.push({curr.first, curr.second + 1});
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (nums1[a[0]] + nums2[a[1]]) - (nums1[b[0]] + nums2[b[1]]));
        for (int i = 0; i < Math.min(nums1.length, k); i++) pq.offer(new int[]{i, 0});
        List<List<Integer>> res = new ArrayList<>();
        while (!pq.isEmpty() && res.size() < k) {
            int[] curr = pq.poll();
            res.add(Arrays.asList(nums1[curr[0]], nums2[curr[1]]));
            if (curr[1] + 1 < nums2.length) pq.offer(new int[]{curr[0], curr[1] + 1});
        }
        return res;
    }
}"""
)

# 163. Reorganize String
add_prob(
    "oa_163_reorganize_string", "Reorganize String", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Medium", ["heap", "string"],
    """#include <string>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;
class Solution {
public:
    string reorganizeString(string s) {
        unordered_map<char, int> count;
        for (char c : s) count[c]++;
        priority_queue<pair<int, char>> pq;
        for (auto& p : count) pq.push({p.second, p.first});
        string res = "";
        pair<int, char> prev = {0, '#'};
        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();
            res += curr.second;
            if (prev.first > 0) pq.push(prev);
            curr.first--;
            prev = curr;
        }
        return res.length() == s.length() ? res : "";
    }
};""",
    """import java.util.*;
class Solution {
    public String reorganizeString(String s) {
        Map<Character, Integer> count = new HashMap<>();
        for (char c : s.toCharArray()) count.put(c, count.getOrDefault(c, 0) + 1);
        PriorityQueue<Character> pq = new PriorityQueue<>((a, b) -> count.get(b) - count.get(a));
        pq.addAll(count.keySet());
        StringBuilder res = new StringBuilder();
        while (pq.size() >= 2) {
            char c1 = pq.poll();
            char c2 = pq.poll();
            res.append(c1).append(c2);
            count.put(c1, count.get(c1) - 1);
            count.put(c2, count.get(c2) - 1);
            if (count.get(c1) > 0) pq.offer(c1);
            if (count.get(c2) > 0) pq.offer(c2);
        }
        if (!pq.isEmpty()) {
            char c = pq.poll();
            if (count.get(c) > 1) return "";
            res.append(c);
        }
        return res.toString();
    }
}"""
)

# 164. Task Scheduler
add_prob(
    "oa_164_task_scheduler", "Task Scheduler", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Medium", ["heap"],
    """#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> count;
        for (char c : tasks) count[c]++;
        priority_queue<int> pq;
        for (auto& p : count) pq.push(p.second);
        int time = 0;
        while (!pq.empty()) {
            vector<int> temp;
            int cycle = n + 1;
            while (cycle > 0 && !pq.empty()) {
                int top = pq.top();
                pq.pop();
                if (top > 1) temp.push_back(top - 1);
                time++;
                cycle--;
            }
            for (int x : temp) pq.push(x);
            if (pq.empty()) break;
            time += cycle;
        }
        return time;
    }
};""",
    """import java.util.*;
class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> count = new HashMap<>();
        for (char c : tasks) count.put(c, count.getOrDefault(c, 0) + 1);
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        pq.addAll(count.values());
        int time = 0;
        while (!pq.isEmpty()) {
            List<Integer> temp = new ArrayList<>();
            int cycle = n + 1;
            while (cycle > 0 && !pq.isEmpty()) {
                int top = pq.poll();
                if (top > 1) temp.add(top - 1);
                time++;
                cycle--;
            }
            pq.addAll(temp);
            if (pq.isEmpty()) break;
            time += cycle;
        }
        return time;
    }
}"""
)

# 165. IPO
add_prob(
    "oa_165_ipo", "IPO", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Hard", ["heap", "greedy"],
    """#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        vector<pair<int, int>> projects(n);
        for (int i = 0; i < n; i++) projects[i] = {capital[i], profits[i]};
        sort(projects.begin(), projects.end());
        priority_queue<int> pq;
        int idx = 0;
        for (int i = 0; i < k; i++) {
            while (idx < n && projects[idx].first <= w) {
                pq.push(projects[idx].second);
                idx++;
            }
            if (pq.empty()) break;
            w += pq.top();
            pq.pop();
        }
        return w;
    }
};""",
    """import java.util.*;
class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        int[][] projects = new int[n][2];
        for (int i = 0; i < n; i++) {
            projects[i][0] = capital[i];
            projects[i][1] = profits[i];
        }
        Arrays.sort(projects, (a, b) -> a[0] - b[0]);
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int idx = 0;
        for (int i = 0; i < k; i++) {
            while (idx < n && projects[idx][0] <= w) {
                pq.offer(projects[idx][1]);
                idx++;
            }
            if (pq.isEmpty()) break;
            w += pq.poll();
        }
        return w;
    }
}"""
)

# 166. Furthest Building You Can Reach
add_prob(
    "oa_166_furthest_building", "Furthest Building You Can Reach", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Medium", ["heap"],
    """#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int i = 0; i < (int)heights.size() - 1; i++) {
            int diff = heights[i + 1] - heights[i];
            if (diff > 0) {
                pq.push(diff);
                if (pq.size() > ladders) {
                    bricks -= pq.top();
                    pq.pop();
                    if (bricks < 0) return i;
                }
            }
        }
        return (int)heights.size() - 1;
    }
};""",
    """import java.util.*;
class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < heights.length - 1; i++) {
            int diff = heights[i + 1] - heights[i];
            if (diff > 0) {
                pq.offer(diff);
                if (pq.size() > ladders) {
                    bricks -= pq.poll();
                    if (bricks < 0) return i;
                }
            }
        }
        return heights.length - 1;
    }
}"""
)

# 167. Maximum Subsequence Score
add_prob(
    "oa_167_max_subsequence_score", "Maximum Subsequence Score", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Medium", ["heap", "sorting"],
    """#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        vector<pair<int, int>> pairs(n);
        for (int i = 0; i < n; i++) pairs[i] = {nums2[i], nums1[i]};
        sort(pairs.rbegin(), pairs.rend());
        priority_queue<int, vector<int>, greater<int>> pq;
        long long accum_score = 0, best = 0;
        for (int i = 0; i < n; i++) {
            accum_score += pairs[i].second;
            pq.push(pairs[i].second);
            if (pq.size() > k) {
                accum_score -= pq.top();
                pq.pop();
            }
            if (pq.size() == k) best = max(best, accum_score * pairs[i].first);
        }
        return best;
    }
};""",
    """import java.util.*;
class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        int[][] pairs = new int[n][2];
        for (int i = 0; i < n; i++) {
            pairs[i][0] = nums2[i];
            pairs[i][1] = nums1[i];
        }
        Arrays.sort(pairs, (a, b) -> b[0] - a[0]);
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        long accumScore = 0, best = 0;
        for (int i = 0; i < n; i++) {
            accumScore += pairs[i][1];
            pq.offer(pairs[i][1]);
            if (pq.size() > k) {
                accumScore -= pq.poll();
            }
            if (pq.size() == k) best = Math.max(best, accumScore * pairs[i][0]);
        }
        return best;
    }
}"""
)

# 168. Total Cost to Hire K Workers
add_prob(
    "oa_168_total_cost_hire_k_workers", "Total Cost to Hire K Workers", "O(n log n)", "O(n)", ["Two Heaps", "Two Pointers"], "Medium", ["heap", "two_heaps"],
    """#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        priority_queue<int, vector<int>, greater<int>> min_heap;
        priority_queue<int, vector<int>, greater<int>> max_heap;
        int i = 0, j = (int)costs.size() - 1;
        long long total = 0;
        while (k > 0) {
            while (min_heap.size() < candidates && i <= j) min_heap.push(costs[i++]);
            while (max_heap.size() < candidates && i <= j) max_heap.push(costs[j--]);
            int a = !min_heap.empty() ? min_heap.top() : 2e9;
            int b = !max_heap.empty() ? max_heap.top() : 2e9;
            if (a <= b) {
                total += a;
                min_heap.pop();
            } else {
                total += b;
                max_heap.pop();
            }
            k--;
        }
        return total;
    }
};""",
    """import java.util.*;
class Solution {
    public long totalCost(int[] costs, int k, int candidates) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        int i = 0, j = costs.length - 1;
        long total = 0;
        while (k > 0) {
            while (minHeap.size() < candidates && i <= j) minHeap.offer(costs[i++]);
            while (maxHeap.size() < candidates && i <= j) maxHeap.offer(costs[j--]);
            int a = !minHeap.isEmpty() ? minHeap.peek() : Integer.MAX_VALUE;
            int b = !maxHeap.isEmpty() ? maxHeap.peek() : Integer.MAX_VALUE;
            if (a <= b) {
                total += a;
                minHeap.poll();
            } else {
                total += b;
                maxHeap.poll();
            }
            k--;
        }
        return total;
    }
}"""
)

# 169. Single-Threaded CPU
add_prob(
    "oa_169_single_threaded_cpu", "Single-Threaded CPU", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Medium", ["heap", "sorting"],
    """#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int n = tasks.size();
        vector<vector<int>> indexed(n);
        for (int i = 0; i < n; i++) indexed[i] = {tasks[i][0], tasks[i][1], i};
        sort(indexed.begin(), indexed.end());
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<int> res;
        long long time = 0;
        int idx = 0;
        while (idx < n || !pq.empty()) {
            if (pq.empty() && time < indexed[idx][0]) time = indexed[idx][0];
            while (idx < n && indexed[idx][0] <= time) {
                pq.push({indexed[idx][1], indexed[idx][2]});
                idx++;
            }
            auto curr = pq.top();
            pq.pop();
            time += curr.first;
            res.push_back(curr.second);
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public int[] getOrder(int[][] tasks) {
        int n = tasks.length;
        int[][] indexed = new int[n][3];
        for (int i = 0; i < n; i++) {
            indexed[i][0] = tasks[i][0];
            indexed[i][1] = tasks[i][1];
            indexed[i][2] = i;
        }
        Arrays.sort(indexed, (a, b) -> a[0] - b[0]);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        int[] res = new int[n];
        long time = 0;
        int idx = 0, resIdx = 0;
        while (idx < n || !pq.isEmpty()) {
            if (pq.isEmpty() && time < indexed[idx][0]) time = indexed[idx][0];
            while (idx < n && indexed[idx][0] <= time) {
                pq.offer(new int[]{indexed[idx][1], indexed[idx][2]});
                idx++;
            }
            int[] curr = pq.poll();
            time += curr[0];
            res[resIdx++] = curr[1];
        }
        return res;
    }
}"""
)

# 170. Seat Reservation Manager
add_prob(
    "oa_170_seat_manager", "Seat Reservation Manager", "O(n log n)", "O(n)", ["Heap / Priority Queue"], "Medium", ["heap"],
    """#include <queue>
#include <vector>
using namespace std;
class SeatManager {
    priority_queue<int, vector<int>, greater<int>> pq;
public:
    SeatManager(int n) {
        for (int i = 1; i <= n; i++) pq.push(i);
    }
    int reserve() {
        int seat = pq.top();
        pq.pop();
        return seat;
    }
    void unreserve(int seatNumber) {
        pq.push(seatNumber);
    }
};""",
    """import java.util.*;
class SeatManager {
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    public SeatManager(int n) {
        for (int i = 1; i <= n; i++) pq.offer(i);
    }
    public int reserve() {
        return pq.poll();
    }
    public void unreserve(int seatNumber) {
        pq.offer(seatNumber);
    }
}"""
)

# ==================== BFS & 0-1 BFS (171 - 180) ====================
# 171. Shortest Path in Binary Matrix
add_prob(
    "oa_171_shortest_path_binary_matrix", "Shortest Path in Binary Matrix", "O(V + E)", "O(V + E)", ["BFS"], "Medium", ["bfs", "graph"],
    """#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) return -1;
        queue<pair<int, int>> q;
        q.push({0, 0});
        grid[0][0] = 1;
        int steps = 1;
        while (!q.empty()) {
            int sz = q.size();
            while (sz--) {
                auto [r, c] = q.front();
                q.pop();
                if (r == n - 1 && c == n - 1) return steps;
                for (int dr = -1; dr <= 1; dr++) {
                    for (int dc = -1; dc <= 1; dc++) {
                        int nr = r + dr, nc = c + dc;
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                            grid[nr][nc] = 1;
                            q.push({nr, nc});
                        }
                    }
                }
            }
            steps++;
        }
        return -1;
    }
};""",
    """import java.util.*;
class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) return -1;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0});
        grid[0][0] = 1;
        int steps = 1;
        while (!q.isEmpty()) {
            int sz = q.size();
            while (sz-- > 0) {
                int[] curr = q.poll();
                if (curr[0] == n - 1 && curr[1] == n - 1) return steps;
                for (int dr = -1; dr <= 1; dr++) {
                    for (int dc = -1; dc <= 1; dc++) {
                        int nr = curr[0] + dr, nc = curr[1] + dc;
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                            grid[nr][nc] = 1;
                            q.offer(new int[]{nr, nc});
                        }
                    }
                }
            }
            steps++;
        }
        return -1;
    }
}"""
)

# 172. Word Ladder
add_prob(
    "oa_172_word_ladder", "Word Ladder", "O(V + E)", "O(V + E)", ["BFS"], "Hard", ["bfs", "string"],
    """#include <vector>
#include <string>
#include <queue>
#include <unordered_set>
using namespace std;
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        if (!dict.count(endWord)) return 0;
        queue<string> q;
        q.push(beginWord);
        int steps = 1;
        while (!q.empty()) {
            int sz = q.size();
            while (sz--) {
                string w = q.front();
                q.pop();
                if (w == endWord) return steps;
                for (int i = 0; i < (int)w.size(); i++) {
                    char orig = w[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        w[i] = c;
                        if (dict.count(w)) {
                            dict.erase(w);
                            q.push(w);
                        }
                    }
                    w[i] = orig;
                }
            }
            steps++;
        }
        return 0;
    }
};""",
    """import java.util.*;
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> dict = new HashSet<>(wordList);
        if (!dict.contains(endWord)) return 0;
        Queue<String> q = new LinkedList<>();
        q.offer(beginWord);
        int steps = 1;
        while (!q.isEmpty()) {
            int sz = q.size();
            while (sz-- > 0) {
                String w = q.poll();
                if (w.equals(endWord)) return steps;
                char[] chs = w.toCharArray();
                for (int i = 0; i < chs.length; i++) {
                    char orig = chs[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        chs[i] = c;
                        String next = new String(chs);
                        if (dict.contains(next)) {
                            dict.remove(next);
                            q.offer(next);
                        }
                    }
                    chs[i] = orig;
                }
            }
            steps++;
        }
        return 0;
    }
}"""
)

# 173. Open the Lock
add_prob(
    "oa_173_open_the_lock", "Open the Lock", "O(V + E)", "O(V + E)", ["BFS"], "Medium", ["bfs"],
    """#include <vector>
#include <string>
#include <queue>
#include <unordered_set>
using namespace std;
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> dead(deadends.begin(), deadends.end());
        if (dead.count("0000")) return -1;
        queue<string> q;
        q.push("0000");
        dead.insert("0000");
        int steps = 0;
        while (!q.empty()) {
            int sz = q.size();
            while (sz--) {
                string curr = q.front();
                q.pop();
                if (curr == target) return steps;
                for (int i = 0; i < 4; i++) {
                    for (int d = -1; d <= 1; d += 2) {
                        string next = curr;
                        next[i] = (next[i] - '0' + d + 10) % 10 + '0';
                        if (!dead.count(next)) {
                            dead.insert(next);
                            q.push(next);
                        }
                    }
                }
            }
            steps++;
        }
        return -1;
    }
};""",
    """import java.util.*;
class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> dead = new HashSet<>(Arrays.asList(deadends));
        if (dead.contains("0000")) return -1;
        Queue<String> q = new LinkedList<>();
        q.offer("0000");
        dead.add("0000");
        int steps = 0;
        while (!q.isEmpty()) {
            int sz = q.size();
            while (sz-- > 0) {
                String curr = q.poll();
                if (curr.equals(target)) return steps;
                for (int i = 0; i < 4; i++) {
                    for (int d = -1; d <= 1; d += 2) {
                        char[] chs = curr.toCharArray();
                        chs[i] = (char)((chs[i] - '0' + d + 10) % 10 + '0');
                        String next = new String(chs);
                        if (!dead.contains(next)) {
                            dead.add(next);
                            q.offer(next);
                        }
                    }
                }
            }
            steps++;
        }
        return -1;
    }
}"""
)

# 174. Minimum Depth of Binary Tree
add_prob(
    "oa_174_min_depth_binary_tree", "Minimum Depth of Binary Tree", "O(V + E)", "O(V + E)", ["BFS"], "Easy", ["bfs", "tree"],
    """#include <queue>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> q;
        q.push(root);
        int depth = 1;
        while (!q.empty()) {
            int sz = q.size();
            while (sz--) {
                TreeNode* node = q.front();
                q.pop();
                if (!node->left && !node->right) return depth;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            depth++;
        }
        return depth;
    }
};""",
    """import java.util.*;
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int depth = 1;
        while (!q.isEmpty()) {
            int sz = q.size();
            while (sz-- > 0) {
                TreeNode node = q.poll();
                if (node.left == null && node.right == null) return depth;
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
            depth++;
        }
        return depth;
    }
}"""
)

# 175. Bus Routes
add_prob(
    "oa_175_bus_routes", "Bus Routes", "O(V + E)", "O(V + E)", ["BFS"], "Hard", ["bfs", "graph"],
    """#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;
class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target) return 0;
        unordered_map<int, vector<int>> stop_to_routes;
        for (int i = 0; i < (int)routes.size(); i++) {
            for (int stop : routes[i]) stop_to_routes[stop].push_back(i);
        }
        queue<int> q;
        unordered_set<int> visited_routes;
        q.push(source);
        int buses = 0;
        while (!q.empty()) {
            int sz = q.size();
            buses++;
            while (sz--) {
                int stop = q.front();
                q.pop();
                for (int r : stop_to_routes[stop]) {
                    if (visited_routes.count(r)) continue;
                    visited_routes.insert(r);
                    for (int next_stop : routes[r]) {
                        if (next_stop == target) return buses;
                        q.push(next_stop);
                    }
                }
            }
        }
        return -1;
    }
};""",
    """import java.util.*;
class Solution {
    public int numBusesToDestination(int[][] routes, int source, int target) {
        if (source == target) return 0;
        Map<Integer, List<Integer>> stopToRoutes = new HashMap<>();
        for (int i = 0; i < routes.length; i++) {
            for (int stop : routes[i]) {
                stopToRoutes.computeIfAbsent(stop, k -> new ArrayList<>()).add(i);
            }
        }
        Queue<Integer> q = new LinkedList<>();
        Set<Integer> visitedRoutes = new HashSet<>();
        q.offer(source);
        int buses = 0;
        while (!q.isEmpty()) {
            int sz = q.size();
            buses++;
            while (sz-- > 0) {
                int stop = q.poll();
                for (int r : stopToRoutes.getOrDefault(stop, Collections.emptyList())) {
                    if (visitedRoutes.contains(r)) continue;
                    visitedRoutes.add(r);
                    for (int nextStop : routes[r]) {
                        if (nextStop == target) return buses;
                        q.offer(nextStop);
                    }
                }
            }
        }
        return -1;
    }
}"""
)

# 176. Snakes and Ladders
add_prob(
    "oa_176_snakes_and_ladders", "Snakes and Ladders", "O(V + E)", "O(V + E)", ["BFS"], "Medium", ["bfs"],
    """#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        auto get_pos = [&](int s) -> pair<int, int> {
            int r = (s - 1) / n;
            int c = (s - 1) % n;
            if (r % 2 == 1) c = n - 1 - c;
            return {n - 1 - r, c};
        };
        vector<int> dist(n * n + 1, -1);
        queue<int> q;
        q.push(1);
        dist[1] = 0;
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            if (curr == n * n) return dist[curr];
            for (int i = 1; i <= 6 && curr + i <= n * n; i++) {
                int next = curr + i;
                auto [r, c] = get_pos(next);
                if (board[r][c] != -1) next = board[r][c];
                if (dist[next] == -1) {
                    dist[next] = dist[curr] + 1;
                    q.push(next);
                }
            }
        }
        return -1;
    }
};""",
    """import java.util.*;
class Solution {
    public int snakesAndLadders(int[][] board) {
        int n = board.length;
        int[] dist = new int[n * n + 1];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new LinkedList<>();
        q.offer(1);
        dist[1] = 0;
        while (!q.isEmpty()) {
            int curr = q.poll();
            if (curr == n * n) return dist[curr];
            for (int i = 1; i <= 6 && curr + i <= n * n; i++) {
                int next = curr + i;
                int r = (next - 1) / n;
                int c = (next - 1) % n;
                if (r % 2 == 1) c = n - 1 - c;
                r = n - 1 - r;
                if (board[r][c] != -1) next = board[r][c];
                if (dist[next] == -1) {
                    dist[next] = dist[curr] + 1;
                    q.offer(next);
                }
            }
        }
        return -1;
    }
}"""
)

# 177. Jump Game III
add_prob(
    "oa_177_jump_game_iii", "Jump Game III", "O(V + E)", "O(V + E)", ["BFS"], "Medium", ["bfs"],
    """#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        queue<int> q;
        vector<bool> visited(n, false);
        q.push(start);
        visited[start] = true;
        while (!q.empty()) {
            int idx = q.front();
            q.pop();
            if (arr[idx] == 0) return true;
            for (int next : {idx + arr[idx], idx - arr[idx]}) {
                if (next >= 0 && next < n && !visited[next]) {
                    visited[next] = true;
                    q.push(next);
                }
            }
        }
        return false;
    }
};""",
    """import java.util.*;
class Solution {
    public boolean canReach(int[] arr, int start) {
        int n = arr.length;
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[n];
        q.offer(start);
        visited[start] = true;
        while (!q.isEmpty()) {
            int idx = q.poll();
            if (arr[idx] == 0) return true;
            int[] nexts = new int[]{idx + arr[idx], idx - arr[idx]};
            for (int next : nexts) {
                if (next >= 0 && next < n && !visited[next]) {
                    visited[next] = true;
                    q.offer(next);
                }
            }
        }
        return false;
    }
}"""
)

# 178. Minimum Genetic Mutation
add_prob(
    "oa_178_min_genetic_mutation", "Minimum Genetic Mutation", "O(V + E)", "O(V + E)", ["BFS"], "Medium", ["bfs", "string"],
    """#include <vector>
#include <string>
#include <queue>
#include <unordered_set>
using namespace std;
class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        unordered_set<string> valid(bank.begin(), bank.end());
        if (!valid.count(endGene)) return -1;
        queue<string> q;
        q.push(startGene);
        int steps = 0;
        char genes[] = {'A', 'C', 'G', 'T'};
        while (!q.empty()) {
            int sz = q.size();
            while (sz--) {
                string curr = q.front();
                q.pop();
                if (curr == endGene) return steps;
                for (int i = 0; i < 8; i++) {
                    char orig = curr[i];
                    for (char g : genes) {
                        curr[i] = g;
                        if (valid.count(curr)) {
                            valid.erase(curr);
                            q.push(curr);
                        }
                    }
                    curr[i] = orig;
                }
            }
            steps++;
        }
        return -1;
    }
};""",
    """import java.util.*;
class Solution {
    public int minMutation(String startGene, String endGene, String[] bank) {
        Set<String> valid = new HashSet<>(Arrays.asList(bank));
        if (!valid.contains(endGene)) return -1;
        Queue<String> q = new LinkedList<>();
        q.offer(startGene);
        int steps = 0;
        char[] genes = new char[]{'A', 'C', 'G', 'T'};
        while (!q.isEmpty()) {
            int sz = q.size();
            while (sz-- > 0) {
                String curr = q.poll();
                if (curr.equals(endGene)) return steps;
                char[] chs = curr.toCharArray();
                for (int i = 0; i < 8; i++) {
                    char orig = chs[i];
                    for (char g : genes) {
                        chs[i] = g;
                        String next = new String(chs);
                        if (valid.contains(next)) {
                            valid.remove(next);
                            q.offer(next);
                        }
                    }
                    chs[i] = orig;
                }
            }
            steps++;
        }
        return -1;
    }
}"""
)

# 179. Rotting Oranges
add_prob(
    "oa_179_rotting_oranges", "Rotting Oranges", "O(V + E)", "O(V + E)", ["BFS"], "Medium", ["bfs"],
    """#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        queue<pair<int, int>> q;
        int fresh = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) q.push({i, j});
                else if (grid[i][j] == 1) fresh++;
            }
        }
        int minutes = 0;
        int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!q.empty() && fresh > 0) {
            int sz = q.size();
            while (sz--) {
                auto [r, c] = q.front();
                q.pop();
                for (auto& d : dirs) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        fresh--;
                        q.push({nr, nc});
                    }
                }
            }
            minutes++;
        }
        return fresh == 0 ? minutes : -1;
    }
};""",
    """import java.util.*;
class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        int fresh = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) q.offer(new int[]{i, j});
                else if (grid[i][j] == 1) fresh++;
            }
        }
        int minutes = 0;
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!q.isEmpty() && fresh > 0) {
            int sz = q.size();
            while (sz-- > 0) {
                int[] curr = q.poll();
                for (int[] d : dirs) {
                    int nr = curr[0] + d[0], nc = curr[1] + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        fresh--;
                        q.offer(new int[]{nr, nc});
                    }
                }
            }
            minutes++;
        }
        return fresh == 0 ? minutes : -1;
    }
}"""
)

# 180. 0-1 BFS Valid Path in Grid
add_prob(
    "oa_180_zero_one_bfs_grid", "0-1 BFS Grid Path", "O(V + E)", "O(V + E)", ["BFS"], "Hard", ["bfs"],
    """#include <vector>
#include <deque>
using namespace std;
class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dist(m, vector<int>(n, 1e9));
        deque<pair<int, int>> dq;
        dist[0][0] = 0;
        dq.push_back({0, 0});
        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!dq.empty()) {
            auto [r, c] = dq.front();
            dq.pop_front();
            for (int i = 0; i < 4; i++) {
                int nr = r + dirs[i][0], nc = c + dirs[i][1];
                int cost = (grid[r][c] == i + 1) ? 0 : 1;
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && dist[r][c] + cost < dist[nr][nc]) {
                    dist[nr][nc] = dist[r][c] + cost;
                    if (cost == 0) dq.push_front({nr, nc});
                    else dq.push_back({nr, nc});
                }
            }
        }
        return dist[m - 1][n - 1];
    }
};""",
    """import java.util.*;
class Solution {
    public int minCost(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dist = new int[m][n];
        for (int[] row : dist) Arrays.fill(row, 1000000000);
        Deque<int[]> dq = new ArrayDeque<>();
        dist[0][0] = 0;
        dq.addLast(new int[]{0, 0});
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!dq.isEmpty()) {
            int[] curr = dq.pollFirst();
            int r = curr[0], c = curr[1];
            for (int i = 0; i < 4; i++) {
                int nr = r + dirs[i][0], nc = c + dirs[i][1];
                int cost = (grid[r][c] == i + 1) ? 0 : 1;
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && dist[r][c] + cost < dist[nr][nc]) {
                    dist[nr][nc] = dist[r][c] + cost;
                    if (cost == 0) dq.addFirst(new int[]{nr, nc});
                    else dq.addLast(new int[]{nr, nc});
                }
            }
        }
        return dist[m - 1][n - 1];
    }
}"""
)

# ==================== TOPOLOGICAL SORT (181 - 187) ====================
# 181. Course Schedule I
add_prob(
    "oa_181_course_schedule_i", "Course Schedule I", "O(V + E)", "O(V + E)", ["Topological Sort"], "Medium", ["topological_sort", "graph"],
    """#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> in_degree(numCourses, 0);
        for (auto& pre : prerequisites) {
            adj[pre[1]].push_back(pre[0]);
            in_degree[pre[0]]++;
        }
        queue<int> q;
        for (int i = 0; i < numCourses; i++) if (in_degree[i] == 0) q.push(i);
        int visited = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            visited++;
            for (int v : adj[u]) {
                in_degree[v]--;
                if (in_degree[v] == 0) q.push(v);
            }
        }
        return visited == numCourses;
    }
};""",
    """import java.util.*;
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        int[] inDegree = new int[numCourses];
        for (int[] pre : prerequisites) {
            adj.get(pre[1]).add(pre[0]);
            inDegree[pre[0]]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) if (inDegree[i] == 0) q.offer(i);
        int visited = 0;
        while (!q.isEmpty()) {
            int u = q.poll();
            visited++;
            for (int v : adj.get(u)) {
                inDegree[v]--;
                if (inDegree[v] == 0) q.offer(v);
            }
        }
        return visited == numCourses;
    }
}"""
)

# 182. Course Schedule II
add_prob(
    "oa_182_course_schedule_ii", "Course Schedule II", "O(V + E)", "O(V + E)", ["Topological Sort"], "Medium", ["topological_sort", "graph"],
    """#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> in_degree(numCourses, 0);
        for (auto& pre : prerequisites) {
            adj[pre[1]].push_back(pre[0]);
            in_degree[pre[0]]++;
        }
        queue<int> q;
        for (int i = 0; i < numCourses; i++) if (in_degree[i] == 0) q.push(i);
        vector<int> order;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            order.push_back(u);
            for (int v : adj[u]) {
                in_degree[v]--;
                if (in_degree[v] == 0) q.push(v);
            }
        }
        return order.size() == numCourses ? order : vector<int>{};
    }
};""",
    """import java.util.*;
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        int[] inDegree = new int[numCourses];
        for (int[] pre : prerequisites) {
            adj.get(pre[1]).add(pre[0]);
            inDegree[pre[0]]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) if (inDegree[i] == 0) q.offer(i);
        int[] order = new int[numCourses];
        int idx = 0;
        while (!q.isEmpty()) {
            int u = q.poll();
            order[idx++] = u;
            for (int v : adj.get(u)) {
                inDegree[v]--;
                if (inDegree[v] == 0) q.offer(v);
            }
        }
        return idx == numCourses ? order : new int[]{};
    }
}"""
)

# 183. Alien Dictionary
add_prob(
    "oa_183_alien_dictionary", "Alien Dictionary", "O(V + E)", "O(V + E)", ["Topological Sort"], "Hard", ["topological_sort", "string"],
    """#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;
class Solution {
public:
    string alienOrder(vector<string>& words) {
        unordered_map<char, unordered_set<char>> adj;
        unordered_map<char, int> in_degree;
        for (auto& w : words) for (char c : w) in_degree[c] = 0;
        for (int i = 0; i < (int)words.size() - 1; i++) {
            string w1 = words[i], w2 = words[i + 1];
            int len = min(w1.size(), w2.size());
            bool diff = false;
            for (int j = 0; j < len; j++) {
                if (w1[j] != w2[j]) {
                    if (!adj[w1[j]].count(w2[j])) {
                        adj[w1[j]].insert(w2[j]);
                        in_degree[w2[j]]++;
                    }
                    diff = true;
                    break;
                }
            }
            if (!diff && w1.size() > w2.size()) return "";
        }
        queue<char> q;
        for (auto& p : in_degree) if (p.second == 0) q.push(p.first);
        string res = "";
        while (!q.empty()) {
            char u = q.front();
            q.pop();
            res += u;
            for (char v : adj[u]) {
                in_degree[v]--;
                if (in_degree[v] == 0) q.push(v);
            }
        }
        return res.size() == in_degree.size() ? res : "";
    }
};""",
    """import java.util.*;
class Solution {
    public String alienOrder(String[] words) {
        Map<Character, Set<Character>> adj = new HashMap<>();
        Map<Character, Integer> inDegree = new HashMap<>();
        for (String w : words) for (char c : w.toCharArray()) inDegree.put(c, 0);
        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i], w2 = words[i + 1];
            int len = Math.min(w1.length(), w2.length());
            boolean diff = false;
            for (int j = 0; j < len; j++) {
                if (w1.charAt(j) != w2.charAt(j)) {
                    adj.computeIfAbsent(w1.charAt(j), k -> new HashSet<>());
                    if (adj.get(w1.charAt(j)).add(w2.charAt(j))) {
                        inDegree.put(w2.charAt(j), inDegree.get(w2.charAt(j)) + 1);
                    }
                    diff = true;
                    break;
                }
            }
            if (!diff && w1.length() > w2.length()) return "";
        }
        Queue<Character> q = new LinkedList<>();
        for (char c : inDegree.keySet()) if (inDegree.get(c) == 0) q.offer(c);
        StringBuilder res = new StringBuilder();
        while (!q.isEmpty()) {
            char u = q.poll();
            res.append(u);
            for (char v : adj.getOrDefault(u, Collections.emptySet())) {
                inDegree.put(v, inDegree.get(v) - 1);
                if (inDegree.get(v) == 0) q.offer(v);
            }
        }
        return res.length() == inDegree.size() ? res.toString() : "";
    }
}"""
)

# 184. Minimum Height Trees
add_prob(
    "oa_184_minimum_height_trees", "Minimum Height Trees", "O(V + E)", "O(V + E)", ["Topological Sort"], "Medium", ["topological_sort", "tree"],
    """#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) return {0};
        vector<vector<int>> adj(n);
        vector<int> in_degree(n, 0);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
            in_degree[e[0]]++;
            in_degree[e[1]]++;
        }
        queue<int> q;
        for (int i = 0; i < n; i++) if (in_degree[i] == 1) q.push(i);
        int remaining = n;
        while (remaining > 2) {
            int sz = q.size();
            remaining -= sz;
            while (sz--) {
                int u = q.front();
                q.pop();
                for (int v : adj[u]) {
                    in_degree[v]--;
                    if (in_degree[v] == 1) q.push(v);
                }
            }
        }
        vector<int> res;
        while (!q.empty()) {
            res.push_back(q.front());
            q.pop();
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return Collections.singletonList(0);
        List<Set<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new HashSet<>());
        int[] inDegree = new int[n];
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
            inDegree[e[0]]++;
            inDegree[e[1]]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < n; i++) if (inDegree[i] == 1) q.offer(i);
        int remaining = n;
        while (remaining > 2) {
            int sz = q.size();
            remaining -= sz;
            while (sz-- > 0) {
                int u = q.poll();
                for (int v : adj.get(u)) {
                    inDegree[v]--;
                    if (inDegree[v] == 1) q.offer(v);
                }
            }
        }
        return new ArrayList<>(q);
    }
}"""
)

# 185. Find Eventual Safe States
add_prob(
    "oa_185_eventual_safe_states", "Find Eventual Safe States", "O(V + E)", "O(V + E)", ["Topological Sort"], "Medium", ["topological_sort", "graph"],
    """#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<vector<int>> rev(n);
        vector<int> in_degree(n, 0);
        for (int i = 0; i < n; i++) {
            for (int v : graph[i]) {
                rev[v].push_back(i);
            }
            in_degree[i] = graph[i].size();
        }
        queue<int> q;
        for (int i = 0; i < n; i++) if (in_degree[i] == 0) q.push(i);
        vector<int> safe;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            safe.push_back(u);
            for (int v : rev[u]) {
                in_degree[v]--;
                if (in_degree[v] == 0) q.push(v);
            }
        }
        sort(safe.begin(), safe.end());
        return safe;
    }
};""",
    """import java.util.*;
class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        List<List<Integer>> rev = new ArrayList<>();
        for (int i = 0; i < n; i++) rev.add(new ArrayList<>());
        int[] inDegree = new int[n];
        for (int i = 0; i < n; i++) {
            for (int v : graph[i]) {
                rev.get(v).add(i);
            }
            inDegree[i] = graph[i].length;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < n; i++) if (inDegree[i] == 0) q.offer(i);
        List<Integer> safe = new ArrayList<>();
        while (!q.isEmpty()) {
            int u = q.poll();
            safe.add(u);
            for (int v : rev.get(u)) {
                inDegree[v]--;
                if (inDegree[v] == 0) q.offer(v);
            }
        }
        Collections.sort(safe);
        return safe;
    }
}"""
)

# 186. Loud and Rich
add_prob(
    "oa_186_loud_and_rich", "Loud and Rich", "O(V + E)", "O(V + E)", ["Topological Sort"], "Medium", ["topological_sort", "graph"],
    """#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
        int n = quiet.size();
        vector<vector<int>> adj(n);
        vector<int> in_degree(n, 0);
        for (auto& r : richer) {
            adj[r[0]].push_back(r[1]);
            in_degree[r[1]]++;
        }
        vector<int> ans(n);
        for (int i = 0; i < n; i++) ans[i] = i;
        queue<int> q;
        for (int i = 0; i < n; i++) if (in_degree[i] == 0) q.push(i);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (quiet[ans[u]] < quiet[ans[v]]) ans[v] = ans[u];
                in_degree[v]--;
                if (in_degree[v] == 0) q.push(v);
            }
        }
        return ans;
    }
};""",
    """import java.util.*;
class Solution {
    public int[] loudAndRich(int[][] richer, int[] quiet) {
        int n = quiet.length;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        int[] inDegree = new int[n];
        for (int[] r : richer) {
            adj.get(r[0]).add(r[1]);
            inDegree[r[1]]++;
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = i;
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < n; i++) if (inDegree[i] == 0) q.offer(i);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj.get(u)) {
                if (quiet[ans[u]] < quiet[ans[v]]) ans[v] = ans[u];
                inDegree[v]--;
                if (inDegree[v] == 0) q.offer(v);
            }
        }
        return ans;
    }
}"""
)

# 187. Sequence Reconstruction
add_prob(
    "oa_187_sequence_reconstruction", "Sequence Reconstruction", "O(V + E)", "O(V + E)", ["Topological Sort"], "Medium", ["topological_sort"],
    """#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    bool sequenceReconstruction(vector<int>& nums, vector<vector<int>>& sequences) {
        int n = nums.size();
        vector<vector<int>> adj(n + 1);
        vector<int> in_degree(n + 1, 0);
        for (auto& seq : sequences) {
            for (int i = 0; i < (int)seq.size() - 1; i++) {
                adj[seq[i]].push_back(seq[i + 1]);
                in_degree[seq[i + 1]]++;
            }
        }
        queue<int> q;
        for (int i = 1; i <= n; i++) if (in_degree[i] == 0) q.push(i);
        while (!q.empty()) {
            if (q.size() > 1) return false;
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                in_degree[v]--;
                if (in_degree[v] == 0) q.push(v);
            }
        }
        return true;
    }
};""",
    """import java.util.*;
class Solution {
    public boolean sequenceReconstruction(int[] nums, List<List<Integer>> sequences) {
        int n = nums.length;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        int[] inDegree = new int[n + 1];
        for (List<Integer> seq : sequences) {
            for (int i = 0; i < seq.size() - 1; i++) {
                adj.get(seq.get(i)).add(seq.get(i + 1));
                inDegree[seq.get(i + 1)]++;
            }
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= n; i++) if (inDegree[i] == 0) q.offer(i);
        while (!q.isEmpty()) {
            if (q.size() > 1) return false;
            int u = q.poll();
            for (int v : adj.get(u)) {
                inDegree[v]--;
                if (inDegree[v] == 0) q.offer(v);
            }
        }
        return true;
    }
}"""
)

# ==================== DSU / UNION-FIND (188 - 195) ====================
# 188. Number of Connected Components in an Undirected Graph
add_prob(
    "oa_188_number_connected_components", "Number of Connected Components", "O(n)", "O(n)", ["DSU"], "Medium", ["dsu", "graph"],
    """#include <vector>
#include <numeric>
using namespace std;
class Solution {
    vector<int> parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void union_set(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) parent[root_i] = root_j;
    }
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        int components = n;
        for (auto& e : edges) {
            int root_u = find(e[0]), root_v = find(e[1]);
            if (root_u != root_v) {
                union_set(root_u, root_v);
                components--;
            }
        }
        return components;
    }
};""",
    """import java.util.*;
class Solution {
    int[] parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unionSet(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI != rootJ) parent[rootI] = rootJ;
    }
    public int countComponents(int n, int[][] edges) {
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int components = n;
        for (int[] e : edges) {
            int rootU = find(e[0]), rootV = find(e[1]);
            if (rootU != rootV) {
                unionSet(rootU, rootV);
                components--;
            }
        }
        return components;
    }
}"""
)

# 189. Redundant Connection
add_prob(
    "oa_189_redundant_connection", "Redundant Connection", "O(n)", "O(n)", ["DSU"], "Medium", ["dsu", "graph"],
    """#include <vector>
#include <numeric>
using namespace std;
class Solution {
    vector<int> parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        parent.resize(n + 1);
        iota(parent.begin(), parent.end(), 0);
        for (auto& e : edges) {
            int root_u = find(e[0]);
            int root_v = find(e[1]);
            if (root_u == root_v) return e;
            parent[root_u] = root_v;
        }
        return {};
    }
};""",
    """import java.util.*;
class Solution {
    int[] parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        parent = new int[n + 1];
        for (int i = 0; i <= n; i++) parent[i] = i;
        for (int[] e : edges) {
            int rootU = find(e[0]);
            int rootV = find(e[1]);
            if (rootU == rootV) return e;
            parent[rootU] = rootV;
        }
        return new int[]{};
    }
}"""
)

# 190. Accounts Merge
add_prob(
    "oa_190_accounts_merge", "Accounts Merge", "O(n)", "O(n)", ["DSU"], "Medium", ["dsu"],
    """#include <vector>
#include <string>
#include <unordered_map>
#include <numeric>
using namespace std;
class Solution {
    vector<int> parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void union_set(int i, int j) {
        int ri = find(i), rj = find(j);
        if (ri != rj) parent[ri] = rj;
    }
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        int n = accounts.size();
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        unordered_map<string, int> email_to_id;
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < (int)accounts[i].size(); j++) {
                string email = accounts[i][j];
                if (email_to_id.count(email)) {
                    union_set(i, email_to_id[email]);
                } else {
                    email_to_id[email] = i;
                }
            }
        }
        return {};
    }
};""",
    """import java.util.*;
class Solution {
    int[] parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unionSet(int i, int j) {
        int ri = find(i), rj = find(j);
        if (ri != rj) parent[ri] = rj;
    }
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        int n = accounts.size();
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        Map<String, Integer> emailToId = new HashMap<>();
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < accounts.get(i).size(); j++) {
                String email = accounts.get(i).get(j);
                if (emailToId.containsKey(email)) {
                    unionSet(i, emailToId.get(email));
                } else {
                    emailToId.put(email, i);
                }
            }
        }
        return new ArrayList<>();
    }
}"""
)

# 191. Graph Valid Tree
add_prob(
    "oa_191_graph_valid_tree", "Graph Valid Tree", "O(n)", "O(n)", ["DSU"], "Medium", ["dsu", "graph", "tree"],
    """#include <vector>
#include <numeric>
using namespace std;
class Solution {
    vector<int> parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if ((int)edges.size() != n - 1) return false;
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        for (auto& e : edges) {
            int ru = find(e[0]), rv = find(e[1]);
            if (ru == rv) return false;
            parent[ru] = rv;
        }
        return true;
    }
};""",
    """import java.util.*;
class Solution {
    int[] parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int[] e : edges) {
            int ru = find(e[0]), rv = find(e[1]);
            if (ru == rv) return false;
            parent[ru] = rv;
        }
        return true;
    }
}"""
)

# 192. Number of Provinces
add_prob(
    "oa_192_number_of_provinces", "Number of Provinces", "O(n)", "O(n)", ["DSU"], "Medium", ["dsu", "graph"],
    """#include <vector>
#include <numeric>
using namespace std;
class Solution {
    vector<int> parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        int provinces = n;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    int ri = find(i), rj = find(j);
                    if (ri != rj) {
                        parent[ri] = rj;
                        provinces--;
                    }
                }
            }
        }
        return provinces;
    }
};""",
    """import java.util.*;
class Solution {
    int[] parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int provinces = n;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    int ri = find(i), rj = find(j);
                    if (ri != rj) {
                        parent[ri] = rj;
                        provinces--;
                    }
                }
            }
        }
        return provinces;
    }
}"""
)

# 193. Satisfiability of Equality Equations
add_prob(
    "oa_193_satisfiability_equality_equations", "Satisfiability of Equality Equations", "O(n)", "O(n)", ["DSU"], "Medium", ["dsu", "graph"],
    """#include <vector>
#include <string>
#include <numeric>
using namespace std;
class Solution {
    vector<int> parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
public:
    bool equationsPossible(vector<string>& equations) {
        parent.resize(26);
        iota(parent.begin(), parent.end(), 0);
        for (auto& eq : equations) {
            if (eq[1] == '=') {
                int u = eq[0] - 'a', v = eq[3] - 'a';
                parent[find(u)] = find(v);
            }
        }
        for (auto& eq : equations) {
            if (eq[1] == '!') {
                int u = eq[0] - 'a', v = eq[3] - 'a';
                if (find(u) == find(v)) return false;
            }
        }
        return true;
    }
};""",
    """import java.util.*;
class Solution {
    int[] parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    public boolean equationsPossible(String[] equations) {
        parent = new int[26];
        for (int i = 0; i < 26; i++) parent[i] = i;
        for (String eq : equations) {
            if (eq.charAt(1) == '=') {
                int u = eq.charAt(0) - 'a', v = eq.charAt(3) - 'a';
                parent[find(u)] = find(v);
            }
        }
        for (String eq : equations) {
            if (eq.charAt(1) == '!') {
                int u = eq.charAt(0) - 'a', v = eq.charAt(3) - 'a';
                if (find(u) == find(v)) return false;
            }
        }
        return true;
    }
}"""
)

# 194. Min Cost to Connect All Points (Kruskal MST)
add_prob(
    "oa_194_min_cost_connect_points", "Min Cost to Connect All Points", "O(E log V)", "O(V + E)", ["MST"], "Medium", ["mst", "dsu", "graph"],
    """#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric>
using namespace std;
class Solution {
    vector<int> parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        vector<vector<int>> edges;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                edges.push_back({d, i, j});
            }
        }
        sort(edges.begin(), edges.end());
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        int cost = 0, count = 0;
        for (auto& e : edges) {
            int ru = find(e[1]), rv = find(e[2]);
            if (ru != rv) {
                parent[ru] = rv;
                cost += e[0];
                count++;
                if (count == n - 1) break;
            }
        }
        return cost;
    }
};""",
    """import java.util.*;
class Solution {
    int[] parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int d = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                edges.add(new int[]{d, i, j});
            }
        }
        edges.sort((a, b) -> a[0] - b[0]);
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int cost = 0, count = 0;
        for (int[] e : edges) {
            int ru = find(e[1]), rv = find(e[2]);
            if (ru != rv) {
                parent[ru] = rv;
                cost += e[0];
                count++;
                if (count == n - 1) break;
            }
        }
        return cost;
    }
}"""
)

# 195. Smallest String With Swaps
add_prob(
    "oa_195_smallest_string_with_swaps", "Smallest String With Swaps", "O(n)", "O(n)", ["DSU"], "Medium", ["dsu", "string"],
    """#include <vector>
#include <string>
#include <numeric>
using namespace std;
class Solution {
    vector<int> parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        int n = s.size();
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        for (auto& p : pairs) {
            int ru = find(p[0]), rv = find(p[1]);
            if (ru != rv) parent[ru] = rv;
        }
        return s;
    }
};""",
    """import java.util.*;
class Solution {
    int[] parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        int n = s.length();
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (List<Integer> p : pairs) {
            int ru = find(p.get(0)), rv = find(p.get(1));
            if (ru != rv) parent[ru] = rv;
        }
        return s;
    }
}"""
)

# Generate corpus_part3.py
with open('benchmark/corpus/corpus_part3.py', 'w', encoding='utf-8') as f:
    f.write("# corpus_part3.py: Problems 146 to 195 (50 problems = 100 cases)\n")
    f.write("PART3_CASES = []\n\n")
    f.write("""def add_prob(pid, name, tc, sc, algos, rating, tags, cpp_code, java_code):
    PART3_CASES.append({
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
    PART3_CASES.append({
        "id": f"{pid}_java",
        "name": f"{name} (Java)",
        "language": "java",
        "rating": rating,
        "tags": tags,
        "expected_tc": tc,
        "expected_sc": sc,
        "expected_algorithms": algos,
        "code": java_code
    })\n\n""")
    for e in code_entries:
        f.write(f"# {e['id']}\n")
        f.write(f"add_prob(\n    {json.dumps(e['id'])}, {json.dumps(e['name'])}, {json.dumps(e['tc'])}, {json.dumps(e['sc'])}, {json.dumps(e['algos'])}, {json.dumps(e['rating'])}, {json.dumps(e['tags'])},\n")
        f.write(f"    '''{e['cpp']}''',\n")
        f.write(f"    '''{e['java']}'''\n)\n\n")
    f.write("print(f'Part 3 loaded with {len(PART3_CASES)} cases ({len(PART3_CASES)//2} problems: 146 to 195).')\n")

print(f"Successfully generated corpus_part3.py with {len(code_entries)} problems ({len(code_entries)*2} cases).")
