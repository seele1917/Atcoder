import sys
input = sys.stdin.readline

a, b = map(int, input().split())

ans = a - 2*b
if ans < 0:
    ans = 0

print(ans)