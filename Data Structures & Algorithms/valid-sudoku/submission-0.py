class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for i in range(len(board))]
        colSet = [set() for i in range(len(board[0]))] 
        squareSet = [[set() for i in range(len(board[0])//3)] for j in range(len(board)//3)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col] 
                if val == ".":
                    continue
                
                squareRow = row // 3
                squareCol = col // 3
                if val in rowSet[row] or val in colSet[col] or val in squareSet[squareRow][squareCol]:
                    return False
                
                rowSet[row].add(val)
                colSet[col].add(val)
                squareSet[squareRow][squareCol].add(val)
        return True