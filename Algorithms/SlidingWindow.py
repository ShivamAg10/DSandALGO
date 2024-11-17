nums = [8,3,-2,4,5,-1,0,5,3,9,-6]
currSum = maxSumLst = sum(nums[0:4])
pointer = 0

for i in range(4,len(nums)):
    currSum = currSum - nums[pointer] + nums[i]
    maxSumLst = max(maxSumLst, currSum)
    pointer += 1

print(maxSumLst)