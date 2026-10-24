class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters case-insensitively
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

# Time Complexity: O(n), where n is the length of the string.
# We traverse the string once with two pointers.
# Space Complexity: O(1)
# We use a constant amount of extra space for the pointers and variables.