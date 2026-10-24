class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]

# Time Complexity: O(n), where n is the length of the string.
# We traverse the string once to filter and once to check for palindrome.
# Space Complexity: O(n)
# We use extra space to store the filtered characters.