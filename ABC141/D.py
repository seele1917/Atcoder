import heapq

n, m = map(int, input().split())
*a, = map(int, input().split())

ans = []
for i in range(n):
    heapq.heappush(ans, -a[i])

for i in range(m):
    temp = -heapq.heappop(ans)
    heapq.heappush(ans, -(temp//2))

print(-sum(ans))