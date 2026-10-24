class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Only start counting if 'num' is the beginning of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# Time Complexity: O(n)
# We iterate through the set of numbers, and for each number, we may check for the next consecutive number in the set, which takes O(1) time on average.
# Space Complexity: O(n)
# We are using a set to store the numbers, which takes O(n) space in the worst case.