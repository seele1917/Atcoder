import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

temp = [1, 2, 3]
if a in temp:
    temp.remove(a)
if b in temp:
    temp.remove(b)
print(temp[0])