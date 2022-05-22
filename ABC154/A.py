import sys
input = sys.stdin.readline

s, t = input().split()
a, b = map(int, input().split())
u = input().split()[0]

if u == s:
    print(a-1, b)
else:
    print(a, b-1)