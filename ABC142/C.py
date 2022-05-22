n = int(input())
*a, = map(int, input().split())

import numpy as np
a = np.array(a)
a_sort = np.argsort(a)
a_sort = a_sort + 1

print(*a_sort)