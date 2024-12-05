'''
    Product of Array Except Self

    Given an integer array nums, return an array answer such that answer[i] is 
    equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
    integer.
    You must write an algorithm that runs in O(n) time and without using the 
    division operation.

    Example 1:  
        Input: 
            nums = [1,2,3,4]
        Output: 
            [24,12,8,6]

    Example 2:
        Input: 
            nums = [-1,1,0,-3,3]
        Output: 
            [0,0,9,0,0]
'''

def productExceptSelf(nums):
    answer = []
    left = [1]
    right = [0]*(len(nums)-1) + [1]
    for leftt in range(len(nums)-1):
        left.append(left[leftt]*nums[leftt])
    for rightt in range(len(nums)-1,0,-1):
        right[rightt-1] = right[rightt]*nums[rightt]
    for i in range(len(left)):
        answer.append(left[i] * right[i])
    return answer

arr = [0,4,0]

print(productExceptSelf(arr))