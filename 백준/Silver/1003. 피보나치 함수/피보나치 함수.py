N = int(input())

for _ in range(N) : 
    lis = [1, 2]
    tmp = int(input())
    if tmp == 0 : 
        print("1 0")
    elif tmp == 1 : 
        print("0 1")
    elif tmp == 2 : 
        print("1 1")
    else : 
        for _ in range(tmp - 3) : 
            temp = lis[0] + lis[1]
            lis[0] = lis[1]
            lis[1] = temp
        print(lis[0],lis[1])