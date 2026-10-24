# 167. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium

## Problem
You are given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**.

Find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers `index1` and `index2` as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

**Example 1:** <br>
Input: numbers = [2,7,11,15], target = 9 <br>
Output: [1,2]

Explanation: <br>
The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

**Example 2:** <br>
Input: numbers = [2,3,4], target = 6 <br>
Output: [1,3]

Explanation: <br>
The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

**Example 3:** <br>
Input: numbers = [-1,0], target = -1 <br>
Output: [1,2]

Explanation: <br>
The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

**Constraints:** <br>
2 <= numbers.length <= 3 * 104 <br>
-1000 <= numbers[i] <= 1000 <br>
`numbers` is sorted in **non-decreasing order**. <br>
-1000 <= target <= 1000 <br>
The tests are generated such that there is **exactly one solution**.


## Solution

#### **Intuition:**
Unlike the standard Two Sum problem where elements are unsorted and a hash map is used ($O(n)$ space), here the input array is already **sorted in non-decreasing order**, and we are strictly constrained to **constant extra space** ($O(1)$).

The sorted property gives us a directional guarantee when using the **Two-Pointer technique**:
- Placing a pointer at the beginning (`left`) gives us the smallest available value.
- Placing a pointer at the end (`right`) gives us the largest available value.

By calculating `cur_sum = numbers[left] + numbers[right]`:
- If `cur_sum > target`, the sum is too large. Because the array is sorted, the only way to decrease the sum is to move `right` to the left.
- If `cur_sum < target`, the sum is too small. The only way to increase the sum is to move `left` to the right.
- If `cur_sum == target`, we have found the unique pair.

This allows us to eliminate one element at each step without ever needing to allocate extra memory.

#### **Logic:**
1. Initialize Two Pointers: Set `left = 0` (pointing to the smallest element) and `right = len(numbers) - 1` (pointing to the largest element).
2. Search While `left < right`:
   - Compute the sum: `cur_sum = numbers[left] + numbers[right]`.
   - If `cur_sum == target`: Return the **1-indexed** positions: `[left + 1, right + 1]`.
   - If `cur_sum > target`: Decrement `right -= 1` to decrease the total sum.
   - If `cur_sum < target`: Increment `left += 1` to increase the total sum.
3. The problem guarantees exactly one valid solution, so the pointers will always meet at the correct pair.

#### **Example Walkthrough:**
Consider Example 1: `numbers = [2, 7, 11, 15]`, `target = 9`

**Initial State:** `left = 0`, `right = 3`

| Step | `left` (`numbers[left]`) | `right` (`numbers[right]`) | `cur_sum` | Comparison to `target = 9` | Action |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `0` (`2`) | `3` (`15`) | `2 + 15 = 17` | `17 > 9` (Too large) | Decrement `right` $\rightarrow$ `right = 2` |
| 2 | `0` (`2`) | `2` (`11`) | `2 + 11 = 13` | `13 > 9` (Too large) | Decrement `right` $\rightarrow$ `right = 1` |
| 3 | `0` (`2`) | `1` (`7`) | `2 + 7 = 9` | `9 == 9` (**Match!**) | Return `[0 + 1, 1 + 1]` $\rightarrow$ `[1, 2]` |

* **Result:** `[1, 2]`

#### **Time Complexity:**
$O(n)$ <br>
We traverse the list once with two pointers.

#### **Space Complexity:**
$O(1)$ <br>
We use constant extra space, as we only store the indices of the two numbers.