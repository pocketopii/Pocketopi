import sys
N = int(input())
M = int(input())
data = sys.stdin.read().strip().splitlines()

for i in range(M) : 
    data[i] = list(map(int, data[i].split()))
    data[i].sort()

answer = set([1])
prev_size = 0


while len(answer) != prev_size:
    prev_size = len(answer)
    for a, b in data:
        if a in answer or b in answer:
            answer.update([a, b])

print(len(answer) - 1)