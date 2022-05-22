import sys
import math
input = sys.stdin.readline

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

sum = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        sum += math.sqrt((xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2)

ans = sum / n
print(ans)