lst = []
leng = []
for _ in range(5) : 
    a = input()
    leng.append(len(a))
    lst.append(a)
    
max_len = max(leng)

for i in range(max_len) : 
    for j in range(5) : 
        if i < leng[j]:
            print(lst[j][i], end='')
        else:
            print('', end='')