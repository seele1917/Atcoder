import sys
import re
input = sys.stdin.readline

a, b, c = [input().split()[0] for _ in range(3)]

a = a.replace('?', '.')
b = b.replace('?', '.')
c = c.replace('?', '.')

a_ma = '.'*(len(b)-1) + a + '.'*(len(b)-1)
result = re.finditer(re.compile(a_ma), re.compile(c))

print(a_ma, list(result))

for m in result:
    print(m)