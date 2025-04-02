N = int(input())
score = []
dp = []
for _ in range(N) : 
    a = int(input())
    score.append(a)

dp.append(score[0])

if N >= 2 : 
    dp.append(score[0] + score[1])

if N >= 3 : 
    if score[0] + score[2] > score[1] + score[2] :
        dp.append(score[0]+score[2])
    else : 
        dp.append(score[1]+score[2])

if N >= 4 :
    for i in range(3,N) : 
        if dp[i-2] + score[i] > dp[i-3] + score[i-1] + score[i] : 
            dp.append(dp[i-2] + score[i])
        else :
            dp.append(dp[i-3] + score[i-1] + score[i])

print(dp[-1])