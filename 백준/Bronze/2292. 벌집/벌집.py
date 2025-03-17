N = int(input())

room = 1
max = 1
count = 1

while max < N:
    max += 6 * count
    room += 1
    count += 1

print(room)