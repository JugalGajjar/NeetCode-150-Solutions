# 424. Longest Repeating Character Replacement

**Difficulty:** Medium

## Problem
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

**Example 1:** <br>
Input: s = "ABAB", k = 2 <br>
Output: 4

Explanation: <br>
Replace the two 'A's with two 'B's or vice versa.

**Example 2:** <br>
Input: s = "AABABBA", k = 1 <br>
Output: 4

Explanation: <br>
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

**Constraints:** <br>
1 <= s.length <= 10^5 <br>
`s` consists of only uppercase English letters. <br>
0 <= k <= s.length


## Solution

#### **Intuition:**
In any contiguous substring, the most efficient way to form a sequence of identical characters is to convert all minority characters into the majority character (the character that already occurs most frequently).

Therefore, for any given window:
$$\text{Replacements Needed} = (\text{Window Length}) - \text{Max Frequency}$$

A window is valid if and only if $\text{Replacements Needed} \le k$.

Checking every possible substring takes $O(n^2)$ time. Instead, we can expand a dynamic window using the **Sliding Window** technique with two pointers (`left` and `right`). As `right` expands, we maintain the frequency of each character and track `max_freq`, the highest count of any single character in our current window. 

When the number of characters we need to replace exceeds $k$ ($(\text{right} - \text{left} + 1) - \text{max\_freq} > k$), the window becomes invalid, so we increment `left` to shrink it. Importantly, we do not need to decrement `max_freq` when shrinking the window because our goal is to find a larger window than our current best. A smaller `max_freq` could never help us exceed our existing maximum valid window size.

#### **Logic:**
1. Initialize State:
   - A hash map `count` to store character frequencies in the active window.
   - Pointers `left = 0` and variables `max_freq = 0`, `max_len = 0`.
2. Expand the Window: Iterate `right` across the string from `0` to `len(s) - 1`:
   - Increment the frequency of `s[right]` in `count`.
   - Update `max_freq = max(max_freq, count[s[right]])`.
   - Validate the Window:
     - While the replacements needed exceed $k$ ($(\text{right} - \text{left} + 1) - \text{max\_freq} > k$):
       - Decrement the count of `s[left]`.
       - Advance `left += 1` to shrink the window back to a valid state.
   - Update `max_len = max(max_len, right - left + 1)`.
3. Return Result: Return `max_len`.

#### **Example Walkthrough:**
Consider Example 2: `s = "AABABBA"`, `k = 1`

* **Initial State:** `count = {}`, `left = 0`, `max_freq = 0`, `max_len = 0`

| `right` | `s[right]` | `count` | `max_freq` | Window Length | Replacements (`len - max_freq`) | Valid ($\le k$)? | Action / Updated `left` | Window Substring | `max_len` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | `'A'` | `{'A': 1}` | 1 | 1 | $1 - 1 = 0$ | Yes ($0 \le 1$) | Keep `left = 0` | `"A"` | **1** |
| 1 | `'A'` | `{'A': 2}` | 2 | 2 | $2 - 2 = 0$ | Yes ($0 \le 1$) | Keep `left = 0` | `"AA"` | **2** |
| 2 | `'B'` | `{'A': 2, 'B': 1}` | 2 | 3 | $3 - 2 = 1$ | Yes ($1 \le 1$) | Keep `left = 0` | `"AAB"` | **3** |
| 3 | `'A'` | `{'A': 3, 'B': 1}` | 3 | 4 | $4 - 3 = 1$ | Yes ($1 \le 1$) | Keep `left = 0` | `"AABA"` | **4** |
| 4 | `'B'` | `{'A': 3, 'B': 2}` | 3 | 5 | $5 - 3 = 2$ | **No** ($2 > 1$) | Evict `'A'`, `left` $\rightarrow$ `1` | `"ABAB"` | 4 |
| 5 | `'B'` | `{'A': 2, 'B': 3}` | 3 | 5 | $5 - 3 = 2$ | **No** ($2 > 1$) | Evict `'A'`, `left` $\rightarrow$ `2` | `"BABB"` | 4 |
| 6 | `'A'` | `{'A': 2, 'B': 3}` | 3 | 5 | $5 - 3 = 2$ | **No** ($2 > 1$) | Evict `'B'`, `left` $\rightarrow$ `3` | `"ABBA"` | 4 |

* **Final Result:** `4`

#### **Time Complexity:**
$O(n)$ <br>
Both `left` and `right` pointers traverse the string of length $n$ at most once. Hash map updates and lookups take $O(1)$ constant time.

#### **Space Complexity:**
$O(1)$ <br>
We use a fixed-size dictionary to store character counts, which is limited to the number of unique characters (at most 26 for uppercase English letters).