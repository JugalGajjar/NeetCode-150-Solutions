# 49. Group Anagrams

**Difficulty:** Medium

## Problem
Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

**Example 1:** <br>
Input: strs = ["eat","tea","tan","ate","nat","bat"] <br>
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation: <br>
* There is no string in strs that can be rearranged to form `"bat"`.
* The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
* The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:** <br>
Input: strs = [""] <br>
Output: [[""]]

**Example 3:** <br>
Input: strs = ["a"] <br>
Output: [["a"]]

**Constraints:** <br>
1 <= strs.length <= 104 <br>
0 <= strs[i].length <= 100 <br>
`strs[i]` consists of lowercase English letters.


## Solution

#### **Intuition:**
Two strings are anagrams if and only if they contain the exact same characters with the exact same frequencies. This means any two anagrams will share an identical "fingerprint."

While sorting each string alphabetically yields a valid key (e.g., `"eat"` $\rightarrow$ `"aet"`), sorting takes $O(k \log k)$ time per word. Because the problem guarantees strings consist only of lowercase English letters, we can create an even faster fingerprint in $O(k)$ time: a 26-element frequency count. By converting this fixed-size frequency array into an immutable tuple, we can use it directly as the hash key in a hash map to group all anagrams together in linear time.

#### **Logic:**
1. Initialize a Hash Map: Use a hash map (or `defaultdict(list)`) where the key is a character frequency fingerprint and the value is a list of strings matching that fingerprint.
2. Build Frequency Fingerprint: For every string `s` in `strs`:
   - Initialize an array `count` of size 26 with all zeros.
   - Iterate through every character in `s`, incrementing `count[ord(char) - ord('a')] += 1`.
   - Convert `count` into an immutable `tuple` (since Python lists cannot be dictionary keys).
3. Group Strings: Append the original string `s` to the list mapped to `tuple(count)`: `anagram_map[tuple(count)].append(s)`.
4. Return Results: Convert and return the dictionary values as a list of lists: `list(anagram_map.values())`.

#### **Example Walkthrough:**
Consider Example 1: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`

* **Initialization:** `anagram_map = defaultdict(list)`

| Word (`s`) | Non-Zero Character Counts | Tuple Key (Indices with count) | Action on `anagram_map` |
| :---: | :---: | :---: | :--- |
| `"eat"` | `a: 1, e: 1, t: 1` | `(1, 0, ..., 1, ..., 1, ...)` | Key created $\rightarrow$ `["eat"]` |
| `"tea"` | `a: 1, e: 1, t: 1` | `(1, 0, ..., 1, ..., 1, ...)` | Appends to existing key $\rightarrow$ `["eat", "tea"]` |
| `"tan"` | `a: 1, n: 1, t: 1` | `(1, 0, ..., 1, ..., 1, ...)` | New key created $\rightarrow$ `["tan"]` |
| `"ate"` | `a: 1, e: 1, t: 1` | `(1, 0, ..., 1, ..., 1, ...)` | Appends to existing key $\rightarrow$ `["eat", "tea", "ate"]` |
| `"nat"` | `a: 1, n: 1, t: 1` | `(1, 0, ..., 1, ..., 1, ...)` | Appends to existing key $\rightarrow$ `["tan", "nat"]` |
| `"bat"` | `a: 1, b: 1, t: 1` | `(1, 1, ..., 0, ..., 1, ...)` | New key created $\rightarrow$ `["bat"]` |

* **Final Result:** `list(anagram_map.values())` $\rightarrow$ `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

#### **Time Complexity:**
$O(n * k)$ <br>
We traverse each string and count the frequency of each character, which takes O(k) time. We do this for all n strings.

#### **Space Complexity:**
$O(n * k)$ <br>
To store the grouped strings and frequency keys in the hash map.