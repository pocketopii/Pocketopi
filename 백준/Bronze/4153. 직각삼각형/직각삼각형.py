A,B,C = map(int, input().split())

while A != 0 and B != 0 and C != 0 : 
    if A >= B and A >= C : 
        if A**2 == B**2 + C**2 :
            print("right")
        else : 
            print("wrong")
    elif B >= A and B >= C :
        if B**2 == A**2 + C**2 :
            print("right")
        else : 
            print("wrong")
    else : 
        if C**2 == A**2 + B**2 :
            print("right")
        else : 
            print("wrong")
    A,B,C = map(int, input().split())