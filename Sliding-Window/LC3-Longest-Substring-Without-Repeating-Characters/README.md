# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium

## Problem
Given a string `s`, find the length of the longest substring without duplicate characters.

**Example 1:** <br>
Input: s = "abcabcbb" <br>
Output: 3

Explanation: <br>
The answer is "abc", with the length of 3. Note that `"bca"` and `"cab"` are also correct answers.

**Example 2:** <br>
Input: s = "bbbbb" <br>
Output: 1

Explanation: <br>
The answer is "b", with the length of 1.

**Example 3:** <br>
Input: s = "pwwkew" <br>
Output: 3

Explanation: <br>
The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

**Constraints:** <br>
0 <= s.length <= 10^5 <br>
`s` consists of English letters, digits, symbols and spaces.


## Solution

#### **Intuition:**
A substring must consist of contiguous characters with zero duplicates. Checking every possible substring requires $O(n^2)$ time, which becomes inefficient for strings up to $10^5$ characters.

Instead, we can use the **Sliding Window** technique with two pointers (`left` and `right`) to represent a valid window of unique characters. 

In a standard sliding window, whenever we encounter a duplicate character, we increment the `left` pointer step-by-step until the duplicate is evicted. We can optimize this by maintaining a **Hash Map** that stores the most recent index of each character. When a repeating character is encountered within our current window, rather than incrementing `left` one step at a time, we jump `left` directly past the character's last seen position:
$$\text{left} = \text{char\_index}[s[\text{right}]] + 1$$

This ensures that the window always contains unique characters and allows both pointers to traverse the string in a single linear pass.

#### **Logic:**
1. Initialize State:
   - A hash map `char_index` to map characters to their most recent index.
   - A pointer `left = 0` to denote the start of the current window.
   - A variable `max_len = 0` to track the maximum length found.
2. Iterate with `right` Pointer:
   - Loop through each index `right` and character `char` in `s`:
     - If `char` exists in `char_index` **and** its recorded index is within the current window (`char_index[char] >= left`):
       - Move `left` forward to `char_index[char] + 1` (immediately following the duplicate character).
     - Update the character's latest index: `char_index[char] = right`.
     - Calculate the current window size (`right - left + 1`) and update `max_len = max(max_len, right - left + 1)`.
3. Return Result: Return `max_len`.

#### **Example Walkthrough:**
Consider Example 1: `s = "abcabcbb"`

* **Initial State:** `char_index = {}`, `left = 0`, `max_len = 0`

| Step (`right`) | `char` | In map & $\ge$ `left`? | Updated `left` | Window Substring | Window Length (`right - left + 1`) | `max_len` | Updated `char_index` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | `'a'` | No | `0` | `"a"` | $0 - 0 + 1 = 1$ | **1** | `{'a': 0}` |
| 1 | `'b'` | No | `0` | `"ab"` | $1 - 0 + 1 = 2$ | **2** | `{'a': 0, 'b': 1}` |
| 2 | `'c'` | No | `0` | `"abc"` | $2 - 0 + 1 = 3$ | **3** | `{'a': 0, 'b': 1, 'c': 2}` |
| 3 | `'a'` | Yes (`0 >= 0`) | `0 + 1 = 1` | `"bca"` | $3 - 1 + 1 = 3$ | 3 | `{'a': 3, 'b': 1, 'c': 2}` |
| 4 | `'b'` | Yes (`1 >= 1`) | `1 + 1 = 2` | `"cab"` | $4 - 2 + 1 = 3$ | 3 | `{'a': 3, 'b': 4, 'c': 2}` |
| 5 | `'c'` | Yes (`2 >= 2`) | `2 + 1 = 3` | `"abc"` | $5 - 3 + 1 = 3$ | 3 | `{'a': 3, 'b': 4, 'c': 5}` |
| 6 | `'b'` | Yes (`4 >= 3`) | `4 + 1 = 5` | `"cb"` | $6 - 5 + 1 = 2$ | 3 | `{'a': 3, 'b': 6, 'c': 5}` |
| 7 | `'b'` | Yes (`6 >= 5`) | `6 + 1 = 7` | `"b"` | $7 - 7 + 1 = 1$ | 3 | `{'a': 3, 'b': 7, 'c': 5}` |

* **Final Result:** `3`

#### **Time Complexity:**
$O(n)$ <br>
The right pointer iterates through the string of length $n$ once. All lookups, insertions, and updates in the hash map take $O(1)$ average time.

#### **Space Complexity:**
$O(\min(n, m))$ <br>
Where $m$ is the size of the character set (at most $128$ for standard ASCII or $256$ for extended ASCII). The hash map stores at most $\min(n, m)$ unique keys.