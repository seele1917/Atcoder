n = int(input())
a = [int(input()) for _ in range(n)]

a_sort = sorted(a, reverse=True)

for ele in a:
    if ele==a_sort[0]:
        print(a_sort[1])
    else:
        print(a_sort[0])