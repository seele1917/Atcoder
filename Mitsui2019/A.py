import sys
input = sys.stdin.readline

m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())

if d1+1 != d2:
    print(1)
else:
    print(0)