import sys
from collections import deque
size = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
stack = deque()
answer = [-1] * size

for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
print(*answer)
    

