import sys
input = sys.stdin.readline

n, m = map(int, input().split())

inf = float('inf')
p = 2**n
dp = [inf]*p
dp[0] = 0

for _ in range(m):
    a, _ = map(int, input().split())
    c = sum([2**(i-1) for i in map(int, input().split())])
    for i in range(p):
        if dp[i|c] > dp[i] + a: 
            dp[i|c] = dp[i] + a
    
if dp[-1] == inf:
    print(-1)
else:
    print(dp[-1])

    