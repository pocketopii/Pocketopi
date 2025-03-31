N, K = map(int,input().split())
money = []

for _ in range(N) :
    tmp = int(input()) 
    money.append(tmp)

answer = 0
for i in money[::-1] : 
    if K//i > 0 :
        answer += K//i
        K -= (K//i) * i
    else :
        continue
print(answer)