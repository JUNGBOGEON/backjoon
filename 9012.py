import sys

vps_count = int(sys.stdin.readline())

for i in range(vps_count):
    vps_list = list(map(str, sys.stdin.readline()))
    vps_opening_count = 0
    vps_closing_count = 0
    stop_code = 0

    for i in range(len(vps_list)):
        if vps_opening_count < vps_closing_count:
            print('NO')
            stop_code = 1
            break
        elif '(' == vps_list[i]:
            vps_opening_count += 1
        elif ')' == vps_list[i]:
            vps_closing_count += 1

    if stop_code == 1:
        continue
    elif vps_opening_count == vps_closing_count:
        print('YES')
    else:
        print('NO')
