'''
    Rotate Image

    You are given an n x n 2D matrix representing an image, rotate the image by 
    90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the 
    input 2D matrix directly. DO NOT allocate another 2D matrix and do the 
    rotation.

    Example 1:
        Input: 
            matrix= [[1,2,3],[4,5,6],[7,8,9]]
        Output: 
            [[7,4,1],[8,5,2],[9,6,3]]

    Example 2:
        Input: 
            matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        Output: 
            [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''

# Worst Case Solution
# def rotate(matrix):
#     answer = []
#     for i in range(len(matrix)):
#         temp = []
#         for j in range(len(matrix)):
#             r = i
#             c = abs(j-(len(matrix)-1))
#             temp.append(matrix[c][r])
#         answer.append(temp)
#     return answer

def rotate1(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()    
    return matrix

arr2d = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

# print(rotate(arr2d))
print(rotate1(arr2d))