string = input()
stack = []
total = 0
for i in range(len(string)):
    # stack.append(string[i])
    if string[i] == '(':
        stack.append(string[i])
    elif string[i] == ')':
        if string[i-1] == ')':
            stack.pop()
            total += 1
        elif stack[-1] == '(':
            stack.pop()
            total += len(stack)
print(total)

