a, b = map(int, input().split())

ans = (b-1)/(a-1)

if ans%1 > 0:
    ans += 1
print(int(ans))