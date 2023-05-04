a = int(input())
a_list = list(map(int, input().split()))
stack = []
dp = [1] * (a+1)

for i in range(a):
  for j in range(i):
    if a_list[j] < a_list[i]:
      dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
x = max(dp)

for i in range(a-1, -1, -1):
  if dp[i] == x:
    stack.append(a_list[i])
    x -= 1
stack.reverse()
print(*stack)