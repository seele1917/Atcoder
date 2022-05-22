import sys
input = sys.stdin.readline

n, m = map(int, input().split())
*a, = map(int, input().split()) 

a = [ai >> 1 for ai in a]

import fractions
from functools import reduce

def getLCM(a, b):
    return a * b // fractions.gcd(a, b)

def f(x):
    cnt = 0
    while x%2 == 0:
        x //= 2
        cnt += 1
    return cnt

cnt = f(a[0])
for i in range(1, len(a)):
    if cnt != f(a[i]):
        print(0)
        break
else:
    lcm = reduce(lambda x, y: getLCM(x, y), a)
    ans = (m-lcm) // (lcm*2) + 1 if m >= lcm else 0
    print(ans)