import sys
input = sys.stdin.read

def solve():
    data = input().splitlines()
    
    N = int(data[0])  # first list의 크기
    first_list = set(map(int, data[1].split()))  # first list를 set으로 변환
    
    M = int(data[2])  # second list의 크기
    second_list = list(map(int, data[3].split()))  # second list
    
    result = []
    for num in second_list:
        if num in first_list:
            result.append("1")
        else:
            result.append("0")
    
    sys.stdout.write("\n".join(result) + "\n")

solve()
