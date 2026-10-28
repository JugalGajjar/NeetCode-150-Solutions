class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            for val in row:
                if val == target:
                    return True
        
        return False

# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix.
# We traverse the entire matrix to search for the target value.
# Space Complexity: O(1)
# We use constant extra space, as we only store a few variables for the search.