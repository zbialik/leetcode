from typing import List
import itertools

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:
    # Each of the digits 1-9 must occur exactly once in each row.
    # Each of the digits 1-9 must occur exactly once in each column.
    # Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    # The '.' character indicates empty cells.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        allDigits = ['1','2','3','4','5','6','7','8','9']
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
        unfilledCellPositions:List[List[int]] = []

        """
        Do not return anything, modify board in-place instead.
        """
        def getUsedColumnDigits(j: int) -> List[str]:
            return [row[j] for row in board if row[j] != '.']
        
        def getUsedRowDigits(i: int) -> List[str]:
            return [digit for digit in board[i] if digit != '.']
        
        def getUsedSquareDigits(i: int, j: int) -> List[str]:
            rowEdges = squareIndexesMap[i]
            colEdges = squareIndexesMap[j]
            out = []
            for row in board[rowEdges[0]:rowEdges[1]+1]:
                out += [digit for digit in row[colEdges[0]:colEdges[1]+1] if digit != '.']
            return out
        
        def getPossibleColumnDigits(j: int) -> List[str]:
            return [d for d in allDigits if d not in getUsedColumnDigits(j)]
        
        def getPossibleRowDigits(i: int) -> List[str]:
            return [d for d in allDigits if d not in getUsedRowDigits(i)]
        
        def getPossibleSquareDigits(i: int, j: int) -> List[str]:
            return [d for d in allDigits if d not in getUsedSquareDigits(i, j)]

        def getPossibleDigits(i: int, j: int) -> List[str]:
            return list(set.intersection(*map(set, [
                getPossibleColumnDigits(j), 
                getPossibleRowDigits(i), 
                getPossibleSquareDigits(i, j)
            ])))
        
        # 1. for each empty cell:
        #   identify possible digits
        #   if there's only 1 possible digit --> update board with digit
        def fillRequiredDigits():
            reloop = True
            while reloop:
                reloop = False
                for i, j in itertools.product(range(9), range(9)):
                    if board[i][j] == '.':
                        possibleDigits = getPossibleDigits(i, j)
                        if len(possibleDigits) == 1:
                            board[i][j] = possibleDigits[0]
                            reloop = True

        # 2. recursion:
        def move(guessPointer: int) -> bool: # returns True when reached winning game
            if len(unfilledCellPositions) == 0:
                return True # accounts for when function is first entered with already solved game
            
            cellLocation = unfilledCellPositions.pop() # [i,j] for cell to assign digit
            i = cellLocation[0]; j = cellLocation[1]
            possibleDigits = getPossibleDigits(i, j)
            
            if guessPointer < len(possibleDigits): # WIN !!
                board[i][j] = possibleDigits[guessPointer] # assign cell
                return True
            else:
                if guessPointer >= len(possibleDigits): # INVALID MOVE
                    unfilledCellPositions.append(cellLocation) # revert pop
                    board[i][j] = '.'
                    return False
                else:
                    board[i][j] = possibleDigits[guessPointer] # assign cell
                    valid = move(0)
                    if not valid: # recurse and check next move
                        board[i][j] = '.'
                        unfilledCellPositions.append(cellLocation) # revert pop
                        return move(guessPointer + 1)
                    else:
                        return True
        
        # MAIN PROCESS
        fillRequiredDigits() # first clean board

        # get list of cells 
        for i, j in itertools.product(range(9), range(9)):
            if board[i][j] == '.':
                unfilledCellPositions.append([i,j]) # append cell
        
        move(0)






# example
b1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
check = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
solution = Solution()
solution.solveSudoku(board=b1)
if b1 != check:
    print('fail')
else:
    print('pass')


b2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
solution.solveSudoku(board=b2)
if b2 != check:
    print('fail')
else:
    print('pass')
