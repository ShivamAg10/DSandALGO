def strStr(h,n):
    if n not in h:
        return {1:-1}
    if n==h:
        return 0
    length = len(n)
    for i in range(0,len(h)):
        if h[i:i+length] == n:
            return i
    return {2:-1}

haystack = "butsad"
needle = "sad"

a = strStr(haystack, needle)
print(a)