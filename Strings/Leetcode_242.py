s = "anagram"
t = "nagaram"

# if len(s) != len(t):
#     print(False)

# for char in s:
#     if s.count(char) != t.count(char):
#         print(False)
#         break

from collections import Counter

print(Counter(s) == Counter(t))