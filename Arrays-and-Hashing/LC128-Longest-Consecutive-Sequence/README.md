# 128. Longest Consecutive Sequence

**Difficulty:** Medium

## Problem
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in $O(n)$ time.

**Example 1:** <br>
Input: nums = [100,4,200,1,3,2] <br>
Output: 4

Explanation: <br>
The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

**Example 2:** <br>
Input: nums = [0,3,7,2,5,8,4,6,0,1] <br>
Output: 9

**Example 3:** <br>
Input: nums = [1,0,1,2] <br>
Output: 3

**Constraints:** <br>
0 <= nums.length <= 10^5 <br>
-10^9 <= nums[i] <= 10^9


## Solution

#### **Intuition:**
A sorting-based approach sorts the array and counts adjacent elements, but that takes $O(n \log n)$ time and fails the problem's strict $O(n)$ time constraint.

To achieve linear time, we can store all numbers in a **Hash Set**, which allows $O(1)$ average time lookups. However, if we attempt to build a sequence starting from *every* number, the time complexity could still degrade back to $O(n^2)$. 

The critical insight to guarantee $O(n)$ time is to only attempt building a sequence from numbers that can be the **start of a sequence**. A number `num` is the start of a sequence if and only if its predecessor `num - 1` does **not** exist in the set. If `num - 1` is present, `num` is part of a longer sequence that will be counted (or has already been counted) when starting from an earlier element, so we can skip it immediately in $O(1)$ time.

#### **Logic:**
1. Initialize a Hash Set: Convert the input array `nums` into a set `num_set` to remove duplicates and enable $O(1)$ lookups.
2. Track the Maximum Length: Initialize `longest_streak = 0`.
3. Scan Elements: Iterate through each number `num` in `num_set`:
   - Check if `(num - 1)` is in `num_set`:
     - If `(num - 1)` **is** in the set, skip `num` (it cannot be the start of a sequence).
     - If `(num - 1)` **is not** in the set, `num` is the beginning of a new sequence:
       - Set `current_num = num` and `current_streak = 1`.
       - While `(current_num + 1)` exists in `num_set`, increment both `current_num` and `current_streak` by 1.
       - Update `longest_streak = max(longest_streak, current_streak)`.
4. Return Result: Return `longest_streak`.

#### **Example Walkthrough:**
Consider Example 1: `nums = [100, 4, 200, 1, 3, 2]`

**Set Conversion:** `num_set = {100, 4, 200, 1, 3, 2}`

**Initial State:** `longest_streak = 0`

| Element (`num`) | Is `num - 1` in `num_set`? | Is Sequence Start? | Sequence Exploration | `current_streak` | `longest_streak` |
| :---: | :---: | :---: | :--- | :---: | :---: |
| `100` | `99` in set? $\rightarrow$ **No** | Yes | Check `101`: not in set | 1 | `max(0, 1) = 1` |
| `4` | `3` in set? $\rightarrow$ **Yes** | No | *Skipped immediately* | — | 1 |
| `200` | `199` in set? $\rightarrow$ **No** | Yes | Check `201`: not in set | 1 | `max(1, 1) = 1` |
| `1` | `0` in set? $\rightarrow$ **No** | Yes | `1 -> 2 -> 3 -> 4` (all in set); `5` not in set | 4 | `max(1, 4) = 4` |
| `3` | `2` in set? $\rightarrow$ **Yes** | No | *Skipped immediately* | — | 4 |
| `2` | `1` in set? $\rightarrow$ **Yes** | No | *Skipped immediately* | — | 4 |

* **Final Result:** `4`

#### **Time Complexity:**
$O(n)$ <br>
We iterate through the set of numbers, and for each number, we may check for the next consecutive number in the set, which takes O(1) time on average.

#### **Space Complexity:**
$O(n)$ <br>
We are using a set to store the numbers, which takes O(n) space in the worst case.