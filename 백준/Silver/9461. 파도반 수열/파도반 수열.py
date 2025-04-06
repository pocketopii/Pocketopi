N = int(input())
lst = [1,1,1,2,2,3,4,5]

for i in range(8,101) : 
    lst.append(lst[i - 1] + lst[i-5])

for _ in range(N) : 
    a = int(input())
    print(lst[a-1])