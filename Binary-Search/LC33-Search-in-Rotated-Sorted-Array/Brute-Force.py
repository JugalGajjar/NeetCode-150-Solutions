class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        
        return -1

# Time Complexity: O(n), where n is the length of the nums list.
# We traverse the list once to find the target.
# Space Complexity: O(1)
# We use constant extra space, as we only store the index of the target if found.