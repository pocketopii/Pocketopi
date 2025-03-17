N = int(input())

def sum_of_digits(x):
    return sum(map(int, str(x)))

min = 0
for i in range(N, 0, -1) : 
    if i + sum_of_digits(i) == N : 
        min = i

print(min)