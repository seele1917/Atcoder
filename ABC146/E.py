import sys
input = sys.stdin.readline

n, k = map(int, input().split())
*a, = map(int, input().split())

s = [0]*(n+1)
for i in range(len(a)):
    s[i+1] = s[i] + a[i]
for i in range(len(s)):
    s[i] = (s[i] - i)%k

from collections import defaultdict
cnt = defaultdict(int)

left = 0
right = k-1
if right > n:
    right = n

for i in range(right+1):
    cnt[s[i]] += 1

ans = 0
while left < right:
    ans += cnt[s[left]]-1
    if right == n:
        cnt[s[left]] -= 1
        left += 1
    else:
        cnt[s[left]] -= 1 
        left += 1
        right += 1
        cnt[s[right]] += 1 

print(ans)
