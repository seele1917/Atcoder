n = int(input())
*p, = map(int, input().split())

p_sorted = sorted(p)

ans = 'YES'

cnt = 0
for i in range(n):
    if p[i] != p_sorted[i]:
        cnt += 1

if cnt > 2:
    ans = 'NO'

print(ans)
