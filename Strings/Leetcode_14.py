'''
    Longest Common Prefix

    Write a function to find the longest common prefix string amongst an array of
    strings.
    If there is no common prefix, return an empty string "".

    Example 1:

    Input: 
        strs = ["flower","flow","flight"]
    Output: 
        "fl"

    Example 2:
        Input: 
            strs = ["dog","racecar","car"]
        Output: 
            ""
        Explanation: 
            There is no common prefix among the input strings.
'''

strs = ["flower","flow","flight"]

# find min length 
min_length = len(strs[0])
for s in strs:
    if len(s) < min_length:
        min_length = len(s)

i = 0
while i < min_length:
    for s in strs:
        if s[i] != strs[0][i]:
            print(s[:i])
            break
    i += 1
print(strs[0][:i])

