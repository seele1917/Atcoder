n, y = map(int, input().split())

for i in range(n+1):
    for j in range(n+1-i):
        k = n - (i + j)
        if 10000*i + 5000*j + 1000*k == y:
            print('{} {} {}'.format(i, j, k))
            break
    else:
        continue
    break
else:
    print('-1 -1 -1')