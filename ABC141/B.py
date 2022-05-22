s = input()

temp = True
for i in range(1,len(s),2):
    if s[i] == 'L' or s[i] == 'U' or s[i] == 'D':
        continue
    else:
        temp = False
for i in range(0,len(s),2):
    if s[i] == 'R' or s[i] == 'U' or s[i] == 'D':
        continue
    else:
        temp = False
if temp:
    print('Yes')
else:
    print('No')