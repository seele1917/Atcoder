# 迷路をグラフにする：本質的に深さ優先探索
import itertools as it
import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
S = [list(input().split()[0]) for _ in range(H)]

def isWall(s):
    return 1 if s == '#' else 0

def getWalls(arr, i, j):
    return isWall(arr[i+1][j]) + isWall(arr[i-1][j]) + isWall(arr[i][j+1]) + isWall(arr[i][j-1])

def getEdge(arr, i, j, edges, v, c):
    for (a,b) in zip([1,-1,0,0], [0,0,1,-1]):
        if isWall(arr[i+a][j+b]) == 0:
            arr[i+a][j+b] = '#'
            if arr[i+2*a][j+2*b] == 0:
                vn = v
                cn = c + 1
            else:
                vn = arr[i+2*a][j+2*b]
                edges.append((v, vn, c))
                cn = 1
            getEdge(arr, i+2*a, j+2*b, edges, vn, cn)

vs = 0
edges = list()
arr = S
height = len(arr)
width = len(arr[height - 1])
cellidi = range(1,width,2)
cellidj = range(1,height,2)
for i,j in it.product(cellidi, cellidj):
    if getWalls(arr, i, j) == 2:
        arr[i][j] = 0
    elif arr[i][j] == '.':
        vs += 1
        arr[i][j] = vs

# 今回のデータ用の設定
print(getEdge(arr, 0, 0, edges, 1, 1))