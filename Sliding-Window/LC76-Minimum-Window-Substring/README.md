# 76. Minimum Window Substring

**Difficulty:** Hard

## Problem
Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the **minimum window** substring of `s` such that every character in `t` **(including duplicates)** is included in the window*. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is **unique**.

**Example 1:** <br>
Input: s = "ADOBECODEBANC", t = "ABC" <br>
Output: "BANC"

Explanation: <br>
The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

**Example 2:** <br>
Input: s = "a", t = "a" <br>
Output: "a"

Explanation: <br>
The entire string s is the minimum window.

**Example 3:** <br>
Input: s = "a", t = "aa" <br>
Output: ""

Explanation: <br>
Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

**Constraints:** <br>
m == s.length <br>
n == t.length <br>
1 <= m, n <= 10^5 <br>
`s` and `t` consist of uppercase and lowercase English letters.


## Solution

#### **Intuition:**
A brute-force solution checks every possible substring in $s$ and verifies whether it contains all characters of $t$, which takes $O(m^2 \cdot \vert{}\Sigma\vert{})$ time and causes Time Limit Exceeded (TLE) when $m \le 10^5$.

Instead, we can use an expand-and-contract **Sliding Window** with two pointers (`left` and `right`):
1. **Expand (`right`):** Grow the window to the right until it contains every character in $t$ with the required frequency.
2. **Contract (`left`):** Once valid, shrink the window from the left to discard unnecessary characters and minimize the window size while keeping it valid.

To determine whether the current window is valid in $O(1)$ time (avoiding a full scan of all character counts), we track:
- `need`: the number of distinct characters in $t$.
- `have`: the number of distinct characters in $t$ whose required frequency is currently fully satisfied inside the window.

A window is valid if and only if `have == need`.

#### **Logic:**
1. Edge Case: If `len(s) < len(t)` or either string is empty, return `""`.
2. Target Frequencies & Window Tracking:
   - Precompute `t_count = Counter(t)` and set `need = len(t_count)`.
   - Maintain `window_count = {}` and `have = 0`.
   - Track the best window using `res_len = float('inf')` and `res_indices = [-1, -1]`.
3. Iterate with `right` Pointer:
   - Add `char = s[right]` to `window_count`.
   - If `char` is in `t_count` and `window_count[char] == t_count[char]`, increment `have += 1`.
   - Contract with `left` Pointer while `have == need`:
     - If the current window length (`right - left + 1`) is smaller than `res_len`, update `res_len = right - left + 1` and `res_indices = [left, right]`.
     - Decrement the count of `s[left]` in `window_count`.
     - If `s[left]` is in `t_count` and its count drops below the requirement (`window_count[s[left]] < t_count[s[left]]`), decrement `have -= 1`.
     - Increment `left += 1` to shrink the window.
4. Return Result: Using `res_indices`, return `s[l : r + 1]` if a valid window was found (`res_len != float('inf')`), otherwise return `""`.

#### **Example Walkthrough:**
Consider Example 1: `s = "ADOBECODEBANC"`, `t = "ABC"`

* `t_count = {'A': 1, 'B': 1, 'C': 1}`, `need = 3`
* Key events during the traversal:

| `right` | `s[right]` | Window State | `have` / `need` | Valid? | Action / Window Minimized |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 0–4 | `'A'...'E'` | `"ADOBE"` | $2/3$ | No | Contains `'A'`, `'B'`. Missing `'C'`. |
| 5 | `'C'` | `"ADOBEC"` | **$3/3$** | **Yes** | Valid window found: `"ADOBEC"` (len 6). Shrinking attempts: removing `'A'` causes `have = 2`. Stop shrinking. `left = 1`. |
| 6–9 | `'O'...'E'` | `"DOBECODE"` | $2/3$ | No | Missing `'A'`. Expanding `right`. |
| 9 | `'B'` | `"DOBECODEB"` | $2/3$ | No | Extra `'B'` added. |
| 10 | `'A'` | `"DOBECODEBA"` | **$3/3$** | **Yes** | Valid window found. Shrinking: advance `left` past `'D'`, `'O'`, `'B'`, `'E'`, `'C'`... until invalid. |
| 12 | `'C'` | `...` | **$3/3$** | **Yes** | Reaches end. Shrinks left boundary past redundant `'D'`, `'E'` until window is `"BANC"` (len 4). |

* **Final Result:** `"BANC"`

#### **Time Complexity:**
$O(m + n)$ <br>
Building t_count takes $O(n)$ where $n = \text{len}(t)$. In string $s$ ($m = \text{len}(s)$), each pointer left and right visits every character at most once, performing $O(1)$ dictionary operations per step.

#### **Space Complexity:**
$O(|\Sigma|)$ auxiliary space <br>
Where $|\Sigma|$ is the number of distinct characters in $s$ and $t$ (at most 52 uppercase and lowercase English letters).