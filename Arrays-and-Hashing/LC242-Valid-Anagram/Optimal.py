class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False

        return True

# Time Complexity: O(n), where n is the length of the input strings.
# Space Complexity: O(1)
# The size of the count array is fixed at 26, regardless of the input size.