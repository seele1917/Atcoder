import sys
import numpy as np
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())

ma = max([r1, c1, r2, c2])

seq = range(ma+1)
L = [list(seq) for _ in seq]

for a in seq:
    for b in seq[a:]:
        if a == 0:
            temp = 1
        elif a == b:
            temp = L[a-1][b]*2
        else:
            temp =  L[a-1][b]+L[a][b-1]
        L[a][b] = temp

L = np.array(L)
ans = sum(L[c1+1:c2][r1+1:r2]) + L[c1][r1]
print(L)
print(L[r1-1:2, 0:2])