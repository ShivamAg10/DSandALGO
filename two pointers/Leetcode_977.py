# Squares of Sorted Array

class Solution:
    def sortedSquares(self, nums):
        answer = []
        for i in nums:
            answer.append(i*i)
        answer.sort()
        return answer