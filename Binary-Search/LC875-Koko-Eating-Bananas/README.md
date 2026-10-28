# 875. Koko Eating Bananas

**Difficulty:** Medium

## Problem
Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

**Example 1:** <br>
Input: piles = [3,6,7,11], h = 8 <br>
Output: 4

**Example 2:** <br>
Input: piles = [30,11,23,4,20], h = 5 <br>
Output: 30

**Example 3:** <br>
Input: piles = [30,11,23,4,20], h = 6 <br>
Output: 23

**Constraints:** <br>
1 <= piles.length <= 10^4 <br>
piles.length <= h <= 10^9 <br>
1 <= piles[i] <= 10^9


## Solution

#### **Intuition:**
The eating speed $k$ must be at least $1$ (the minimum possible speed) and at most $\max(\text{piles})$ (at which speed Koko can eat each pile in exactly $1$ hour, requiring $n$ hours total, and since $h \ge n$, this is always feasible).

A brute-force linear search tests every speed starting from $k = 1$ up to $\max(\text{piles})$, which takes $O(n \cdot \max(\text{piles}))$ time and leads to Time Limit Exceeded (TLE) when $\max(\text{piles}) \le 10^9$.

Notice that the total time required is a **monotonically decreasing function** of eating speed $k$:
- As speed $k$ increases, the total hours required decreases or stays the same.
- As speed $k$ decreases, the total hours required increases or stays the same.

Because this search space $[1, \max(\text{piles})]$ exhibits a monotonic true/false condition (whether all bananas can be finished within $h$ hours), we can use **Binary Search on Answer**:
- If speed $k$ allows Koko to finish within $h$ hours, then any speed greater than $k$ will also work. We record $k$ as a potential minimum and search the slower/left half (`right = mid - 1`).
- If speed $k$ is too slow (hours $> h$), any speed less than or equal to $k$ is invalid, so we must search the faster/right half (`left = mid + 1`).

#### **Logic:**
1. Define Search Boundaries:
   - Set `left = 1` (minimum feasible speed).
   - Set `right = max(piles)` (maximum required speed).
   - Initialize `res = right`.
2. Binary Search Loop (`while left <= right`):
   - Midpoint speed: `mid = left + (right - left) // 2`.
   - Calculate Total Hours Needed: For each pile, the hours taken is $\lceil \text{pile} / \text{mid} \rceil$, which can be computed with integer arithmetic as `(pile + mid - 1) // mid`.
   - Evaluate Feasibility:
     - If `total_hours <= h`: Koko can finish in time at this speed. Record `res = mid` and try to find a smaller valid speed by setting `right = mid - 1`.
     - If `total_hours > h`: Speed is too slow to finish within $h$ hours, so Koko must eat faster: set `left = mid + 1`.
3. Return Result: Return `res`.

#### **Example Walkthrough:**
Consider Example 1: `piles = [3, 6, 7, 11]`, `h = 8`

* Search space: `left = 1`, `right = max([3, 6, 7, 11]) = 11`, `res = 11`

| Iteration | `left` | `right` | `mid` (speed $k$) | Hours per Pile $\lceil \text{pile} / k \rceil$ | `total_hours` | Comparison to $h = 8$ | Action |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `1` | `11` | **`6`** | $\lceil 3/6 \rceil=1, \lceil 6/6 \rceil=1, \lceil 7/6 \rceil=2, \lceil 11/6 \rceil=2$ | $1 + 1 + 2 + 2 = \mathbf{6}$ | $6 \le 8$ (Valid) | `res = 6`, `right = mid - 1 = 5` |
| 2 | `1` | `5` | **`3`** | $\lceil 3/3 \rceil=1, \lceil 6/3 \rceil=2, \lceil 7/3 \rceil=3, \lceil 11/3 \rceil=4$ | $1 + 2 + 3 + 4 = \mathbf{10}$ | $10 > 8$ (Too slow) | `left = mid + 1 = 4` |
| 3 | `4` | `5` | **`4`** | $\lceil 3/4 \rceil=1, \lceil 6/4 \rceil=2, \lceil 7/4 \rceil=2, \lceil 11/4 \rceil=3$ | $1 + 2 + 2 + 3 = \mathbf{8}$ | $8 \le 8$ (Valid) | `res = 4`, `right = mid - 1 = 3` |

* Pointers cross (`left = 4 > right = 3`), loop terminates.
* **Final Result:** `4`

#### **Time Complexity:**
$O(n \log m)$ <br>
We perform a binary search on the range of possible eating speeds (from 1 to max(piles)), and for each speed, we iterate through all piles to calculate the total hours needed to finish eating all the bananas.

#### **Space Complexity:**
$O(1)$ <br>
We use constant extra space, as we only store a few variables for the binary search and total hours calculation.