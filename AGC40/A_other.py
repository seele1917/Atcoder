import sys
input = sys.stdin.readline

s = input()[:-1]

a = [0]*(len(s)+1)
l = [0]*len(a)
r = [0]*len(a)

for i in range(1, len(a)):
    if s[i-1] == '<':
        l[i] = l[i-1] + 1
        
for i in range(len(a)-2, -1, -1):
    if s[i] == '>':
        r[i] = r[i+1] + 1

for i in range(len(a)):
    a[i] = max(l[i], r[i])

print(sum(a))