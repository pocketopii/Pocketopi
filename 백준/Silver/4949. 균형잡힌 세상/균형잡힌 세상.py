while 1:
    i = input()
    if i == ".":
        break
    else:
        sol = []
        for j in i:
            if j == "(" or j == ")" or j == "[" or j == "]":
                sol.append(j)

    while True:
        try:
            flag = False
            for i in range(len(sol) - 1):
                if sol[i] == "(" and sol[i + 1] == ")":
                    sol.pop(i)
                    sol.pop(i)
                    flag = True
                    break
                elif sol[i] == "[" and sol[i + 1] == "]":
                    sol.pop(i)
                    sol.pop(i)
                    flag = True
                    break

            if not flag:
                break
        except:
            break
        
    if sol == []:
        print("yes")
    else:
        print("no")
