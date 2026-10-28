class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# Time Complexity: O(log(m * n)), where m is the number of rows and n is the number of columns in the matrix.
# We perform a binary search on the entire matrix, which has m * n elements.
# Space Complexity: O(1)
# We use constant extra space, as we only store a few variables for the binary search.