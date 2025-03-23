N = int(input())
n = list(map(int, input().split()))

min = n[0]
max = n[0]

for i in range(1,N) :
    if min > n[i] :
        min = n[i]
    elif max < n[i] :
        max = n[i]

print(min, max)