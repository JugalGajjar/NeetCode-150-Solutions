class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            # Keep searching for the next consecutive number in nums
            while (current_num + 1) in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

# Time Complexity: O(n^2)
# For each number, we may have to check for the next consecutive number in the list, which takes O(n) time.
# Space Complexity: O(1)
# We are using a constant amount of space regardless of the input size.