'''
    Baseball Game
'''

def baseball(ops):
    lst = []
    count = -1
    # arr1 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    for i in ops:
        if i == "C" and lst != []:
            lst.pop()
            count -= 1
        elif i == "D" and lst != []:
            lst.append(int(lst[count])*2)
            count += 1
        elif i == "+":
            lst.append(int(lst[count]) + int(lst[count-1]))
            count += 1
        else:
            lst.append(int(i))
            count += 1
    sum = 0
    for i in lst:
        sum += i
    return sum

arr = ["5", "2", "C", "D", "+"]
arr1 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
arr2 = ["1", "C"]

print(baseball(arr))
print(baseball(arr1))
print(baseball(arr2))