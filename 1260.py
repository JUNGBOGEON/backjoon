import sys
from collections import defaultdict

node, edge, startNum = map(int, sys.stdin.readline().split())
world = defaultdict(list)

for i in range(edge):
    parent, child = map(int, sys.stdin.readline().split())
    world[parent].append(child)

# def depth_first_search(world):
#     visited = []

#     # world 의 작은 값을 가져오기
#     # if visited 의 이미 있는 값인가? 맞다면 건너뛰기

#     # 아니라면 visited 의 추가하고, 
#     # 작은 작은 값의 자식 중에 제일 작은 자식 보기

#     # 제일 작은 자식도 visited 의 있나 확인
#     # 만약 맞다면 건너뛰고, 아니라면 visited 추가

#     # 해결해야될거
#     # 1. 반복 조건? 부모와 자시

world_list = []

for key, value in world.items():
    world_list.append(key)
    world_list.append(value)

print(set(world_list))

# depth_first_search(world)
