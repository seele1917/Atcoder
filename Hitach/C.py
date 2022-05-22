import sys
input = sys.stdin.readline

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n-1)]

graph = [[] for _ in range(n)]
for a, b in ab:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

root = None
for i, node in enumerate(graph):
    if len(node) == 1:
        root = i

