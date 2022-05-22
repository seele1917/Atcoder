import sys
input = sys.stdin.readline

n = int(input())

if (n/1.08)%1 == 0:
    x = int(n/1.08)
else:
    x = int((n+1)/1.08)
if int(x*1.08) != n:
    print(':(')
else:
    print(x)