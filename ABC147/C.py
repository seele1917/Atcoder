import sys
input = sys.stdin.readline

n = int(input())
xys = []
for _ in range(n):
    a = int(input())
    xy = [list(map(int, input().split())) for _ in range(a)]
    xys.append(xy)


def bc(x):
    return bin(x).count("1")

ans = 0
for i in range(2**n):
    is_ok = True
    for j in range(n):
        if (i>>j) & 1:
            for x, y in xys[j]:
                if ((i>>(x-1)) & 1) != y :
                    is_ok = False
                    break
    if is_ok:
        cnt = bc(i)
        if ans < cnt:
            ans = cnt
print(ans)
    
