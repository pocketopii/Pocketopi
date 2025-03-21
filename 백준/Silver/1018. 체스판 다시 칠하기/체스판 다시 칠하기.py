import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
min_change = 63

#시작점
for i in range(n-7) :
    for j in range(m-7) : 
        startw = 0
        startb = 0
        for a in range(i,i+8) :
            for b in range(j,j+8) :
                now = board[a][b]
                if (a + b) % 2 == 0:
                    if now != 'W':
                        startw += 1
                    if now != 'B':
                        startb += 1
                else:
                    if now != 'B':
                        startw += 1
                    if now != 'W':
                        startb += 1

        min_change = min(min_change, startw, startb)

print(min_change)