import sys
input = sys.stdin.readline
import numpy as np

N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]
wv = np.array(wv)
V = max(wv[:, 1])
dp = np.array([float('inf')]*(N*V+1))

dp[0] = 0
for i in range(1, N):
    w, v = wv[i]
    dp[v:] = np.minimum(dp[v:], dp[:-v]+w)
    print(dp)
print(max(np.where(dp<=W)[0]))

