import sys
input = sys.stdin.readline

n = int(input())
*a, = map(int, input().split())

if len(set(a)) == n:
    print('YES')
else:
    print('NO')