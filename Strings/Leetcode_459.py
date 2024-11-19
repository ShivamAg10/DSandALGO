s = "abaababaab"
window = 0

for i in range(0,len(s)//2):
    if s[:i+1] == s[-(i+1):]:
        window = i+1
print(window)

newStr = s[:window]
for i in range(0,len(s),window):
    if s[i:i+window] != newStr:
        print(False)
        break

if window >= len(s)//2:
    print(False)