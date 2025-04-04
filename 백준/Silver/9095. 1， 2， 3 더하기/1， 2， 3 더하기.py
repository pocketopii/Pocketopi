from collections import deque

N = int(input())

for _ in range(N) : 
    queue = deque()
    M = int(input())
    count = 0
    queue.append(M)

    while len(queue) != 0 : 
        a = queue.popleft()
        if a >= 3 : 
            queue.append(a-3)
            queue.append(a-2)
            queue.append(a-1)
        elif a == 2 : 
            queue.append(a-2)
            queue.append(a-1)
        elif a == 1 :
            queue.append(a-1)
        else : 
            count += 1
    print(count)