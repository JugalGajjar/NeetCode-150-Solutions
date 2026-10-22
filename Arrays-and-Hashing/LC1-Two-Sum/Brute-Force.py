class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        return []

# Time Complexity: O(n^2), where n is the length of the input list.
# We have a nested loop that goes through the list, resulting in a quadratic time complexity.
# Space Complexity: O(1)
# We are not using any additional data structures that scale with the input size.