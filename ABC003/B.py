import numpy as np

n = int(input())
*s, = [input() for _ in range(n)]

s_reverse = [word[::-1] for word in s]
ans_index = np.argsort(s_reverse)

for i in ans_index:
    print(s[i])