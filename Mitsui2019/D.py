import sys
input = sys.stdin.readline

n = int(input())
s = input().split()[0]

ans = 0
for i in range(1000):
    num_str = str(i).zfill(3)
    a = s.find(num_str[0])
    if a==-1:
        continue
    b = s[a+1:].find(num_str[1])
    if b==-1:
        continue
    b += a+1
    c = s[b+1:].find(num_str[2])
    if c!=-1:
        ans += 1
print(ans)

