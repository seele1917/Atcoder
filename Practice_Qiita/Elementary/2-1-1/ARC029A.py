N = int(input())
T = [int(input()) for _ in range(N)]

time = float('inf')
for i in range(2**N):
    bit = format(i, f'0{N}b')
    c = [0, 0]
    for j in range(N):
        c[int(bit[j])] += T[j]

    time = min(time, max(c))
print(time)
