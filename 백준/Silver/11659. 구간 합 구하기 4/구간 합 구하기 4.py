import sys
data = sys.stdin.read().strip().splitlines()

a, b = map(int, data[0].split())
num = list(map(int, data[1].split()))

sum_num = [0] * (a + 1)
for i in range(1, a + 1):
    sum_num[i] = sum_num[i - 1] + num[i - 1]

for j in range(2, 2 + b):
    sm, bg = map(int, data[j].split())
    print(sum_num[bg] - sum_num[sm - 1])
