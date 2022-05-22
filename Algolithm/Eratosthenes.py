import sys
input = sys.stdin.readline
import math

n = int(input())
a = list(range(2, n))
p = []

while True:
    prime = min(a)
    if prime > math.sqrt(n):
        break

    p.append(prime)
    i = 0
    while i < len(a):
        if a[i]%prime == 0:
            a.pop(i)
            continue
        i += 1
    
p += a

print(p)
