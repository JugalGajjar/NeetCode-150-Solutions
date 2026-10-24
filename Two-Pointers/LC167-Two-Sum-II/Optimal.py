class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            cur_sum = numbers[left] + numbers[right]

            if cur_sum == target:
                return [left + 1, right + 1]
            elif cur_sum > target:
                right -= 1
            else:
                left += 1

        return []

# Time Complexity: O(n), where n is the length of the numbers list.
# We traverse the list once with two pointers.
# Space Complexity: O(1)
# We use constant extra space, as we only store the indices of the two numbers.