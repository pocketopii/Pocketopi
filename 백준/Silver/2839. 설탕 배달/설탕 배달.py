N = int(input())
count = 0
while 1 :
    if N == 1 or N == 2 or N == 4 :
        print(-1)
        break
    elif N == 3 : 
        count += 1
        print(count)
        break
    elif N == 5 :
        count += 1
        print(count)
        break
    elif N == 6 :
        count += 2
        print(count)
        break
    elif N == 9 :
        count += 3
        print(count)
        break
    elif N == 12 :
        count += 4
        print(count)
        break
    else :
        count += 1
        N -= 5