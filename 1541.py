import sys
import re

number = sys.stdin.readline()
token = re.findall(r'\d+|[+-]', number)

# - 가 나온 순간부터, 그 뒤 숫자들은 모두 더해버린다.
# for 문을 돌려서 - 값을 찾는데
# 찾았다면 - 왼쪽에 있는 값은 냅두고, 
# 오른쪽에 있는 값들은 + 기준으로 모두 더하기
# 못찾았다면 모두 + 라는 거니, 모두 더하고 출력
# 그리고 '00009' 같은 불쾌한 골짜기 수식 수정

minus = []
plus = []

for i in range(len(token)):
    if token[i] == '-':
        # 반복문을 통해서 i - 1을 계속 한다음에 0 이기 전까지 계속 넣기
        while (i - 1) >= 0:
            
        
        


print(token)
