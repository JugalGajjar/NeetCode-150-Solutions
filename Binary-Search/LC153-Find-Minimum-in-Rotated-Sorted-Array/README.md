# 153. Find Minimum in Rotated Sorted Array

**Difficulty:** Medium

## Problem
Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

* `[4,5,6,7,0,1,2]` if it was rotated `4` times.
* `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:** <br>
Input: nums = [3,4,5,1,2] <br>
Output: 1

Explanation: <br>
The original array was [1,2,3,4,5] rotated 3 times.

**Example 2:** <br>
Input: nums = [4,5,6,7,0,1,2] <br>
Output: 0

Explanation: <br>
The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

**Example 3:** <br>
Input: nums = [11,13,15,17] <br>
Output: 11

Explanation: <br>
The original array was [11,13,15,17] and it was rotated 4 times.

**Constraints:** <br>
n == nums.length <br>
1 <= n <= 5000 <br>
-5000 <= nums[i] <= 5000 <br>
All the integers of `nums` are **unique**. <br>
`nums` is sorted and rotated between `1` and `n` times.


## Solution

#### **Intuition:**
A simple linear scan finds the minimum in $O(n)$ time, but the problem explicitly requires an $O(\log n)$ runtime.

Because the array was originally sorted in ascending order and all elements are unique, rotating the array splits it into at most two sorted subarrays:
- A left sorted portion containing larger numbers.
- A right sorted portion containing smaller numbers, starting with the array's true minimum (the inflection point).

To find this inflection point in $O(\log n)$ time, we use **Binary Search** by comparing `nums[mid]` to the right boundary element `nums[right]`:
- **If `nums[mid] > nums[right]`:** The midpoint belongs to the left sorted portion, which means the inflection point (minimum value) must lie strictly to the right of `mid`. We discard the left half by setting `left = mid + 1`.
- **If `nums[mid] <= nums[right]`:** The subarray from `mid` to `right` is properly sorted. This means `nums[mid]` could itself be the minimum, or the true minimum lies somewhere to its left. We keep `mid` in our search range by setting `right = mid`.

By repeatedly narrowing the search space, the pointers converge on the minimum element when `left == right`.

#### **Logic:**
1. Initialize Boundaries:
   - Set `left = 0` and `right = len(nums) - 1`.
2. Binary Search Loop (`while left < right`):
   - Calculate midpoint: `mid = left + (right - left) // 2`.
   - Check Right Subarray:
     - If `nums[mid] > nums[right]`: The minimum is strictly in the right half $\rightarrow$ `left = mid + 1`.
     - Otherwise (`nums[mid] <= nums[right]`): The minimum is at `mid` or to its left $\rightarrow$ `right = mid`.
3. Termination: When `left == right`, the search space has shrunk to a single element. Return `nums[left]`.

#### **Example Walkthrough:**
Consider Example 2: `nums = [4, 5, 6, 7, 0, 1, 2]`

* **Initial State:** `left = 0`, `right = 6`

| Iteration | `left` | `right` | `mid` | `nums[mid]` | `nums[right]` | Comparison (`nums[mid] vs nums[right]`) | Action | Search Range Next |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| 1 | `0` | `6` | **`3`** | `7` | `2` | `7 > 2` (Inflection to the right) | `left = mid + 1 = 4` | Indices `[4 ... 6]` |
| 2 | `4` | `6` | **`5`** | `1` | `2` | `1 <= 2` (Sorted right side; min $\le$ `mid`) | `right = mid = 5` | Indices `[4 ... 5]` |
| 3 | `4` | `5` | **`4`** | `0` | `1` | `0 <= 1` (Sorted right side; min $\le$ `mid`) | `right = mid = 4` | Indices `[4 ... 4]` |

* Loop terminates because `left == right == 4`.
* **Final Result:** `nums[4] = 0`

#### **Time Complexity:**
$O(\log n)$ <br>
Each iteration halves the active search window, guaranteeing logarithmic runtime for an array of size `n`.

#### **Space Complexity:**
$O(1)$ <br>
Only two pointer variables (`left`, `right`) and a midpoint variable (`mid`) are used.