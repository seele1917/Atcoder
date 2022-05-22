import sys
input = sys.stdin.readline

s = input().split()[0]
t = input().split()[0]

dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
for i in range(len(s)):
    for j in range((len(t))):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i][j]+1, dp[i+1][j], dp[i][j+1])
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

i = len(s)
j = len(t)
ans = ''
while i>0 and j>0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        i -= 1
        j -= 1
        ans = s[i] + ans
print(ans)