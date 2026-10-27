from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n or not t:
            return ""

        t_count = Counter(t)
        min_len = float('inf')
        min_sub = ""

        for i in range(m):
            window_count = Counter()
            for j in range(i, m):
                window_count[s[j]] += 1

                # Substring must be at least length n to contain all characters of t
                if (j - i + 1) >= n:
                    # Check if current window satisfies all character counts of t
                    is_valid = True
                    for char, count in t_count.items():
                        if window_count[char] < count:
                            is_valid = False
                            break

                    if is_valid:
                        if (j - i + 1) < min_len:
                            min_len = j - i + 1
                            min_sub = s[i : j + 1]
                        # Once a valid window is found starting at i, expanding j further will only increase length
                        break

        return min_sub

# Time Complexity: O(m * n), where m is the length of string s and n is the length of string t.
# In the worst case, we may have to check every substring of s, and for each substring, we check if it contains all characters of t.
# Space Complexity: O(x + y), where x is the number of unique characters in s and y is the number of unique characters in t.
# We use additional space for the frequency counters.