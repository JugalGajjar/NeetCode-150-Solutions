# 567. Permutation in String

**Difficulty:** Medium

## Problem
Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

**Example 1:** <br>
Input: s1 = "ab", s2 = "eidbaooo" <br>
Output: true

Explanation: <br>
s2 contains one permutation of s1 ("ba").

**Example 2:** <br>
Input: s1 = "ab", s2 = "eidboaoo" <br>
Output: false

**Constraints:** <br>
1 <= s1.length, s2.length <= 10^4 <br>
`s1` and `s2` consist of lowercase English letters.


## Solution

#### **Intuition:**
A permutation of a string $s_1$ is simply an anagram of $s_1$. This means any valid permutation substring in $s_2$ must have the exact same length as $s_1$ (`len(s1)`) and identical character frequencies across all 26 lowercase English letters.

Checking every substring of length `len(s1)` by sorting takes $O((n_2 - n_1 + 1) \cdot n_1 \log n_1)$ time, which is too slow. 

Instead, we can maintain a **fixed-size sliding window** of length `len(s1)` across $s_2$. Rather than rechecking and comparing all 26 character frequencies on every step ($O(26 \cdot n_2)$), we can optimize down to strictly $O(1)$ updates per slide by tracking a `matches` counter. The `matches` counter keeps track of how many of the 26 lowercase characters currently have matching counts between $s_1$ and the current window in $s_2$. When sliding the window by one position, only two characters change: the incoming character at `right` and the outgoing character at `left`. If `matches == 26`, the current window is an exact permutation of $s_1$.

#### **Logic:**
1. Edge Case: If `len(s1) > len(s2)`, return `False` immediately.
2. Frequency Arrays & Initial Match Count:
   - Create two arrays of size 26 (`s1_count` and `s2_count`) initialized to `0`.
   - Populate `s1_count` for all characters in $s_1$, and populate `s2_count` for the initial window of size `len(s1)` in $s_2$.
   - Count initial matches: iterate through indices `0` to `25`. If `s1_count[i] == s2_count[i]`, increment `matches += 1`.
3. Slide the Window Across $s_2$:
   - Maintain `left = 0` and iterate `right` from `len(s1)` to `len(s2) - 1`:
     - If `matches == 26`, return `True`.
     - Add Incoming Character (`s2[right]`):
       - Increment `s2_count[r_idx]`.
       - If it now matches `s1_count[r_idx]`, increment `matches += 1`.
       - If it was previously matching and now exceeds by 1 (`s2_count[r_idx] == s1_count[r_idx] + 1`), decrement `matches -= 1`.
     - Remove Outgoing Character (`s2[left]`):
       - Decrement `s2_count[l_idx]`.
       - If it now matches `s1_count[l_idx]`, increment `matches += 1`.
       - If it was previously matching and now falls short by 1 (`s2_count[l_idx] == s1_count[l_idx] - 1`), decrement `matches -= 1`.
     - Advance `left += 1`.
4. Final Check: Return `matches == 26` to evaluate the last window.

#### **Example Walkthrough:**
Consider Example 1: `s1 = "ab"`, `s2 = "eidbaooo"`

* `len(s1) = 2`, `len(s2) = 8`

**Target `s1_count`:** `'a': 1`, `'b': 1`, all other 24 characters: `0`

**Initial Window in $s_2$ (indices 0 to 1, `"ei"`):**
  - `s2_count`: `'e': 1`, `'i': 1`, all other 24 characters: `0`
  - Matching letters: 22 characters match with count 0 (all letters except `'a'`, `'b'`, `'e'`, `'i'`).
  - `matches = 24`

| Step (`right`) | Window Substring | Incoming Char (`s2[right]`) | Outgoing Char (`s2[left]`) | Net Impact on `matches` | `matches` | Condition Check |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| Start | `"ei"` | — | — | — | 24 | `matches == 26`? No |
| `2` | `"id"` | `'d'` (count $0 \rightarrow 1$) | `'e'` (count $1 \rightarrow 0$) | `'d'` mismatch (-1); `'e'` matches (+1) | 24 | `matches == 26`? No |
| `3` | `"db"` | `'b'` (count $0 \rightarrow 1$) | `'i'` (count $1 \rightarrow 0$) | `'b'` matches (+1); `'i'` matches (+1) | 26 | Next loop checks `matches == 26` |
| `4` | `"ba"` | — | — | — | **26** | **`matches == 26` $\rightarrow$ Return `True`** |

* **Final Result:** `True`

#### **Time Complexity:**
$O(n1 + n2)$, where n1 is the length of s1 and n2 is the length of s2. <br>
We traverse both strings once to build the character counts and then slide the window across s2.

#### **Space Complexity:**
$O(1)$ <br>
We use constant extra space for the character counts, which is fixed at 26 for lowercase letters.