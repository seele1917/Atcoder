import copy
import fractions
a, b = map(int, input().split())

temp = fractions.gcd(a, b)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

d = make_divisors(temp)
d.sort()

for ele in d:
    if ele==1:
        continue
    d = [e for e in d if e%ele!=0 or ele==e] 

print(len(d))
# print(len(ans)+1)