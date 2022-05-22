import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
S = [list(input().split()[0]) for _ in range(H)]

def bfs(S, H, W, start):
    INF = -1
    stack=deque([start])
    distance = [[INF]*W for _ in range(H)]
    distance[start[1]][start[0]] = 0
    while stack:
        x, y = stack.popleft()
        for i, j in [(1,0),(0,1),(-1,0),(0,-1)]:
            next_x = x + i
            next_y = y + j
            if not(0 <= next_x < W and 0 <= next_y < H):
                continue
            if S[next_y][next_x] != '#' and distance[next_y][next_x] == -1:
                stack.append([next_x, next_y])
                distance[next_y][next_x] = distance[y][x] + 1
    return max(map(max, distance))

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] != "#":
            ans = max(ans, bfs(S, H, W, (j, i)))
print(ans)