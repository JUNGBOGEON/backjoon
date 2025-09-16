import sys

stick_heigth_count = int(sys.stdin.readline())
stick_heigth_stack = []

for _ in range(stick_heigth_count):
    stick_heigth_stack.append(int(sys.stdin.readline()))

last_number = stick_heigth_stack[-1]
count = 1

for i in range(len(stick_heigth_stack)):
    if last_number > stick_heigth_stack[-(i+1)]:
        continue
    elif last_number < stick_heigth_stack[-(i+1)]:
        last_number = stick_heigth_stack[-(i+1)]
        count += 1

print(count)
