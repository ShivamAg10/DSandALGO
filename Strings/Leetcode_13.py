s = "III"
roman = {
    'M' : 1000,
    'D' : 500,
    'C' : 100,
    'L' : 50,
    'X' : 10,
    'V' : 5,
    'I' : 1
}

number = 0
# s = "MCMXCIV"
i=0
while i<len(s)-1:
    if roman[s[i+1]] > roman[s[i]]:
        number += roman[s[i+1]] - roman[s[i]]
        i+=1
    else:
        number += roman[s[i]]
    i+=1
    print(i, number)

if i<len(s):
    print(number + roman[s[len(s)-1]])