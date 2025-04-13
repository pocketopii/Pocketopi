while 1 : 
    a = input()
    cnt = 0
    if a == '#' : 
        break
    else : 
        a = list(a)
        for i in a : 
            if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u' : 
                cnt += 1
        print(cnt)