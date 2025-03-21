import sys
 
m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 1:
        if cmd[0] == "all":
            S = set([i for i in range(1, 21)])
        else:   # empty
            S = set()
    else:
        cmd, num = cmd[0], cmd[1] 
        num = int(num)
        if cmd == "add":
            S.add(num)
        elif cmd == "remove":
            S.discard(num)
        elif cmd == "check":
            print(1 if (num in S) else 0)
        elif cmd == "toggle":
            S.discard(num) if (num in S) else S.add(num)
