from heapq import heappush, heappop

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort()
ans = 0
hq = []
idx = 0
for i in range(1, m+1):
    for j in range(idx, n):
        if ab[j][0] == i:
            heappush(hq, (-ab[j][1], ab[j][0]))
            idx += 1
        else:
            break
    if len(hq) != 0:
        ans -= heappop(hq)[0]
    
print(ans)
