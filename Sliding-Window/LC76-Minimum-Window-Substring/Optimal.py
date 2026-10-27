from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        t_count = Counter(t)
        window_count = {}

        have, need = 0, len(t_count)
        res_len = float('inf')
        res_indices = [-1, -1]

        left = 0
        for right, char in enumerate(s):
            window_count[char] = window_count.get(char, 0) + 1

            # Check if current character satisfies required count from t
            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            # Contract window from left while all requirements are met
            while have == need:
                # Update minimum window result
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res_indices = [left, right]

                # Pop left character from window
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1

                left += 1

        l, r = res_indices
        return s[l : r + 1] if res_len != float('inf') else ""

# Time Complexity: O(n + m), where n is the length of string s and m is the length of string t.
# We traverse the string s once and the string t once to build the frequency counter.
# Space Complexity: O(x + y), where x is the number of unique characters in s and y is the number of unique characters in t.
# We use additional space for the frequency counters.