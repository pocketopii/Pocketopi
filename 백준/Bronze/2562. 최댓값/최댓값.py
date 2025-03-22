count = 1
max = int(input())

for i in range(2,10) : 
    temp = int(input())
    if temp > max :
        max = temp 
        count = i

print(max)
print(count)