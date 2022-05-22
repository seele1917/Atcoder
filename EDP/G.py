import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N)]
out_deg = [0]*N
for x, y in xy:
    graph[y-1].append(x-1)
    out_deg[x-1] += 1


dp = [0]*N
stack = deque([i for i in range(N) if out_deg[i]==0])
while stack:
    node = stack.popleft()
    for child in graph[node]:
        dp[child] = max(dp[child], dp[node]+1)
        out_deg[child] -= 1
        if out_deg[child] == 0:
            stack.append(child)
    
print(max(dp))