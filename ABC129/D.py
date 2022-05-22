import sys 
input = sys.stdin.readline

h, w = map(int, input().split())
s = [list(input().replace('\n', '')) for _ in range(h)]

import numpy as np


up = np.zeros((h, w))
down = np.zeros((h, w))
right = np.zeros((h, w))
left = np.zeros((h, w))

s = (np.array(s)==".").astype(np.int)

for i in range(h):
    down[-i-1] = (down[-i] + 1)*s[-i-1]
    up[i] = (up[i-1] + 1)*s[i]
    

for i in range(w):
    left[:,-i-1] = (left[:,-i] + 1)*s[:,-i-1]
    right[:,i] = (right[:,i-1] + 1)*s[:,i]
    
ans = np.max(up+down+left+right-3)
print(int(ans))