import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, max(n+1, 11)):
    if (n/i)%1 == 0:
        if 1 <= n//i <= 9 and 1 <= i <= 9:
            print("Yes")
            break
else:
    print("No")