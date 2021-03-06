import sys
input = sys.stdin.readline

a, b = map(int, input().split())


#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

print(lcm(a, b))