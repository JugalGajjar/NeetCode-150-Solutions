class Solution:
    def findMin(self, nums: list[int]) -> int:
        min_val = nums[0]
        for num in nums:
            if num < min_val:
                min_val = num
        
        return min_val

# Time Complexity: O(n), where n is the length of the nums list.
# We traverse the entire list once to find the minimum value.
# Space Complexity: O(1)
# We use constant extra space, as we only store the minimum value found so far.