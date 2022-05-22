import sys
input = sys.stdin.readline

n = int(input())
s = input()

if n%2 == 0:
    if s[:n//2] == s[n//2:n]:
        print("Yes")
    else:
        print("No")
else:
    print('No')