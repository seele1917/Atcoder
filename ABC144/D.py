import sys
import math
input = sys.stdin.readline

a, b, x = map(int, input().split())

if a*a*b/2 <= x:
    temp = 2*(b - x/(a**2))
    theta = math.atan2(temp, a)
    ans = math.degrees(theta)
else:
    temp = 2*x/(a*b)
    theta = math.atan2(temp, b)
    ans = 90 - math.degrees(theta)
print(ans)