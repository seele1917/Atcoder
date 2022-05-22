import sys
import math
input = sys.stdin.readline

h, w = map(int, input().split())

ans = math.ceil(h*w/2)
if h == 1 or w == 1:
    ans = 1
print(ans)