s = "aba"

if not s:
    print(False)

ss = (s+s)[1:-1]
print(ss.find(s) != -1)