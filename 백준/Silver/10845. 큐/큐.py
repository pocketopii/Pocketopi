import sys
from collections import deque

data = sys.stdin.read().strip().splitlines()
N = int(data[0])
queue = deque()

for i in range(1, N + 1) : 
    temp = data[i]
    try : 
        a,b = temp.split()
        
        queue.append(b)

    except : 
        if temp == 'pop' : 
            if len(queue) == 0 :
                print(-1)
            else : 
                a = queue.popleft()
                print(a)
        elif temp == "size" : 
            print(len(queue))
        elif temp == "empty" : 
            if len(queue) == 0 :
                print(1)
            else :
                print(0)
        elif temp == "front" : 
            if len(queue) == 0 : 
                print(-1)
            else : 
                print(queue[0])
        else :
            if len(queue) == 0 : 
                print(-1)
            else : 
                print(queue[len(queue) - 1])
