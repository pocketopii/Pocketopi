import re

a = input()
tokens = re.split(r'(\+|\-)', a)
answer = 0
temp = 0
open = False
re_open = False
for i in tokens : 
    if i == "+" :
        pass
    elif i == "-" and open == False :
        open = True
    elif i == "-" and open == True : 
        pass
    else : 
        i = int(i)
        if open == True : 
            answer -= i
        else : 
            answer += i


print(answer)