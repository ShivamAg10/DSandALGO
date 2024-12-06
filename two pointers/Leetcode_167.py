# Two Sum of Sorted Array

class Solution:
    def twoSum(self, numbers, target):
        start = 0
        end = len(numbers)-1
        answer = []
        for i in range(len(numbers)):
            twoSum = numbers[start] + numbers[end]
            if twoSum < target:
                start += 1
            elif twoSum > target:
                end -= 1
            else:
                answer = [start+1, end+1]
        return answer