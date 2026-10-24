# 125. Valid Palindrome

**Difficulty:** Easy

## Problem
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Example 1:** <br>
Input: s = "A man, a plan, a canal: Panama" <br>
Output: true

Explanation: <br>
"amanaplanacanalpanama" is a palindrome.

**Example 2:** <br>
Input: s = "race a car" <br>
Output: false

Explanation: <br>
"raceacar" is not a palindrome.

**Example 3:** <br>
Input: s = " " <br>
Output: true

Explanation: <br>
s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

**Constraints:** <br>
1 <= s.length <= 2 * 10^5 <br>
`s` consists only of printable ASCII characters.


## Solution

#### **Intuition:**
A phrase is a palindrome if it reads the same forward and backward after filtering out non-alphanumeric characters and normalizing case.

A naive approach creates a filtered copy of the string and compares it to its reverse, which consumes $O(n)$ extra memory. To optimize memory to strictly $O(1)$ auxiliary space, we can use the **Two-Pointer technique**. By placing one pointer at the start of the string (`left`) and one at the end (`right`), we move inward toward the center, skipping any non-alphanumeric characters on the fly. Whenever both pointers rest on valid alphanumeric characters, we compare them case-insensitively. If any pair does not match, the string cannot be a palindrome.

#### **Logic:**
1. Initialize Two Pointers: Set `left = 0` and `right = len(s) - 1`.
2. Move Inward While `left < right`:
   - Advance `left` forward while `left < right` and `s[left]` is not alphanumeric (`not s[left].isalnum()`).
   - Move `right` backward while `left < right` and `s[right]` is not alphanumeric (`not s[right].isalnum()`).
   - Check character equality:
     - Convert both to lowercase (`s[left].lower() != s[right].lower()`).
     - If they do not match, return `False`.
   - If they match, increment `left += 1` and decrement `right -= 1` to inspect the next pair.
3. Return `True`: If the pointers meet or cross without any mismatch, return `True`.

#### **Example Walkthrough:**
Consider Example 2: `s = "race a car"`

**Initial State:** `left = 0`, `right = len(s) - 1 = 9`

| Step | `left` (`s[left]`) | `right` (`s[right]`) | Skip Non-Alphanumeric? | Match (`.lower()`)? | Action |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `0` (`'r'`) | `9` (`'r'`) | None | `'r' == 'r'` (Match) | `left = 1`, `right = 8` |
| 2 | `1` (`'a'`) | `8` (`'a'`) | None | `'a' == 'a'` (Match) | `left = 2`, `right = 7` |
| 3 | `2` (`'c'`) | `7` (`'c'`) | None | `'c' == 'c'` (Match) | `left = 3`, `right = 6` |
| 4 | `3` (`'e'`) | `6` (`' '`) | `right` moves over `' '` to index `5` (`'a'`) | `'e' != 'a'` (**Mismatch!**) | **Return `False`** |

* **Result:** `False` (Terminated immediately upon detecting mismatch).

#### **Time Complexity:**
$O(n)$ <br>
We traverse the string once with two pointers.

#### **Space Complexity:**
$O(1)$ <br>
We use a constant amount of extra space for the pointers and variables.