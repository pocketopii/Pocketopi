import sys

N, M = map(int, input().split())
pokemon_dic = {}
pokemon_list = []

for i in range(1, N + 1) : 
    a = sys.stdin.readline().strip()
    pokemon_dic[a] = i
    pokemon_list.append(a)

for _ in range(M) : 
    a = input()
    try : 
        a = int(a)
        print(pokemon_list[a - 1])
    except : 
        print(pokemon_dic[a])