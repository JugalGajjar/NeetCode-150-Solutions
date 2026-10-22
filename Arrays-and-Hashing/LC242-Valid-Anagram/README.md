# 242. Valid Anagram

**Difficulty:** Easy

## Problem
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

**Example 1:** <br>
Input: s = "anagram", t = "nagaram" <br>
Output: true

**Example 2:** <br>
Input: s = "rat", t = "car" <br>
Output: false

**Constraints:** <br>
1 <= s.length, t.length <= 5 * 104 <br>
`s` and `t` consist of lowercase English letters.


## Solution

#### **Intuition:**
An anagram is formed by rearranging the letters of a word, meaning two strings are anagrams if and only if they contain the exact same characters with the exact same frequencies. 

First, if the lengths of `s` and `t` are different, they cannot be anagrams. Otherwise, instead of sorting the strings which takes $O(n \log n)$ time, we can track character counts in linear $O(n)$ time. Since the input is constrained to 26 lowercase English letters, a fixed-size frequency array (or hash map) allows us to increment counts for characters in `s` and decrement for characters in `t`. If all final counts return to zero, the two strings are valid anagrams.

#### **Logic:**
1. Length Check: If `len(s) != len(t)`, return `False` immediately.
2. Frequency Tracking: Initialize an array of size 26 (initialized to 0) to track character frequencies.
3. Count Characters: Iterate through both strings simultaneously:
   - Increment the count for the character at index `i` in `s` via `ord(s[i]) - ord('a')`.
   - Decrement the count for the character at index `i` in `t` via `ord(t[i]) - ord('a')`.
4. Verification: Iterate through the count array. If any count is non-zero, return `False`. If all counts are zero, return `True`.

#### **Example Walkthrough:**
Consider Example 1: `s = "anagram"`, `t = "nagaram"`

* **Length Check:** `len(s) == len(t) == 7` (Pass)
* **Initial State:** `count = [0] * 26`

| Step (`i`) | `s[i]` / `t[i]` | Character Index (`ord(c) - ord('a')`) | Action | Net Change |
| :---: | :---: | :---: | :--- | :---: |
| 0 | `'a'` / `'n'` | Index 0 (`'a'`), Index 13 (`'n'`) | `count[0] += 1`, `count[13] -= 1` | `a: +1, n: -1` |
| 1 | `'n'` / `'a'` | Index 13 (`'n'`), Index 0 (`'a'`) | `count[13] += 1`, `count[0] -= 1` | `a: 0, n: 0` |
| 2 | `'a'` / `'g'` | Index 0 (`'a'`), Index 6 (`'g'`) | `count[0] += 1`, `count[6] -= 1` | `a: +1, g: -1` |
| 3 | `'g'` / `'a'` | Index 6 (`'g'`), Index 0 (`'a'`) | `count[6] += 1`, `count[0] -= 1` | `a: 0, g: 0` |
| 4 | `'r'` / `'r'` | Index 17 (`'r'`), Index 17 (`'r'`) | `count[17] += 1`, `count[17] -= 1` | `r: 0` |
| 5 | `'a'` / `'a'` | Index 0 (`'a'`), Index 0 (`'a'`) | `count[0] += 1`, `count[0] -= 1` | `a: 0` |
| 6 | `'m'` / `'m'` | Index 12 (`'m'`), Index 12 (`'m'`) | `count[12] += 1`, `count[12] -= 1` | `m: 0` |

* **Final Check:** Every element in `count` is `0`.
* **Result:** `True`

#### **Time Complexity:**
$O(n)$ <br>
We iterate through the strings of length `n` once, followed by a constant scan of the 26-element array.

#### **Space Complexity:**
$O(1)$ <br>
The size of the count array is fixed at 26, regardless of the input size.