import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

cnt = n//(a+b)
mod = n%(a+b)
if a < mod:
    ans = (cnt+1) * a
else:
    ans = cnt * a + mod

print(ans)
