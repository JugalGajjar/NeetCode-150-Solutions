class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # Window is invalid if characters to replace exceed k
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

# Time Complexity: O(n), where n is the length of the string s.
# We traverse the string once with a sliding window approach.
# Space Complexity: O(1)
# We use a fixed-size dictionary to store character counts, which is limited to the number of unique characters (at most 26 for uppercase English letters).