N = list(input())

op_num = 3

for i in range(2**op_num):
    op = ['-'] * op_num
    for j in range(op_num):
        if (i >> j) & 1:
            op[j] = '+'

    formula = N[0]
    for j in range(op_num):
        formula += op[j] + N[j+1]

    if eval(formula) == 7:
        print(formula+'=7')
        break
