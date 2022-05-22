import sys
input = sys.stdin.readline

a, b, m = map(int, input().split())
*a, = map(int, input().split())
*b, = map(int, input().split())  

mi = min(a) + min(b)
for _ in range(m):
    x, y, c = map(int, input().split())
    price = a[x-1]+b[y-1]-c
    if mi > price:
        mi = price

print(mi)