import sys
input = sys.stdin.readline
from collections import deque
 
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n-1)]
 
graph = [[] for _ in range(n)]
for a, b in ab:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

stack = deque([0])
parent = [None]*n
colors = [0]*n
while stack:
    node = stack.popleft()
    color = 1
    for child in graph[node]:
        if child == parent[node]:
            continue
        parent[child] = node
        if color == colors[node]:
            color += 1
        colors[child] = color
        color += 1
        stack.append(child)

 
k = max(colors)
print(k)
for a, b in ab:
    if (a-1) == parent[b-1]:
        print(colors[b-1])
    else:
        print(colors[a-1])
