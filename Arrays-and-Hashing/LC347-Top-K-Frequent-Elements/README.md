# 347. Top K Frequent Elements

**Difficulty:** Medium

## Problem
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Example 1:** <br>
Input: nums = [1,1,1,2,2,3], k = 2 <br>
Output: [1,2]

**Example 2:** <br>
Input: nums = [1], k = 1 <br>
Output: [1]

**Example 3:** <br>
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2 <br>
Output: [1,2]

**Constraints:** <br>
1 <= nums.length <= 105 <br>
-104 <= nums[i] <= 104 <br>
`k` is in the range [1, the number of unique elements in the array]. <br>
It is **guaranteed** that the answer is **unique**.


## Solution

#### **Intuition:**
A standard approach is to count element frequencies and sort them, which takes $O(n \log n)$ time, or use a min-heap of size $k$, which takes $O(n \log k)$ time. However, the problem asks for a solution faster than $O(n \log n)$, and we can achieve strictly linear $O(n)$ time using **Bucket Sort**.

The key insight is that the frequency of any element in an array of size $n$ is bounded between $1$ and $n$. Instead of sorting elements by their counts, we can create an array of "buckets" where the index represents the frequency, and each bucket holds a list of numbers that appear with that exact frequency. By scanning the buckets backward from index $n$ down to $1$, we naturally encounter the elements with the highest frequencies first.

#### **Logic:**
1. Count Frequencies: Count the occurrence of each unique number using a hash map (or `Counter`).
2. Build Buckets: Create a list of empty lists (`buckets`) of length `len(nums) + 1`, where index `i` will store all numbers that appear with frequency `i`.
3. Populate Buckets: Iterate through the key-value pairs of the frequency map and append each number to `buckets[frequency]`.
4. Collect Top $k$ Elements: Initialize an empty result list `res`. Iterate backward through `buckets` from the highest possible frequency (`len(nums)`) down to `1`:
   - Append each number in the current bucket to `res`.
   - Once `len(res) == k`, return `res` immediately.

#### **Example Walkthrough:**
Consider Example 1: `nums = [1, 1, 1, 2, 2, 3]`, `k = 2`

* `len(nums) = 6`

**Count Frequencies:** `{1: 3, 2: 2, 3: 1}`

**Populate Buckets** (`buckets` size = 7, indices 0 to 6):

| Frequency Index (`i`) | Elements in `buckets[i]` |
| :---: | :---: |
| 0 | `[]` |
| 1 | `[3]` |
| 2 | `[2]` |
| 3 | `[1]` |
| 4 | `[]` |
| 5 | `[]` |
| 6 | `[]` |

**Traverse Buckets Backward** (from index 6 down to 1):
   - Indices 6, 5, 4: Empty.
   - Index 3: Contains `[1]`. Add `1` to `res` $\rightarrow$ `res = [1]` (`len(res) = 1 < 2`).
   - Index 2: Contains `[2]`. Add `2` to `res` $\rightarrow$ `res = [1, 2]` (`len(res) == 2`).
   - Target size `k = 2` reached; return `[1, 2]`.

* **Result:** `[1, 2]`

#### **Time Complexity:**
$O(n)$ <br>
We traverse the list containing n elements to count frequencies and then traverse the buckets to collect the top k frequent elements.

#### **Space Complexity:**
$O(n)$ <br>
We store the frequency counts in a hash map and the buckets can take up to $O(n)$ space in the worst case.