n, k = map(int, input().split())
dp = [[1] * (k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][1] = 1

for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(dp[n][k-1] % 1000000000)
print(dp)
