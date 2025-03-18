while 1 :
    i = int(input())
    if i == 0 :
        break

    i = str(i)
    if i == i[::-1] :
        print("yes")
    else :
        print("no")