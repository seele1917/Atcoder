n = int(input())
*h, = map(int, input().split())

for i in range(n-1, 0, -1):
    if h[i] >= h[i-1]:
        continue
    elif h[i-1]-h[i] == 1:
        h[i-1] -= 1
    else:
        print('No')
        break
else:
    print('Yes')



