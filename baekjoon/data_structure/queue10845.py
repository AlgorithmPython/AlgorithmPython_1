import sys


count = int(input()) # 명령어 개수 받기
data = [(sys.stdin.readline()) for i in range(count)]

stack = []

for x in data:
    x = x.strip()
    if(x[0:4] == 'push'):
        num = int(x[5:])
        stack.append(num)
    elif(x == 'pop'):
        if stack:
            print(stack.pop(0)) # 가장 앞에 것을 삭제 가능
        else:
            print(-1)
    elif(x == 'size'):
        print(len(stack))
    elif(x == 'empty'):
        if not stack:
            print(1)
        else:
            print(0)
    elif(x == 'front'):
        if stack:
            print(stack[0])
        else:
            print(-1)    
    
    elif(x == 'back'):
        if stack:
            print(stack[-1])
        else:
            print(-1)    