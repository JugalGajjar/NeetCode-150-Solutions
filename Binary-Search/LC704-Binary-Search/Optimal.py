class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

# Time Complexity: O(log n), where n is the length of the nums list.
# We divide the search space in half with each iteration.
# Space Complexity: O(1)
# We use constant extra space, as we only store the left, right, and mid indices.