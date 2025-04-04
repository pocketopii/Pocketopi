import sys
from collections import deque

data = sys.stdin.read().strip().splitlines()
T = int(data[0])

for i in range(T):
    n, m = map(int, data[i * 2 + 1].split())
    priorities = list(map(int, data[i * 2 + 2].split()))
    
    queue = deque([(p, idx) for idx, p in enumerate(priorities)])
    count = 0

    while queue:
        cur = queue.popleft()
        if any(cur[0] < other[0] for other in queue):
            queue.append(cur)
        else:
            count += 1
            if cur[1] == m:
                print(count)
                break
