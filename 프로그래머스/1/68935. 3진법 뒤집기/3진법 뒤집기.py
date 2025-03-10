def solution(n):
    answer = ""
    m = 1
    start = 0
    
    #3진법 자리수 구하기 (1 3 9 27 81...)
    while m <= n : 
        start += 1
        m *= 3
        
    #3진법 구하기
    for i in range(start - 1, -1, -1) :
        temp = n // 3**i
        n -= 3**i * temp
        answer = answer + str(temp)

    #10진법으로 바꾸기
    answer2 = 0
    for i in range(len(answer)) : 
        answer2 += int(answer[i]) * (3**i)
        
    
    return answer2