import sys
input = sys.stdin.readline

n, k = map(int, input().split())
*a, = map(int, input().split())

cnt = 0
su = a[0]
l = 0
r = 1
for _ in range(2*n):
    # print(a[l:r])
    if su >= k:
        cnt += n-r+1
        l += 1
        su -= a[l-1]
    else:
        if r == n:
            break
        r += 1
        su += a[r-1]
print(cnt)