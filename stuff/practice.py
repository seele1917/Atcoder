import numpy as np

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

xy = np.array(xy)

print(np.linalg.norm(xy[0]-xy[1]))

# # 2点のユークリッド距離を求めるメソッド（何次元でも対応）
# import math
# def get_distance(p1, p2):
#     distance = 0
#     for i in range(2):
#         distance += (p1[i]-p2[i])**2
#     distance = math.sqrt(distance)
#     return distance



# max_len = 0
# for i in xy:
#     for j in xy:
#         if i != j:
#             len = get_distance(i, j)
#             if max_len < len:
#                 max_len = len

# print(max_len)



