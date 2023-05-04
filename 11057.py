n = int(input())
# dp = [[0] * (10) for _ in range(n+1)]

# if n == 1:
#   print(10)
# elif n == 2:
#   for i in range(10):
#     dp[2][i] = 10 - i
#   print(sum(dp[n]))

# else:
#   for i in range(10):
#     dp[2][i] = 10 - i

#   for i in range(3, n+1):
#     for j in range(10):
#         dp[i][j] += dp[i-1][j]
#   print(sum(dp[n]) % 10007)

dp = [1] * 10
for i in range(1, n):
    for j in range(1, 10):
        dp[j] += dp[j-1]
print(sum(dp) % 10007)