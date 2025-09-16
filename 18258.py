import sys
from collections import deque

stack = deque()
command_count = int(sys.stdin.readline())

for _ in range(0, command_count):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if len(stack) != 0:
            print(stack[0])
            stack.popleft()
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif command[0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
