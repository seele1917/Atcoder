import sys
input = sys.stdin.readline

n, k = map(int, input().split())
*p, = map(int, input().split())

*p, = map(lambda x:(x+1)/2, p)

# r, l = 0, 0
# su = 0
# ans = 0
# while r < n:
#     if r - l >= k-1:
#         su -= p[r]
#         r += 1
#         ans = max(ans, su)
#     else:
#         l += 1
#         su += p[l]
su = sum(p[:k])
ans = su
for i in range(k, n):
    su += p[i]
    su -= p[i-k]
    ans = max(su, ans)

print(ans)