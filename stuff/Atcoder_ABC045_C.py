s = list(input())

op_cnt = len(s)-1
sum = 0
for i in range(2**op_cnt):
    op = ['+']*op_cnt
    for j in range(op_cnt):
        if (i>>j) & 1:
            op[j] = '-' 

    fomula = s[0]
    for j in range(op_cnt):
        fomula += op[j]
        fomula += s[j+1]
    
    if eval(fomula) == 7:
        print('{}=7'.format(fomula))
        break

