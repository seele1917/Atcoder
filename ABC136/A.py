a, b, c = map(int, input().split())
ans = c - (a-b)
print(ans if ans>=0 else 0)