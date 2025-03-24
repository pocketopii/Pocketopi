N = int(input())

for _ in range(N) : 
    temp = list(input())
    if len(temp) % 2 == 1 :
        print("NO")
    else : 
        i = 0
        while 1 : 
            try : 
                flag = False
                for i in range(len(temp) - 1) :
                    if temp[i] == "(" and temp[i+1] == ")" :
                        temp.pop(i)
                        temp.pop(i)
                        flag = True
                        break
                
                if not flag :
                    break
            except:
                break
    
        if len(temp) == 0 :
            print("YES")
        else :
            print("NO")
