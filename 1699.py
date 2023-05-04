from collections import Counter
n = int(input())
dp = [0] * (int(n**0.5)+2)
for i in range(int(n**0.5), 0, -1):
    if i*i <= n:
      n -= i*i
      dp[i] += 1
      if n%(i*i) == 0:
         dp[i] += n//(i*i)
         n -= (n//(i*i)) * (i*i)
    if n == 0:
       break
answer = 0
for i in dp:
   if i != 0:
      answer += i
print(answer)       

# import sys
# input = sys.stdin.readline

# n = int(input())
# dp = [k for k in range(n+1)]

# for i in range(1, n + 1):
#     for j in range(1, i):
#         if j*j > i:
#             break
#         if dp[i] > dp[i-j*j]+1:
#             dp[i] = dp[i-j*j] + 1
# print(dp[n])