import sys

s1 = list(map(str, sys.stdin.readline().rstrip()))
s2 = list(map(str, sys.stdin.readline().rstrip()))

result = []
s2_state = 0

for i in range(len(s1)):
    
    s2_state_start = s2_state

    while len(s2) > s2_state_start:
        try:
            if s1[i] == s2[s2_state_start]:
                result.append(s1[i])
                s2_state += s2_state_start + 1
                break
            else:
                s2_state_start += 1
        except:
            break

print(result)
