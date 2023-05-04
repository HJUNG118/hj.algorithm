# n = int(input())
# stack = []
# arr = []
# for _ in range(n):
#     a = int(input())
#     arr.append(a)
# for i in range(n):
#     stack.append(i)
#     print('+')
#     while stack[-1] == arr[0]:
#           print('-')
#           arr.pop(0)
#           stack.pop()

n = int(input())
s = []
op = []
count = 1
temp = True
for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)