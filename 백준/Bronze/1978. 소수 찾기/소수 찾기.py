import math

N = int(input())

num = list(map(int,input().split()))
count = 0
for i in num : 
    if i == 1 :
        continue
    elif i == 2 or i == 3 : 
        count += 1
    else : 
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1) : 
            if i % j == 0 :
                is_prime = False
                break
        if is_prime :
            count += 1

print(count)