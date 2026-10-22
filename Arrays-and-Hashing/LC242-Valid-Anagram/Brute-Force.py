class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

# Time Complexity: O(nlogn), where n is the length of the input strings.
# The sorting operation takes O(nlogn) time.
# Space Complexity: O(n), where n is the length of the input strings.
# The space used by the sorted lists.