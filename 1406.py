
# string = list(sys.stdin.readline())
# case = int(sys.stdin.readline())
# cur = len(string)
# for _ in range(case):
#     command = list(sys.stdin.readline().split())
#     if command[0] == 'L':
#         if cur > 0:
#           cur -= 1
#     elif command[0] == 'D':
#         if cur < len(string):
#           cur += 1
#     elif command[0] == 'P':
#        string.insert(cur, command[1]) # 커서의 왼쪽에 넣기 때문에 cur 즉, string의 길이를 추가해야 한다
#        cur += 1
#     else:
#        if cur > 0:
#           string.remove(string[cur-1])
# print(''.join(string))
import sys
str1 = list(sys.stdin.readline().rstrip())
str2 = []
case = int(sys.stdin.readline().rstrip())
for _ in range(case):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if str1:
            str2.append(str1.pop())
    elif command[0] == 'D':
        if str2:
            str1.append(str2.pop())
    elif command[0] == 'P':
        str1.append(command[1])
    else:
        if str1:
            str1.pop()
str1.extend(reversed(str2))
print(''.join(str1))
    
    

    
