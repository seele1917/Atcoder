n = int(input())
*a, = map(int, input().split())

ans = a[:]

for i in range(n//2, 0, -1):
    cnt = 0
    for times in range(i, n+1, i):
        cnt += ans[times-1]
    if cnt%2 != a[i-1]:
        ans[i-1] = (ans[i-1]+1)%2

print(sum(ans))
for i in range(n):
    if ans[i] == 1:
        print(i+1, end=' ')
