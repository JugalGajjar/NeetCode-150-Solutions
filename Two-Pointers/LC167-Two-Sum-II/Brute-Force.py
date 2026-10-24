class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    # Return 1-indexed positions
                    return [i + 1, j + 1]
        
        return []

# Time Complexity: O(n^2), where n is the length of the numbers list.
# We have a nested loop that checks each pair of numbers.
# Space Complexity: O(1)
# We use constant extra space, as we only store the indices of the two numbers.