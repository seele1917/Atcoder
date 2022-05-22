import sys
input = sys.stdin.readline

n = int(input())
*a, = map(int, input().split())

from fractions import gcd
from functools import reduce
import numpy as np

new_gcd = np.frompyfunc(gcd, 2, 1)

a = np.array(a)
left = new_gcd.accumulate(a, dtype=np.object).astype(np.int)
right = new_gcd.accumulate(a[::-1], dtype=np.object).astype(np.int)[::-1]
left = np.append([0], left[:-1])
right = np.append(right[1:], 0)

ans = 0
for i in range(n):
    ans = max(ans, gcd(left[i], right[i]))
print(ans)
# print(left, right)