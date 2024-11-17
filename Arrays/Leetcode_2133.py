'''
    An n x n matrix is valid if every row and every column 
    contains all the integers from 1 to n (inclusive).
    Given an n x n integer matrix matrix, return true if the 
    matrix is valid. Otherwise, return false.

    Example 1:
        Input: 
            matrix = [[1,2,3],[3,1,2],[2,3,1]]
        Output: 
            true
        Explanation: 
        In this case, n = 3, and every row and column contains 
        the numbers 1, 2, and 3.
        Hence, we return true.

    Example 2:
        Input: 
            matrix = [[1,1,1],[1,2,3],[1,2,3]]
        Output: 
            false
        Explanation: 
            In this case, n = 3, but the first row and the first 
            column do not contain the numbers 2 or 3.
            Hence, we return false.
'''

matrix = [[1,2,3],[3,1,2],[2,3,1]]
row = len(matrix[0])
Sn = (row * (row+1))//2
colSum = 0

for i in range(0,len(matrix)):
    # checks rows
    if sum(matrix[i]) != Sn:
        print(False)
        break
    # checks columns
    for j in range(0,len(matrix)):
        colSum += matrix[j][i]
    if colSum != Sn:
        print(False)
    colSum = 0
print("Loops ended", True)