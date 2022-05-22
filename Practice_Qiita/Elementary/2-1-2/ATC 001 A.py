from collections import deque

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]


def get_start_idx(C):
    for i in range(H):
        for j in range(W):
            if C[i][j] == 's':
                return (i, j)
    return (-1, -1)


def check(y, x):
    if y < 0 or y >= H or x < 0 or x >= W:
        return False
    else:
        return True


def dfs(C, start):
    sy, sx = start
    stack = deque([(sy, sx)])
    go_idx = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    reached = [[False] * W for _ in range(H)]
    while stack:
        y, x = stack.pop()
        reached[y][x] = True

        if C[y][x] == 'g':
            return 'Yes'

        for idx in go_idx:
            y_next, x_next = y + idx[0], x + idx[1]
            if check(y_next, x_next) and C[y_next][x_next] != '#' and reached[y_next][x_next] == False:
                stack.append((y_next, x_next))
    return 'No'


print(dfs(C, get_start_idx(C)))
