# S = input()

# n = len(S) - 1


# def calc(S, mask):
#     formula = ''
#     for i in range(n):
#         formula += S[i]
#         if mask[i] == '1':
#             formula += '+'
#     formula += S[-1]
#     return sum(map(int, formula.split('+')))


# ans = 0
# for i in range(2**n):
#     mask = format(i, f'0{n}b')
#     ans += calc(S, mask)

# print(ans)

s = list(input())

op_cnt = len(s)-1
sum = 0
for i in range(2**op_cnt):
    op = ['']*op_cnt
    for j in range(op_cnt):
        if (i >> j) & 1:
            op[j] = '+'

    fomula = s[0]
    for j in range(op_cnt):
        fomula += op[j]
        fomula += s[j+1]

    sum += eval(fomula)

print(sum)
