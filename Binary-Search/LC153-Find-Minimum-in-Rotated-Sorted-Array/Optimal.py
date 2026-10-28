class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # Inflection point is in the right half
                left = mid + 1
            else:
                # nums[mid] could be the min, or min is to the left
                right = mid

        return nums[left]

# Time Complexity: O(log n), where n is the length of the nums list.
# We perform a binary search, halving the search space with each iteration.
# Space Complexity: O(1)
# We use constant extra space, as we only store a few variables for indices and the mid value.