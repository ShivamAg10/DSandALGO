s = "A man, a dplan, a canal: Panama"


s = s.lower()
l = 0
r = len(s)-1
while l < r:
    if not s[l].isalnum():
        l += 1
        continue
    if not s[r].isalnum():
        r -= 1
        continue
    if s[l] != s[r]:
        print(False)
    l += 1
    r -= 1
print(True)
        
        