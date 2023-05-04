from itertools import combinations, permutations
import math
t = int(input())
gcd_list = []
for _ in range(t):
    answer = 0
    gcd = list(map(int, input().split()))
    for i in range(1, len(gcd)):
        for j in range(i+1, len(gcd)):
            answer += math.gcd(gcd[i], gcd[j])
        # for j in range(min(gcd_list[i][0], gcd_list[i][1]), 0, -1):
        # #     if gcd_list[i][1]%j == 0 and gcd_list[i][0]%j == 0:
        #         answer += j
        #         break
    print(answer)
