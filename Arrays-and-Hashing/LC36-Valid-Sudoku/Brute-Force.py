class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 1. Check rows
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

        # 2. Check columns
        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

        # 3. Check 3x3 sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        val = board[r][c]
                        if val != ".":
                            if val in seen:
                                return False
                            seen.add(val)

        return True

# Time Complexity: O(1)
# The board is always 9x9, so the number of operations is constant.
# Space Complexity: O(1)
# The space used by the sets is also constant, as there are at most 9 unique values in each row, column, or sub-box.