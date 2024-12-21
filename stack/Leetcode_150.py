''' 
    Evaluate Reverse Polish Notation
'''

def evalRPN(tokens):
    num = []
    for i in range(0,len(tokens)):
        if tokens[i] == '+':
            answer = num[len(num)-1] + num[len(num)-2]
            num.pop()
            num.pop()
            num.append(answer)
        elif tokens[i] == '-':
            answer = num[len(num)-2] - num[len(num)-1]
            num.pop()
            num.pop()
            num.append(answer)
        elif tokens[i] == '*':
            answer = num[len(num)-1] * num[len(num)-2]
            num.pop()
            num.pop()
            num.append(answer)
        elif tokens[i] == '/':
            answer = int(num[len(num)-2] / num[len(num)-1])
            num.pop()
            num.pop()
            num.append(answer)
        else:
            num.append(int(tokens[i]))
    return num[0]

arr = ['2','1','+','3','*']
arr1 = ['4','13','5','/','+']
arr2 = ['10','6','9','3','+','-11','*','/','*','17','+','5','+']

# print(evalRPN(arr))
# print(evalRPN(arr1))
print(evalRPN(arr2))