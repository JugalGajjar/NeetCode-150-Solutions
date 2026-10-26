class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        left = 0
        for right in range(n1, n2):
            if matches == 26:
                return True

            # Add incoming character at `right`
            r_idx = ord(s2[right]) - ord('a')
            s2_count[r_idx] += 1
            if s2_count[r_idx] == s1_count[r_idx]:
                matches += 1
            elif s2_count[r_idx] == s1_count[r_idx] + 1:
                matches -= 1

            # Remove outgoing character at `left`
            l_idx = ord(s2[left]) - ord('a')
            s2_count[l_idx] -= 1
            if s2_count[l_idx] == s1_count[l_idx]:
                matches += 1
            elif s2_count[l_idx] == s1_count[l_idx] - 1:
                matches -= 1

            left += 1

        return matches == 26

# Time Complexity: O(n1 + n2), where n1 is the length of s1 and n2 is the length of s2.
# We traverse both strings once to build the character counts and then slide the window across s2.
# Space Complexity: O(1)
# We use constant extra space for the character counts, which is fixed at 26 for lowercase letters.