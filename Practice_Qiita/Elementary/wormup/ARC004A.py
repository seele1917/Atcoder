N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for x1, y1 in xy:
    for x2, y2 in xy:
        if x1 == x2 and y1 == y2:
            continue
        length = (x1-x2)**2 + (y1-y2)**2
        if length > ans:
            ans = length

print(ans ** (1/2))
