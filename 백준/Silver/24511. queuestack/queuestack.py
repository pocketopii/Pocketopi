from collections import deque

N = int(input())
stqu = list(map(int, input().split()))
lists = list(map(int, input().split()))
putN = int(input())
putlist = list(map(int, input().split()))

queue = deque()

for i in range(N-1,-1,-1): 
    if stqu[i] == 0:
        queue.append(lists[i])

for i in putlist: 
    queue.append(i)
    a = queue.popleft()
    print(a, end=" ")
