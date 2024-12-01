s = "([{}])"

s_dict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

stack = []

for b in s:
    if b in s_dict:
        if s_dict[b] not in stack:
            print(False)
            break
        top_element = stack.pop()
        if s_dict[b] != top_element:
            print(False)
            break
    else:
        stack.append(b)