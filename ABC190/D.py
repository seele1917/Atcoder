import math
N = int(input())

N = 2 * N

ans = 0
for i in range(1, int(math.sqrt(N))+1):
    if N % i != 0:
        continue

    x, y = i, N//i
    n, a = x, (y-x-1)/2
    if a % 1 == 0:
        ans += 1

    x, y = N//i, i
    n, a = x, (y-x-1)/2
    if a % 1 == 0:
        ans += 1

print(ans)
