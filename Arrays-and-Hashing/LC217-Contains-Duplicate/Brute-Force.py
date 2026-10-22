class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
                
        return False

# Time Complexity: O(n^2), where n is the length of the input list nums.
# This is because we have a nested loop that iterates through the list to check for duplicates.
# Space Complexity: O(1)
# We are not using any additional data structures that grow with the input size.