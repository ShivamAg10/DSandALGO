'''
    Given a binary array nums, return the maximum number of consecutive 1's in the array.

    Example 1:
        Input: 
            nums = [1,1,0,1,1,1]
        Output: 
            3
        Explanation: 
            The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

    Example 2:
        Input: 
            nums = [1,0,1,1,0,1]
        Output: 
            2
'''

nums = [1,0,1,1,0,1]
# maxCons, currCons, pointer = 0,0,1

# for index, bin in enumerate(nums):
#     currCons += bin
#     if currCons//pointer == 1:
#         maxCons = max(maxCons,currCons)
#     else:
#         currCons = pointer = 0
#     pointer += 1
# print(maxCons)

curr, a = 0, []

for i in nums:
    if i == 1:
        curr += 1
    else:
        a.append(curr)
        curr = 0
a.append(curr)
print(max(a))