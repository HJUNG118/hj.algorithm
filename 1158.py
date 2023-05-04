import sys

n, k = map(int, input().split())
answer = []
arr = [i for i in range(1, n+1)]
num = 0 # 삭제될 자리의 인덱스를 담을 것이다
while arr:
    num += k-1
    if num >= len(arr):
        num = num%len(arr)
    answer.append(str(arr.pop(num)))
print('<', ', '.join(answer), '>', sep='')



    