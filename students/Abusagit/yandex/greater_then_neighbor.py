import sys


def greater_then_to_neares(array):
    count = 0
    i = 1
    while i < len(array) - 1:
        if array[i - 1] < array[i] > array[i + 1]:
            count += 1
            i += 2
        else:
            i += 1
    print(count)


array_ = tuple(map(float, sys.stdin.read().strip().split()))
greater_then_to_neares(array_)
