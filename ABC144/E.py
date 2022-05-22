import sys
import numpy as np
input = sys.stdin.readline

n, k = map(int, input().split())
*a, = map(int, input().split())
*f, = map(int, input().split())

a_sort = np.array(sorted(a))
f_sort = np.array(sorted(f, reverse=True))

def check(x):
    cost = np.maximum(0, a_sort-x//f_sort).sum()
    return cost <= k

left = -1
right = 10**12

while left+1 < right:
    mid = (left+right)//2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)


