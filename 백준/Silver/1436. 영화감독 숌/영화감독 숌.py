N = int(input())
count = 0
number = 666

while 1 :
    if '666' in str(number) :
        count += 1

    if N == count :
        print(number)
        break
    number += 1