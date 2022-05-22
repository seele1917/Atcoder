import sys
input = sys.stdin.readline

import numpy as np

n, k = map(int, input().split())
*v, = map(int, input().split())

v = np.array(v)

ans = 0
if n <= k:
    ans = v[v>0].sum()
else:
    for i in range(k+1):
        for j in range(k-i+1):
            if j == 0:
                take = v[0:i]
            else:
                take = np.append(v[0:i], v[-j:])
            take.sort()
            throw_num = k-i-j
            throw_num = min(throw_num, len(take[take<0]))
            su = take[throw_num:].sum()
            if su > ans:
                ans = su
print(ans)
        