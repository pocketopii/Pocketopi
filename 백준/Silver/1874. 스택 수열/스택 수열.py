import sys

data = list(map(int,sys.stdin.read().strip().splitlines()))
stack = []
num = list(range(data[0],0,-1))
answer = []

for i in data[1:] : 
    #num pop / stack push
    while not stack or stack[-1] < i : 
        stack.append(num.pop())
        answer.append('+')
    
    if stack and stack[-1] == i:
        stack.pop()
        answer.append('-')
        
    else:
        answer = ["NO"]
        break

sys.stdout.write("\n".join(answer) + "\n")