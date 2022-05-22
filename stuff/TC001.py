import sys
sys.setrecursionlimit(10000000)

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
c_prime = [[False]*w for _ in range(h)]

def dfs(x, y, w, h, maze, reached):
    if not 0<=x<w or not 0<=y<h or maze[y][x] == '#': return
    if reached[y][x]: return

    reached[y][x] = True

    dfs(x+1, y, w, h, maze, reached)
    dfs(x, y+1, w, h, maze, reached)
    dfs(x-1, y, w, h, maze, reached)
    dfs(x, y-1, w, h, maze, reached)


for i in range(h):
    if 's' in c[i]:
        sx, sy = c[i].index('s'), i
        break
for i in range(h):
    if 'g' in c[i]:
        gx, gy = c[i].index('g'), i
        break

dfs(sx, sy, w, h, c, c_prime)
if c_prime[gy][gx]:
    print('Yes')
else:
    print('No')