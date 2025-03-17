N,M = map(int, input().split())
nums = list(map(int,input().split()))
passed = []

for i in range(N - 2) : 
    for j in range(i + 1, N - 1) : 
        for m in range(j + 1, N) : 
            if nums[i] + nums[j] + nums[m] <= M :
                passed.append(nums[i] + nums[j] + nums[m])
max = 0
for n in passed : 
    if n >= max :
        max = n

print(max)