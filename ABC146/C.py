import sys
input = sys.stdin.readline

a, b, x = map(int, input().split())

l =0
r = x
ans = 0
precost = x
while l<=r:
    mid = (l+r) // 2
    cost = a*mid+b*len(str(mid))
    if precost == cost:
        ans = mid
        break
    if cost < x:
        l = mid
    elif cost > x:
        r = mid
    precost = cost

if ans > 10**9:
    ans = 10**9

print(ans)