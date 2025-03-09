def solution(s):
    answer = ''
    s = s.lower()
    if 'a' <= s[0] <= 'z' : 
        answer += s[0].upper()
    else : 
        answer += s[0]

    for i in range(1, len(s)) : 
        if s[i - 1] == " " and 'a' <= s[i] <= 'z' : 
            answer += s[i].upper()
        else : 
            answer += s[i]
    
    return answer