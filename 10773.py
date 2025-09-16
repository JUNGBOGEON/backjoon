import sys

economy = int(sys.stdin.readline())
economy_stack = []

for _ in range(economy):
    try_economy = int(sys.stdin.readline())
    if try_economy == 0:
        economy_stack.pop()
    else:
        economy_stack.append(try_economy)

if len(economy_stack) == 0:
    print(0)
else:
    count = 0
    for i in range(len(economy_stack)):
        count += economy_stack[i]
    print(count)
