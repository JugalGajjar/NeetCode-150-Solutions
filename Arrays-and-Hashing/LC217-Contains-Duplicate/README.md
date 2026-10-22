# 217. Contains Duplicate

**Difficulty:** Easy

## Problem
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Example 1:** <br>
Input: nums = [1,2,3,1] <br>
Output: true

Explanation: <br>
The element 1 occurs at the indices 0 and 3.

**Example 2:** <br>
Input: nums = [1,2,3,4] <br>
Output: false

Explanation: <br>
All elements are distinct.

**Example 3:** <br>
Input: nums = [1,1,1,3,3,4,3,2,4,2] <br>
Output: true

**Constraints:** <br>
1 <= nums.length <= 105 <br>
-109 <= nums[i] <= 109


## Solution

#### **Intuition:**
To determine whether an array contains any duplicates, we need a way to remember numbers we have already seen as we iterate through the list. While comparing every pair takes quadratic time $O(n^2)$, a **Hash Set** provides average $O(1)$ time complexity for both insertions and lookups. By maintaining a set of visited elements, we can identify a duplicate the moment we encounter a number that is already present in the set.

#### **Logic:**
1. Initialize an empty hash set (e.g., `seen`) to keep track of visited numbers.
2. Iterate through the array one element `i` at a time:
   - Check if `i` is already in `seen`. If it is, return `True` immediately (duplicate found).
   - Otherwise, insert `i` into `seen` and continue to the next element.
3. Return `False` if the loop finishes without finding any repeated elements, meaning all values in the array are distinct.

#### **Example Walkthrough:**
Consider Example 1: `nums = [1, 2, 3, 1]`

**Initialization:** `seen = set()`

| Step | Current Element (`i`) | In `seen`? | Action | `seen` State |
| :---: | :---: | :---: | :--- | :--- |
| 1 | `1` | No | Add `1` to `seen` | `{1}` |
| 2 | `2` | No | Add `2` to `seen` | `{1, 2}` |
| 3 | `3` | No | Add `3` to `seen` | `{1, 2, 3}` |
| 4 | `1` | **Yes** | Duplicate detected; return `True` | `{1, 2, 3}` |

**Result:** `True` (Terminates early at index 3 without scanning any further).

#### **Time Complexity:**
$O(n)$ <br>
This is because we iterate through the list once, and set operations (insertion and lookup) are $O(1)$ on average.

#### **Space Complexity:**
$O(n)$ <br>
We are using a set to store the unique elements from the input list, which can grow up to the size of the input list in the worst case.