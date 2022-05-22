import sys
input = sys.stdin.readline

import bisect

n = int(input())
*l, = map(int, input().split())
l.sort()

ans = 0
for i in range(n-1, -1, -1):
    for j in range(i-1, 0, -1):
        sub = l[i]-l[j] 
        idx = bisect.bisect_right(l, sub)
        if idx >= j: continue
        ans += j-idx
print(ans)
