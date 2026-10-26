class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            # If the character was seen inside the current window, jump left past it
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            char_index[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len

# Time Complexity: O(n), where n is the length of the string s.
# We traverse the string once with two pointers.
# Space Complexity: O(min(n, m)), where m is the size of the character set.
# We use a dictionary to store the characters and their indices in the current substring, which can be at most the size of the character set (e.g., 26 for lowercase letters, 128 for ASCII).