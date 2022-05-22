import sys
input = sys.stdin.readline

n = int(input())
uvw = [list(map(int, input().split())) for _ in range(n-1)]

graph = [[] for _ in range(n)]
for i in range(n-1):
    graph[uvw[i][0]-1].append((uvw[i][1]-1, uvw[i][2]))
    graph[uvw[i][1]-1].append((uvw[i][0]-1, uvw[i][2]))

stack = [0]
ans = [-1]*n
ans[0] = 0
while stack:
    node = stack.pop()
    for child in graph[node]:
        if ans[child[0]]!=-1:
            continue
        
        stack.append(child[0])
        if child[1]%2 == 0:
            ans[child[0]] = ans[node]
        else:
            ans[child[0]] = (ans[node]+1)%2

for a in ans:
    print(a)

