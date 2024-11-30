'''
    Reverse String

    Write a function that reverses a string. The input string is given as an 
    array of characters s.

    You must do this by modifying the input array in-place with O(1) extra memory.

    Example 1:
        Input: s = ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]

    Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
'''

s = ["h","e","l","l","o"]

# right but uses little bit more time
# start, end = 0, len(s)-1
# for i in range(0,len(s)//2):
#     temp = s[start]
#     s[start] = s[end]
#     s[end] = temp
#     start += 1
#     end -= 1

print(s.reverse())