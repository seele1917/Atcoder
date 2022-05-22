A, B, C = map(int, input().split())

isA = False
if C == 0:
    if A > B:
        isA = True
    else:
        isA = False
else:
    if B > A:
        isA = False
    else:
        isA = True

if isA:
    print('Takahashi')
else:
    print('Aoki')
