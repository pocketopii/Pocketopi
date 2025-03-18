A, B, V = map(int, input().split())

distance = V - A

if distance <= 0:
    print(1)
else:
    days = (distance + (A - B) - 1) // (A - B) + 1
    print(days)