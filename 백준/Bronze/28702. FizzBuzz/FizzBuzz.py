num = []
for i in range(3) :
    a = input()
    try:
        a = int(a)  # 정수로 변환 가능 시
        if i == 0:
            num.append(a)
            num.append(a + 1)
            num.append(a + 2)
        elif i == 1:
            num.append(a - 1)
            num.append(a)
            num.append(a + 1)
        else:
            num.append(a - 2)
            num.append(a - 1)
            num.append(a)
        break

    except ValueError : #불가능 시
        continue

answer = num[2]+1
if answer % 3 == 0 and answer % 5 == 0 :
    print("FizzBuzz")
elif answer % 3 == 0 and answer % 5 != 0 :
    print("Fizz")
elif answer % 3 != 0 and answer %5 == 0 :
    print("Buzz")
else :
    print(answer)