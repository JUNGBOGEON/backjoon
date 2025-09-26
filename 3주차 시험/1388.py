import sys

row, column = map(int, sys.stdin.readline().split())
wood_list = []
count = 0

for i in range(row):
    wood_list.append(list(map(str, sys.stdin.readline().rstrip())))

# for i in range(row):
stack = 0
for j in range(column):
    try:
        if wood_list[i][j+stack] == wood_list[i][j+stack+1]:
            stack += 1
        else:
            count += 1
    except:
        pass

print(stack)

# 문제가, 배열의 행과 열의 연속성을 검사하는건데 어떤식으로?
# 그래프 이론인 이유가 있지 않을까

# 0번째 인덱스와 1번 인덱스를 비교한다.

# (1 if) 일치하지 않는 경우, count + 1 (종료)

# (1 if) 일치할 경우, 1번 인덱스와 2번 인덱스를 비교한다
# (1 if) 일치할 경우, 2번 인덱스와 3번 인덱스를 비교한다.
