# 74. Search a 2D Matrix

**Difficulty:** Medium

## Problem
You are given an `m x n` integer matrix matrix with the following two properties:
* Each row is sorted in non-decreasing order.
* The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in matrix or `false` otherwise.

You must write a solution in `O(log(m * n))` time complexity.

**Example 1:** <br>
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 <br>
Output: true

**Example 2:** <br>
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 <br>
Output: false

**Constraints:** <br>
m == matrix.length <br>
n == matrix[i].length <br>
1 <= m, n <= 100 <br>
-10^4 <= matrix[i][j], target <= 10^4


## Solution

#### **Intuition:**
A brute-force scan across every element takes $O(m \cdot n)$ time. 

However, the problem specifies two critical properties:
1. Each row is sorted in non-decreasing order.
2. The first element of each row is strictly greater than the last element of the preceding row.

Because each row picks up directly where the previous one left off in terms of ordering, the entire 2D matrix can be visualized as a single, contiguous sorted 1D array of length $m \times n$. 

Instead of performing two separate binary searches (one to find the correct row and another to find the column), we can perform a **single standard Binary Search** over a virtual 1D range from index `0` to `m * n - 1`. For any 1D index `mid`, we map it back to 2D coordinates using integer division and modulo:
$$\text{row} = \text{mid} // n, \quad \text{col} = \text{mid} \% n$$

This enables us to find the target or conclude it is absent in optimal $O(\log(m \cdot n))$ time without reshaping or allocating additional memory.

#### **Logic:**
1. Edge Case: If the matrix is empty or has no columns, return `False`.
2. Virtual Boundaries:
   - Let `m = len(matrix)` (number of rows) and `n = len(matrix[0])` (number of columns).
   - Set virtual 1D pointers: `left = 0` and `right = (m * n) - 1`.
3. Binary Search Loop (`while left <= right`):
   - Calculate the 1D midpoint: `mid = left + (right - left) // 2`.
   - Convert `mid` into 2D indices:
     - `row = mid // n`
     - `col = mid % n`
   - Access the element: `mid_val = matrix[row][col]`.
   - Evaluate Value:
     - If `mid_val == target`: Return `True`.
     - If `mid_val < target`: Discard the left half $\rightarrow$ `left = mid + 1`.
     - If `mid_val > target`: Discard the right half $\rightarrow$ `right = mid - 1`.
4. Target Not Found: If `left > right` without finding a match, return `False`.

#### **Example Walkthrough:**
Consider Example 1: `matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]`, `target = 3`

* Dimensions: $m = 3$, $n = 4$
* Total elements: $3 \times 4 = 12$
* Initial search range: `left = 0`, `right = 11`

| Iteration | `left` | `right` | `mid` | 2D Coords (`row`, `col`) | `mid_val` | Comparison to `target = 3` | Action |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `0` | `11` | $0 + (11 - 0) // 2 = \mathbf{5}$ | `row = 5 // 4 = 1`<br>`col = 5 % 4 = 1` | `11` | `11 > 3` (Too large) | `right = mid - 1 = 4` |
| 2 | `0` | `4` | $0 + (4 - 0) // 2 = \mathbf{2}$ | `row = 2 // 4 = 0`<br>`col = 2 % 4 = 2` | `5` | `5 > 3` (Too large) | `right = mid - 1 = 1` |
| 3 | `0` | `1` | $0 + (1 - 0) // 2 = \mathbf{0}$ | `row = 0 // 4 = 0`<br>`col = 0 % 4 = 0` | `1` | `1 < 3` (Too small) | `left = mid + 1 = 1` |
| 4 | `1` | `1` | $1 + (1 - 1) // 2 = \mathbf{1}$ | `row = 1 // 4 = 0`<br>`col = 1 % 4 = 1` | `3` | `3 == 3` (**Match!**) | **Return `True`** |

* **Final Result:** `true`

#### **Time Complexity:**
$O(\log (m * n))$ <br>
We perform a binary search on the entire matrix, which has m * n elements.

#### **Space Complexity:**
$O(1)$ <br>
We use constant extra space, as we only store a few variables for the binary search.