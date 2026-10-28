# 704. Binary Search

**Difficulty:** Easy

## Problem
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:** <br>
Input: nums = [-1,0,3,5,9,12], target = 9 <br>
Output: 4

Explanation: <br>
9 exists in nums and its index is 4.

**Example 2:** <br>
Input: nums = [-1,0,3,5,9,12], target = 2 <br>
Output: -1

Explanation: <br>
2 does not exist in nums so return -1.

**Constraints:** <br>
1 <= nums.length <= 10^4 <br>
-10^4 < nums[i], target < 10^4 <br>
All the integers in `nums` are unique. <br>
`nums` is sorted in ascending order.


## Solution

#### **Intuition:**
A linear search scans each element one by one from left to right, running in $O(n)$ time. However, the problem explicitly requires an $O(\log n)$ runtime and states that `nums` is already **sorted in ascending order** with all elements being unique.

Because the array is sorted, we can leverage the **Binary Search** technique:
- By looking at the middle element `nums[mid]`, we can determine whether the target lies at the midpoint, in the left half, or in the right half.
- If `nums[mid] == target`, we immediately return its index.
- If `nums[mid] < target`, all elements to the left of `mid` are also smaller than `target`, so we can safely eliminate the entire left half.
- If `nums[mid] > target`, all elements to the right of `mid` are also greater than `target`, allowing us to discard the entire right half.

By discarding half the remaining search space on every iteration, we locate the target or determine its absence in logarithmic $O(\log n)$ time.

#### **Logic:**
1. Initialize Boundary Pointers:
   - Set `left = 0` (start of the array).
   - Set `right = len(nums) - 1` (end of the array).
2. Search Loop (`while left <= right`):
   - Compute the midpoint safely to avoid potential integer overflow: `mid = left + (right - left) // 2`.
   - Check Match: If `nums[mid] == target`, return `mid`.
   - Target is Larger: If `nums[mid] < target`, shift the search boundary rightward: `left = mid + 1`.
   - Target is Smaller: If `nums[mid] > target`, shift the search boundary leftward: `right = mid - 1`.
3. Target Not Found: If the loop terminates (`left > right`) without finding `target`, return `-1`.

#### **Example Walkthrough:**
Consider Example 1: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`

* **Initial State:** `left = 0`, `right = 5`

| Iteration | `left` | `right` | `mid` | `nums[mid]` | Comparison to `target = 9` | Action |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `0` | `5` | $0 + (5 - 0) // 2 = \mathbf{2}$ | `3` | `3 < 9` | Target is larger $\rightarrow$ `left = mid + 1 = 3` |
| 2 | `3` | `5` | $3 + (5 - 3) // 2 = \mathbf{4}$ | `9` | `9 == 9` | **Target found!** $\rightarrow$ Return `mid = 4` |

* **Final Result:** `4`

Consider Example 2: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 2`

* **Initial State:** `left = 0`, `right = 5`

| Iteration | `left` | `right` | `mid` | `nums[mid]` | Comparison to `target = 2` | Action |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `0` | `5` | `2` | `3` | `3 > 2` | Target is smaller $\rightarrow$ `right = mid - 1 = 1` |
| 2 | `0` | `1` | `0` | `-1` | `-1 < 2` | Target is larger $\rightarrow$ `left = mid + 1 = 1` |
| 3 | `1` | `1` | `1` | `0` | `0 < 2` | Target is larger $\rightarrow$ `left = mid + 1 = 2` |

* Loop condition breaks since `left (2) > right (1)`.
* **Final Result:** `-1`

#### **Time Complexity:**
$O(\log n)$ <br>
At every step, the search window size is divided by 2, requiring at most $\lceil \log_2 n \rceil + 1$ iterations.

#### **Space Complexity:**
$O(1)$ <br>
Only constant memory is used for the index pointers `left`, `right`, and `mid`.