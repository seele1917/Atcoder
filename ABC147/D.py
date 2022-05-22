import sys
input = sys.stdin.readline

import numpy as np

mod = 10**9+7

n = int(input())
*a, = map(int, input().split())
a = np.array(a)

ans = 0
for i in range(60):
    bits = np.count_nonzero(a&1)
    ans += 2**i*bits*(n-bits)
    a >>= 1
    
print(ans%mod)

