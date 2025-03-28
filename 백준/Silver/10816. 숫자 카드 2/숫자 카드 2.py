N = int(input())

p_card = [0] * 10000001
m_card = [0] * 10000001

card = list(map(int, input().split()))
for i in card : 
    if i >= 0 : 
        p_card[i] += 1
    else : 
        m_card[i] += 1

M = int(input())
my_card = list(map(int, input().split()))
for i in my_card : 
    if i >= 0 : 
        print(p_card[i], end = " ")
    else :
        print(m_card[i], end = " ")