a, b = map(int, input().split())
for i in range(a, b+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        print(i) 
# def find_prime(target, dev):
#     if dev < 2:
#         return 0
#     for j in range(2, dev+1):
#         if target%j == 0:
#             return 1
#     return 0

# for i in range(a, b+1):
#     if i == 1:
#         a = 1
#         continue
#     if i == 2:
#         a = 0
#     dev = i//2
#     a = find_prime(i, dev)
#     if a == 0:
#         print(i)   
