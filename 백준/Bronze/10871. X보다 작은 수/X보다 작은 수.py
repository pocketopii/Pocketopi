A,X = map(int,input().split())

nums = list(map(int,input().split()))

answer = []
for i in range(A) : 
    if nums[i] < X :
        answer.append(nums[i])

result = ' '.join(map(str, answer))
print(result)