import sys
input = sys.stdin.readline

n, m = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(m)]

cnt_list = [0]*n
for x, y, z in xyz:
    cnt_list[x-1] += 1
    cnt_list[y-1] += 1
print(cnt_list)