N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]

ans = 0
for i in range(2**K):
    bit = format(i, f'0{K}b')

    pattern_list = [0] * N
    for j in range(K):
        idx = CD[j][int(bit[j])] - 1
        pattern_list[idx] = 1

    cnt = 0
    for A, B in AB:
        if pattern_list[A-1] and pattern_list[B-1]:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
