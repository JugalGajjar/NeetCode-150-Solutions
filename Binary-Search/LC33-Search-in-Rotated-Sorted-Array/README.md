# 33. Search in Rotated Sorted Array

**Difficulty:** Medium

## Problem
There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly left rotated at an unknown index `k` `(1 <= k < nums.length)` such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` **(0-indexed)**. For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`, *or* `-1` *if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:** <br>
Input: Input: nums = [4,5,6,7,0,1,2], target = 0 <br>
Output: 4

**Example 2:** <br>
Input: nums = [4,5,6,7,0,1,2], target = 3 <br>
Output: -1

**Example 3:** <br>
Input: nums = [1], target = 0 <br>
Output: -1

**Constraints:** <br>
1 <= nums.length <= 5000 <br>
-10^4 <= nums[i] <= 10^4 <br>
All values of `nums` are **unique**. <br>
`nums` is an ascending array that is possibly rotated. <br>
-10^4 <= target <= 10^4


## Solution

#### **Intuition:**
A standard linear search takes $O(n)$ time, but the problem requires an $O(\log n)$ runtime. 

Even though the array has been rotated, it retains a critical invariant: **for any middle index `mid`, at least one half of the array (`[left ... mid]` or `[mid ... right]`) is guaranteed to be sorted**.

Because one half is always sorted, we can easily verify whether the `target` falls within the range of that sorted half:
- If `nums[left] <= nums[mid]`, the left portion is strictly ordered. We check if `nums[left] <= target < nums[mid]`. If it is, `target` must be in the left half; otherwise, it must be in the right half.
- If `nums[left] > nums[mid]`, the right portion must be sorted (`nums[mid] <= nums[right]`). We check if `nums[mid] < target <= nums[right]`. If it is, `target` must be in the right half; otherwise, it must be in the left half.

By determining which half is sorted and whether `target` falls inside its boundaries, we can discard half the remaining search space on every iteration in $O(\log n)$ time.

#### **Logic:**
1. Initialize Boundary Pointers:
   - Set `left = 0` and `right = len(nums) - 1`.
2. Binary Search Loop (`while left <= right`):
   - Compute midpoint: `mid = left + (right - left) // 2`.
   - Direct Match: If `nums[mid] == target`, return `mid`.
   - Determine Which Half is Sorted:
     - Case 1: Left half is sorted (`nums[left] <= nums[mid]`):
       - Check if `target` lies within `[nums[left], nums[mid])`:
         - If `nums[left] <= target < nums[mid]`: search left by setting `right = mid - 1`.
         - Otherwise: search right by setting `left = mid + 1`.
     - Case 2: Right half is sorted (`nums[left] > nums[mid]`):
       - Check if `target` lies within `(nums[mid], nums[right]]`:
         - If `nums[mid] < target <= nums[right]`: search right by setting `left = mid + 1`.
         - Otherwise: search left by setting `right = mid - 1`.
3. Target Not Found: If the loop terminates without finding `target`, return `-1`.

#### **Example Walkthrough:**
Consider Example 1: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`

* **Initial State:** `left = 0`, `right = 6`

| Iteration | `left` | `right` | `mid` | `nums[mid]` | Sorted Half | In Range of Sorted Half? | Action | Next Range |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| 1 | `0` | `6` | `3` | `7` | Left (`nums[0] <= nums[3]`, `4 <= 7`) | No (`0` not in `[4, 7)`) | Search right $\rightarrow$ `left = mid + 1 = 4` | Indices `[4 ... 6]` |
| 2 | `4` | `6` | `5` | `1` | Left (`nums[4] <= nums[5]`, `0 <= 1`) | Yes (`0` in `[0, 1)`) | Search left $\rightarrow$ `right = mid - 1 = 4` | Indices `[4 ... 4]` |
| 3 | `4` | `4` | `4` | `0` | `nums[4] == 0` | **Target Found!** | Return `mid = 4` | — |

* **Final Result:** `4`

#### **Time Complexity:**
$O(\log n)$ <br>
At each iteration, the algorithm discards half the remaining search space, ensuring a logarithmic number of steps.

#### **Space Complexity:**
$O(1)$ <br>
Only pointers (`left`, `right`, `mid`) are maintained.