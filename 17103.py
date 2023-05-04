t = int(input())
# def is_prime(prime):
#     for j in range(2, int(prime**0.5)+1):
#             if prime%j == 0:
#                  return 0
#     return 1
prime = {}
for _ in range(t):
    target = int(input())
    # prime = [False, False] + [True] * (target-1)
    answer = 0
    for i in range(2, target+1):
          flg = 0
          for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                flg = 1
                prime[i] = False
                break
          if flg == 0:
              prime[i] = True

    for i in range(2, (target//2)+1):
         if prime[i] and prime[target-i]:
             answer += 1
    print(answer)