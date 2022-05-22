import sys
input = sys.stdin.readline

s = input().split()[0]

for i in range(1, 6):
    if 'hi'*i == s:
        print('Yes')
        break
else:
    print('No')