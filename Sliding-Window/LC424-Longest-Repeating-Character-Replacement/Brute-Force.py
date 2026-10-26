class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            counts = {}
            max_freq = 0
            for j in range(i, n):
                char = s[j]
                counts[char] = counts.get(char, 0) + 1
                max_freq = max(max_freq, counts[char])

                # Total substitutions needed = window length - max_freq
                window_len = j - i + 1
                if window_len - max_freq <= k:
                    max_len = max(max_len, window_len)
                else:
                    # Expanding further will only increase or maintain replacements needed
                    break

        return max_len

# Time Complexity: O(n^2), where n is the length of the string s.
# We have a nested loop where the outer loop iterates through each character in the string,
# and the inner loop expands the window to the right, checking the condition for valid replacements.
# Space Complexity: O(1)
# We use a fixed-size dictionary to store character counts, which is limited to the number of unique characters (at most 26 for uppercase English letters).