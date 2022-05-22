import sys
input = sys.stdin.readline

x = int(input())

two_bit = x%100
five = two_bit//5
two_bit-= 5*five
if two_bit==0:
    amari = 0
else:
    amari = 1
if (five+amari) <= x//100:
    print(1)
else:
    print(0)