import sys
input = sys.stdin.readline

n = int(input())
*d, = map(int, input().split())

ans = 0
for i in range(n):
    for j in range(i+1, n):
        ans += d[i]*d[j]
print(ans)