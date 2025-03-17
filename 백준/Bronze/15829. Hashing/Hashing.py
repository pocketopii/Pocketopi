N = int(input())
M = str(input())
M_num = []

for i in M : 
    M_num.append(ord(i) - ord('a') + 1)

count = 0
total = 0
for j in M_num :
    total += j * 31**count
    count += 1

print(total%1234567891)