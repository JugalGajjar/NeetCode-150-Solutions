class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_len = max(max_len, j - i + 1)

        return max_len

# Time Complexity: O(n^2), where n is the length of the string s.
# We have two nested loops, each iterating over the string.
# Space Complexity: O(min(n, m)), where m is the size of the character set.
# We use a set to store the characters in the current substring, which can be at most the size of the character set (e.g., 26 for lowercase letters, 128 for ASCII).