'''
    Merge String Alternately

    You are given two strings word1 and word2. Merge the strings by adding 
    letters in alternating order, starting with word1. If a string is longer 
    than the other, append the additional letters onto the end of the merged 
    string.
    Return the merged string.

    Example 1:  
        Input: 
            word1 = "abc", word2 = "pqr"
        Output: 
            "apbqcr"
        Explanation: 
            The merged string will be merged as so:
            word1:  a   b   c
            word2:    p   q   r
            merged: a p b q c r

    Example 2:
        Input: 
            word1 = "ab", word2 = "pqrs"
        Output: 
            "apbqrs"
        Explanation: 
            Notice that as word2 is longer, "rs" is appended to the end.
            word1:  a   b 
            word2:    p   q   r   s
            merged: a p b q   r   s

    Example 3:
        Input: 
            word1 = "abcd", word2 = "pq"
        Output: 
            "apbqcd"
        Explanation: 
            Notice that as word1 is longer, "cd" is appended to the end.
            word1:  a   b   c   d
            word2:    p   q 
            merged: a p b q c   d
'''
# Worst Solution
# def mergeAlternately(word1, word2):
#     mergedStr = ""
#     if len(word1) == len(word2):
#         for i in range(len(word2)):
#             mergedStr += (word1[i] + word2[i])
#     elif len(word1) > len(word2):
#         for i in range(len(word2)):
#             mergedStr += (word1[i] + word2[i])
#         mergedStr += word1[len(word2):]
#     else:
#         for i in range(len(word1)):
#             mergedStr += (word1[i] + word2[i])
#         mergedStr += word2[len(word1):]
#     return mergedStr

# Optimal Solution
# def mergeAlternately1(word1, word2):
#     len_word1 = len(word1)
#     len_word2 = len(word2)
#     a = b = 0
#     mergedStr = ""
#     while a<len_word1 or b<len_word2:
#         if a<len_word1:
#             mergedStr += word1[a]
#             a += 1
#         if b<len_word2:
#             mergedStr += word2[b]
#             b += 1
#     return mergedStr

# Best Solution - 34ms
def mergeAlternately2(word1, word2):
    len_word1 = len(word1)
    len_word2 = len(word2)
    a = b = 0
    str_lst = []
    while a<len_word1 or b<len_word2:
        if a<len_word1:
            str_lst += word1[a]
            a += 1
        if b<len_word2:
            str_lst += word2[b]
            b += 1
    return "".join(str_lst)

str1 = "abcd"
str2 = "pqrs"

# print(mergeAlternately(str1, str2))
# print(mergeAlternately1(str1, str2))
print(mergeAlternately2(str1, str2))