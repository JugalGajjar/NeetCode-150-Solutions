# 4. Median of Two Sorted Arrays

**Difficulty:** Hard

## Problem
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the `median` of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

**Example 1:** <br>
Input: nums1 = [1,3], nums2 = [2] <br>
Output: 2.00000

Explanation: <br>
merged array = [1,2,3] and median is 2.


**Example 2:** <br>
Input: nums1 = [1,2], nums2 = [3,4] <br>
Output: 2.50000

Explanation: <br>
merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

**Constraints:** <br>
nums1.length == m <br>
nums2.length == n <br>
0 <= m <= 1000 <br>
0 <= n <= 1000 <br>
1 <= m + n <= 2000 <br>
-10^6 <= nums1[i], nums2[i] <= 10^6


## Solution

#### **Intuition:**
Merging both arrays takes $O(m + n)$ time, which violates the strict $O(\log (m + n))$ runtime constraint.

The median of a combined sorted array splits all elements into two equal halves (a left half and a right half) such that every element in the left half is less than or equal to every element in the right half:
- If the total length $m + n$ is **even**, the median is the average of the largest value in the left half and the smallest value in the right half.
- If the total length is **odd**, the median is simply the smallest value in the right half (or largest in the left half, depending on convention).

Instead of merging the arrays, we can partition both arrays simultaneously using **Binary Search**:
- We binary search for the correct partition cut index `i` in the **smaller array** `A` (to guarantee $O(\log(\min(m, n)))$ steps).
- The partition cut `j` in array `B` is derived automatically such that the total number of elements on the left matches `half = (m + n) // 2`.
- Let the elements adjacent to the cuts be:
  - `A_left` (largest in left partition of `A`) and `A_right` (smallest in right partition of `A`)
  - `B_left` (largest in left partition of `B`) and `B_right` (smallest in right partition of `B`)
- The partition is valid when:
  $$A_{\text{left}} \le B_{\text{right}} \quad \text{and} \quad B_{\text{left}} \le A_{\text{right}}$$
- If $A_{\text{left}} > B_{\text{right}}$, our cut in `A` is too far right $\rightarrow$ search left (`right = i - 1`).
- If $B_{\text{left}} > A_{\text{right}}$, our cut in `A` is too far left $\rightarrow$ search right (`left = i + 1`).

#### **Logic:**
1. Ensure Smaller Array First:
   - If `len(nums1) > len(nums2)`, swap them so that `A` is always the shorter array ($len(A) \le len(B)$).
2. Setup Variables & Binary Search Boundaries:
   - Let `total = len(A) + len(B)` and `half = total // 2`.
   - Set binary search range on `A`'s cut index: `left = 0`, `right = len(A)`.
3. Binary Search Loop (`while True`):
   - Compute partition indices:
     - `i = (left + right) // 2` (elements contributed by `A` to left half)
     - `j = half - i` (elements contributed by `B` to left half)
   - Determine boundary values, using $-\infty$ and $+\infty$ for out-of-bounds indices:
     - `A_left = A[i - 1]` if `i > 0` else $-\infty$
     - `A_right = A[i]` if `i < len(A)` else $+\infty$
     - `B_left = B[j - 1]` if `j > 0` else $-\infty$
     - `B_right = B[j]` if `j < len(B)` else $+\infty$
   - Evaluate Partition Validity:
     - Valid Partition (`A_left <= B_right` and `B_left <= A_right`):
       - If `total` is odd: `return float(min(A_right, B_right))`
       - If `total` is even: `return (max(A_left, B_left) + min(A_right, B_right)) / 2.0`
     - Cut `i` is too far right (`A_left > B_right`):
       - Shrink cut in `A`: `right = i - 1`.
     - Cut `i` is too far left (`B_left > A_right`):
       - Expand cut in `A`: `left = i + 1`.

#### **Example Walkthrough:**
Consider Example 2: `nums1 = [1, 2]`, `nums2 = [3, 4]`

* `A = [1, 2]`, `B = [3, 4]`
* `total = 2 + 2 = 4`, `half = 4 // 2 = 2`
* `left = 0`, `right = 2`

| Iteration | `left` | `right` | `i` | `j = half - i` | `A_left` | `A_right` | `B_left` | `B_right` | Valid Partition? | Action / Result |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `0` | `2` | **`1`** | **`1`** | `A[0] = 1` | `A[1] = 2` | `B[0] = 3` | `B[1] = 4` | $1 \le 4$ (Yes), but $3 \le 2$ (**No**) | `B_left > A_right` $\rightarrow$ cut in `A` too small $\rightarrow$ `left = i + 1 = 2` |
| 2 | `2` | `2` | **`2`** | **`0`** | `A[1] = 2` | `+∞` | `-∞` | `B[0] = 3` | $2 \le 3$ (Yes) and $-\infty \le +\infty$ (Yes) | **Valid partition found!** |

* Since `total = 4` is even:
  $$\text{Median} = \frac{\max(A_{\text{left}}, B_{\text{left}}) + \min(A_{\text{right}}, B_{\text{right}})}{2.0} = \frac{\max(2, -\infty) + \min(+\infty, 3)}{2.0} = \frac{2 + 3}{2.0} = 2.5$$
* **Final Result:** `2.50000`

#### **Time Complexity:**
$O(\log(\min(m, n)))$  <br>
Binary search is performed strictly over the smaller array of length $\min(m, n)$, which is bounded well within the required $O(\log(m + n))$.

#### **Space Complexity:**
$O(1)$ <br>
Only constant memory is used for pointers and partition boundary values.