N = int(input())
listN = list(range(1, N+1))

if N == 1:
    print(1)
else:
    while len(listN) > 1:
        # 짝수 길이일 때
        if len(listN) % 2 == 0:
            listN = [listN[i] for i in range(1, len(listN), 2)]
        # 홀수 길이일 때
        else:
            listN = [listN[i] for i in range(1, len(listN), 2)]
            a = listN[0]
            listN = listN[1:] + [a]

    print(listN[0])
