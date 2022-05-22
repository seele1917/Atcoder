n = int(input())
*a, = map(int, input().split())
*b, = map(int, input().split())

ans = sum(a)
for i in range(n):
    if a[i] < b[i]:
        b[i] -= a[i]
        a[i] = 0
    else:
        a[i] -= b[i]
        b[i] = 0
    
    if a[i+1] < b[i]:
        b[i] -= a[i+1]
        a[i+1] = 0
    else:
        a[i+1] -= b[i]
        b[i] = 0
ans = ans - sum(a)
print(ans)