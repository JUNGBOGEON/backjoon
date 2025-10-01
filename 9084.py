import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    
    coin_cases = int(sys.stdin.readline())
    coin_list = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())

    print(coin_cases)
    print(coin_list)
    print(target)
