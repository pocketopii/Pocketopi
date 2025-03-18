A,B = map(int,input().split())

if A >= B : 
    min_num = B
    max_num = A
else :
    min_num = A
    max_num = B

i = 2
dlist = []
while i <= min_num : 
    if max_num % i == 0 and min_num % i == 0 : 
        max_num /= i
        min_num /= i
        dlist.append(i)
        i = 2
    else : 
        i += 1

dlist.sort()
gcd = 1
for i in dlist :
    gcd *= i

print(gcd)
print(int(A*B/gcd))