from collections import deque

n, k = map(int, input().split())
devies = deque(map(int, input().split()))
p = [0]*n
replace_count = 0  # 뽑은 횟수

while devies:
    current = devies.popleft()

    if current in p:
        # 이미 꽂혀 있으면 패스
        continue

    # 빈 슬롯 있으면 그냥 꽂기
    if 0 in p:
        idx = p.index(0)
        p[idx] = current
        continue

    # 멀티탭이 꽉 찼고, current가 없음 → 교체 필요
    latest_index = -1
    idx_to_replace = -1

    for i in range(n):
        try:
            # 앞으로 다시 등장하는 인덱스 확인
            next_use = devies.index(p[i])
        except ValueError:
            # 안 쓰이면 바로 교체 대상
            idx_to_replace = i
            break
        # 가장 늦게 등장하는 기기 찾기
        if next_use > latest_index:
            latest_index = next_use
            idx_to_replace = i

    # 기기 교체
    p[idx_to_replace] = current
    replace_count += 1

print(replace_count)
