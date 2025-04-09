import heapq
import sys
data = sys.stdin.read().strip().splitlines()
n = int(data[0])
hq = []

for i in range(1,n+1) : 
    a = int(data[i])
    #0
    if a == 0 : 
        if len(hq) == 0 : 
            print(0)
        else : 
            a = heapq.heappop(hq)
            print(a)
    #0이 아닌 양수
    else : 
        heapq.heappush(hq, a)