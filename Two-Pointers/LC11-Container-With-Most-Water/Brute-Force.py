class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        n = len(height)

        for i in range(n):
            for j in range(i + 1, n):
                current_area = (j - i) * min(height[i], height[j])
                max_water = max(max_water, current_area)

        return max_water

# Time Complexity: O(n^2), where n is the length of the height list.
# We use two nested loops to calculate the area for every pair of lines.
# Space Complexity: O(1)
# We use constant extra space, as we only store the maximum area found.