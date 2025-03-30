import sys

data = sys.stdin.read().strip().splitlines()

N , M = map(int, data[0].split())

n = set(data[1:N+1])
m = set(data[N+1:])

answer = sorted(n&m)

print(len(answer))
for name in answer:
    print(name)