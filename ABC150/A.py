import sys
input = sys.stdin.readline

k, x = map(int, input().split())
if 500*k >= x:
    print("Yes")
else:
    print("No")