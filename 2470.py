# import bisect

# N = input()
# input_arr = list(map(int, input().split()))
# negative = []
# positive = []
# count_dict = {}

# for idx in range(len(input_arr)):
#     if 0 > input_arr[idx]:
#         negative.append(input_arr[idx])
#     elif 0 <= input_arr[idx]:
#         positive.append(input_arr[idx])

# negative.sort()
# positive.sort()

# if 0 == len(positive):
#     print(negative[-1], negative[-2])
# elif 0 == len(negative):
#     print(positive[0], positive[1])
# else:
#     for i in range(len(negative)):
#         count_dict[f'{negative[i]} {positive[bisect.bisect_left(positive, -negative[i])-1]}'] = f'{negative[i] + positive[bisect.bisect_left(positive, -negative[i])-1]}'

#     minimum_arr = min(list(count_dict.values()))

#     for key, value in count_dict.items():
#         if 0 == value:
#             print(key)
#         elif minimum_arr == value:
#             print(key)

from sys import stdin
input = stdin.readline
N = int(input())
solution = sorted(list(map(int, input().split())))

start, end = 0, N-1
ans = abs(solution[start] + solution[end])
final = [solution[start], solution[end]]

while start < end:
    left = solution[start]
    right = solution[end]
    sum = left + right
    if abs(sum) < ans:
        ans = abs(sum)
        final = [left, right]
        if ans == 0:
            break
    if sum < 0:
        start += 1
    else:
        end -= 1

print(final[0], final[1])
