import sys

N = int(input())
num = []
avg = 0

frq = {}

for i in range(N) : 
    a = int(sys.stdin.readline().strip())
    if len(num) == 0 :
        max_value = a
        min_value = a
    else :
        if min_value > a :
            min_value = a
        elif max_value < a :
            max_value = a

    num.append(a)
    avg += a

    if a in frq : 
        frq[a] += 1
    else : 
        frq[a] = 1

num.sort()

#산술 평균
print(int(round(avg/N,0)))

#중앙값
print(num[N//2])

#최빈값 (같을 시 두 번째로 작은 값)
max_frq = max(frq.values())
most_frq = []
for key, value in frq.items():
    if value == max_frq:
        most_frq.append(key)

#2개 이상
if len(most_frq) > 1 :
    most_frq.sort()
    print(most_frq[1])
#1개
else : 
    print(most_frq[0])

#범위
print(max_value - min_value)