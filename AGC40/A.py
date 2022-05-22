import sys
input = sys.stdin.readline
import numpy as np

s = input()[:-1]

cnts = []

tmp = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        tmp += 1
    else:
        if s[i] == '>':
            tmp *= -1
        cnts.append(tmp)
        tmp = 1

if s[-1] == '>':
    tmp *= -1
cnts.append(tmp)

idx = 0
a = [0] * (len(s)+1)

for i in range(len(cnts)):
    if i != 0 and cnts[i-1] > 0 and cnts[i] < 0 and a[idx-1] >=  abs(cnts[i]):
        a[idx] = a[idx-1] + 1

    for j in range(abs(cnts[i])):
        if a[idx] != 0:
            idx += 1
            continue
        if cnts[i] > 0:
            a[idx] = j
        else:
            a[idx] = abs(cnts[i]) - j
        idx += 1
if s[-1] == '<':
    a[-1] = a[-2] + 1

# print(*cnts)
# print(*a)
print(sum(a))
# for i in range(len(s)):
#     print(a[i],s[i],end='')
# print(a[-1])
