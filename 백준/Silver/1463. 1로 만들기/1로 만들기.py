N = int(input())

answer = 0
num = [0,0,1,1]

for i in range(4,N + 1) : 
    count = 1
    while 1 : 
        if i % 3 == 0 and i % 2 == 0 : 
            i = min(num[i//2], num[i//3], num[i-1]) + count
            num.append(i)
            break
        elif i % 3 == 0 : 
            i = min(num[i//3], num[i-1]) + count
            num.append(i)
            break
        elif i % 2 == 0 : 
            i = min(num[i//2], num[i-1]) + count
            num.append(i)
            break
        else : 
            count += 1
            i -= 1

print(num[N])