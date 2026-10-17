# corpus_part1.py: Problems 41 to 90 (50 distinct problems)
# Arrays, Two Pointers, Sliding Window, Prefix Sum, Difference Array

PART1_CASES = []

def add_prob(pid, name, tc, sc, algos, rating, tags, cpp_code, java_code):
    PART1_CASES.append({
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
    PART1_CASES.append({
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

# 41. Two Sum II
add_prob(
    "oa_041_two_sum_ii", "Two Sum II", "O(n)", "O(1)", ["Two Pointers"], "Medium", ["two_pointers", "array"],
    """#include <vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) return {left + 1, right + 1};
            if (sum < target) left++;
            else right--;
        }
        return {-1, -1};
    }
};""",
    """class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1;
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) return new int[]{left + 1, right + 1};
            if (sum < target) left++;
            else right--;
        }
        return new int[]{-1, -1};
    }
}"""
)

# 42. Container With Most Water
add_prob(
    "oa_042_container_water", "Container With Most Water", "O(n)", "O(1)", ["Two Pointers"], "Medium", ["two_pointers", "array"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1, max_w = 0;
        while (left < right) {
            int h = min(height[left], height[right]);
            max_w = max(max_w, h * (right - left));
            if (height[left] < height[right]) left++;
            else right--;
        }
        return max_w;
    }
};""",
    """class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1, maxWater = 0;
        while (left < right) {
            int h = Math.min(height[left], height[right]);
            maxWater = Math.max(maxWater, h * (right - left));
            if (height[left] < height[right]) left++;
            else right--;
        }
        return maxWater;
    }
}"""
)

# 43. 3Sum Closest
add_prob(
    "oa_043_3sum_closest", "3Sum Closest", "O(n^2)", "O(1)", ["Two Pointers"], "Medium", ["two_pointers", "sorting"],
    """#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size(), closest = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < n - 2; i++) {
            int l = i + 1, r = n - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (abs(sum - target) < abs(closest - target)) closest = sum;
                if (sum < target) l++;
                else if (sum > target) r--;
                else return target;
            }
        }
        return closest;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length, closest = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < n - 2; i++) {
            int l = i + 1, r = n - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (Math.abs(sum - target) < Math.abs(closest - target)) closest = sum;
                if (sum < target) l++;
                else if (sum > target) r--;
                else return target;
            }
        }
        return closest;
    }
}"""
)

# 44. 4Sum
add_prob(
    "oa_044_4sum", "4Sum", "O(n^3)", "O(1)", ["Two Pointers"], "Medium", ["two_pointers", "sorting"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                int l = j + 1, r = n - 1;
                while (l < r) {
                    long long sum = (long long)nums[i] + nums[j] + nums[l] + nums[r];
                    if (sum == target) {
                        res.push_back({nums[i], nums[j], nums[l], nums[r]});
                        while (l < r && nums[l] == nums[l + 1]) l++;
                        while (l < r && nums[r] == nums[r - 1]) r--;
                        l++; r--;
                    } else if (sum < target) l++;
                    else r--;
                }
            }
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                int l = j + 1, r = n - 1;
                while (l < r) {
                    long sum = (long)nums[i] + nums[j] + nums[l] + nums[r];
                    if (sum == target) {
                        res.add(Arrays.asList(nums[i], nums[j], nums[l], nums[r]));
                        while (l < r && nums[l] == nums[l + 1]) l++;
                        while (l < r && nums[r] == nums[r - 1]) r--;
                        l++; r--;
                    } else if (sum < target) l++;
                    else r--;
                }
            }
        }
        return res;
    }
}"""
)

# 45. Trapping Rain Water
add_prob(
    "oa_045_trapping_rain_water", "Trapping Rain Water", "O(n)", "O(1)", ["Two Pointers"], "Hard", ["two_pointers", "array"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int max_l = 0, max_r = 0, water = 0;
        while (left <= right) {
            if (height[left] <= height[right]) {
                if (height[left] >= max_l) max_l = height[left];
                else water += max_l - height[left];
                left++;
            } else {
                if (height[right] >= max_r) max_r = height[right];
                else water += max_r - height[right];
                right--;
            }
        }
        return water;
    }
};""",
    """class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int maxL = 0, maxR = 0, water = 0;
        while (left <= right) {
            if (height[left] <= height[right]) {
                if (height[left] >= maxL) maxL = height[left];
                else water += maxL - height[left];
                left++;
            } else {
                if (height[right] >= maxR) maxR = height[right];
                else water += maxR - height[right];
                right--;
            }
        }
        return water;
    }
}"""
)

# 46. Valid Palindrome
add_prob(
    "oa_046_valid_palindrome", "Valid Palindrome", "O(n)", "O(1)", ["Two Pointers"], "Easy", ["two_pointers", "string"],
    """#include <string>
#include <cctype>
using namespace std;
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            while (l < r && !isalnum(s[l])) l++;
            while (l < r && !isalnum(s[r])) r--;
            if (tolower(s[l]) != tolower(s[r])) return false;
            l++; r--;
        }
        return true;
    }
};""",
    """class Solution {
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
            while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) return false;
            l++; r--;
        }
        return true;
    }
}"""
)

# 47. Boats to Save People
add_prob(
    "oa_047_boats_save_people", "Boats to Save People", "O(n)", "O(1)", ["Two Pointers"], "Medium", ["two_pointers", "greedy"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int l = 0, r = people.size() - 1, boats = 0;
        while (l <= r) {
            if (people[l] + people[r] <= limit) l++;
            r--;
            boats++;
        }
        return boats;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int l = 0, r = people.length - 1, boats = 0;
        while (l <= r) {
            if (people[l] + people[r] <= limit) l++;
            r--;
            boats++;
        }
        return boats;
    }
}"""
)

# 48. Reverse String
add_prob(
    "oa_048_reverse_string", "Reverse String", "O(n)", "O(1)", ["Two Pointers"], "Easy", ["two_pointers", "string"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            swap(s[l], s[r]);
            l++; r--;
        }
    }
};""",
    """class Solution {
    public void reverseString(char[] s) {
        int l = 0, r = s.length - 1;
        while (l < r) {
            char tmp = s[l]; s[l] = s[r]; s[r] = tmp;
            l++; r--;
        }
    }
}"""
)

# 49. Reverse Vowels of a String
add_prob(
    "oa_049_reverse_vowels", "Reverse Vowels", "O(n)", "O(1)", ["Two Pointers"], "Easy", ["two_pointers", "string"],
    """#include <string>
#include <algorithm>
using namespace std;
class Solution {
    bool isVowel(char c) {
        c = tolower(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
public:
    string reverseVowels(string s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            while (l < r && !isVowel(s[l])) l++;
            while (l < r && !isVowel(s[r])) r--;
            if (l < r) {
                swap(s[l], s[r]);
                l++; r--;
            }
        }
        return s;
    }
};""",
    """class Solution {
    boolean isVowel(char c) {
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
    public String reverseVowels(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            while (l < r && !isVowel(s.charAt(l))) l++;
            while (l < r && !isVowel(s.charAt(r))) r--;
            if (l < r) {
                l++; r--;
            }
        }
        return s;
    }
}"""
)

# 50. Remove Duplicates from Sorted Array
add_prob(
    "oa_050_remove_duplicates", "Remove Duplicates Sorted Array", "O(n)", "O(1)", [], "Easy", ["two_pointers", "array"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        int i = 0;
        for (int j = 1; j < nums.size(); j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
};""",
    """class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
}"""
)

# 51. Remove Duplicates from Sorted Array II
add_prob(
    "oa_051_remove_duplicates_ii", "Remove Duplicates from Sorted Array II", "O(n)", "O(1)", [], "Medium", ["two_pointers", "array"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2) return n;
        int j = 2;
        for (int i = 2; i < n; i++) {
            if (nums[i] != nums[j - 2]) {
                nums[j++] = nums[i];
            }
        }
        return j;
    }
};""",
    """class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        if (n <= 2) return n;
        int j = 2;
        for (int i = 2; i < n; i++) {
            if (nums[i] != nums[j - 2]) {
                nums[j++] = nums[i];
            }
        }
        return j;
    }
}"""
)

# 52. Remove Element
add_prob(
    "oa_052_remove_element", "Remove Element", "O(n)", "O(1)", [], "Easy", ["two_pointers", "array"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
};""",
    """class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
}"""
)

# 53. Move Zeroes
add_prob(
    "oa_053_move_zeroes", "Move Zeroes", "O(n)", "O(1)", [], "Easy", ["two_pointers", "array"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int last_non_zero = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                swap(nums[last_non_zero++], nums[i]);
            }
        }
    }
};""",
    """class Solution {
    public void moveZeroes(int[] nums) {
        int lastNonZero = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int tmp = nums[lastNonZero];
                nums[lastNonZero++] = nums[i];
                nums[i] = tmp;
            }
        }
    }
}"""
)

# 54. Duplicate Zeros
add_prob(
    "oa_054_duplicate_zeros", "Duplicate Zeros", "O(n)", "O(1)", [], "Easy", ["two_pointers", "array"],
    """#include <vector>
using namespace std;
class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int n = arr.size(), zeros = 0;
        for (int x : arr) if (x == 0) zeros++;
        int i = n - 1, j = n + zeros - 1;
        while (i >= 0) {
            if (j < n) arr[j] = arr[i];
            if (arr[i] == 0) {
                j--;
                if (j < n) arr[j] = 0;
            }
            i--; j--;
        }
    }
};""",
    """class Solution {
    public void duplicateZeros(int[] arr) {
        int n = arr.length, zeros = 0;
        for (int x : arr) if (x == 0) zeros++;
        int i = n - 1, j = n + zeros - 1;
        while (i >= 0) {
            if (j < n) arr[j] = arr[i];
            if (arr[i] == 0) {
                j--;
                if (j < n) arr[j] = 0;
            }
            i--; j--;
        }
    }
}"""
)

# 55. Sort Colors / Dutch National Flag
add_prob(
    "oa_055_sort_colors", "Sort Colors (Dutch National Flag)", "O(n)", "O(1)", [], "Medium", ["two_pointers", "sorting"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0, mid = 0, high = nums.size() - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums[low++], nums[mid++]);
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                swap(nums[mid], nums[high--]);
            }
        }
    }
};""",
    """class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                int tmp = nums[low]; nums[low++] = nums[mid]; nums[mid++] = tmp;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                int tmp = nums[mid]; nums[mid] = nums[high]; nums[high--] = tmp;
            }
        }
    }
}"""
)

# 56. Squares of a Sorted Array
add_prob(
    "oa_056_squares_sorted_array", "Squares of a Sorted Array", "O(n)", "O(n)", ["Two Pointers"], "Easy", ["two_pointers", "array"],
    """#include <vector>
using namespace std;
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size(), l = 0, r = n - 1, p = n - 1;
        vector<int> res(n);
        while (l <= r) {
            if (nums[l] * nums[l] > nums[r] * nums[r]) {
                res[p--] = nums[l] * nums[l];
                l++;
            } else {
                res[p--] = nums[r] * nums[r];
                r--;
            }
        }
        return res;
    }
};""",
    """class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length, l = 0, r = n - 1, p = n - 1;
        int[] res = new int[n];
        while (l <= r) {
            if (nums[l] * nums[l] > nums[r] * nums[r]) {
                res[p--] = nums[l] * nums[l];
                l++;
            } else {
                res[p--] = nums[r] * nums[r];
                r--;
            }
        }
        return res;
    }
}"""
)

# 57. Compare Version Numbers
add_prob(
    "oa_057_compare_version_numbers", "Compare Version Numbers", "O(n)", "O(1)", ["Two Pointers"], "Medium", ["two_pointers", "string"],
    """#include <string>
using namespace std;
class Solution {
public:
    int compareVersion(string version1, string version2) {
        int i = 0, j = 0, n1 = version1.size(), n2 = version2.size();
        while (i < n1 || j < n2) {
            int num1 = 0, num2 = 0;
            while (i < n1 && version1[i] != '.') num1 = num1 * 10 + (version1[i++] - '0');
            while (j < n2 && version2[j] != '.') num2 = num2 * 10 + (version2[j++] - '0');
            if (num1 < num2) return -1;
            if (num1 > num2) return 1;
            i++; j++;
        }
        return 0;
    }
};""",
    """class Solution {
    public int compareVersion(String version1, String version2) {
        int i = 0, j = 0, n1 = version1.length(), n2 = version2.length();
        while (i < n1 || j < n2) {
            int num1 = 0, num2 = 0;
            while (i < n1 && version1.charAt(i) != '.') num1 = num1 * 10 + (version1.charAt(i++) - '0');
            while (j < n2 && version2.charAt(j) != '.') num2 = num2 * 10 + (version2.charAt(j++) - '0');
            if (num1 < num2) return -1;
            if (num1 > num2) return 1;
            i++; j++;
        }
        return 0;
    }
}"""
)

# 58. Interval List Intersections
add_prob(
    "oa_058_interval_list_intersections", "Interval List Intersections", "O(n)", "O(1)", ["Two Pointers"], "Medium", ["two_pointers", "intervals"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        vector<vector<int>> res;
        int i = 0, j = 0;
        while (i < firstList.size() && j < secondList.size()) {
            int start = max(firstList[i][0], secondList[j][0]);
            int end = min(firstList[i][1], secondList[j][1]);
            if (start <= end) res.push_back({start, end});
            if (firstList[i][1] < secondList[j][1]) i++;
            else j++;
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> res = new ArrayList<>();
        int i = 0, j = 0;
        while (i < firstList.length && j < secondList.length) {
            int start = Math.max(firstList[i][0], secondList[j][0]);
            int end = Math.min(firstList[i][1], secondList[j][1]);
            if (start <= end) res.add(new int[]{start, end});
            if (firstList[i][1] < secondList[j][1]) i++;
            else j++;
        }
        return res.toArray(new int[res.size()][]);
    }
}"""
)

# 59. Backspace String Compare
add_prob(
    "oa_059_backspace_string_compare", "Backspace String Compare", "O(n)", "O(1)", ["Two Pointers"], "Easy", ["two_pointers", "string"],
    """#include <string>
using namespace std;
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        int i = s.size() - 1, j = t.size() - 1, skip_s = 0, skip_t = 0;
        while (i >= 0 || j >= 0) {
            while (i >= 0) {
                if (s[i] == '#') { skip_s++; i--; }
                else if (skip_s > 0) { skip_s--; i--; }
                else break;
            }
            while (j >= 0) {
                if (t[j] == '#') { skip_t++; j--; }
                else if (skip_t > 0) { skip_t--; j--; }
                else break;
            }
            if (i >= 0 && j >= 0 && s[i] != t[j]) return false;
            if ((i >= 0) != (j >= 0)) return false;
            i--; j--;
        }
        return true;
    }
};""",
    """class Solution {
    public boolean backspaceCompare(String s, String t) {
        int i = s.length() - 1, j = t.length() - 1, skipS = 0, skipT = 0;
        while (i >= 0 || j >= 0) {
            while (i >= 0) {
                if (s.charAt(i) == '#') { skipS++; i--; }
                else if (skipS > 0) { skipS--; i--; }
                else break;
            }
            while (j >= 0) {
                if (t.charAt(j) == '#') { skipT++; j--; }
                else if (skipT > 0) { skipT--; j--; }
                else break;
            }
            if (i >= 0 && j >= 0 && s.charAt(i) != t.charAt(j)) return false;
            if ((i >= 0) != (j >= 0)) return false;
            i--; j--;
        }
        return true;
    }
}"""
)

# 60. Longest Mountain in Array
add_prob(
    "oa_060_longest_mountain", "Longest Mountain in Array", "O(n)", "O(1)", [], "Medium", ["two_pointers", "array"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int n = arr.size(), ans = 0, base = 0;
        while (base < n) {
            int end = base;
            if (end + 1 < n && arr[end] < arr[end + 1]) {
                while (end + 1 < n && arr[end] < arr[end + 1]) end++;
                if (end + 1 < n && arr[end] > arr[end + 1]) {
                    while (end + 1 < n && arr[end] > arr[end + 1]) end++;
                    ans = max(ans, end - base + 1);
                }
            }
            base = max(end, base + 1);
        }
        return ans;
    }
};""",
    """class Solution {
    public int longestMountain(int[] arr) {
        int n = arr.length, ans = 0, base = 0;
        while (base < n) {
            int end = base;
            if (end + 1 < n && arr[end] < arr[end + 1]) {
                while (end + 1 < n && arr[end] < arr[end + 1]) end++;
                if (end + 1 < n && arr[end] > arr[end + 1]) {
                    while (end + 1 < n && arr[end] > arr[end + 1]) end++;
                    ans = Math.max(ans, end - base + 1);
                }
            }
            base = Math.max(end, base + 1);
        }
        return ans;
    }
}"""
)

# 61. Push Dominoes
add_prob(
    "oa_061_push_dominoes", "Push Dominoes", "O(n)", "O(n)", ["Two Pointers"], "Medium", ["two_pointers", "string"],
    """#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
    string pushDominoes(string dominoes) {
        string d = "L" + dominoes + "R";
        string res = "";
        int l = 0;
        for (int r = 1; r < d.size(); r++) {
            if (d[r] == '.') continue;
            if (l > 0) res += d[l];
            int mid = r - l - 1;
            if (d[l] == d[r]) res.append(mid, d[l]);
            else if (d[l] == 'L' && d[r] == 'R') res.append(mid, '.');
            else {
                res.append(mid / 2, 'R');
                if (mid % 2 == 1) res += '.';
                res.append(mid / 2, 'L');
            }
            l = r;
        }
        return res;
    }
};""",
    """class Solution {
    public String pushDominoes(String dominoes) {
        String d = "L" + dominoes + "R";
        StringBuilder res = new StringBuilder();
        int l = 0;
        for (int r = 1; r < d.length(); r++) {
            if (d.charAt(r) == '.') continue;
            if (l > 0) res.append(d.charAt(l));
            int mid = r - l - 1;
            if (d.charAt(l) == d.charAt(r)) {
                for (int k = 0; k < mid; k++) res.append(d.charAt(l));
            } else if (d.charAt(l) == 'L' && d.charAt(r) == 'R') {
                for (int k = 0; k < mid; k++) res.append('.');
            } else {
                for (int k = 0; k < mid / 2; k++) res.append('R');
                if (mid % 2 == 1) res.append('.');
                for (int k = 0; k < mid / 2; k++) res.append('L');
            }
            l = r;
        }
        return res.toString();
    }
}"""
)

# 62. Bag of Tokens
add_prob(
    "oa_062_bag_of_tokens", "Bag of Tokens", "O(n)", "O(1)", ["Two Pointers"], "Medium", ["two_pointers", "greedy"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(), tokens.end());
        int l = 0, r = tokens.size() - 1, score = 0, max_score = 0;
        while (l <= r) {
            if (power >= tokens[l]) {
                power -= tokens[l++];
                score++;
                max_score = max(max_score, score);
            } else if (score > 0) {
                power += tokens[r--];
                score--;
            } else break;
        }
        return max_score;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        int l = 0, r = tokens.length - 1, score = 0, maxScore = 0;
        while (l <= r) {
            if (power >= tokens[l]) {
                power -= tokens[l++];
                score++;
                maxScore = Math.max(maxScore, score);
            } else if (score > 0) {
                power += tokens[r--];
                score--;
            } else break;
        }
        return maxScore;
    }
}"""
)

# 63. Valid Palindrome II
add_prob(
    "oa_063_valid_palindrome_ii", "Valid Palindrome II", "O(n)", "O(1)", ["Two Pointers"], "Easy", ["two_pointers", "string"],
    """#include <string>
using namespace std;
class Solution {
    bool check(const string& s, int l, int r) {
        while (l < r) {
            if (s[l] != s[r]) return false;
            l++; r--;
        }
        return true;
    }
public:
    bool validPalindrome(string s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            if (s[l] != s[r]) {
                return check(s, l + 1, r) || check(s, l, r - 1);
            }
            l++; r--;
        }
        return true;
    }
};""",
    """class Solution {
    boolean check(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++; r--;
        }
        return true;
    }
    public boolean validPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return check(s, l + 1, r) || check(s, l, r - 1);
            }
            l++; r--;
        }
        return true;
    }
}"""
)

# 64. String Compression
add_prob(
    "oa_064_string_compression", "String Compression", "O(n)", "O(1)", [], "Medium", ["two_pointers", "string"],
    """#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    int compress(vector<char>& chars) {
        int write = 0, anchor = 0, n = chars.size();
        for (int read = 0; read < n; read++) {
            if (read + 1 == n || chars[read + 1] != chars[read]) {
                chars[write++] = chars[anchor];
                if (read > anchor) {
                    string cnt = to_string(read - anchor + 1);
                    for (char c : cnt) chars[write++] = c;
                }
                anchor = read + 1;
            }
        }
        return write;
    }
};""",
    """class Solution {
    public int compress(char[] chars) {
        int write = 0, anchor = 0, n = chars.length;
        for (int read = 0; read < n; read++) {
            if (read + 1 == n || chars[read + 1] != chars[read]) {
                chars[write++] = chars[anchor];
                if (read > anchor) {
                    String cnt = Integer.toString(read - anchor + 1);
                    for (char c : cnt.toCharArray()) chars[write++] = c;
                }
                anchor = read + 1;
            }
        }
        return write;
    }
}"""
)

# 65. Partition Labels
add_prob(
    "oa_065_partition_labels", "Partition Labels", "O(n)", "O(1)", ["Two Pointers"], "Medium", ["two_pointers", "greedy"],
    """#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> last(26, 0);
        for (int i = 0; i < s.size(); i++) last[s[i] - 'a'] = i;
        vector<int> res;
        int start = 0, end = 0;
        for (int i = 0; i < s.size(); i++) {
            end = max(end, last[s[i] - 'a']);
            if (i == end) {
                res.push_back(end - start + 1);
                start = i + 1;
            }
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public List<Integer> partitionLabels(String s) {
        int[] last = new int[26];
        for (int i = 0; i < s.length(); i++) last[s.charAt(i) - 'a'] = i;
        List<Integer> res = new ArrayList<>();
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            end = Math.max(end, last[s.charAt(i) - 'a']);
            if (i == end) {
                res.add(end - start + 1);
                start = i + 1;
            }
        }
        return res;
    }
}"""
)

# 66. Longest Substring Without Repeating Characters
add_prob(
    "oa_066_longest_substring_no_repeats", "Longest Substring Without Repeating Characters", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "string"],
    """#include <string>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> last(128, -1);
        int max_len = 0, left = 0;
        for (int right = 0; right < s.size(); right++) {
            if (last[s[right]] >= left) left = last[s[right]] + 1;
            last[s[right]] = right;
            max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] last = new int[128];
        Arrays.fill(last, -1);
        int maxLen = 0, left = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (last[c] >= left) left = last[c] + 1;
            last[c] = right;
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}"""
)

# 67. Maximum Average Subarray I
add_prob(
    "oa_067_max_avg_subarray", "Maximum Average Subarray I", "O(n)", "O(1)", ["Sliding Window"], "Easy", ["sliding_window", "array"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        double max_sum = sum;
        for (int i = k; i < nums.size(); i++) {
            sum += nums[i] - nums[i - k];
            max_sum = max(max_sum, sum);
        }
        return max_sum / k;
    }
};""",
    """class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        double maxSum = sum;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            maxSum = Math.max(maxSum, sum);
        }
        return maxSum / k;
    }
}"""
)

# 68. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
add_prob(
    "oa_068_subarrays_avg_threshold", "Subarrays of Size K Average Threshold", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "array"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int target = k * threshold, sum = 0, count = 0;
        for (int i = 0; i < k; i++) sum += arr[i];
        if (sum >= target) count++;
        for (int i = k; i < arr.size(); i++) {
            sum += arr[i] - arr[i - k];
            if (sum >= target) count++;
        }
        return count;
    }
};""",
    """class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int target = k * threshold, sum = 0, count = 0;
        for (int i = 0; i < k; i++) sum += arr[i];
        if (sum >= target) count++;
        for (int i = k; i < arr.length; i++) {
            sum += arr[i] - arr[i - k];
            if (sum >= target) count++;
        }
        return count;
    }
}"""
)

# 69. Find All Anagrams in a String
add_prob(
    "oa_069_find_anagrams", "Find All Anagrams in a String", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "string"],
    """#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> res;
        if (s.size() < p.size()) return res;
        vector<int> p_cnt(26, 0), s_cnt(26, 0);
        for (char c : p) p_cnt[c - 'a']++;
        int k = p.size();
        for (int i = 0; i < k; i++) s_cnt[s[i] - 'a']++;
        if (s_cnt == p_cnt) res.push_back(0);
        for (int i = k; i < s.size(); i++) {
            s_cnt[s[i] - 'a']++;
            s_cnt[s[i - k] - 'a']--;
            if (s_cnt == p_cnt) res.push_back(i - k + 1);
        }
        return res;
    }
};""",
    """import java.util.*;
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        if (s.length() < p.length()) return res;
        int[] pCnt = new int[26], sCnt = new int[26];
        for (char c : p.toCharArray()) pCnt[c - 'a']++;
        int k = p.length();
        for (int i = 0; i < k; i++) sCnt[s.charAt(i) - 'a']++;
        if (Arrays.equals(sCnt, pCnt)) res.add(0);
        for (int i = k; i < s.length(); i++) {
            sCnt[s.charAt(i) - 'a']++;
            sCnt[s.charAt(i - k) - 'a']--;
            if (Arrays.equals(sCnt, pCnt)) res.add(i - k + 1);
        }
        return res;
    }
}"""
)

# 70. Permutation in String
add_prob(
    "oa_070_permutation_in_string", "Permutation in String", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "string"],
    """#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;
        vector<int> c1(26, 0), c2(26, 0);
        for (char c : s1) c1[c - 'a']++;
        int k = s1.size();
        for (int i = 0; i < k; i++) c2[s2[i] - 'a']++;
        if (c1 == c2) return true;
        for (int i = k; i < s2.size(); i++) {
            c2[s2[i] - 'a']++;
            c2[s2[i - k] - 'a']--;
            if (c1 == c2) return true;
        }
        return false;
    }
};""",
    """import java.util.Arrays;
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;
        int[] c1 = new int[26], c2 = new int[26];
        for (char c : s1.toCharArray()) c1[c - 'a']++;
        int k = s1.length();
        for (int i = 0; i < k; i++) c2[s2.charAt(i) - 'a']++;
        if (Arrays.equals(c1, c2)) return true;
        for (int i = k; i < s2.length(); i++) {
            c2[s2.charAt(i) - 'a']++;
            c2[s2.charAt(i - k) - 'a']--;
            if (Arrays.equals(c1, c2)) return true;
        }
        return false;
    }
}"""
)

# 71. Grumpy Bookstore Owner
add_prob(
    "oa_071_grumpy_bookstore", "Grumpy Bookstore Owner", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "array"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        int total = 0, extra = 0, n = customers.size();
        for (int i = 0; i < n; i++) {
            if (grumpy[i] == 0) total += customers[i];
        }
        for (int i = 0; i < minutes; i++) {
            if (grumpy[i] == 1) extra += customers[i];
        }
        int max_extra = extra;
        for (int i = minutes; i < n; i++) {
            if (grumpy[i] == 1) extra += customers[i];
            if (grumpy[i - minutes] == 1) extra -= customers[i - minutes];
            max_extra = max(max_extra, extra);
        }
        return total + max_extra;
    }
};""",
    """class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int total = 0, extra = 0, n = customers.length;
        for (int i = 0; i < n; i++) {
            if (grumpy[i] == 0) total += customers[i];
        }
        for (int i = 0; i < minutes; i++) {
            if (grumpy[i] == 1) extra += customers[i];
        }
        int maxExtra = extra;
        for (int i = minutes; i < n; i++) {
            if (grumpy[i] == 1) extra += customers[i];
            if (grumpy[i - minutes] == 1) extra -= customers[i - minutes];
            maxExtra = Math.max(maxExtra, extra);
        }
        return total + maxExtra;
    }
}"""
)

# 72. Longest Repeating Character Replacement
add_prob(
    "oa_072_character_replacement", "Longest Repeating Character Replacement", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "string"],
    """#include <string>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> count(26, 0);
        int max_count = 0, max_len = 0, left = 0;
        for (int right = 0; right < s.size(); right++) {
            max_count = max(max_count, ++count[s[right] - 'A']);
            while (right - left + 1 - max_count > k) {
                count[s[left] - 'A']--;
                left++;
            }
            max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};""",
    """class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int maxCount = 0, maxLen = 0, left = 0;
        for (int right = 0; right < s.length(); right++) {
            maxCount = Math.max(maxCount, ++count[s.charAt(right) - 'A']);
            while (right - left + 1 - maxCount > k) {
                count[s.charAt(left) - 'A']--;
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}"""
)

# 73. Max Consecutive Ones III
add_prob(
    "oa_073_max_consecutive_ones_iii", "Max Consecutive Ones III", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "array"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int left = 0, zeros = 0, max_len = 0;
        for (int right = 0; right < nums.size(); right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > k) {
                if (nums[left] == 0) zeros--;
                left++;
            }
            max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};""",
    """class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0, zeros = 0, maxLen = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > k) {
                if (nums[left] == 0) zeros--;
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}"""
)

# 74. Subarray Product Less Than K
add_prob(
    "oa_074_subarray_product_less_k", "Subarray Product Less Than K", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "array"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 1) return 0;
        int prod = 1, ans = 0, left = 0;
        for (int right = 0; right < nums.size(); right++) {
            prod *= nums[right];
            while (prod >= k) {
                prod /= nums[left++];
            }
            ans += right - left + 1;
        }
        return ans;
    }
};""",
    """class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) return 0;
        int prod = 1, ans = 0, left = 0;
        for (int right = 0; right < nums.length; right++) {
            prod *= nums[right];
            while (prod >= k) {
                prod /= nums[left++];
            }
            ans += right - left + 1;
        }
        return ans;
    }
}"""
)

# 75. Fruit Into Baskets
add_prob(
    "oa_075_fruit_into_baskets", "Fruit Into Baskets", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "array"],
    """#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int, int> count;
        int left = 0, max_fruits = 0;
        for (int right = 0; right < fruits.size(); right++) {
            count[fruits[right]]++;
            while (count.size() > 2) {
                count[fruits[left]]--;
                if (count[fruits[left]] == 0) count.erase(fruits[left]);
                left++;
            }
            max_fruits = max(max_fruits, right - left + 1);
        }
        return max_fruits;
    }
};""",
    """import java.util.*;
class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> count = new HashMap<>();
        int left = 0, maxFruits = 0;
        for (int right = 0; right < fruits.length; right++) {
            count.put(fruits[right], count.getOrDefault(fruits[right], 0) + 1);
            while (count.size() > 2) {
                count.put(fruits[left], count.get(fruits[left]) - 1);
                if (count.get(fruits[left]) == 0) count.remove(fruits[left]);
                left++;
            }
            maxFruits = Math.max(maxFruits, right - left + 1);
        }
        return maxFruits;
    }
}"""
)

# 76. Minimum Size Subarray Sum
add_prob(
    "oa_076_min_size_subarray_sum", "Minimum Size Subarray Sum", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "array"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0, sum = 0, min_len = 1e9;
        for (int right = 0; right < nums.size(); right++) {
            sum += nums[right];
            while (sum >= target) {
                min_len = min(min_len, right - left + 1);
                sum -= nums[left++];
            }
        }
        return min_len == 1e9 ? 0 : min_len;
    }
};""",
    """class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, sum = 0, minLen = 1000000000;
        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];
            while (sum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                sum -= nums[left++];
            }
        }
        return minLen == 1000000000 ? 0 : minLen;
    }
}"""
)

# 77. Longest Substring with At Most Two Distinct Characters
add_prob(
    "oa_077_longest_sub_two_distinct", "Longest Substring Two Distinct", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "string"],
    """#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        unordered_map<char, int> count;
        int left = 0, max_len = 0;
        for (int right = 0; right < s.size(); right++) {
            count[s[right]]++;
            while (count.size() > 2) {
                count[s[left]]--;
                if (count[s[left]] == 0) count.erase(s[left]);
                left++;
            }
            max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};""",
    """import java.util.*;
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character, Integer> count = new HashMap<>();
        int left = 0, maxLen = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            count.put(c, count.getOrDefault(c, 0) + 1);
            while (count.size() > 2) {
                char lc = s.charAt(left);
                count.put(lc, count.get(lc) - 1);
                if (count.get(lc) == 0) count.remove(lc);
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}"""
)

# 78. Longest Substring with At Most K Distinct Characters
add_prob(
    "oa_078_longest_sub_k_distinct", "Longest Substring K Distinct", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "string"],
    """#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        if (k == 0) return 0;
        unordered_map<char, int> count;
        int left = 0, max_len = 0;
        for (int right = 0; right < s.size(); right++) {
            count[s[right]]++;
            while (count.size() > k) {
                count[s[left]]--;
                if (count[s[left]] == 0) count.erase(s[left]);
                left++;
            }
            max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};""",
    """import java.util.*;
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if (k == 0) return 0;
        Map<Character, Integer> count = new HashMap<>();
        int left = 0, maxLen = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            count.put(c, count.getOrDefault(c, 0) + 1);
            while (count.size() > k) {
                char lc = s.charAt(left);
                count.put(lc, count.get(lc) - 1);
                if (count.get(lc) == 0) count.remove(lc);
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}"""
)

# 79. Replace the Substring for Balanced String
add_prob(
    "oa_079_balanced_string_replace", "Replace Substring for Balanced String", "O(n)", "O(1)", ["Sliding Window"], "Medium", ["sliding_window", "string"],
    """#include <string>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int balancedString(string s) {
        vector<int> count(128, 0);
        int n = s.size(), k = n / 4;
        for (char c : s) count[c]++;
        int left = 0, min_len = n;
        for (int right = 0; right < n; right++) {
            count[s[right]]--;
            while (left < n && count['Q'] <= k && count['W'] <= k && count['E'] <= k && count['R'] <= k) {
                min_len = min(min_len, right - left + 1);
                count[s[left++]]++;
            }
        }
        return min_len;
    }
};""",
    """class Solution {
    public int balancedString(String s) {
        int[] count = new int[128];
        int n = s.length(), k = n / 4;
        for (char c : s.toCharArray()) count[c]++;
        int left = 0, minLen = n;
        for (int right = 0; right < n; right++) {
            count[s.charAt(right)]--;
            while (left < n && count['Q'] <= k && count['W'] <= k && count['E'] <= k && count['R'] <= k) {
                minLen = Math.min(minLen, right - left + 1);
                count[s.charAt(left++)]++;
            }
        }
        return minLen;
    }
}"""
)

# 80. Max Consecutive Ones
add_prob(
    "oa_080_max_consecutive_ones", "Max Consecutive Ones", "O(n)", "O(1)", [], "Easy", ["array"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_cnt = 0, cur = 0;
        for (int x : nums) {
            if (x == 1) {
                cur++;
                max_cnt = max(max_cnt, cur);
            } else {
                cur = 0;
            }
        }
        return max_cnt;
    }
};""",
    """class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCnt = 0, cur = 0;
        for (int x : nums) {
            if (x == 1) {
                cur++;
                maxCnt = Math.max(maxCnt, cur);
            } else {
                cur = 0;
            }
        }
        return maxCnt;
    }
}"""
)

# 81. Range Sum Query - Immutable
add_prob(
    "oa_081_range_sum_query_immutable", "Range Sum Query Immutable", "O(n)", "O(n)", ["Prefix Sum"], "Easy", ["prefix_sum", "array"],
    """#include <vector>
using namespace std;
class NumArray {
    vector<int> pref;
public:
    NumArray(vector<int>& nums) {
        pref.resize(nums.size() + 1, 0);
        for (int i = 0; i < nums.size(); i++) {
            pref[i + 1] = pref[i] + nums[i];
        }
    }
    int sumRange(int left, int right) {
        return pref[right + 1] - pref[left];
    }
};""",
    """class NumArray {
    int[] pref;
    public NumArray(int[] nums) {
        pref = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            pref[i + 1] = pref[i] + nums[i];
        }
    }
    public int sumRange(int left, int right) {
        return pref[right + 1] - pref[left];
    }
}"""
)

# 82. Subarray Sum Equals K
add_prob(
    "oa_082_subarray_sum_equals_k", "Subarray Sum Equals K", "O(n)", "O(1)", ["Prefix Sum"], "Medium", ["prefix_sum", "hash_map"],
    """#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        count[0] = 1;
        int sum = 0, ans = 0;
        for (int x : nums) {
            sum += x;
            if (count.find(sum - k) != count.end()) ans += count[sum - k];
            count[sum]++;
        }
        return ans;
    }
};""",
    """import java.util.*;
class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        count.put(0, 1);
        int sum = 0, ans = 0;
        for (int x : nums) {
            sum += x;
            ans += count.getOrDefault(sum - k, 0);
            count.put(sum, count.getOrDefault(sum, 0) + 1);
        }
        return ans;
    }
}"""
)

# 83. Continuous Subarray Sum
add_prob(
    "oa_083_continuous_subarray_sum", "Continuous Subarray Sum", "O(n)", "O(1)", ["Prefix Sum"], "Medium", ["prefix_sum", "hash_map"],
    """#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> rem;
        rem[0] = -1;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            int r = sum % k;
            if (rem.find(r) != rem.end()) {
                if (i - rem[r] > 1) return true;
            } else {
                rem[r] = i;
            }
        }
        return false;
    }
};""",
    """import java.util.*;
class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> rem = new HashMap<>();
        rem.put(0, -1);
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            int r = sum % k;
            if (rem.containsKey(r)) {
                if (i - rem.get(r) > 1) return true;
            } else {
                rem.put(r, i);
            }
        }
        return false;
    }
}"""
)

# 84. Contiguous Array (Equal 0s and 1s)
add_prob(
    "oa_084_contiguous_array", "Contiguous Array Equal Zeros Ones", "O(n)", "O(1)", ["Prefix Sum"], "Medium", ["prefix_sum", "hash_map"],
    """#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> count;
        count[0] = -1;
        int balance = 0, max_len = 0;
        for (int i = 0; i < nums.size(); i++) {
            balance += (nums[i] == 1 ? 1 : -1);
            if (count.find(balance) != count.end()) {
                max_len = max(max_len, i - count[balance]);
            } else {
                count[balance] = i;
            }
        }
        return max_len;
    }
};""",
    """import java.util.*;
class Solution {
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        count.put(0, -1);
        int balance = 0, maxLen = 0;
        for (int i = 0; i < nums.length; i++) {
            balance += (nums[i] == 1 ? 1 : -1);
            if (count.containsKey(balance)) {
                maxLen = Math.max(maxLen, i - count.get(balance));
            } else {
                count.put(balance, i);
            }
        }
        return maxLen;
    }
}"""
)

# 85. Subarray Sums Divisible by K
add_prob(
    "oa_085_subarray_sums_divisible_k", "Subarray Sums Divisible by K", "O(n)", "O(1)", ["Prefix Sum"], "Medium", ["prefix_sum", "hash_map"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        vector<int> count(k, 0);
        count[0] = 1;
        int sum = 0, ans = 0;
        for (int x : nums) {
            sum = ((sum + x) % k + k) % k;
            ans += count[sum];
            count[sum]++;
        }
        return ans;
    }
};""",
    """class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int[] count = new int[k];
        count[0] = 1;
        int sum = 0, ans = 0;
        for (int x : nums) {
            sum = ((sum + x) % k + k) % k;
            ans += count[sum];
            count[sum]++;
        }
        return ans;
    }
}"""
)

# 86. Product of Array Except Self
add_prob(
    "oa_086_product_array_except_self", "Product of Array Except Self", "O(n)", "O(n)", [], "Medium", ["prefix_sum", "array"],
    """#include <vector>
using namespace std;
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);
        int left = 1;
        for (int i = 0; i < n; i++) {
            res[i] = left;
            left *= nums[i];
        }
        int right = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= right;
            right *= nums[i];
        }
        return res;
    }
};""",
    """class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int left = 1;
        for (int i = 0; i < n; i++) {
            res[i] = left;
            left *= nums[i];
        }
        int right = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= right;
            right *= nums[i];
        }
        return res;
    }
}"""
)

# 87. Find Pivot Index
add_prob(
    "oa_087_find_pivot_index", "Find Pivot Index", "O(n)", "O(1)", ["Prefix Sum"], "Easy", ["prefix_sum", "array"],
    """#include <vector>
using namespace std;
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total = 0, left = 0;
        for (int x : nums) total += x;
        for (int i = 0; i < nums.size(); i++) {
            if (left == total - left - nums[i]) return i;
            left += nums[i];
        }
        return -1;
    }
};""",
    """class Solution {
    public int pivotIndex(int[] nums) {
        int total = 0, left = 0;
        for (int x : nums) total += x;
        for (int i = 0; i < nums.length; i++) {
            if (left == total - left - nums[i]) return i;
            left += nums[i];
        }
        return -1;
    }
}"""
)

# 88. Minimum Value to Get Positive Step by Step Sum
add_prob(
    "oa_088_min_step_sum", "Minimum Value Positive Step Sum", "O(n)", "O(1)", ["Prefix Sum"], "Easy", ["prefix_sum", "array"],
    """#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int min_pref = 0, cur = 0;
        for (int x : nums) {
            cur += x;
            min_pref = min(min_pref, cur);
        }
        return 1 - min_pref;
    }
};""",
    """class Solution {
    public int minStartValue(int[] nums) {
        int minPref = 0, cur = 0;
        for (int x : nums) {
            cur += x;
            minPref = Math.min(minPref, cur);
        }
        return 1 - minPref;
    }
}"""
)

# 89. Car Pooling (Difference Array)
add_prob(
    "oa_089_car_pooling", "Car Pooling Difference Array", "O(n)", "O(1)", [], "Medium", ["difference_array", "prefix_sum"],
    """#include <vector>
using namespace std;
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        vector<int> diff(1001, 0);
        for (const auto& t : trips) {
            diff[t[1]] += t[0];
            diff[t[2]] -= t[0];
        }
        int cur = 0;
        for (int i = 0; i <= 1000; i++) {
            cur += diff[i];
            if (cur > capacity) return false;
        }
        return true;
    }
};""",
    """class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int[] diff = new int[1001];
        for (int[] t : trips) {
            diff[t[1]] += t[0];
            diff[t[2]] -= t[0];
        }
        int cur = 0;
        for (int i = 0; i <= 1000; i++) {
            cur += diff[i];
            if (cur > capacity) return false;
        }
        return true;
    }
}"""
)

# 90. Range Addition (Difference Array)
add_prob(
    "oa_090_range_addition", "Range Addition Difference Array", "O(n)", "O(n)", [], "Medium", ["difference_array", "prefix_sum"],
    """#include <vector>
using namespace std;
class Solution {
public:
    vector<int> getModifiedArray(int n, vector<vector<int>>& updates) {
        vector<int> diff(n + 1, 0);
        for (const auto& u : updates) {
            diff[u[0]] += u[2];
            diff[u[1] + 1] -= u[2];
        }
        vector<int> res(n);
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            res[i] = cur;
        }
        return res;
    }
};""",
    """class Solution {
    public int[] getModifiedArray(int n, int[][] updates) {
        int[] diff = new int[n + 1];
        for (int[] u : updates) {
            diff[u[0]] += u[2];
            diff[u[1] + 1] -= u[2];
        }
        int[] res = new int[n];
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            res[i] = cur;
        }
        return res;
    }
}"""
)

print(f"Part 1 loaded with {len(PART1_CASES)} cases ({len(PART1_CASES)//2} problems: 41 to 90).")
