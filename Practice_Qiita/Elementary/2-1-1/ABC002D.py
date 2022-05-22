import itertools
import numpy as np

N, M = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(M)]


def check(mask):
    check_mask = True
    mask = np.array(list(mask))
    idx = np.where(mask == '1')[0]
    for x, y in itertools.combinations(idx, 2):
        if [x+1, y+1] not in xy:
            check_mask = False
            break
    return check_mask


cnt = 0
for i in range(2 ** N):
    bit = format(i, f'0{N}b')
    if check(bit):
        cnt = max(cnt, bit.count('1'))

print(cnt)
