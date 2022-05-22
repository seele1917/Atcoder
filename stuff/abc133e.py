import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
ab = [list(map(lambda x:int(x)-1, input().split())) for _ in range(n-1)]

mod = 10**9+7

def dfs(K, graph, now, src):
    if src == -1:
        use_num_color = k-1
    else:
        use_num_color = k-2

    if len(graph[now])>k:
        return 0
    
    num_cases = 1
    for e in graph[now]:
        if e==src: continue
        num_cases *= use_num_color
        num_cases %= mod
        use_num_color -= 1

    for e in graph[now]:
        if e==src: continue
        num_cases *= dfs(K, graph, e, now)
        num_cases %= mod

    return num_cases

def make_graph(list):
    n = len(list)
    graph = [[] for _ in range(n+1)]
    for a, b in list:
        graph[a].append(b)
        graph[b].append(a)
    return graph

graph = make_graph(ab)
ans = k*dfs(k, graph, 0, -1)
ans %= mod
print(ans)

