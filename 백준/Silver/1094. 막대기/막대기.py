x = int(input())
answer = 0
while x != 0:
    if x >= 64:
        x -= 64
        answer += 1
    elif x >= 32:
        x -= 32
        answer += 1
    elif x >= 16:
        x -= 16
        answer += 1
    elif x >= 8:
        x -= 8
        answer += 1
    elif x >= 4:
        x -= 4
        answer += 1
    elif x >= 2:
        x -= 2
        answer += 1
    else:
        x -= 1
        answer += 1

print(answer)
