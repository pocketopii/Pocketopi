N = int(input())
arr = [[0]* 2 for _ in range(N)]

for i in range(N) : 
    a,b = map(int,input().split())
    arr[i] = [a,b]

arr.sort(key = lambda x : (x[1],x[0]))
for a,b in arr:
    print(a,b)