import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pS = [input().split()[:2] for _ in range(m)]

AC = [0]*n
WA = [0]*n

for p, S in pS:
    p = int(p)
    if AC[p-1] == 0:
        if S == 'AC':
            AC[p-1] = 1
        else:
            WA[p-1] += 1

for i in range(n):
    if WA[i] > 0 and AC[i] == 0:
        WA[i] = 0
print(sum(AC), sum(WA))