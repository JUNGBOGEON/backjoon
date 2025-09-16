import sys
stack = []
command_count = int(sys.stdin.readline())

for _ in range(0, command_count):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if len(stack) != 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif command[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

# push 1
# push 2
# [1, 2]

# top
# 2 (stack 의 맨 마지막꺼 출력) 

# size
# 2 (현재 stack 의 크기)

# 비어있나요? 아니면 0
# 0 

# -1 
# 0 
# 1 
# -1
# 0 
# 3
