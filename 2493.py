import sys

top_count = int(sys.stdin.readline())
top_list = list(map(int, sys.stdin.readline().split()))
top_result = []

top_main_count = 0
top_sub_count = 0

for i in range(len(top_list)):
    main_index = -(top_main_count + 1)
    sub_index = -(1 + top_sub_count) + main_index

    # print(f'{i} for 문 분기점\nmain_index: {main_index}\n sub_index: {sub_index}\n top_list[main_index]: {top_list[main_index]}\n top_list[sub_index]: {top_list[sub_index]}\ntop_sub_count: {top_sub_count}')

    if main_index == -len(top_list):
        top_result.append(0)
    elif sub_index == -len(top_list):
        top_result.append(0)
    
    if top_list[main_index] < top_list[sub_index]:
        # print(f'{i} if 문 분기점\nmain_index: {main_index}\n sub_index: {sub_index}\n top_list[main_index]: {top_list[main_index]}\n top_list[sub_index]: {top_list[sub_index]}\ntop_sub_count: {top_sub_count}')
        top_result.append(top_list.index(top_list[sub_index]) + 1)
        top_sub_count = 0
        top_main_count += 1
    elif top_list[main_index] > top_list[sub_index]:
        top_sub_count += 1

top_result.append(0)
top_result.reverse()
print(*top_result)
# 지금 문제가, 만약 7 < 5 같은 결론이 나왔을때,
# 5 오른쪽으로 이동하고 9 를 찾는 로직이 필요하고
# 다시 5로 이동할 수 있어야됨

# 7 보다 큰 수를 찾기 위한 인덱스 카운터가 필요하고
# 현재 차례를 기억하기 위한 인덱스 카운터도 필요함

# 4보다 큰 숫자 먼저 찾기
# 7이기 때문에 7의 위치인 4 저장

# 7보다 큰 숫자 찾기
# 5는 작기때문에 건너뛰기
# 9가 크기 때문의 9의 위치인 2 저장

# 5보다 큰 숫자 찾기
# 9가 크기 때문에 9의 위치인 2 저장

# 9보다 큰 숫자 찾기
# 9보다 큰 숫자는 없기 때문에
# 0 저장

# 마지막 숫자는 항상 0 저장
