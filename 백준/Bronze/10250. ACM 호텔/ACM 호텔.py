T = int(input())

for _ in range(T) :
    h = 1
    a,b,c = map(int,input().split())
    while a < c :
        c -= a
        h += 1
    if h < 10 :
        answer = str(c) + '0' + str(h)
    else :
        answer = str(c) + str(h)
    print(answer)