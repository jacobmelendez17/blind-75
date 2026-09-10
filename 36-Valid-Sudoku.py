class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rows = set()
            for j in range(9):
                if board[i][j] in rows:
                    return False
                elif board[i][j] != '.':
                    rows.add(board[i][j])
              
        for i in range(9):
            cols = set()
            for j in range(9):
                if board[j][i] in cols:
                    return False
                elif board[j][i] != '.':
                    cols.add(board[j][i])
                    
        starts = [(0,0), (0,3), (0,6),
                   (3,0), (3,3), (3,6),
                   (6,0), (6,3), (6,6)]

        for i, j in starts:
            boxes = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if board[row][col] in boxes:
                        return False
                    elif board[row][col] != '.':
                        boxes.add(board[row][col])

        return True

# In this solution, we utilize a set to track repeated numbers in rows, columns, and boxes
# Rows and columns are pretty straightforward. Iterate and check if the number is in the set already
# For boxes, we create a list of starting points of each box and iterate through every cell of that box