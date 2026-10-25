# 42. Trapping Rain Water

**Difficulty:** Hard

## Problem
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:** <br>
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] <br>
Output: 6

Explanation: <br>
The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

**Example 2:** <br>
Input: height = [4,2,0,3,2,5] <br>
Output: 9

**Constraints:** <br>
n == height.length <br>
1 <= n <= 2 * 10^4 <br>
0 <= height[i] <= 10^5


## Solution

#### **Intuition:**
The amount of water trapped above any individual bar at index `i` is determined by the shorter of the maximum heights to its left and right, minus its own height:
$$\text{water}[i] = \max(0, \min(\text{left\_max}, \text{right\_max}) - \text{height}[i])$$

A dynamic programming approach precomputes prefix and suffix maximum arrays in $O(n)$ time and $O(n)$ space. To optimize auxiliary space down to strictly $O(1)$, we use the **Two-Pointer technique**.

By placing `left = 0` and `right = len(height) - 1`, we maintain running values for `left_max` and `right_max`. The crucial insight is:
- The water level at any point is bottlenecked entirely by $\min(\text{left\_max}, \text{right\_max})$.
- If `left_max < right_max`, we know for certain that the left boundary is the smaller bottleneck. Regardless of how high bars further to the right might be, the water level at the `left` position is strictly limited by `left_max`. Thus, we can safely compute trapped water at `left` and advance `left += 1`.
- Conversely, if `right_max <= left_max`, the right boundary is the bottleneck, so we compute trapped water at `right` and advance `right -= 1`.

#### **Logic:**
1. Edge Case: If `height` is empty, return `0`.
2. Initialize Pointers & Variables:
   - `left = 0`, `right = len(height) - 1`.
   - `left_max = height[left]`, `right_max = height[right]`.
   - `total_water = 0`.
3. Traverse Inward While `left < right`:
   - Case 1: `left_max < right_max`
     - Advance `left += 1`.
     - Update `left_max = max(left_max, height[left])`.
     - Add trapped water: `total_water += left_max - height[left]`.
   - Case 2: `left_max >= right_max`
     - Advance `right -= 1`.
     - Update `right_max = max(right_max, height[right])`.
     - Add trapped water: `total_water += right_max - height[right]`.
4. Return Result: Return `total_water`.

#### **Example Walkthrough:**
Consider Example 2: `height = [4, 2, 0, 3, 2, 5]`

* **Initial State:** `left = 0`, `right = 5`, `left_max = 4`, `right_max = 5`, `total_water = 0`

| Step | `left` (`val`) | `right` (`val`) | Condition | Action | Updated Max | Water Added | `total_water` |
| :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: |
| Start | `0` (`4`) | `5` (`5`) | `left_max (4) < right_max (5)` | `left += 1` $\rightarrow$ `1` (`2`) | `left_max = max(4, 2) = 4` | $4 - 2 = 2$ | **2** |
| 1 | `1` (`2`) | `5` (`5`) | `left_max (4) < right_max (5)` | `left += 1` $\rightarrow$ `2` (`0`) | `left_max = max(4, 0) = 4` | $4 - 0 = 4$ | **6** |
| 2 | `2` (`0`) | `5` (`5`) | `left_max (4) < right_max (5)` | `left += 1` $\rightarrow$ `3` (`3`) | `left_max = max(4, 3) = 4` | $4 - 3 = 1$ | **7** |
| 3 | `3` (`3`) | `5` (`5`) | `left_max (4) < right_max (5)` | `left += 1` $\rightarrow$ `4` (`2`) | `left_max = max(4, 2) = 4` | $4 - 2 = 2$ | **9** |
| 4 | `4` (`2`) | `5` (`5`) | `left_max (4) < right_max (5)` | `left += 1` $\rightarrow$ `5` (`5`) | `left_max = max(4, 5) = 5` | $5 - 5 = 0$ | **9** |

* Pointers meet (`left == right == 5`), loop terminates.
* **Final Result:** `9`

#### **Time Complexity:**
$O(n)$, where n is the length of the height list. <br>
We traverse the list once with two pointers.

#### **Space Complexity:**
$O(1)$ <br>
We use constant extra space, as we only store a few variables for the pointers and maximum heights.