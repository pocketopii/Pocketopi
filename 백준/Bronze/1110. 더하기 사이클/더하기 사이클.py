N = int(input())
original = N
cnt = 0

while True:
    a = N // 10
    b = N % 10
    c = a + b
    N = b * 10 + c % 10
    cnt += 1
    if N == original:
        print(cnt)
        break