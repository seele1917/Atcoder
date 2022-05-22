import sys
input = sys.stdin.readline

s = input()[:-1]
if s[-1] == 's':
    print(s + 'es')
else:
    print(s + 's')