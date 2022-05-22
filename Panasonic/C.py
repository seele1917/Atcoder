import sys
# import math
from decimal import *
input = sys.stdin.readline

a, b, c = map(int, input().split())


if Decimal(a).sqrt() + Decimal(b).sqrt() < Decimal(c).sqrt():
    print('Yes')
else:
    print('No')