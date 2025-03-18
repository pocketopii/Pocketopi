N = int(input())
apart = [[0] * 15 for _ in range(15)]

for i in range(1,15) :
    apart[0][i] = i

for i in range(1,15) :
    for j in range(1,15) : 
        apart[i][j] = apart[i-1][j] + apart[i][j-1]


for i in range(N) : 
    floor = int(input())
    room = int(input())
    print(apart[floor][room])