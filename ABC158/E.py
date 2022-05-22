import sys
input = sys.stdin.readline
from math import factorial

def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)

n, p = map(int, input().split())
s = input().split()[0]

list = []
for i in range(1, len(s)+1):
    list += [int(s[-i:])%p]

cnt = [0]*10
ans = 0
for i in range(len(s)):
    cnt[list[i]] += 1

ans = cnt[0]
for i in range(10):
    if cnt[i] >= 2:
        ans += comb(cnt[i], 2)
print(int(ans))