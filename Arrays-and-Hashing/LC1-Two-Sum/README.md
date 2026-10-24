# 1. Two Sum

**Difficulty:** Easy

## Problem
You are given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:** <br>
Input: nums = [2,7,11,15], target = 9 <br>
Output: [0,1]

Explanation: <br>
The sum of `nums[0]` and `nums[1]` is 2 + 7 = 9, which equals the target. Therefore, the indices `[0, 1]` are returned.

**Example 2:** <br>
Input: nums = [3,2,4], target = 6 <br>
Output: [1,2]

Explanation: <br>
The sum of `nums[1]` and `nums[2]` is 2 + 4 = 6, which equals the target. Therefore, the indices `[1, 2]` are returned.

**Example 3:** <br>
Input: nums = [3,3], target = 6 <br>
Output: [0,1]

Explanation: <br>
The sum of `nums[0]` and `nums[1]` is 3 + 3 = 6, which equals the target. Therefore, the indices `[0, 1]` are returned.

**Constraints:** <br>
2 <= nums.length <= 10^4 <br>
-10^9 <= nums[i] <= 10^9 <br>
-10^9 <= target <= 10^9 <br>
Only one valid answer exists.


## Solution

#### **Intuition:**
Instead of checking every possible pair with nested loops in $O(n^2)$ time, we can reframe the problem: for any number `x`, we need to find if its complement `y = target - x` has already appeared before it in the array. 

By using a **Hash Map** to store each number and its corresponding index as we iterate through `nums`, we can check whether the complement `y` exists in $O(1)$ average time. This allows us to find the pair in a single pass through the array.

#### **Logic:**
1. Initialize an empty hash map (e.g., `prev_map`) to store numbers as keys and their array indices as values (`num -> index`).
2. Iterate through the array with index `i` and element `num`:
   - Compute the required complement: `diff = target - num`.
   - Check if `diff` exists in `prev_map`:
     - If it exists, return `[prev_map[diff], i]`.
     - If it does not exist, store `num` and its index `i` into `prev_map`: `prev_map[num] = i`.
3. Since the problem guarantees exactly one valid solution, the loop will always find and return the matching pair.

#### **Example Walkthrough:**
Consider Example 1: `nums = [2, 7, 11, 15]`, `target = 9`

* **Initialization:** `prev_map = {}`

| Step (`i`) | Current Element (`num`) | Required Complement (`diff = 9 - num`) | In `prev_map`? | Action | `prev_map` State |
| :---: | :---: | :---: | :---: | :--- | :--- |
| 0 | `2` | `9 - 2 = 7` | No | Store `prev_map[2] = 0` | `{2: 0}` |
| 1 | `7` | `9 - 7 = 2` | **Yes** (at index `0`) | Return `[prev_map[2], 1]` -> `[0, 1]` | `{2: 0}` |

* **Result:** `[0, 1]` (Terminates early at index 1 without scanning the remaining elements).

#### **Time Complexity:**
$O(n)$ <br>
We traverse the list containing n elements only once. Each lookup in the map costs only O(1) time.

#### **Space Complexity:**
$O(n)$ <br>
We store up to n elements in the hash map.