n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n-1)]
px = [list(map(int, input().split())) for _ in range(q)]
 
l = [[] for i in range(n+1)]
for a, b in ab:  
    l[a].append(b)
    l[b].append(a)

value = [0 for i in range(n+1)]
for p, x in px:
    value[p] += x

stack = [1]
flag = [False]*(n+1)
while stack:
    v = stack.pop()
    flag[v] = True
    for e in l[v]:
        if flag[e]:
            continue
        value[e] += value[v]
        stack.append(e)
        
print(*value[1:])
