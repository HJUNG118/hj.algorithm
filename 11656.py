str = list(input())
stack = []
for i in range(len(str)):
    stack.append(str[i:])
stack.sort()
for i in range(len(stack)):
    print(''.join(stack[i]))