a = set()
for _ in range(10) :
    b = int(input())
    a.add(b%42)

print(len(a))