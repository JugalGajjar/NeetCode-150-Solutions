class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_map = {}  # num -> index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], i]
            
            prev_map[num] = i
            
        return []

# Time Complexity: O(n), where n is the length of the input list.
# We traverse the list containing n elements only once. Each lookup in the map costs only O(1) time.
# Space Complexity: O(n), where n is the length of the input list.
# We store up to n elements in the hash map.