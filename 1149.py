n = int(input())
house_list = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
for i in range(n):
    for j in range(3):
        dp[i][j] = house_list[i][j]

for i in range(1, n):
  for j in range(3):
    dp[i][j] = min(dp[i][j] + dp[i-1][j-1], dp[i][j] + dp[i-1][j-2])
print(min(dp[n-1]))