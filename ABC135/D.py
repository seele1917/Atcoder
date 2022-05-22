s = list(input())

mod = 10**9 + 7

N = 13
dp = [0]*N
dp[0] = 1
mul = 1
for i in range(len(s)-1, -1, -1):
    nextDP = [0]*N
    if s[i] == '?':
        for k in range(10):
            for j in range(N):
                nextDP[(k*mul + j)%N] += dp[j]
                nextDP[(k*mul + j)%N] %= mod
    else:
        k = int(s[i])
        for j in range(N):
            nextDP[(k*mul + j)%N] += dp[j]
            nextDP[(k*mul + j)%N] %= mod

    mul = (mul*10)%N
    dp = nextDP

print(dp[5])

上下関係
古きよきにほん
上下関係がストレス（正しいことを否定される）
テクノロジー（ブロックチェーン）これからくるテクノロジーに対してついていかなければ
エンジニアリング

商社　若い　ジェネレーション
三菱（　NYに視点　情報をバイアス

リクルートだめなとこ
メンバーの連携，起業家の集合体
PDCAサイクル回す，
メール，細かい作業，
いい塩梅，

ボトムアップ
信頼残高　信頼
