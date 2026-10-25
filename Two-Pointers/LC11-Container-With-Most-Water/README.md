# 11. Container With Most Water

**Difficulty:** Medium

## Problem
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

**Example 1:** <br>
Input: height = [1,8,6,2,5,4,8,3,7] <br>
Output: 49

Explanation: <br>
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

**Example 2:** <br>
Input: height = [1,1] <br>
Output: 1

**Constraints:** <br>
n == height.length <br>
2 <= n <= 10^5 <br>
0 <= height[i] <= 10^4


## Solution

#### **Intuition:**
The amount of water contained between any two lines at indices `left` and `right` is determined by two factors:
$$\text{Area} = (\text{right} - \text{left}) \times \min(\text{height}[\text{left}], \text{height}[\text{right}])$$

The width is the horizontal distance between the lines, and the height is strictly limited by the shorter line (the bottleneck).

A brute-force search over all pairs takes $O(n^2)$ time. To optimize this to linear $O(n)$ time, we use the **Two-Pointer technique**:
1. Start with the widest possible container by setting `left = 0` and `right = len(height) - 1`.
2. As we move the pointers inward, the width $(\text{right} - \text{left})$ strictly decreases at every step.
3. Therefore, the only way to achieve a larger area is to find a significantly taller bottleneck. 
4. If we move the taller line inward, the container height will still be constrained by the shorter line (or an even shorter one), but with a smaller width, guaranteeing a smaller area. Thus, the only choice that could potentially yield a larger area is to move the pointer pointing to the **shorter line** inward.

#### **Logic:**
1. Initialize Two Pointers & Max Tracker:
   - Set `left = 0` and `right = len(height) - 1`.
   - Set `max_water = 0`.
2. Scan Inward While `left < right`:
   - Compute the container width: `width = right - left`.
   - Compute current water volume: `current_area = width * min(height[left], height[right])`.
   - Update maximum area: `max_water = max(max_water, current_area)`.
   - Move the Bottleneck:
     - If `height[left] < height[right]`, increment `left += 1` in search of a taller left boundary.
     - Otherwise, decrement `right -= 1` in search of a taller right boundary.
3. Return Result: Return `max_water`.

#### **Example Walkthrough:**
Consider Example 1: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`

* **Initial State:** `left = 0`, `right = 8`, `max_water = 0`

| Step | `left` (`height[left]`) | `right` (`height[right]`) | `width` | Bottleneck Height | `current_area` | `max_water` | Pointer Shift |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `0` (`1`) | `8` (`7`) | $8 - 0 = 8$ | $\min(1, 7) = 1$ | $8 \times 1 = 8$ | $8$ | `height[0] < height[8]` $\rightarrow$ `left += 1` (`1`) |
| 2 | `1` (`8`) | `8` (`7`) | $8 - 1 = 7$ | $\min(8, 7) = 7$ | $7 \times 7 = 49$ | **$49$** | `height[8] <= height[1]` $\rightarrow$ `right -= 1` (`7`) |
| 3 | `1` (`8`) | `7` (`3`) | $7 - 1 = 6$ | $\min(8, 3) = 3$ | $6 \times 3 = 18$ | $49$ | `height[7] < height[1]` $\rightarrow$ `right -= 1` (`6`) |
| 4 | `1` (`8`) | `6` (`8`) | $6 - 1 = 5$ | $\min(8, 8) = 8$ | $5 \times 8 = 40$ | $49$ | `height[6] <= height[1]` $\rightarrow$ `right -= 1` (`5`) |
| 5 | `1` (`8`) | `5` (`4`) | $5 - 1 = 4$ | $\min(8, 4) = 4$ | $4 \times 4 = 16$ | $49$ | `height[5] < height[1]` $\rightarrow$ `right -= 1` (`4`) |
| 6 | `1` (`8`) | `4` (`5`) | $4 - 1 = 3$ | $\min(8, 5) = 5$ | $3 \times 5 = 15$ | $49$ | `height[4] < height[1]` $\rightarrow$ `right -= 1` (`3`) |
| 7 | `1` (`8`) | `3` (`2`) | $3 - 1 = 2$ | $\min(8, 2) = 2$ | $2 \times 2 = 4$ | $49$ | `height[3] < height[1]` $\rightarrow$ `right -= 1` (`2`) |
| 8 | `1` (`8`) | `2` (`6`) | $2 - 1 = 1$ | $\min(8, 6) = 6$ | $1 \times 6 = 6$ | $49$ | `height[2] < height[1]` $\rightarrow$ `right -= 1` (`1`) |

* Pointers meet (`left == right == 1`), loop terminates.
* **Final Result:** `49`

#### **Time Complexity:**
$O(n)$, where n is the length of the height list. <br>
We traverse the list once with two pointers.

#### **Space Complexity:**
$O(1)$ <br>
We use constant extra space, as we only store the maximum area found and the two pointers.