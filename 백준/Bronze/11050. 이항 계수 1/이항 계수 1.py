N,K = map(int, input().split())
answer = 1

for i in range(K) :
    answer *= N - i
    answer //= i + 1

print(int(answer))