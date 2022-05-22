import sys
input = sys.stdin.readline

n = int(input())
s = input().replace('\n', '')

ans = ''
for i in range(len(s)):
    ch = (ord(s[i])+n)
    if ch > ord('Z'):
        ch -= 26
    ans += chr(ch) 
print(ans)

