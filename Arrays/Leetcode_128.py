'''
    Longest Consecutive Sequence
'''

def longestConsecutive(nums):
    longest = 0
    for num in nums:
        if num - 1 not in nums:
            next_num = num + 1
            length = 1
            while next_num in nums:
                length += 1
                next_num += 1
            longest = max(longest, length)
    return longest

arr = [1,2,99,100,101,34]

print(longestConsecutive(arr))