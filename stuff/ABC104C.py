d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]

ans_num = 1000000
for i in range(2**d):
    bit = format(i,'0'+str(d)+'b')
    score = 0
    ans = 0
    for j in range(d):
        if bit[j] == '1':
            score += pc[j][1] + 100*pc[j][0]*(j+1)
            ans += pc[j][0]
    if score >= g:
        if ans < ans_num:
            ans_num = ans
    else:
        for j in range(d-1, -1, -1):
            if bit[j] == '0':
                p, c = pc[j]
                for k in range(p):
                    score += 100 * (j + 1)
                    ans += 1
                    if score >= g:
                        break
                else:
                    continue
                break
        if score >= g and ans < ans_num:
            ans_num = ans

print(ans_num)