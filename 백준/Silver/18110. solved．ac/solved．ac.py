import math
import sys

def custom_round(n):
    if n % 1 >= 0.5:
        return math.ceil(n)
    else:
        return math.floor(n)

N = int(sys.stdin.readline().strip())
cut = custom_round(N*0.15)

if N == 0 :
    print(0)
else : 
    arr = []
    for i in range(N):
        arr.append(int(sys.stdin.readline().rstrip()))

    arr.sort()
    arr = arr[cut : len(arr) - cut]

    avg = custom_round(sum(arr) / len(arr))
    print(avg)