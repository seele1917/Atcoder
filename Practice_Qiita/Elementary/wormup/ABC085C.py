from collections import deque

N, L, T = map(int, input().split())
XW = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

ans = []
for x, w in XW:
    if w == 1:
        cnt += T//L + T % L//(L-x)
        ans += [(x + T % L) % L]
    else:
        cnt -= T//L + T % L//x
        ans += [(x - T % L) % L]

cnt = (cnt+1) % N
ans = deque(ans)
ans.rotate(cnt)

for ele in ans:
    print(ele)
