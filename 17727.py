
tile = int(input())
dp = [0] * (tile + 1)
if tile== 1:
    print(n)
elif tile== 2:
    print(n+1)
else:
    dp[1] = 1
    dp[2] = 3
    for i in range(3, tile+1):
        dp[i] = dp[i-1] + dp[i-2]*2
    print(dp[tile]%10007)
        