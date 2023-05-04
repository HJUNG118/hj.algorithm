import sys
from collections import Counter
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
stack = []
counter = Counter(a)
answer = [-1] * n
for i in range(n):
    while stack and counter[a[i]] > counter[a[stack[-1]]]:
        answer[stack.pop()] = a[i]
    stack.append(i)
print(*answer)


    