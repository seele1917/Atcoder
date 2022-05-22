import sys
input = sys.stdin.readline
import itertools

n = int(input())
*p, = map(int, input().split())
*q, = map(int, input().split())

l = list(range(1, n+1))
l = list(itertools.permutations(l))
a = l.index(tuple(p))
b = l.index(tuple(q))

print(abs(a-b))