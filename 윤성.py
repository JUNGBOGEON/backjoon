import sys
input = sys.stdin.readline

cabinet = []
n = int(input())
for _ in range(n):
    start, end = map(int, input().strip().split())
    cabinet.append((start, end))

cabinet.sort(key = lambda x: (x[1], x[0]))

cnt_meeting = 0
end_time = 0

for meeting_times in cabinet:
    if meeting_times[0] >= end_time:
        cnt_meeting += 1
        end_time = meeting_times[1]

print(cnt_meeting)
