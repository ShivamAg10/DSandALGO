'''
    Spiral Matrix

    Given an m x n matrix, return all elements of the matrix in spiral order.

    Example 1:
        Input: 
            matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: 
            [1,2,3,6,9,8,7,4,5]

    Example 2:
        Input: 
            matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        Output: 
            [1,2,3,4,8,12,11,10,9,5,6,7]
'''

def spiralOrder(matrix):
    answer = []
    top = 0
    right = len(matrix[0])
    left = -1
    bottom = len(matrix)
    direction = right
    i = j = 0
    while len(answer) != len(matrix[0])*len(matrix):
        if direction == right:
            while j < right:
                answer.append(matrix[i][j])
                j += 1
            i += 1
            j -= 1
            right -= 1
            direction = bottom
        elif direction == bottom:
            while i < bottom:
                answer.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            bottom -= 1
            direction = left
        elif direction == left:
            while j > left:
                answer.append(matrix[i][j])
                j -= 1
            i -= 1
            j += 1
            left += 1
            direction = top
        else:
            while i > top:
                answer.append(matrix[i][j])
                i -= 1
            i += 1
            j += 1
            top += 1
            direction = right
    return answer

arr2d = [[1,2,3],[4,5,6],[7,8,9]]

print(spiralOrder(arr2d))