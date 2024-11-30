from collections import Counter
s = "loveleetcode"

# ---------TLE----------
# for i in range(0,len(s)):
#     count = s.count(s[i])
#     if count == 1:
#         print(i)
#         break

# Best Complexity
# beat - 97%3..
a = Counter(s)
for i in a:
    if a[i] == 1:
        print(s.index(i))
        break