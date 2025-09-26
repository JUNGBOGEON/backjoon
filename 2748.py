import sys

fibonacci_input = int(sys.stdin.readline())

def fibonacci(number) -> int:
    array = [0, 1]
    counting = 0

    if number < len(array):
        return array[number]
    else:
        while number >= len(array):
            next_array = array[counting] + array[counting + 1]
            array.append(next_array)
            counting += 1
    
    return array[number]

print(fibonacci(fibonacci_input))
