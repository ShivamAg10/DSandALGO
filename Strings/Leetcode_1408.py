'''
    Given an array of string words, return all strings in words that is a 
    substring of another word. You can return the answer in any order.

    A substring is a contiguous sequence of characters within a string

    Example 1:
        Input: 
            words = ["mass","as","hero","superhero"]
        Output: 
            ["as","hero"]
        Explanation: 
            "as" is substring of "mass" and "hero" is substring of "superhero".
            ["hero","as"] is also a valid answer.

    Example 2:
        Input: 
            words = ["leetcode","et","code"]
        Output: 
            ["et","code"]
        Explanation: 
            "et", "code" are substring of "leetcode".

    Example 3:
        Input: 
            words = ["blue","green","bu"]
        Output: 
            []
        Explanation: 
            No string of words is substring of another string.
'''

words = ["leetcoder","leetcode","od","hamlet","am"]
output = []

for i in range(0,len(words)):
    for j in range(0, len(words)):
        if i==j:
            pass
        elif words[i] in words[j] and words[i] not in output:
            output.append(words[i])

print(output)