import sys
input = sys.stdin.readline

h, n = map(int, input().split())
*a, = map(int, input().split())

if h <= sum(a):
    print("Yes")
else:
    print("No")