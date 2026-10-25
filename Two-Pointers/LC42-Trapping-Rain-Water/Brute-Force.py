class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        total_water = 0

        for i in range(n):
            left_max = 0
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])

            right_max = 0
            for j in range(i, n):
                right_max = max(right_max, height[j])

            water_at_i = min(left_max, right_max) - height[i]
            if water_at_i > 0:
                total_water += water_at_i

        return total_water

# Time Complexity: O(n^2), where n is the length of the height list.
# We have two nested loops, each traversing the height list.
# Space Complexity: O(1)
# We use constant extra space, as we only store a few variables for the maximum heights and total water.