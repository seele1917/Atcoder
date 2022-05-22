n = int(input())

length = len(str(n))

temp = 10
ans = 0
for i in range(length-1):
    if i%2 == 0:
        ans += temp * 0.9
    temp *= 10

if length%2 == 1:
    ans += n - temp/10 + 1
print(int(ans))