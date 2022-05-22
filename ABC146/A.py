import sys
input = sys.stdin.readline

s = input()

date = [ 'SUN','MON','TUE','WED','THU','FRI','SAT' ]

ans = date.index(s.replace("\n", ''))
print(7-ans)