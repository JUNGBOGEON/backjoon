# https://www.acmicpc.net/problem/2805

n = list(map(int, input().split()))
tree = list(map(int, input().split()))
M = n[1]

def tree_binary_search(target, data):
    start = 0
    end = max(data)

    while start <= end:
        mid = (start + end) // 2

        count = 0
        for h in data:
            if h > mid:
                count += h - mid

        if count >= target:
            start = mid + 1
        else:
            end = mid - 1

    return end

print(tree_binary_search(M, tree))
