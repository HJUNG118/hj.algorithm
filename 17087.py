import sys, math
number, o_s = map(int, sys.stdin.readline().split())
y_location = list(map(int, sys.stdin.readline().split()))
answer = abs(o_s - y_location[0])
if number == 1:
    answer = abs(o_s - y_location[0])
else:
    for i in range(1, number):
        answer = math.gcd(answer, abs(o_s - y_location[i]))

print(answer)