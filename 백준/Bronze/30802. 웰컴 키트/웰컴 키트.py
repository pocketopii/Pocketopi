n = int(input())
size = list(map(int, input().split()))
shirt,pen = map(int, input().split())

re_shirt = 0
for i in size : 
    re_shirt += (i + shirt - 1) // shirt
print(re_shirt)

print(n//pen, n%pen)