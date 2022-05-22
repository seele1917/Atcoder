import sys
input = sys.stdin.readline

h, a = map(int, input().split())

if h%a == 0:
    print(h//a)
else:
    print(h//a+1)
