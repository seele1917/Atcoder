import sys
import math
input = sys.stdin.readline

n = int(input())

cnt = 0
for i in range(n):
    a = i+1
    cnt += n//a
    if n%a == 0:
        cnt -= 1

print(cnt)