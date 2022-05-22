import sys
import math
input = sys.stdin.readline

n = int(input())

ans = n
for i in range(1, int(math.sqrt(n))+1):
    if (n/i)%1 == 0 and ans > i+n//i-2:
        ans = i+n//i-2
print(ans)