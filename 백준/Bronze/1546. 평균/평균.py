N = int(input())
score = list(map(int, input().split()))

total = 0
max = 0
for i in score : 
    total += i
    if max < i : 
        max = i

avg = total/max*100 / N
print(avg)