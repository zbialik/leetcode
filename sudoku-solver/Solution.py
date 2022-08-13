from typing import List

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:
    # Each of the digits 1-9 must occur exactly once in each row.
    # Each of the digits 1-9 must occur exactly once in each column.
    # Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    # The '.' character indicates empty cells.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        squareIndexesMap = {
            0: [0, 2],
            1: [0, 2],
            2: [0, 2],
            3: [3, 5],
            4: [3, 5],
            5: [3, 5],
            6: [6, 8],
            7: [6, 8],
            8: [6, 8]
        }
        """
        Do not return anything, modify board in-place instead.
        """
        def getUsedColumnDigits(b: List[List[str]], j: int) -> List[str]:
            return [row[j] for row in b if row[j] != '.']
        
        def getUsedRowDigits(b: List[List[str]], i: int) -> List[str]:
            return [digit for digit in b[i] if digit != '.']
        
        def getUsedSquareDigits(b: List[List[str]], i: int, j: int) -> List[str]:
            rowEdges = squareIndexesMap[i]
            colEdges = squareIndexesMap[j]
            out = []
            for row in b[rowEdges[0]:rowEdges[1]+1]:
                out += [digit for digit in row[colEdges[0]:colEdges[1]+1] if digit != '.']
            return out
        
        # 1. for each empty cell:
        #   identify possible digits
        #   if there's only 1 possible digit --> update board with digit
        def addRequiredDigits(): # TODO: implement
            print('starting addRequiredDigits()')
        
        # 2. recursion:
        #       - guess 
        def move(b: List[List[str]], i: int, j: int) -> List[List[str]]:
            print('starting move()')
            # make copy of board
            bcopy = b
            


        





# example
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
check = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
solution = Solution()
solution.solveSudoku(board = board)
if board != check:
    print('fail')
else:
    print('pass')
