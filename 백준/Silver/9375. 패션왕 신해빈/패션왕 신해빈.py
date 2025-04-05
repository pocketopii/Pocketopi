import sys

data = sys.stdin.read().strip().splitlines()
N = int(data[0])
n = 1

# 테스트 케이스 별로
for _ in range(N):
    M = int(data[n])
    cloth = {}
    
    for i in range(n + 1, n + M + 1):
        a, b = data[i].split()
        if b not in cloth:
            cloth[b] = 1
        else:
            cloth[b] += 1

    result = 1
    for count in cloth.values():
        result *= (count + 1)

    result -= 1  # 아무것도 안 입는 경우 제외
    print(result)

    n += M + 1  # 다음 테스트케이스
