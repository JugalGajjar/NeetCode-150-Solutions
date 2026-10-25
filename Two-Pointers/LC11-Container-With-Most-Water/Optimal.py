class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # Area is width * min. height
            width = right - left
            current_area = width * min(height[left], height[right])
            max_water = max(max_water, current_area)

            # Move the pointer at the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

# Time Complexity: O(n), where n is the length of the height list.
# We traverse the list once with two pointers.
# Space Complexity: O(1)
# We use constant extra space, as we only store the maximum area found and the two pointers.