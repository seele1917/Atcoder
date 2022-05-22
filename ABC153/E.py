import sys
input = sys.stdin.readline
import numpy as np

h, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab = np.array(ab)

a = ab[:, 0]
b = ab[:, 1]

dp = np.zeros(100001, dtype=np.int)
for i in range(1, h+1):
    dp[i] = (dp[i-a]+b).min()

print(dp[h])