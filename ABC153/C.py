import sys
input = sys.stdin.readline

n, k = map(int, input().split())
*h, = map(int, input().split())

h = sorted(h, reverse=True)
if k >= len(h):
    print(0)
else:
    print(sum(h[k:]))