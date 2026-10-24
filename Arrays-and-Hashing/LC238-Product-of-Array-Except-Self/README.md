# 238. Product of Array Except Self

**Difficulty:** Medium

## Problem
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in $O(n)$ time and without using the division operation.

**Example 1:** <br>
Input: nums = [1,2,3,4] <br>
Output: [24,12,8,6]

**Example 2:** <br>
Input: nums = [-1,1,0,-3,3] <br>
Output: [0,0,9,0,0]

**Constraints:** <br>
2 <= nums.length <= 10^5 <br>
-30 <= nums[i] <= 30 <br>
The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.


## Solution

#### **Intuition:**
For any given index `i`, the product of all elements except `nums[i]` can be decomposed into two independent parts:
1. The product of all numbers to the **left** of `i` (prefix product).
2. The product of all numbers to the **right** of `i` (suffix/postfix product).

Therefore:
$$\text{answer}[i] = (\text{prefix product before } i) \times (\text{postfix product after } i)$$

While we could create separate arrays for prefix and postfix products, that requires $O(n)$ auxiliary memory. To solve it in $O(1)$ extra space, we can compute the prefix products directly inside our output array `answer` during a first pass from left to right. Then, in a second pass from right to left, we maintain a running `postfix` variable and multiply it into each element of `answer[i]`.

#### **Logic:**
1. Initialize Output Array: Create an array `answer` of length $n$ initialized to `1`.
2. First Pass (Left-to-Right for Prefix):
   - Maintain a running product variable `prefix = 1`.
   - For every index `i` from `0` to `n - 1`:
     - Assign `answer[i] = prefix` (the product of all elements to the left of `i`).
     - Update `prefix *= nums[i]` to include the current element for upcoming indices.
3. Second Pass (Right-to-Left for Postfix):
   - Maintain a running product variable `postfix = 1`.
   - For every index `i` from `n - 1` down to `0`:
     - Multiply the existing value in `answer[i]` by `postfix`: `answer[i] *= postfix`.
     - Update `postfix *= nums[i]` to include the current element for preceding indices.
4. Return `answer`.

#### **Example Walkthrough:**
Consider Example 1: `nums = [1, 2, 3, 4]`, $n = 4$

**Initialization:** `answer = [1, 1, 1, 1]`

**Pass 1:** Prefix Products (Left $\rightarrow$ Right)

| Index `i` | `nums[i]` | Prefix Before `i` | `answer[i] = prefix` | Updated `prefix` (`prefix * nums[i]`) |
| :---: | :---: | :---: | :---: | :---: |
| 0 | `1` | `1` | `answer[0] = 1` | `1 * 1 = 1` |
| 1 | `2` | `1` | `answer[1] = 1` | `1 * 2 = 2` |
| 2 | `3` | `2` | `answer[2] = 2` | `2 * 3 = 6` |
| 3 | `4` | `6` | `answer[3] = 6` | `6 * 4 = 24` |

* `answer` after Pass 1: `[1, 1, 2, 6]`

**Pass 2:** Suffix Products (Right $\rightarrow$ Left)

| Index `i` | `nums[i]` | Current `answer[i]` | `postfix` | `answer[i] *= postfix` | Updated `postfix` (`postfix * nums[i]`) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 3 | `4` | `6` | `1` | `6 * 1 = 6` | `1 * 4 = 4` |
| 2 | `3` | `2` | `4` | `2 * 4 = 8` | `4 * 3 = 12` |
| 1 | `2` | `1` | `12` | `1 * 12 = 12` | `12 * 2 = 24` |
| 0 | `1` | `1` | `24` | `1 * 24 = 24` | `24 * 1 = 24` |

* **Final Result:** `[24, 12, 8, 6]`

#### **Time Complexity:**
$O(n)$ <br>
Two sequential linear traversals over the array of size $n$.

#### **Space Complexity:**
$O(1)$ <br>
As per the problem description, the output array `answer` does not count toward auxiliary memory complexity, and only a constant number of scalar variables (`prefix`, `postfix`) are used.