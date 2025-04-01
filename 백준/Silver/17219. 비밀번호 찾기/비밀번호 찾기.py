import sys

data = sys.stdin.read().strip().splitlines()
find = {}
N,M = map(int, data[0].split())

for i in range(1,N+1) : 
    a,b = data[i].split()
    find[a] = b

for i in range(N+1,N+M+1) :
    tmp = data[i]
    print(find[tmp])