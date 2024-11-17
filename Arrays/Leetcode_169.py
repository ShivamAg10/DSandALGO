'''
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than 
    ⌊n / 2⌋ times. You may assume that the majority element 
    always exists in the array.

    Example 1:
        Input: 
            nums = [3,2,3]
        Output: 
            3

    Example 2:
        Input: 
            nums = [2,2,1,1,1,2,2]
        Output: 
            2
'''

nums = [2,2,1,1,1,2,2]

# Brute Force Code
# countDig = 0
# for i in nums:
#     countDig = nums.count(i)
#     if countDig > len(nums)//2:
#         print(i)
#         break

# Optimal Code 
# nums.sort()
# freq,ans = 1,nums[0]
# for i in range(1,len(nums)):
#     if nums[i] == nums[i-1]:
#         freq += 1
#     else:
#         freq,ans = 1, nums[i]
#     if freq > (len(nums)//2):
#         print(ans)
#         break

# Moorse Voting Algo

freq , ans = 0,0
final = ans

for i in nums:
    if freq == 0:
        ans = i
    freq += 1 if i==ans else -1
print(ans)