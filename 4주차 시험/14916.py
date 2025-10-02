import sys

change = int(sys.stdin.readline())

def change_exp(change):
    if change in (1, 3):
        return -1

    count = 0; amount = 0
    
    while change >= amount + 5:
        amount += 5; count += 1
    
    while change != amount:
        while change >= amount + 2:
            amount += 2; count += 1
        if change != amount:
            if count == 0:
                return -1
            amount -= 5; count -= 1
    return count

print(change_exp(change))
