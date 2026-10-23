# 271. Encode and Decode Strings

**Difficulty:** Medium
> **Note:** This is a LeetCode premium problem.

## Problem
Design an algorithm to encode a **list of strings** to **a string**. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
```
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
```
Machine 2 (receiver) has the function:
```
vector<string> decode(string s) {
  //... your code
  return strs;
}
```
So Machine 1 does:
```
string encoded_string = encode(strs);
```
and Machine 2 does:
```
vector<string> strs2 = decode(encoded_string);
```

`strs2` in Machine 2 should be the same as `strs` in Machine 1.

Implement the `encode` and `decode` methods.

You are not allowed to solve the problem using any serialize methods (such as `eval`).

**Example 1:** <br>
Input: dummy_input = ["Hello","World"] <br>
Output: ["Hello","World"]

Explanation: <br>
Machine 1: <br>
Codec encoder = new Codec(); <br>
String msg = encoder.encode(strs); <br>
Machine 1 ---msg---> Machine 2 <br>
Machine 2: <br>
Codec decoder = new Codec(); <br>
String[] strs = decoder.decode(msg);

**Example 2:** <br>
Input: dummy_input = [""] <br>
Output: [""]

**Constraints:** <br>
1 <= strs.length <= 200 <br>
0 <= strs[i].length <= 200 <br>
`strs[i]` contains any possible characters out of `256` valid ASCII characters.


## Solution

#### **Intuition:**
A standard delimiter-based approach (e.g., joining strings using `,` or `#`) fails because the input strings can contain any of the 256 valid ASCII characters, including our chosen delimiter. Escaping delimiters introduces unnecessary parsing overhead and complexity.

To make the encoding completely stateless and robust against any character set, we use **Length-Prefix Framing** (similar to HTTP chunked transfer or network packet headers). For every string, we prefix it with its length followed by a separator: `length#string`. 

During decoding, even if the string's content contains `#` characters or numbers, the decoder reads only the integer before the first `#` delimiter, advances past `#`, and extracts precisely that many characters.

#### **Logic:**
1. Encode:
   - Iterate through the list of strings `strs`.
   - For each string `s`, compute its length `len(s)`.
   - Format each entry as `f"{len(s)}#{s}"` and concatenate them into a single string.
2. Decode:
   - Maintain a pointer `i = 0` representing the start of the current chunk.
   - While `i < len(s)`:
     - Find the delimiter `#` starting from `i` using a pointer `j` until `s[j] == '#'`.
     - Parse the integer `length = int(s[i:j])`.
     - Extract the string slice `s[j + 1 : j + 1 + length]`.
     - Append the extracted string to the result list.
     - Advance the pointer `i = j + 1 + length` to the start of the next chunk.
3. Return the decoded list of strings.

#### **Example Walkthrough:**
Consider Example: `strs = ["leet", "code", "love", "you"]`

**Encoding:**
  - `"leet"` (length 4) $\rightarrow$ `"4#leet"`
  - `"code"` (length 4) $\rightarrow$ `"4#code"`
  - `"love"` (length 4) $\rightarrow$ `"4#love"`
  - `"you"` (length 3) $\rightarrow$ `"3#you"`
  - **Encoded String:** `"4#leet4#code4#love3#you"`

**Decoding:** `s = "4#leet4#code4#love3#you"`

| Step | Pointer `i` | Find `#` at `j` | Substring `s[i:j]` (Length) | Content Range `[j+1 : j+1+length]` | Extracted String | Next Pointer `i` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `0` | `1` | `int("4") = 4` | `[2 : 6]` | `"leet"` | `6` |
| 2 | `6` | `7` | `int("4") = 4` | `[8 : 12]` | `"code"` | `12` |
| 3 | `12` | `13` | `int("4") = 4` | `[14 : 18]` | `"love"` | `18` |
| 4 | `18` | `19` | `int("3") = 3` | `[20 : 23]` | `"you"` | `23` |

* `i = 23 == len(s)` $\rightarrow$ Loop terminates.
* **Decoded Output:** `["leet", "code", "love", "you"]`

#### **Time Complexity:**
**Encode:** $O(n)$, where n is the total number of characters in all strings combined. <br>
We traverse each character in the input list of strings once to encode them. <br>
**Decode:** $O(n)$, where n is the total number of characters in the encoded string. <br>
We traverse each character in the encoded string once to decode it.

#### **Space Complexity:**
**Encode:** $O(n)$ <br>
`n` is the total number of characters in all strings combined. <br>
**Decode:** $O(m)$ <br>
`m` is the number of strings in the decoded list.