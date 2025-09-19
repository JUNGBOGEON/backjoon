# 첫째 줄에는 카드 갯수
# 두번째 줄에는 가지고 있는 카드
# 세번쨰 줄에는 확인해야 하는 카드 갯수
# 네번째 줄에는 확인해야 하는 카드
import sys

my_card = int(sys.stdin.readline())
my_card_list = set(map(int, sys.stdin.readline().split()))
check_card = int(sys.stdin.readline())
check_card_list = list(map(int, sys.stdin.readline().split()))
result = []

for i in range(len(check_card_list)):
    if check_card_list[i] in my_card_list:
        result.append(1)
    else:
        result.append(0)

print(*result)
