# Contains Duplicate

def containsDuplicate(nums):
    return len(nums) != len(set(nums))

nums = [1,2,3,2]
print(containsDuplicate(nums))