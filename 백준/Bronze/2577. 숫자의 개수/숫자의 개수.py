A = int(input())
B = int(input())
C = int(input())
answer = list(str(A*B*C))

for i in range(0,10) : 
    print(answer.count(str(i)))