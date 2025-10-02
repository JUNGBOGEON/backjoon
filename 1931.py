import sys

class MeetingRoom:
    def __init__(self):
        self.rooms = []

    def add_room(self, start, end):
        self.rooms.append((start, end))

    def max_rooms(self):
        self.rooms.sort(key=lambda x: (x[1], x[0]))
        count, last_end = 0, 0
        for start, end in self.rooms:
            if start >= last_end:
                count += 1
                last_end = end
        return count

n = int(sys.stdin.readline())
room = MeetingRoom()

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    room.add_room(start, end)

print(room.max_rooms())
