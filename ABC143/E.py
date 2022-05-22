import sys
input = sys.stdin.readline
 
n, m, l = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]
q = int(input())
 
st = [list(map(int, input().split())) for _ in range(q)]
 
graph = [[float('inf') for _ in range(n)] for _ in range(n)]
 
 
for a, b, c in abc:
    graph[a-1][b-1] = c 
    graph[b-1][a-1] = c
for i in range(n):
    graph[i][i] = 0
 
# print(graph)
 
def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
 
graph = warshall_floyd(graph)
 
for i in range(n):
    for j in range(n):
        if 0 < graph[i][j] <= l:
            graph[i][j] = 1
        if graph[i][j] > l:
            graph[i][j] = float('inf')
 
graph = warshall_floyd(graph)
 
for s, t in st:
    print(graph[s-1][t-1]-1 if graph[s-1][t-1] != float('inf') else -1)