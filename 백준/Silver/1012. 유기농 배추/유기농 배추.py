import sys
from collections import deque

input = sys.stdin.read
data = input().strip().splitlines()

n = int(data[0])
line = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(n):
    a, b, c = map(int, data[line].split())
    line += 1

    farm = [[0] * a for _ in range(b)]
    for _ in range(c):
        x, y = map(int, data[line].split())
        farm[y][x] = 1
        line += 1

    count = 0
    for i in range(b):
        for j in range(a):
            if farm[i][j] == 1:
                queue = deque()
                queue.append((i, j))
                farm[i][j] = 0

                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < b and 0 <= ny < a and farm[nx][ny] == 1:
                            farm[nx][ny] = 0
                            queue.append((nx, ny))

                count += 1

    print(count)
