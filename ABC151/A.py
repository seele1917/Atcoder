import sys
input = sys.stdin.readline

c = input().split()[0]
ans = (ord(c)+1)%ord('a') + ord('a')
ans = chr(ans)
if c == 'z':
    print('a')
else:
    print(ans)