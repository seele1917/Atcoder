import sys
input = sys.stdin.readline
import math

h = int(input())

height = int(math.log2(h))
print(2**(height+1) - 1)