import sys

# 입력 처리
coin_index, coin_target = sys.stdin.readline().split()
coin_list = []
for _ in range(int(coin_index)):
    coin_input = int(sys.stdin.readline())
    if int(coin_target) >= coin_input:
        coin_list.append(coin_input)

stack = 0
stack_coin = 0

# 만약 현재 stack_coin 이 4000원이고
# 타켓 코인이 4800원 일때
# max 값이 1000원을 추가했을때, 타겟 코인을 넘는다면
# 1000원 을 지우고, 다시 max 값 찾기

while int(coin_target) > stack_coin:
    max_coin_list = coin_list[-1]
    if int(coin_target) >= (stack_coin + max_coin_list):
        stack_coin += max_coin_list
        stack += 1
    elif int(coin_target) < (stack_coin + max_coin_list):
        del coin_list[-1]
    
print(stack)
