import sys
input = sys.stdin.readline
from collections import deque
import numpy as np

n, u, v = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n-1)]

graph = [[] for _ in range(n)]
for a, b in ab:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


def dfs(graph, start):
    stack = deque([start])
    dist = [-1]*n
    dist[start] = 0
    while stack:
        node = stack.pop()
        dist_x = dist[node] + 1
        for child in graph[node]:
            if dist[child] != -1:
                continue
            dist[child] = dist_x
            stack.append(child)
    return dist

distance1 = np.array(dfs(graph, u-1))
distance2 = np.array(dfs(graph, v-1))

distance = distance2[distance1<distance2]
ans = max(distance)-1
print(ans)




