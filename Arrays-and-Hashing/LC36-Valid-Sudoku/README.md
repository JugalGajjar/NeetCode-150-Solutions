# 36. Valid Sudoku

**Difficulty:** Medium

## Problem
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**
* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.

**Example 1:** <br>
Input: board =  <br>
[["5","3",".",".","7",".",".",".","."], <br>
["6",".",".","1","9","5",".",".","."], <br>
[".","9","8",".",".",".",".","6","."], <br>
["8",".",".",".","6",".",".",".","3"], <br>
["4",".",".","8",".","3",".",".","1"], <br>
["7",".",".",".","2",".",".",".","6"], <br>
[".","6",".",".",".",".","2","8","."], <br>
[".",".",".","4","1","9",".",".","5"], <br>
[".",".",".",".","8",".",".","7","9"]] <br>
Output: true

**Example 2:** <br>
Input: board =  <br>
[["8","3",".",".","7",".",".",".","."], <br>
["6",".",".","1","9","5",".",".","."], <br>
[".","9","8",".",".",".",".","6","."], <br>
["8",".",".",".","6",".",".",".","3"], <br>
["4",".",".","8",".","3",".",".","1"], <br>
["7",".",".",".","2",".",".",".","6"], <br>
[".","6",".",".",".",".","2","8","."], <br>
[".",".",".","4","1","9",".",".","5"], <br>
[".",".",".",".","8",".",".","7","9"]] <br>
Output: false

Explanation: <br>
Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

**Constraints:** <br>
board.length == 9 <br>
board[i].length == 9 <br>
`board[i][j]` is a digit `1-9` or `'.'`.


## Solution

#### **Intuition:**
A standard Sudoku board has three independent validation rules: no duplicate digits in any row, no duplicates in any column, and no duplicates within any of the nine $3 \times 3$ sub-boxes. 

Rather than iterating over the $9 \times 9$ grid three separate times (once for rows, once for columns, and once for sub-boxes), we can validate all three constraints simultaneously in a **single pass**. 

To track digits across the 9 sub-boxes, we map each coordinate `(r, c)` to a specific sub-box using integer division: `(r // 3, c // 3)`. As `r` and `c` range from $0$ to $8$, the expressions `r // 3` and `c // 3` evaluate to values from $0$ to $2$, cleanly partitioning the grid into a $3 \times 3$ matrix of boxes. Using hash sets for each row, column, and sub-box allows us to check for duplicates in $O(1)$ time per cell.

#### **Logic:**
1. Initialize Data Structures: Create three collections of hash sets (using `defaultdict(set)`):
   - `rows`: maps row index `r` $\rightarrow$ set of digits seen in row `r`.
   - `cols`: maps column index `c` $\rightarrow$ set of digits seen in column `c`.
   - `boxes`: maps box coordinate `(r // 3, c // 3)` $\rightarrow$ set of digits seen in that $3 \times 3$ sub-box.
2. Single Pass Traversal: Iterate through every cell `(r, c)` from `(0, 0)` to `(8, 8)`:
   - If `board[r][c] == "."`, skip to the next cell.
   - Let `val = board[r][c]` and compute the box coordinate `box_key = (r // 3, c // 3)`.
   - Check if `val` already exists in `rows[r]`, `cols[c]`, or `boxes[box_key]`. If present in any of the three, return `False` immediately.
   - If not present, insert `val` into `rows[r]`, `cols[c]`, and `boxes[box_key]`.
3. Return `True`: If all 81 cells are processed without triggering a duplicate collision, the board is valid.

#### **Example Walkthrough:**
Consider Example 2 where `board[0][0] = "8"` and `board[2][2] = "8"`:

**Initial State:** `rows = {}`, `cols = {}`, `boxes = {}`

| Step | Cell `(r, c)` | Value (`val`) | `box_key` `(r // 3, c // 3)` | Seen in `rows[r]` / `cols[c]` / `boxes[box_key]`? | Action |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `(0, 0)` | `"8"` | `(0, 0)` | No / No / No | Add `"8"` to `rows[0]`, `cols[0]`, `boxes[(0, 0)]` |
| 2 | `(0, 1)` | `"3"` | `(0, 0)` | No / No / No | Add `"3"` to `rows[0]`, `cols[1]`, `boxes[(0, 0)]` |
| ... | ... | ... | ... | ... | ... |
| k | `(2, 2)` | `"8"` | `(0, 0)` | `rows[2]`: No<br>`cols[2]`: No<br>`boxes[(0, 0)]`: **Yes** (Contains `"8"` from `(0, 0)`) | **Duplicate detected in sub-box `(0, 0)`!** Return `False` |

* **Result:** `False` (Terminates early without checking the rest of the board).

#### **Time Complexity:**
$O(1)$ <br>
Exactly $9 \times 9 = 81$ iterations (or $O(N^2)$ for an arbitrary $N \times N$ board).

#### **Space Complexity:**
$O(1)$ <br>
Tracking sets for 9 rows, 9 columns, and 9 boxes requires fixed, constant memory.