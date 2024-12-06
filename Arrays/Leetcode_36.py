'''
    Valid Sudoku

    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
    validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:
        A Sudoku board (partially filled) could be valid but is not necessarily 
        solvable.
        Only the filled cells need to be validated according to the mentioned 
        rules.

    Example 1:
        Input: 
            board = 
                [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        Output: 
            true

    Example 2:
        Input: 
            board = 
                [["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        Output: 
            false
        Explanation: 
        Same as Example 1, except with the 5 in the top left corner being 
        modified to 8. Since there are two 8's in the top left 3x3 sub-box, 
        it is invalid.
'''

def isValidSudoku(board):
    # for i in range(9):
    #     rowNumbers = ["1","2","3","4","5","6","7","8","9"]
    #     colNumbers = ["1","2","3","4","5","6","7","8","9"]
    #     for j in range(9):
    #         if board[i][j] in rowNumbers: #board[i][j] != ".":
    #             rowNumbers.remove(board[i][j])
    #             # print(board[i][j])
    #         elif board[i][j] == ".":
    #             pass
    #         else:
    #             return False
            
    #         if board[j][i] in colNumbers: #board[i][j] != ".":
    #             colNumbers.remove(board[j][i])
    #             print(board[j][i])
    #         elif board[j][i] == ".":
    #             pass
    #         else:
    #             return False
    boxNumbers = ["1","2","3","4","5","6","7","8","9"]
    for i in range(3):
        for j in range(3):
            if board[i][j] in boxNumbers: #board[i][j] != ".":
                boxNumbers.remove(board[i][j])
                print(board[i][j])
            elif board[i][j] == ".":
                pass
            else:
                return False
    boxNumbers = ["1","2","3","4","5","6","7","8","9"]
    for i in range(3):
        for j in range(3,6):
            if board[i][j] in boxNumbers: #board[i][j] != ".":
                boxNumbers.remove(board[i][j])
                print(board[i][j])
            elif board[i][j] == ".":
                pass
            else:
                return False
    return True

sudoku = [["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(sudoku))