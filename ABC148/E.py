import sys
input = sys.stdin.readline

n = int(input())

if n%2 == 1:
    print(0)
else:
    cnt = 0
    tmp = 10
    while(tmp <= n):
        cnt += n//tmp
        tmp *= 5
    print(cnt)