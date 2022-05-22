import sys
import math
input = sys.stdin.readline

n = list(input().split()[0])
k = int(input())

if k == 1:
    ans = 10*math.factorial(len(n)-1)-len(n)+1
    ans += int(n[0])
elif k == 2:
    ans += 