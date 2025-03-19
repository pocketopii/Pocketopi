n = int(input())
words = []
for i in range(n) : 
    a = input()
    words.append(a)
words = list(dict.fromkeys(words))

words.sort(key = lambda x :(len(x),x))

for i in words :
    print(i)