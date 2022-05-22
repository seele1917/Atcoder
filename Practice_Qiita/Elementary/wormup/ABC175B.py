import itertools

N = int(input())
*L, = map(int, input().split())

ans = 0
for l1, l2, l3 in itertools.combinations(L, 3):
    if l1 == l2 or l2 == l3 or l1 == l3:
        continue
    if l1 + l2 > l3 and abs(l1 - l2) < l3:
        ans += 1

print(ans)
