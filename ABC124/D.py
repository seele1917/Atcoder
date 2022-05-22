import sys
input =  sys.stdin.readline

n, k = map(int, input().split())
s = input()+'-1'

cnt = 0
cnt_list = []
for i in range(n):
    if s[i] == s[i+1]:
        cnt += 1
    else:
        cnt_list.append(cnt+1)
        cnt = 0

# print(cnt_list)


l = 0
r = 2*k
ma = 0
su = 0
if s[0] == '0':
    r = 2*k
else:
    r = 2*k+1
su = sum(cnt_list[l:r])
while l < r:
    if ma < su:
        ma = su
    if l == 0 and r == 2*k:
        l += 1
        su -= cnt_list[l-1]
    else:
        l += 2
        su -= sum(cnt_list[l-2:l])
    r += 2
    su += sum(cnt_list[r-2:r])
    if r >= len(cnt_list):
        r = len(cnt_list)
    
print(ma)
