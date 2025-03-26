N = int(input())

for _ in range(N) : 
    a,b = input().split()
    a = int(a)
    b = list(b)
    for i in range(len(b)) : 
        print(b[i]*a, end="")
    print()