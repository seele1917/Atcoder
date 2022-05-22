n, k = map(int, input().split())
*h, = map(int, input().split())

ans = 0
for ele in h:
    if ele>=k:
        ans += 1
print(ans)