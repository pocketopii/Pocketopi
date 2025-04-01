N = int(input())
M = list(input())
i = 0
while len(M) > 1 :
    i += 1
    if M[N - i] == M[N - i - 1] :
        M.pop()
    elif M[N - i - 1] == "A" : 
        if M[N - i] == "G" : 
            M.pop()
            M[-1] = "C"
        elif M[N - i] == "C" : 
            M.pop()
        else : 
            M.pop()
            M[-1] = "G"
    elif M[N - i - 1] == "G" : 
        if M[N - i] == "A" : 
            M.pop()
            M[-1] = "C"
        elif M[N - i] == "C" : 
            M.pop()
            M[-1] = "T"
        else : 
            M.pop()
            M[-1] = "A"    
    elif M[N - i - 1] == "C" : 
        if M[N - i] == "A" : 
            M.pop()
            M[-1] = "A"
        elif M[N - i] == "G" : 
            M.pop()
            M[-1] = "T"
        else : 
            M.pop()
            M[-1] = "G"
    else : 
        if M[N - i] == "A" : 
            M.pop()
            M[-1] = "G"
        elif M[N - i] == "G" : 
            M.pop()
            M[-1] = "A"
        else : 
            M.pop()
            M[-1] = "G"

for i in M :
    print(i)