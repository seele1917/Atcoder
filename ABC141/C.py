n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

temp = [0] * n
for i in range(q):
    temp[a[i]-1] += 1

for i in range(n):
    temp[i] += k-q
    if temp[i]>0:
        print('Yes')
    else:
        print('No')
    