# 15. 3Sum

**Difficulty:** Medium

## Problem
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1:** <br>
Input: nums = [-1,0,1,2,-1,-4] <br>
Output: [[-1,-1,2],[-1,0,1]]

Explanation: <br>
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0. <br>
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0. <br>
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0. <br>
The distinct triplets are [-1,0,1] and [-1,-1,2]. <br>
Notice that the order of the output and the order of the triplets does not matter.

**Example 2:** <br>
Input: nums = [0,1,1] <br>
Output: []

Explanation: <br>
The only possible triplet does not sum up to 0.

**Example 3:** <br>
Input: nums = [0,0,0] <br>
Output: [[0,0,0]]

Explanation: <br>
The only possible triplet sums up to 0.

**Constraints:** <br>
3 <= nums.length <= 3000 <br>
-10^5 <= nums[i] <= 10^5


## Solution

#### **Intuition:**
The brute-force approach requires three nested loops to test every triplet in $O(n^3)$ time, plus a set to filter duplicates. 

We can reduce this problem to **Two Sum II (Two Pointers)** by first sorting the array. Sorting takes $O(n \log n)$ time, which is dominated by our target runtime of $O(n^2)$. 

Once the array is sorted:
1. We iterate through the array and fix the first number `nums[i]`.
2. The problem then reduces to finding two numbers to the right of `i` that sum to `-nums[i]`.
3. Because the subarray to the right of index `i` is sorted, we can search for the other two numbers in linear $O(n)$ time using two pointers (`left` and `right`).
4. To satisfy the constraint that the result must not contain duplicate triplets, sorting allows us to skip identical adjacent elements directly without needing a hash set.

#### **Logic:**
1. Sort the Array: Sort `nums` in non-decreasing order.
2. Iterate and Fix `nums[i]`: Loop index `i` from `0` to `len(nums) - 1`:
   - Early Break: If `nums[i] > 0`, break the loop. Since the array is sorted, any two numbers after `nums[i]` will also be positive, making a sum of `0` impossible.
   - Skip Duplicate Anchors: If `i > 0` and `nums[i] == nums[i - 1]`, skip this iteration to prevent duplicate triplets.
3. Two-Pointer Search: Initialize `left = i + 1` and `right = len(nums) - 1`:
   - Compute `three_sum = nums[i] + nums[left] + nums[right]`.
   - If `three_sum > 0`: The sum is too large; decrement `right -= 1`.
   - If `three_sum < 0`: The sum is too small; increment `left += 1`.
   - If `three_sum == 0`:
     - Record the triplet: `res.append([nums[i], nums[left], nums[right]])`.
     - Move both pointers: `left += 1` and `right -= 1`.
     - Advance `left` past any elements identical to the previous `nums[left]` (`while left < right and nums[left] == nums[left - 1]: left += 1`).
     - Advance `right` past any elements identical to the previous `nums[right]` (`while left < right and nums[right] == nums[right + 1]: right -= 1`).
4. Return Results: Return `res`.

#### **Example Walkthrough:**
Consider Example 1: `nums = [-1, 0, 1, 2, -1, -4]`

* **After Sorting:** `nums = [-4, -1, -1, 0, 1, 2]`

| `i` | `nums[i]` | `left` (`nums[left]`) | `right` (`nums[right]`) | `three_sum` | Action |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 0 | `-4` | `1` (`-1`) | `5` (`2`) | `-4 + (-1) + 2 = -3 < 0` | `left += 1` $\rightarrow$ `left = 2` |
| 0 | `-4` | `2` (`-1`) | `5` (`2`) | `-4 + (-1) + 2 = -3 < 0` | `left += 1` $\rightarrow$ `left = 3` |
| 0 | `-4` | `3` (`0`) | `5` (`2`) | `-4 + 0 + 2 = -2 < 0` | `left += 1` $\rightarrow$ `left = 4` |
| 0 | `-4` | `4` (`1`) | `5` (`2`) | `-4 + 1 + 2 = -1 < 0` | `left += 1` $\rightarrow$ `left = 5` (`left == right`, end) |
| 1 | `-1` | `2` (`-1`) | `5` (`2`) | `-1 + (-1) + 2 = 0` | **Found `[-1, -1, 2]`**; `left=3`, `right=4` |
| 1 | `-1` | `3` (`0`) | `4` (`1`) | `-1 + 0 + 1 = 0` | **Found `[-1, 0, 1]`**; `left=4`, `right=3` (cross, end) |
| 2 | `-1` | — | — | — | `nums[2] == nums[1]` $\rightarrow$ **Skip duplicate anchor** |
| 3 | `0` | `4` (`1`) | `5` (`2`) | `0 + 1 + 2 = 3 > 0` | `right -= 1` $\rightarrow$ `right = 4` (cross, end) |
| 4 | `1` | — | — | — | `nums[4] > 0` $\rightarrow$ **Break early** |

* **Final Result:** `[[-1, -1, 2], [-1, 0, 1]]`

#### **Time Complexity:**
$O(n^2)$, where n is the length of the nums list. <br>
We have one loop iterating through the list and a two-pointer approach inside it, which takes linear time.

#### **Space Complexity:**
$O(m)$, where m is the number of unique triplets found. <br>
We use a list to store unique triplets, which can take up space proportional to the number of unique triplets.