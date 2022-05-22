import sys
input = sys.stdin.readline

n = int(input())

def rec(s, kind):
    if len(s) == n:
        print(s)
        return
    for i in range(kind+1):
        end = chr(ord('a')+i)
        if i < kind:
            rec(s+end, kind)
        else:
            rec(s+end, kind+1) 

rec('a', 1)