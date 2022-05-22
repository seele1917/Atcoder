s = input()

idx = 0
ans = [0 for _ in range(len(s))]

if s.find('R') == -1:
    ans[0] = len(s)
elif s.find('L') == -1:
    ans[len(s)-1] = len(s)
else:
    while(idx<=len(s)-1):
        lr_idx = idx
        if s[idx] == 'R':
            lr_idx = s.find('L', idx)
        elif s[idx] == 'L':
            lr_idx = s.find('R', idx)

        
        num = lr_idx - idx

        if s[idx] == 'R':
            if lr_idx == -1:
                ans[len(s)-1] += len(s) - idx
            else:
                ans[lr_idx] += num//2
                ans[lr_idx-1] += num//2
                if num%2 == 1:
                    ans[lr_idx-1] += 1

        elif s[idx] == 'L':
            if lr_idx == -1:
                num = len(s) - idx
            if idx>0:
                ans[idx] += num//2
                ans[idx-1] += num//2
                if num%2 == 1:
                    ans[idx] += 1
            else:
                ans[0] += num
                
        idx = lr_idx
        if lr_idx == -1:
            break

for i in ans:
    print(i, end=' ')

      