n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

times = n*(n-1)//2
graph = [[] for _ in range(times)] 
temp = [[]] * times
idx = 0
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        temp[idx] = [i+1, j+1]
        idx += 1
        
for i in range(len(a)):
    for j in range(len(a[i])-1):
        idx1 = temp.index( [min(a[i][j], i+1), max(a[i][j], i+1)] )
        idx2 = temp.index( [min(a[i][j+1], i+1), max(a[i][j+1], i+1)] )
        graph[idx1].append(idx2)
print(graph)
