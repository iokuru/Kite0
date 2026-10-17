# corpus_part2.py: Problems 91 to 145 (55 distinct problems)
# Binary Search, Binary Search on Answer, Sorting, Intervals, Monotonic Stack

PART2_CASES = []

def add_prob(pid, name, tc, sc, algos, rating, tags, cpp_code, java_code):
    PART2_CASES.append({
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
    PART2_CASES.append({
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

# 91. Standard Binary Search
add_prob(
    "oa_091_binary_search_exact", "Binary Search Exact", "O(log n)", "O(1)", ["Binary Search"], "Easy", ["binary_search"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) l = mid + 1;
            else r = mid - 1;
        }
        return -1;
    }
};""",
    """class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) l = mid + 1;
            else r = mid - 1;
        }
        return -1;
    }
}"""
)

# 92. Search Insert Position
add_prob(
    "oa_092_search_insert_position", "Search Insert Position", "O(log n)", "O(1)", ["Binary Search"], "Easy", ["binary_search"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) l = mid + 1;
            else r = mid - 1;
        }
        return l;
    }
};""",
    """class Solution {
    public int searchInsert(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) l = mid + 1;
            else r = mid - 1;
        }
        return l;
    }
}"""
)

# 93. Find First and Last Position of Element
add_prob(
    "oa_093_first_last_position", "First Last Position in Sorted Array", "O(log n)", "O(1)", ["Binary Search"], "Medium", ["binary_search"],
    """#include <vector>
using namespace std;
class Solution {
    int findBound(vector<int>& nums, int target, bool isFirst) {
        int l = 0, r = nums.size() - 1, ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                ans = mid;
                if (isFirst) r = mid - 1;
                else l = mid + 1;
            } else if (nums[mid] < target) l = mid + 1;
            else r = mid - 1;
        }
        return ans;
    }
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        return {findBound(nums, target, true), findBound(nums, target, false)};
    }
};""",
    """class Solution {
    int findBound(int[] nums, int target, boolean isFirst) {
        int l = 0, r = nums.length - 1, ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                ans = mid;
                if (isFirst) r = mid - 1;
                else l = mid + 1;
            } else if (nums[mid] < target) l = mid + 1;
            else r = mid - 1;
        }
        return ans;
    }
    public int[] searchRange(int[] nums, int target) {
        return new int[]{findBound(nums, target, true), findBound(nums, target, false)};
    }
}"""
)

# 94. Search in Rotated Sorted Array II
add_prob(
    "oa_094_search_rotated_ii", "Search in Rotated Sorted Array II", "O(log n)", "O(1)", ["Binary Search"], "Medium", ["binary_search"],
    """#include <vector>
using namespace std;
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return true;
            if (nums[l] == nums[mid] && nums[mid] == nums[r]) {
                l++; r--;
            } else if (nums[l] <= nums[mid]) {
                if (nums[l] <= target && target < nums[mid]) r = mid - 1;
                else l = mid + 1;
            } else {
                if (nums[mid] < target && target <= nums[r]) l = mid + 1;
                else r = mid - 1;
            }
        }
        return false;
    }
};""",
    """class Solution {
    public boolean search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return true;
            if (nums[l] == nums[mid] && nums[mid] == nums[r]) {
                l++; r--;
            } else if (nums[l] <= nums[mid]) {
                if (nums[l] <= target && target < nums[mid]) r = mid - 1;
                else l = mid + 1;
            } else {
                if (nums[mid] < target && target <= nums[r]) l = mid + 1;
                else r = mid - 1;
            }
        }
        return false;
    }
}"""
)

# 95. Find Minimum in Rotated Sorted Array
add_prob(
    "oa_095_find_min_rotated", "Find Minimum in Rotated Sorted Array", "O(log n)", "O(1)", ["Binary Search"], "Medium", ["binary_search"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] < nums[r]) r = mid;
            else l = mid + 1;
        }
        return nums[l];
    }
};""",
    """class Solution {
    public int findMin(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] < nums[r]) r = mid;
            else l = mid + 1;
        }
        return nums[l];
    }
}"""
)

# 96. Find Minimum in Rotated Sorted Array II
add_prob(
    "oa_096_find_min_rotated_ii", "Find Minimum in Rotated Sorted Array II", "O(log n)", "O(1)", ["Binary Search"], "Hard", ["binary_search"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] < nums[r]) r = mid;
            else if (nums[mid] > nums[r]) l = mid + 1;
            else r--;
        }
        return nums[l];
    }
};""",
    """class Solution {
    public int findMin(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] < nums[r]) r = mid;
            else if (nums[mid] > nums[r]) l = mid + 1;
            else r--;
        }
        return nums[l];
    }
}"""
)

# 97. Search a 2D Matrix
add_prob(
    "oa_097_search_2d_matrix", "Search a 2D Matrix", "O(log n)", "O(1)", ["Binary Search"], "Medium", ["binary_search", "matrix"],
    """#include <vector>
using namespace std;
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        int l = 0, r = m * n - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int val = matrix[mid / n][mid % n];
            if (val == target) return true;
            if (val < target) l = mid + 1;
            else r = mid - 1;
        }
        return false;
    }
};""",
    """class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int l = 0, r = m * n - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int val = matrix[mid / n][mid % n];
            if (val == target) return true;
            if (val < target) l = mid + 1;
            else r = mid - 1;
        }
        return false;
    }
}"""
)

# 98. Search a 2D Matrix II
add_prob(
    "oa_098_search_2d_matrix_ii", "Search a 2D Matrix II", "O(n)", "O(1)", ["Two Pointers"], "Medium", ["matrix", "two_pointers"],
    """#include <vector>
using namespace std;
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        int r = 0, c = n - 1;
        while (r < m && c >= 0) {
            if (matrix[r][c] == target) return true;
            if (matrix[r][c] > target) c--;
            else r++;
        }
        return false;
    }
};""",
    """class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int r = 0, c = n - 1;
        while (r < m && c >= 0) {
            if (matrix[r][c] == target) return true;
            if (matrix[r][c] > target) c--;
            else r++;
        }
        return false;
    }
}"""
)

# 99. Single Element in a Sorted Array
add_prob(
    "oa_099_single_element_sorted", "Single Element in Sorted Array", "O(log n)", "O(1)", ["Binary Search"], "Medium", ["binary_search"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (mid % 2 == 1) mid--;
            if (nums[mid] == nums[mid + 1]) l = mid + 2;
            else r = mid;
        }
        return nums[l];
    }
};""",
    """class Solution {
    public int singleNonDuplicate(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (mid % 2 == 1) mid--;
            if (nums[mid] == nums[mid + 1]) l = mid + 2;
            else r = mid;
        }
        return nums[l];
    }
}"""
)

# 100. Peak Index in a Mountain Array
add_prob(
    "oa_100_peak_index_mountain", "Peak Index in Mountain Array", "O(log n)", "O(1)", ["Binary Search"], "Medium", ["binary_search"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int l = 0, r = arr.size() - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] < arr[mid + 1]) l = mid + 1;
            else r = mid;
        }
        return l;
    }
};""",
    """class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int l = 0, r = arr.length - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] < arr[mid + 1]) l = mid + 1;
            else r = mid;
        }
        return l;
    }
}"""
)

# 101. Find Peak Element
add_prob(
    "oa_101_find_peak_element", "Find Peak Element", "O(log n)", "O(1)", ["Binary Search"], "Medium", ["binary_search"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[mid + 1]) r = mid;
            else l = mid + 1;
        }
        return l;
    }
};""",
    """class Solution {
    public int findPeakElement(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[mid + 1]) r = mid;
            else l = mid + 1;
        }
        return l;
    }
}"""
)

# 102. Sqrt(x)
add_prob(
    "oa_102_sqrtx", "Sqrt(x)", "O(log n)", "O(1)", ["Binary Search"], "Easy", ["binary_search", "math"],
    """class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) return x;
        int l = 1, r = x / 2, ans = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if ((long long)mid * mid <= x) {
                ans = mid;
                l = mid + 1;
            } else r = mid - 1;
        }
        return ans;
    }
};""",
    """class Solution {
    public int mySqrt(int x) {
        if (x < 2) return x;
        int l = 1, r = x / 2, ans = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if ((long)mid * mid <= x) {
                ans = mid;
                l = mid + 1;
            } else r = mid - 1;
        }
        return ans;
    }
}"""
)

# 103. Valid Perfect Square
add_prob(
    "oa_103_valid_perfect_square", "Valid Perfect Square", "O(log n)", "O(1)", ["Binary Search"], "Easy", ["binary_search", "math"],
    """class Solution {
public:
    bool isPerfectSquare(int num) {
        int l = 1, r = num;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            long long sq = (long long)mid * mid;
            if (sq == num) return true;
            if (sq < num) l = mid + 1;
            else r = mid - 1;
        }
        return false;
    }
};""",
    """class Solution {
    public boolean isPerfectSquare(int num) {
        int l = 1, r = num;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            long sq = (long)mid * mid;
            if (sq == num) return true;
            if (sq < num) l = mid + 1;
            else r = mid - 1;
        }
        return false;
    }
}"""
)

# 104. First Bad Version
add_prob(
    "oa_104_first_bad_version", "First Bad Version", "O(log n)", "O(1)", ["Binary Search"], "Easy", ["binary_search"],
    """class Solution {
    bool isBadVersion(int version) { return version >= 4; }
public:
    int firstBadVersion(int n) {
        int l = 1, r = n;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (isBadVersion(mid)) r = mid;
            else l = mid + 1;
        }
        return l;
    }
};""",
    """class Solution {
    boolean isBadVersion(int version) { return version >= 4; }
    public int firstBadVersion(int n) {
        int l = 1, r = n;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (isBadVersion(mid)) r = mid;
            else l = mid + 1;
        }
        return l;
    }
}"""
)

# 105. Arranging Coins
add_prob(
    "oa_105_arranging_coins", "Arranging Coins", "O(log n)", "O(1)", ["Binary Search"], "Easy", ["binary_search", "math"],
    """class Solution {
public:
    int arrangeCoins(int n) {
        long long l = 0, r = n;
        while (l <= r) {
            long long mid = l + (r - l) / 2;
            long long curr = mid * (mid + 1) / 2;
            if (curr == n) return mid;
            if (curr < n) l = mid + 1;
            else r = mid - 1;
        }
        return r;
    }
};""",
    """class Solution {
    public int arrangeCoins(int n) {
        long l = 0, r = n;
        while (l <= r) {
            long mid = l + (r - l) / 2;
            long curr = mid * (mid + 1) / 2;
            if (curr == n) return (int)mid;
            if (curr < n) l = mid + 1;
            else r = mid - 1;
        }
        return (int)r;
    }
}"""
)

# 106. Koko Eating Bananas
add_prob(
    "oa_106_koko_eating_bananas", "Koko Eating Bananas", "O(n log A)", "O(1)", ["Binary Search on Answer"], "Medium", ["binary_search_on_answer"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = 1e9, ans = r;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            long long hours = 0;
            for (int p : piles) hours += (p + mid - 1) / mid;
            if (hours <= h) {
                ans = mid;
                r = mid - 1;
            } else l = mid + 1;
        }
        return ans;
    }
};""",
    """class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1, r = 1000000000, ans = r;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            long hours = 0;
            for (int p : piles) hours += (p + mid - 1) / mid;
            if (hours <= h) {
                ans = mid;
                r = mid - 1;
            } else l = mid + 1;
        }
        return ans;
    }
}"""
)

# 107. Split Array Largest Sum
add_prob(
    "oa_107_split_array_largest_sum", "Split Array Largest Sum", "O(n log A)", "O(1)", ["Binary Search on Answer"], "Hard", ["binary_search_on_answer"],
    """#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;
class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        long long l = *max_element(nums.begin(), nums.end());
        long long r = accumulate(nums.begin(), nums.end(), 0LL), ans = r;
        while (l <= r) {
            long long mid = l + (r - l) / 2;
            int count = 1;
            long long cur = 0;
            for (int x : nums) {
                if (cur + x > mid) { count++; cur = x; }
                else cur += x;
            }
            if (count <= k) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int splitArray(int[] nums, int k) {
        long l = Arrays.stream(nums).max().getAsInt();
        long r = 0;
        for (int x : nums) r += x;
        long ans = r;
        while (l <= r) {
            long mid = l + (r - l) / 2;
            int count = 1;
            long cur = 0;
            for (int x : nums) {
                if (cur + x > mid) { count++; cur = x; }
                else cur += x;
            }
            if (count <= k) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return (int)ans;
    }
}"""
)

# 108. Magnetic Force Between Two Balls
add_prob(
    "oa_108_magnetic_force_balls", "Magnetic Force Between Two Balls", "O(n log A)", "O(1)", ["Binary Search on Answer"], "Medium", ["binary_search_on_answer"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(), position.end());
        int l = 1, r = position.back() - position.front(), ans = 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int count = 1, last = position[0];
            for (int i = 1; i < position.size(); i++) {
                if (position[i] - last >= mid) { count++; last = position[i]; }
            }
            if (count >= m) { ans = mid; l = mid + 1; }
            else r = mid - 1;
        }
        return ans;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);
        int l = 1, r = position[position.length - 1] - position[0], ans = 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int count = 1, last = position[0];
            for (int i = 1; i < position.length; i++) {
                if (position[i] - last >= mid) { count++; last = position[i]; }
            }
            if (count >= m) { ans = mid; l = mid + 1; }
            else r = mid - 1;
        }
        return ans;
    }
}"""
)

# 109. Painter's Partition Problem
add_prob(
    "oa_109_painters_partition", "Painters Partition Problem", "O(n log A)", "O(1)", ["Binary Search on Answer"], "Hard", ["binary_search_on_answer"],
    """#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;
class Solution {
public:
    long long minTimeToPaint(vector<int>& boards, int k) {
        long long l = *max_element(boards.begin(), boards.end());
        long long r = accumulate(boards.begin(), boards.end(), 0LL), ans = r;
        while (l <= r) {
            long long mid = l + (r - l) / 2;
            int painters = 1;
            long long cur = 0;
            for (int b : boards) {
                if (cur + b > mid) { painters++; cur = b; }
                else cur += b;
            }
            if (painters <= k) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
};""",
    """class Solution {
    public long minTimeToPaint(int[] boards, int k) {
        long l = 0, r = 0;
        for (int b : boards) { l = Math.max(l, b); r += b; }
        long ans = r;
        while (l <= r) {
            long mid = l + (r - l) / 2;
            int painters = 1;
            long cur = 0;
            for (int b : boards) {
                if (cur + b > mid) { painters++; cur = b; }
                else cur += b;
            }
            if (painters <= k) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
}"""
)

# 110. Minimum Days to Make m Bouquets
add_prob(
    "oa_110_min_days_bouquets", "Minimum Days Make M Bouquets", "O(n log A)", "O(1)", ["Binary Search on Answer"], "Medium", ["binary_search_on_answer"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        if ((long long)m * k > bloomDay.size()) return -1;
        int l = 1, r = 1e9, ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int flowers = 0, bouquets = 0;
            for (int d : bloomDay) {
                if (d <= mid) {
                    if (++flowers == k) { bouquets++; flowers = 0; }
                } else flowers = 0;
            }
            if (bouquets >= m) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
};""",
    """class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        if ((long)m * k > bloomDay.length) return -1;
        int l = 1, r = 1000000000, ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int flowers = 0, bouquets = 0;
            for (int d : bloomDay) {
                if (d <= mid) {
                    if (++flowers == k) { bouquets++; flowers = 0; }
                } else flowers = 0;
            }
            if (bouquets >= m) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
}"""
)

# 111. Minimum Speed to Arrive on Time
add_prob(
    "oa_111_min_speed_arrive_on_time", "Minimum Speed to Arrive on Time", "O(n log A)", "O(1)", ["Binary Search on Answer"], "Medium", ["binary_search_on_answer"],
    """#include <vector>
#include <cmath>
using namespace std;
class Solution {
public:
    int minSpeedOnTime(vector<int>& dist, double hour) {
        int l = 1, r = 1e7, ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            double time = 0;
            for (int i = 0; i < dist.size() - 1; i++) time += (dist[i] + mid - 1) / mid;
            time += (double)dist.back() / mid;
            if (time <= hour) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
};""",
    """class Solution {
    public int minSpeedOnTime(int[] dist, double hour) {
        int l = 1, r = 10000000, ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            double time = 0;
            for (int i = 0; i < dist.length - 1; i++) time += (dist[i] + mid - 1) / mid;
            time += (double)dist[dist.length - 1] / mid;
            if (time <= hour) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
}"""
)

# 112. Find the Smallest Divisor Given a Threshold
add_prob(
    "oa_112_smallest_divisor_threshold", "Smallest Divisor Given Threshold", "O(n log A)", "O(1)", ["Binary Search on Answer"], "Medium", ["binary_search_on_answer"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {
        int l = 1, r = 1e6, ans = r;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int sum = 0;
            for (int x : nums) sum += (x + mid - 1) / mid;
            if (sum <= threshold) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
};""",
    """class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int l = 1, r = 1000000, ans = r;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int sum = 0;
            for (int x : nums) sum += (x + mid - 1) / mid;
            if (sum <= threshold) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
}"""
)

# 113. Kth Smallest Number in Multiplication Table
add_prob(
    "oa_113_kth_multiplication_table", "Kth Smallest in Multiplication Table", "O(n log A)", "O(1)", ["Binary Search on Answer"], "Hard", ["binary_search_on_answer"],
    """#include <algorithm>
using namespace std;
class Solution {
public:
    int findKthNumber(int m, int n, int k) {
        int l = 1, r = m * n, ans = r;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int count = 0;
            for (int i = 1; i <= m; i++) count += min(mid / i, n);
            if (count >= k) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
};""",
    """class Solution {
    public int findKthNumber(int m, int n, int k) {
        int l = 1, r = m * n, ans = r;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int count = 0;
            for (int i = 1; i <= m; i++) count += Math.min(mid / i, n);
            if (count >= k) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
}"""
)

# 114. Minimize Max Distance to Gas Station
add_prob(
    "oa_114_gas_station_distance", "Minimize Max Distance Gas Station", "O(n log A)", "O(1)", ["Binary Search on Answer"], "Hard", ["binary_search_on_answer"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    double minmaxGasDist(vector<int>& stations, int k) {
        double l = 0, r = 1e8;
        for (int iter = 0; iter < 60; iter++) {
            double mid = l + (r - l) / 2;
            int count = 0;
            for (int i = 0; i < stations.size() - 1; i++) {
                count += (int)((stations[i + 1] - stations[i]) / mid);
            }
            if (count <= k) r = mid;
            else l = mid;
        }
        return l;
    }
};""",
    """class Solution {
    public double minmaxGasDist(int[] stations, int k) {
        double l = 0, r = 100000000;
        for (int iter = 0; iter < 60; iter++) {
            double mid = l + (r - l) / 2;
            int count = 0;
            for (int i = 0; i < stations.length - 1; i++) {
                count += (int)((stations[i + 1] - stations[i]) / mid);
            }
            if (count <= k) r = mid;
            else l = mid;
        }
        return l;
    }
}"""
)

# 115. Capacity to Ship Packages Within D Days Variant
add_prob(
    "oa_115_capacity_ship_packages_ii", "Capacity to Ship Packages Variant", "O(n log A)", "O(1)", ["Binary Search on Answer"], "Medium", ["binary_search_on_answer"],
    """#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;
class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int l = *max_element(weights.begin(), weights.end());
        int r = accumulate(weights.begin(), weights.end(), 0), ans = r;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int d = 1, cur = 0;
            for (int w : weights) {
                if (cur + w > mid) { d++; cur = w; }
                else cur += w;
            }
            if (d <= days) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
};""",
    """class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int l = 0, r = 0;
        for (int w : weights) { l = Math.max(l, w); r += w; }
        int ans = r;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int d = 1, cur = 0;
            for (int w : weights) {
                if (cur + w > mid) { d++; cur = w; }
                else cur += w;
            }
            if (d <= days) { ans = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return ans;
    }
}"""
)

# 116. Merge Intervals
add_prob(
    "oa_116_merge_intervals", "Merge Intervals", "O(n)", "O(1)", [], "Medium", ["intervals", "sorting"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> res;
        for (const auto& iv : intervals) {
            if (res.empty() || res.back()[1] < iv[0]) {
                res.push_back(iv);
            } else {
                res.back()[1] = max(res.back()[1], iv[1]);
            }
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> res = new ArrayList<>();
        for (int[] iv : intervals) {
            if (res.isEmpty() || res.get(res.size() - 1)[1] < iv[0]) {
                res.add(iv);
            } else {
                res.get(res.size() - 1)[1] = Math.max(res.get(res.size() - 1)[1], iv[1]);
            }
        }
        return res.toArray(new int[res.size()][]);
    }
}"""
)

# 117. Insert Interval
add_prob(
    "oa_117_insert_interval", "Insert Interval", "O(n)", "O(1)", [], "Medium", ["intervals"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;
        int i = 0, n = intervals.size();
        while (i < n && intervals[i][1] < newInterval[0]) res.push_back(intervals[i++]);
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        res.push_back(newInterval);
        while (i < n) res.push_back(intervals[i++]);
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();
        int i = 0, n = intervals.length;
        while (i < n && intervals[i][1] < newInterval[0]) res.add(intervals[i++]);
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        res.add(newInterval);
        while (i < n) res.add(intervals[i++]);
        return res.toArray(new int[res.size()][]);
    }
}"""
)

# 118. Non-overlapping Intervals
add_prob(
    "oa_118_non_overlapping_intervals", "Non-overlapping Intervals", "O(n)", "O(1)", [], "Medium", ["intervals", "greedy"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        int count = 0, end = intervals[0][1];
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] < end) count++;
            else end = intervals[i][1];
        }
        return count;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        int count = 0, end = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < end) count++;
            else end = intervals[i][1];
        }
        return count;
    }
}"""
)

# 119. Meeting Rooms
add_prob(
    "oa_119_meeting_rooms", "Meeting Rooms", "O(n)", "O(1)", [], "Easy", ["intervals", "sorting"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] < intervals[i - 1][1]) return false;
        }
        return true;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < intervals[i - 1][1]) return false;
        }
        return true;
    }
}"""
)

# 120. Meeting Rooms II
add_prob(
    "oa_120_meeting_rooms_ii", "Meeting Rooms II", "O(n)", "O(1)", [], "Medium", ["intervals", "two_pointers"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<int> start(n), end(n);
        for (int i = 0; i < n; i++) {
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }
        sort(start.begin(), start.end());
        sort(end.begin(), end.end());
        int rooms = 0, end_ptr = 0;
        for (int i = 0; i < n; i++) {
            if (start[i] < end[end_ptr]) rooms++;
            else end_ptr++;
        }
        return rooms;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int n = intervals.length;
        int[] start = new int[n], end = new int[n];
        for (int i = 0; i < n; i++) {
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }
        Arrays.sort(start);
        Arrays.sort(end);
        int rooms = 0, endPtr = 0;
        for (int i = 0; i < n; i++) {
            if (start[i] < end[endPtr]) rooms++;
            else endPtr++;
        }
        return rooms;
    }
}"""
)

# 121. Minimum Number of Arrows to Burst Balloons
add_prob(
    "oa_121_min_arrows_burst_balloons", "Minimum Number Arrows Burst Balloons", "O(n)", "O(1)", [], "Medium", ["intervals", "greedy"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.empty()) return 0;
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        int arrows = 1, end = points[0][1];
        for (int i = 1; i < points.size(); i++) {
            if (points[i][0] > end) {
                arrows++;
                end = points[i][1];
            }
        }
        return arrows;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) return 0;
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));
        int arrows = 1, end = points[0][1];
        for (int i = 1; i < points.length; i++) {
            if (points[i][0] > end) {
                arrows++;
                end = points[i][1];
            }
        }
        return arrows;
    }
}"""
)

# 122. Car Fleet
add_prob(
    "oa_122_car_fleet", "Car Fleet", "O(n)", "O(1)", [], "Medium", ["monotonic_stack", "sorting"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, double>> cars(n);
        for (int i = 0; i < n; i++) {
            cars[i] = {position[i], (double)(target - position[i]) / speed[i]};
        }
        sort(cars.rbegin(), cars.rend());
        int fleets = 0;
        double max_time = 0;
        for (int i = 0; i < n; i++) {
            if (cars[i].second > max_time) {
                max_time = cars[i].second;
                fleets++;
            }
        }
        return fleets;
    }
};""",
    """import java.util.*;
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        double[][] cars = new double[n][2];
        for (int i = 0; i < n; i++) {
            cars[i][0] = position[i];
            cars[i][1] = (double)(target - position[i]) / speed[i];
        }
        Arrays.sort(cars, (a, b) -> Double.compare(b[0], a[0]));
        int fleets = 0;
        double maxTime = 0;
        for (int i = 0; i < n; i++) {
            if (cars[i][1] > maxTime) {
                maxTime = cars[i][1];
                fleets++;
            }
        }
        return fleets;
    }
}"""
)

# 123. Wiggle Sort
add_prob(
    "oa_123_wiggle_sort", "Wiggle Sort", "O(n)", "O(1)", [], "Medium", ["array"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        for (int i = 0; i < (int)nums.size() - 1; i++) {
            if ((i % 2 == 0 && nums[i] > nums[i + 1]) || (i % 2 == 1 && nums[i] < nums[i + 1])) {
                swap(nums[i], nums[i + 1]);
            }
        }
    }
};""",
    """class Solution {
    public void wiggleSort(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            if ((i % 2 == 0 && nums[i] > nums[i + 1]) || (i % 2 == 1 && nums[i] < nums[i + 1])) {
                int tmp = nums[i]; nums[i] = nums[i + 1]; nums[i + 1] = tmp;
            }
        }
    }
}"""
)

# 124. Custom Sort String
add_prob(
    "oa_124_custom_sort_string", "Custom Sort String", "O(n)", "O(1)", [], "Medium", ["string", "sorting"],
    """#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    string customSortString(string order, string s) {
        vector<int> count(26, 0);
        for (char c : s) count[c - 'a']++;
        string res = "";
        for (char c : order) {
            while (count[c - 'a']-- > 0) res += c;
        }
        for (int i = 0; i < 26; i++) {
            while (count[i]-- > 0) res += (char)('a' + i);
        }
        return res;
    }
};""",
    """class Solution {
    public String customSortString(String order, String s) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) count[c - 'a']++;
        StringBuilder res = new StringBuilder();
        for (char c : order.toCharArray()) {
            while (count[c - 'a']-- > 0) res.append(c);
        }
        for (int i = 0; i < 26; i++) {
            while (count[i]-- > 0) res.append((char)('a' + i));
        }
        return res.toString();
    }
}"""
)

# 125. Largest Number
add_prob(
    "oa_125_largest_number", "Largest Number", "O(n)", "O(1)", [], "Medium", ["sorting", "greedy"],
    """#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> s_nums;
        for (int x : nums) s_nums.push_back(to_string(x));
        sort(s_nums.begin(), s_nums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        if (s_nums[0] == "0") return "0";
        string res = "";
        for (const string& s : s_nums) res += s;
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public String largestNumber(int[] nums) {
        String[] sNums = new String[nums.length];
        for (int i = 0; i < nums.length; i++) sNums[i] = String.valueOf(nums[i]);
        Arrays.sort(sNums, (a, b) -> (b + a).compareTo(a + b));
        if (sNums[0].equals("0")) return "0";
        StringBuilder res = new StringBuilder();
        for (String s : sNums) res.append(s);
        return res.toString();
    }
}"""
)

# 126. H-Index
add_prob(
    "oa_126_h_index", "H-Index", "O(n)", "O(1)", [], "Medium", ["sorting"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end());
        int n = citations.size();
        for (int i = 0; i < n; i++) {
            if (citations[i] >= n - i) return n - i;
        }
        return 0;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        for (int i = 0; i < n; i++) {
            if (citations[i] >= n - i) return n - i;
        }
        return 0;
    }
}"""
)

# 127. Minimum Difference Between Highest and Lowest of K Scores
add_prob(
    "oa_127_min_diff_k_scores", "Min Difference Highest Lowest K Scores", "O(n)", "O(1)", [], "Easy", ["sorting", "sliding_window"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        if (k == 1) return 0;
        sort(nums.begin(), nums.end());
        int min_diff = 1e9;
        for (int i = 0; i + k - 1 < nums.size(); i++) {
            min_diff = min(min_diff, nums[i + k - 1] - nums[i]);
        }
        return min_diff;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int minimumDifference(int[] nums, int k) {
        if (k == 1) return 0;
        Arrays.sort(nums);
        int minDiff = 1000000000;
        for (int i = 0; i + k - 1 < nums.length; i++) {
            minDiff = Math.min(minDiff, nums[i + k - 1] - nums[i]);
        }
        return minDiff;
    }
}"""
)

# 128. Maximum Units on a Truck
add_prob(
    "oa_128_max_units_truck", "Maximum Units on a Truck", "O(n)", "O(1)", [], "Easy", ["greedy", "sorting"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] > b[1];
        });
        int total_units = 0;
        for (const auto& b : boxTypes) {
            int take = min(truckSize, b[0]);
            total_units += take * b[1];
            truckSize -= take;
            if (truckSize == 0) break;
        }
        return total_units;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (a, b) -> Integer.compare(b[1], a[1]));
        int totalUnits = 0;
        for (int[] b : boxTypes) {
            int take = Math.min(truckSize, b[0]);
            totalUnits += take * b[1];
            truckSize -= take;
            if (truckSize == 0) break;
        }
        return totalUnits;
    }
}"""
)

# 129. Maximum Ice Cream Bars
add_prob(
    "oa_129_max_ice_cream_bars", "Maximum Ice Cream Bars", "O(n)", "O(1)", [], "Medium", ["greedy", "sorting"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        sort(costs.begin(), costs.end());
        int count = 0;
        for (int c : costs) {
            if (coins >= c) {
                coins -= c;
                count++;
            } else break;
        }
        return count;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs);
        int count = 0;
        for (int c : costs) {
            if (coins >= c) {
                coins -= c;
                count++;
            } else break;
        }
        return count;
    }
}"""
)

# 130. Minimum Increment to Make Array Unique
add_prob(
    "oa_130_min_increment_unique", "Minimum Increment Make Array Unique", "O(n)", "O(1)", [], "Medium", ["sorting", "greedy"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int moves = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] <= nums[i - 1]) {
                moves += nums[i - 1] + 1 - nums[i];
                nums[i] = nums[i - 1] + 1;
            }
        }
        return moves;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int minIncrementForUnique(int[] nums) {
        Arrays.sort(nums);
        int moves = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] <= nums[i - 1]) {
                moves += nums[i - 1] + 1 - nums[i];
                nums[i] = nums[i - 1] + 1;
            }
        }
        return moves;
    }
}"""
)

# 131. Array Partition
add_prob(
    "oa_131_array_partition", "Array Partition", "O(n)", "O(1)", [], "Easy", ["sorting", "greedy"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int sum = 0;
        for (int i = 0; i < nums.size(); i += 2) sum += nums[i];
        return sum;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int sum = 0;
        for (int i = 0; i < nums.length; i += 2) sum += nums[i];
        return sum;
    }
}"""
)

# 132. How Many Numbers Are Smaller Than Current
add_prob(
    "oa_132_smaller_numbers_than_current", "Smaller Numbers Than Current", "O(n)", "O(n)", [], "Easy", ["array"],
    """#include <vector>
using namespace std;
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> count(101, 0);
        for (int x : nums) count[x]++;
        for (int i = 1; i <= 100; i++) count[i] += count[i - 1];
        vector<int> res(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            res[i] = (nums[i] == 0) ? 0 : count[nums[i] - 1];
        }
        return res;
    }
};""",
    """class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] count = new int[101];
        for (int x : nums) count[x]++;
        for (int i = 1; i <= 100; i++) count[i] += count[i - 1];
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            res[i] = (nums[i] == 0) ? 0 : count[nums[i] - 1];
        }
        return res;
    }
}"""
)

# 133. Sort Integers by The Number of 1 Bits
add_prob(
    "oa_133_sort_by_bits", "Sort Integers by Number of 1 Bits", "O(n)", "O(1)", [], "Easy", ["sorting", "bit_manipulation"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
    static int bitCount(int x) {
        int cnt = 0;
        while (x) { cnt += (x & 1); x >>= 1; }
        return cnt;
    }
public:
    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end(), [](int a, int b) {
            int ca = bitCount(a), cb = bitCount(b);
            if (ca != cb) return ca < cb;
            return a < b;
        });
        return arr;
    }
};""",
    """import java.util.*;
class Solution {
    public int[] sortByBits(int[] arr) {
        Integer[] boxed = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(boxed, (a, b) -> {
            int ca = Integer.bitCount(a), cb = Integer.bitCount(b);
            if (ca != cb) return Integer.compare(ca, cb);
            return Integer.compare(a, b);
        });
        return Arrays.stream(boxed).mapToInt(i -> i).toArray();
    }
}"""
)

# 134. Maximum Number of Coins You Can Get
add_prob(
    "oa_134_max_coins_get", "Maximum Number Coins You Can Get", "O(n)", "O(1)", [], "Medium", ["sorting", "greedy"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(), piles.end());
        int ans = 0, n = piles.size(), rounds = n / 3;
        for (int i = n - 2; rounds > 0; i -= 2, rounds--) {
            ans += piles[i];
        }
        return ans;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int maxCoins(int[] piles) {
        Arrays.sort(piles);
        int ans = 0, n = piles.length, rounds = n / 3;
        for (int i = n - 2; rounds > 0; i -= 2, rounds--) {
            ans += piles[i];
        }
        return ans;
    }
}"""
)

# 135. Relative Sort Array
add_prob(
    "oa_135_relative_sort_array", "Relative Sort Array", "O(n)", "O(n)", [], "Easy", ["sorting", "array"],
    """#include <vector>
using namespace std;
class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        vector<int> count(1001, 0);
        for (int x : arr1) count[x]++;
        vector<int> res;
        for (int x : arr2) {
            while (count[x]-- > 0) res.push_back(x);
        }
        for (int i = 0; i <= 1000; i++) {
            while (count[i]-- > 0) res.push_back(i);
        }
        return res;
    }
};""",
    """class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int[] count = new int[1001];
        for (int x : arr1) count[x]++;
        int[] res = new int[arr1.length];
        int idx = 0;
        for (int x : arr2) {
            while (count[x]-- > 0) res[idx++] = x;
        }
        for (int i = 0; i <= 1000; i++) {
            while (count[i]-- > 0) res[idx++] = i;
        }
        return res;
    }
}"""
)

# 136. Next Greater Element I
add_prob(
    "oa_136_next_greater_element_i", "Next Greater Element I", "O(n)", "O(1)", ["Monotonic Stack"], "Easy", ["monotonic_stack"],
    """#include <vector>
#include <unordered_map>
#include <stack>
using namespace std;
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> next_gr;
        stack<int> st;
        for (int x : nums2) {
            while (!st.empty() && st.top() < x) {
                next_gr[st.top()] = x;
                st.pop();
            }
            st.push(x);
        }
        vector<int> res;
        for (int x : nums1) {
            res.push_back(next_gr.count(x) ? next_gr[x] : -1);
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> nextGr = new HashMap<>();
        Deque<Integer> st = new ArrayDeque<>();
        for (int x : nums2) {
            while (!st.isEmpty() && st.peek() < x) {
                nextGr.put(st.pop(), x);
            }
            st.push(x);
        }
        int[] res = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            res[i] = nextGr.getOrDefault(nums1[i], -1);
        }
        return res;
    }
}"""
)

# 137. Next Greater Element II
add_prob(
    "oa_137_next_greater_element_ii", "Next Greater Element II", "O(n)", "O(n)", ["Monotonic Stack"], "Medium", ["monotonic_stack"],
    """#include <vector>
#include <stack>
using namespace std;
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, -1);
        stack<int> st;
        for (int i = 0; i < 2 * n; i++) {
            while (!st.empty() && nums[st.top()] < nums[i % n]) {
                res[st.top()] = nums[i % n];
                st.pop();
            }
            if (i < n) st.push(i);
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        Arrays.fill(res, -1);
        Deque<Integer> st = new ArrayDeque<>();
        for (int i = 0; i < 2 * n; i++) {
            while (!st.isEmpty() && nums[st.peek()] < nums[i % n]) {
                res[st.pop()] = nums[i % n];
            }
            if (i < n) st.push(i);
        }
        return res;
    }
}"""
)

# 138. Daily Temperatures
add_prob(
    "oa_138_daily_temperatures", "Daily Temperatures", "O(n)", "O(n)", ["Monotonic Stack"], "Medium", ["monotonic_stack"],
    """#include <vector>
#include <stack>
using namespace std;
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
                res[st.top()] = i - st.top();
                st.pop();
            }
            st.push(i);
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        Deque<Integer> st = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!st.isEmpty() && temperatures[i] > temperatures[st.peek()]) {
                int prev = st.pop();
                res[prev] = i - prev;
            }
            st.push(i);
        }
        return res;
    }
}"""
)

# 139. Online Stock Span
add_prob(
    "oa_139_online_stock_span", "Online Stock Span", "O(n)", "O(1)", ["Monotonic Stack"], "Medium", ["monotonic_stack"],
    """#include <stack>
using namespace std;
class StockSpanner {
    stack<pair<int, int>> st;
public:
    StockSpanner() {}
    int next(int price) {
        int span = 1;
        while (!st.empty() && st.top().first <= price) {
            span += st.top().second;
            st.pop();
        }
        st.push({price, span});
        return span;
    }
};""",
    """import java.util.*;
class StockSpanner {
    Deque<int[]> st;
    public StockSpanner() {
        st = new ArrayDeque<>();
    }
    public int next(int price) {
        int span = 1;
        while (!st.isEmpty() && st.peek()[0] <= price) {
            span += st.pop()[1];
        }
        st.push(new int[]{price, span});
        return span;
    }
}"""
)

# 140. Maximal Rectangle
add_prob(
    "oa_140_maximal_rectangle", "Maximal Rectangle", "O(n m)", "O(n)", ["Monotonic Stack"], "Hard", ["monotonic_stack", "dp"],
    """#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
class Solution {
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(0);
        stack<int> st;
        int max_a = 0;
        for (int i = 0; i < heights.size(); i++) {
            while (!st.empty() && heights[st.top()] >= heights[i]) {
                int h = heights[st.top()]; st.pop();
                int w = st.empty() ? i : i - st.top() - 1;
                max_a = max(max_a, h * w);
            }
            st.push(i);
        }
        heights.pop_back();
        return max_a;
    }
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        int m = matrix.size(), n = matrix[0].size(), ans = 0;
        vector<int> heights(n, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') heights[j]++;
                else heights[j] = 0;
            }
            ans = max(ans, largestRectangleArea(heights));
        }
        return ans;
    }
};""",
    """import java.util.*;
class Solution {
    int largestRectangleArea(int[] heights) {
        int[] h = new int[heights.length + 1];
        System.arraycopy(heights, 0, h, 0, heights.length);
        Deque<Integer> st = new ArrayDeque<>();
        int maxA = 0;
        for (int i = 0; i < h.length; i++) {
            while (!st.isEmpty() && h[st.peek()] >= h[i]) {
                int curH = h[st.pop()];
                int w = st.isEmpty() ? i : i - st.peek() - 1;
                maxA = Math.max(maxA, curH * w);
            }
            st.push(i);
        }
        return maxA;
    }
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0) return 0;
        int m = matrix.length, n = matrix[0].length, ans = 0;
        int[] heights = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') heights[j]++;
                else heights[j] = 0;
            }
            ans = Math.max(ans, largestRectangleArea(heights));
        }
        return ans;
    }
}"""
)

# 141. Sum of Subarray Minimums
add_prob(
    "oa_141_sum_subarray_minimums", "Sum of Subarray Minimums", "O(n)", "O(n)", ["Monotonic Stack"], "Medium", ["monotonic_stack"],
    """#include <vector>
#include <stack>
using namespace std;
class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        int n = arr.size(), mod = 1e9 + 7;
        vector<int> ple(n), nle(n);
        stack<int> s1, s2;
        for (int i = 0; i < n; i++) {
            while (!s1.empty() && arr[s1.top()] > arr[i]) s1.pop();
            ple[i] = s1.empty() ? -1 : s1.top();
            s1.push(i);
        }
        for (int i = n - 1; i >= 0; i--) {
            while (!s2.empty() && arr[s2.top()] >= arr[i]) s2.pop();
            nle[i] = s2.empty() ? n : s2.top();
            s2.push(i);
        }
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            long long left = i - ple[i], right = nle[i] - i;
            ans = (ans + (left * right % mod) * arr[i]) % mod;
        }
        return ans;
    }
};""",
    """import java.util.*;
class Solution {
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length, mod = 1000000007;
        int[] ple = new int[n], nle = new int[n];
        Deque<Integer> s1 = new ArrayDeque<>(), s2 = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!s1.isEmpty() && arr[s1.peek()] > arr[i]) s1.pop();
            ple[i] = s1.isEmpty() ? -1 : s1.peek();
            s1.push(i);
        }
        for (int i = n - 1; i >= 0; i--) {
            while (!s2.isEmpty() && arr[s2.peek()] >= arr[i]) s2.pop();
            nle[i] = s2.isEmpty() ? n : s2.peek();
            s2.push(i);
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long left = i - ple[i], right = nle[i] - i;
            ans = (ans + (left * right % mod) * arr[i]) % mod;
        }
        return (int)ans;
    }
}"""
)

# 142. Sum of Subarray Ranges
add_prob(
    "oa_142_sum_subarray_ranges", "Sum of Subarray Ranges", "O(n^2)", "O(1)", [], "Medium", ["monotonic_stack", "array"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {
        long long total = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int min_v = nums[i], max_v = nums[i];
            for (int j = i + 1; j < n; j++) {
                min_v = min(min_v, nums[j]);
                max_v = max(max_v, nums[j]);
                total += max_v - min_v;
            }
        }
        return total;
    }
};""",
    """class Solution {
    public long subArrayRanges(int[] nums) {
        long total = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int minV = nums[i], maxV = nums[i];
            for (int j = i + 1; j < n; j++) {
                minV = Math.min(minV, nums[j]);
                maxV = Math.max(maxV, nums[j]);
                total += maxV - minV;
            }
        }
        return total;
    }
}"""
)

# 143. Remove K Digits
add_prob(
    "oa_143_remove_k_digits", "Remove K Digits", "O(n)", "O(1)", [], "Medium", ["monotonic_stack", "greedy"],
    """#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    string removeKdigits(string num, int k) {
        string st = "";
        for (char c : num) {
            while (!st.empty() && k > 0 && st.back() > c) {
                st.pop_back();
                k--;
            }
            if (!st.empty() || c != '0') st.push_back(c);
        }
        while (!st.empty() && k > 0) {
            st.pop_back();
            k--;
        }
        return st.empty() ? "0" : st;
    }
};""",
    """import java.util.*;
class Solution {
    public String removeKdigits(String num, int k) {
        StringBuilder st = new StringBuilder();
        for (char c : num.toCharArray()) {
            while (st.length() > 0 && k > 0 && st.charAt(st.length() - 1) > c) {
                st.deleteCharAt(st.length() - 1);
                k--;
            }
            if (st.length() > 0 || c != '0') st.append(c);
        }
        while (st.length() > 0 && k > 0) {
            st.deleteCharAt(st.length() - 1);
            k--;
        }
        return st.length() == 0 ? "0" : st.toString();
    }
}"""
)

# 144. 132 Pattern
add_prob(
    "oa_144_132_pattern", "132 Pattern", "O(n)", "O(1)", ["Monotonic Stack"], "Medium", ["monotonic_stack"],
    """#include <vector>
#include <stack>
using namespace std;
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        stack<int> st;
        int s3 = -1e9;
        for (int i = (int)nums.size() - 1; i >= 0; i--) {
            if (nums[i] < s3) return true;
            while (!st.empty() && nums[i] > st.top()) {
                s3 = st.top();
                st.pop();
            }
            st.push(nums[i]);
        }
        return false;
    }
};""",
    """import java.util.*;
class Solution {
    public boolean find132pattern(int[] nums) {
        Deque<Integer> st = new ArrayDeque<>();
        int s3 = -1000000000;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] < s3) return true;
            while (!st.isEmpty() && nums[i] > st.peek()) {
                s3 = st.pop();
            }
            st.push(nums[i]);
        }
        return false;
    }
}"""
)

# 145. Asteroid Collision
add_prob(
    "oa_145_asteroid_collision", "Asteroid Collision", "O(n)", "O(1)", [], "Medium", ["stack"],
    """#include <vector>
#include <cmath>
using namespace std;
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> st;
        for (int ast : asteroids) {
            bool alive = true;
            while (alive && ast < 0 && !st.empty() && st.back() > 0) {
                if (st.back() < -ast) { st.pop_back(); continue; }
                else if (st.back() == -ast) { st.pop_back(); }
                alive = false;
            }
            if (alive) st.push_back(ast);
        }
        return st;
    }
};""",
    """import java.util.*;
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> st = new ArrayDeque<>();
        for (int ast : asteroids) {
            boolean alive = true;
            while (alive && ast < 0 && !st.isEmpty() && st.peek() > 0) {
                if (st.peek() < -ast) { st.pop(); continue; }
                else if (st.peek() == -ast) { st.pop(); }
                alive = false;
            }
            if (alive) st.push(ast);
        }
        int[] res = new int[st.size()];
        for (int i = res.length - 1; i >= 0; i--) res[i] = st.pop();
        return res;
    }
}"""
)

print(f"Part 2 loaded with {len(PART2_CASES)} cases ({len(PART2_CASES)//2} problems: 91 to 145).")
