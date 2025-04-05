H, W = map(int, input().split())
wall = list(map(int, input().split()))

land = [[0 for _ in range(W)] for _ in range(H)]

for x in range(W):
    for y in range(H - 1, H - wall[x] - 1, -1):
        land[y][x] = 1

answer = 0
for y in range(H):
    for x in range(W):
        if land[y][x] == 0:
            left = any(land[y][k] == 1 for k in range(0, x))
            right = any(land[y][k] == 1 for k in range(x + 1, W))
            if left and right:
                answer += 1

print(answer)
