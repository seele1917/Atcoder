n = int(input())
*h, = map(int, input().split())

max_num = 0
temp = 0
for i in range(n-1):
    if h[i]>=h[i+1]:
        temp += 1
    else:
        if max_num < temp:
            max_num = temp
        temp = 0

print(max(max_num, temp))