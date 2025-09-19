# 만약 mirkovC4nizCC44 에서 C4 를 모두 없엔다고 했을때
# mirkovniz 를 출력해야 한다.

import sys

text_list = sys.stdin.readline()
boom_text = sys.stdin.readline().rstrip()
result = ''

for i in text_list:
    if i not in boom_text:
        result += (i)

if len(result) == 0:
    print('FRULA')
else:
    print(result)
