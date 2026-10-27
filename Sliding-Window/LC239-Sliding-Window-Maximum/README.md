# 239. Sliding Window Maximum

**Difficulty:** Hard

## Problem
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the max sliding window*.

**Example 1:** <br>
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3 <br>
Output: [3,3,5,5,6,7]

Explanation: <br>
```
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Example 2:** <br>
Input: nums = [1], k = 1 <br>
Output: [1]

**Constraints:** <br>
1 <= nums.length <= 10^5 <br>
-10^4 <= nums[i] <= 10^4 <br>
1 <= k <= nums.length


## Solution

#### **Intuition:**
A brute-force solution scans all $k$ elements in each window, resulting in $O(n \cdot k)$ time. Given $n, k \le 10^5$, this causes a Time Limit Exceeded (TLE). A max-heap would allow $O(n \log k)$ or $O(n \log n)$ time, but heap removals take $O(\log n)$ time.

To achieve optimal $O(n)$ linear time, we use a **Monotonic Decreasing Deque (Double-Ended Queue)**.

The core insight is:
- If a new number `num` enters the window and is strictly greater than older numbers already in the queue, those older numbers can **never** be the maximum for the current window or any future window because `num` is both larger and will stay in the window longer.
- Therefore, we can safely pop all smaller elements from the back before adding `num`.
- This ensures the deque always stores **indices** of elements in strictly non-increasing / descending order of their values.
- As a result, the maximum element for the current window is always at the front of the deque (`q[0]`).

#### **Logic:**
1. Initialize Data Structures:
   - A double-ended queue `q = deque()` to store indices of elements in descending order of their values.
   - An array `res = []` to store the maximum of each sliding window.
2. Iterate Through `nums`: Loop index `i` and value `num` using `enumerate(nums)`:
   - Evict Expired Indices: If the oldest index at the front of the deque has moved out of the current sliding window (`q[0] < i - k + 1`), remove it using `q.popleft()`.
   - Maintain Monotonicity: While the deque is non-empty and the value at the back of the queue is less than or equal to `num` (`nums[q[-1]] <= num`), pop from the back (`q.pop()`).
   - Append Current Index: Add the current index `i` to the back: `q.append(i)`.
   - Collect Window Maximum: Once `i >= k - 1` (the initial window of size $k$ has fully formed), the element corresponding to the front index `nums[q[0]]` is the maximum for the current window. Append `nums[q[0]]` to `res`.
3. Return Result: Return `res`.

#### **Example Walkthrough:**
Consider Example 1: `nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`

| `i` | `nums[i]` | Expired (`< i - 2`)? | Monotonic Pops (Back) | Deque Indices `q` (Values) | `i >= k - 1`? | Window Max (`nums[q[0]]`) | `res` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | `1` | None | None | `[0]` (`[1]`) | No (`0 < 2`) | — | `[]` |
| 1 | `3` | None | Pop `0` (`1 <= 3`) | `[1]` (`[3]`) | No (`1 < 2`) | — | `[]` |
| 2 | `-1` | None | None | `[1, 2]` (`[3, -1]`) | **Yes** | `nums[1] = 3` | `[3]` |
| 3 | `-3` | None | None | `[1, 2, 3]` (`[3, -1, -3]`) | **Yes** | `nums[1] = 3` | `[3, 3]` |
| 4 | `5` | `q[0] = 1 < 2` $\rightarrow$ pop `1` | Pop `3` (`-3 <= 5`), pop `2` (`-1 <= 5`) | `[4]` (`[5]`) | **Yes** | `nums[4] = 5` | `[3, 3, 5]` |
| 5 | `3` | None | None | `[4, 5]` (`[5, 3]`) | **Yes** | `nums[4] = 5` | `[3, 3, 5, 5]` |
| 6 | `6` | None | Pop `5` (`3 <= 6`), pop `4` (`5 <= 6`) | `[6]` (`[6]`) | **Yes** | `nums[6] = 6` | `[3, 3, 5, 5, 6]` |
| 7 | `7` | None | Pop `6` (`6 <= 7`) | `[7]` (`[7]`) | **Yes** | `nums[7] = 7` | `[3, 3, 5, 5, 6, 7]` |

* **Final Result:** `[3, 3, 5, 5, 6, 7]`


#### **Time Complexity:**
$O(n)$ <br>
Each index is pushed into and popped from the deque at most once.

#### **Space Complexity:**
$O(k)$ <br>
The deque holds at most $k$ indices at any time.