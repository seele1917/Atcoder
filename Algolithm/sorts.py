import sys
input = sys.stdin.readline
import random
import time
sys.setrecursionlimit(2000)

n = int(input())
a = list(range(n))
random.shuffle(a)
# print(a)

def bubble_sort(a):
    l = len(a)
    for i in range(l):
        for j in range(l-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

def select_sort(a):
    l = len(a)
    for i in range(l-1):
        tmp = a.index(min(a[i:]))
        a[i], a[tmp] = a[tmp], a[i]

def inter_sort(a):
    l = len(a)
    for i in range(1, l):
        for j in range(i, 0, -1):
            if a[j] > a[j-1]:
                break
            else:
                a[j], a[j-1] = a[j-1], a[j]

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[-1]
    l = [x for x in a[:-1] if x<=pivot]
    r = [x for x in a[:-1] if x>pivot]
    quick_sort(l)
    quick_sort(r)
    a[:] = l + [pivot] + r

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    l = merge_sort(a[:mid])
    r = merge_sort(a[mid:])
    return merge(l, r)

def merge(l, r):

    n = len(l+r)
    s = max(l+r)+1

    l += [s]
    r += [s]

    a = []
    while len(a) < n:
        if l[0] <= r[0]:
            a.append(l.pop(0))
        else:
            a.append(r.pop(0))
    return a

start = time.time()
# bubble_sort(a)
# select_sort(a)
# inter_sort(a)
# quick_sort(a)
a = merge_sort(a)
end = time.time()
print(a)
print(end-start)