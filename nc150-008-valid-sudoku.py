# Brute force
# O(n^2) time complexity, where
# n : side length of sudoku board

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sideLen = len(board)
        
        # maintain an array of 1s 
        # each time a number appears in a group (row, column or square), subtract
        # 1 from corresponding index.
        # if index drops below 0, declare sudoku invalid        
        
        # rows
        for i in range(sideLen):
            numList = [1] * (sideLen + 1)
            for j in range(sideLen):
                if board[i][j] != ".":
                    if numList[int(board[i][j])] < 1:
                        return False
                    numList[int(board[i][j])] -= 1
        
        # columns
        for i in range(sideLen):
            numList = [1] * (sideLen + 1)
            for j in range(sideLen):
                if board[j][i] != ".":
                    if numList[int(board[j][i])] < 1:
                        return False
                    numList[int(board[j][i])] -= 1

        # squares
        sideLenBy3 = sideLen // 3
        for i in range(0, sideLen, sideLenBy3):
            for j in range(0, sideLen, sideLenBy3):
                numList = [1] * (sideLen + 1)
                for k in range(i, i+sideLenBy3):
                    for l in range(j, j+sideLenBy3):
                        if board[k][l] != ".":
                            if numList[int(board[k][l])] < 1:
                                return False
                            numList[int(board[k][l])] -= 1

        return True
