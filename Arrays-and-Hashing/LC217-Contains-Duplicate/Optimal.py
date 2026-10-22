class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
            
        return False

# Time Complexity: O(n), where n is the length of the input list nums.
# This is because we iterate through the list once, and set operations (insertion and lookup) are O(1) on average.
# Space Complexity: O(n)
# We are using a set to store the unique elements from the input list, which can grow up to the size of the input list in the worst case.