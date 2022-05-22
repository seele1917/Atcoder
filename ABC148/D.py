import sys
input = sys.stdin.readline

n = int(input())
*a, = map(int, input().split())

tmp = 1
cnt = 0
for i in range(n):
    if a[i] == tmp:
        tmp += 1
    else:
        cnt += 1

if cnt == n:
    print(-1)
else:
    print(cnt)