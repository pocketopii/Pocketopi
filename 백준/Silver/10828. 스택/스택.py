import sys
N = int(input())
stack = []

for _ in range(N) : 
    a = list(sys.stdin.readline().strip().split())
    if a[0] == "push" : 
        stack.append(a[1])
    elif a[0] == "pop" :
        if len(stack) == 0 : 
            print(-1)
        else :
            pops = stack.pop()
            print(pops)
    elif a[0] == "size" : 
        print(len(stack))
    elif a[0] == "empty" : 
        if len(stack) == 0 : 
            print(1)
        else : 
            print(0)
    else : 
        if len(stack) == 0 : 
            print(-1)
        else : 
            print(stack[len(stack) - 1])