'''
    Is Sequence

    Given two strings s and t, return true if s is a subsequence of t, or false 
    otherwise.
    A subsequence of a string is a new string that is formed from the original 
    string by deleting some (can be none) of the characters without disturbing 
    the relative positions of the remaining characters. (i.e., "ace" is a 
    subsequence of "abcde" while "aec" is not).

    Example 1:
        Input: 
            s = "abc", t = "ahbgdc"
        Output: 
            true

    Example 2:
        Input: 
            s = "axc", t = "ahbgdc"
        Output: 
            false
'''

def isSubsequence(s,t):
    if s == "":
        return True
    sIndex = 0
    for i in range(len(t)):
        if s[sIndex] == t[i]:
            sIndex += 1
        if len(s) == sIndex:
            return True
    return sIndex==len(s)

subsequence = "aec"
targeted = "abcde"

print(isSubsequence(subsequence, targeted))