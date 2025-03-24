N = input().strip()  # 입력받은 문자열의 앞뒤 공백 제거

# 공백을 기준으로 문자열을 나누고 단어의 개수를 세기
words = N.split()
print(len(words))