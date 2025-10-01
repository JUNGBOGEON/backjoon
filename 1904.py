import sys

tail_input = int(sys.stdin.readline())
memo = {}

def dp(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    memo[n] = dp(n-1) + dp(n-2)
    return memo[n]

print(dp(tail_input))
