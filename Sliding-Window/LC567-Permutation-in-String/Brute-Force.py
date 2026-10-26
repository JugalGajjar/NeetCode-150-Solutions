class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        sorted_s1 = sorted(s1)

        for i in range(n2 - n1 + 1):
            sub = s2[i : i + n1]
            if sorted(sub) == sorted_s1:
                return True

        return False

# Time Complexity: O((n2 - n1 + 1) * n1 * log(n1))
# We sort s1 once, then sort each substring of s2 of length n1.
# Space Complexity: O(n1), where n1 is the length of s1.
# We use extra space to store the sorted version of s1 and the substring of s2.