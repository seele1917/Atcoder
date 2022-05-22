import sys
input = sys.stdin.readline

n, w = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(w+1) for _ in range(n)]

for i in range(wv[0][0], w+1):
    dp[0][i] = wv[0][1]

for i in range(1, n):
    for j in range(w+1):
        if j-wv[i][0] < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wv[i][0]]+wv[i][1])
print(dp[n-1][w])
