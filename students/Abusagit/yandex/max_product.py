import sys
import itertools

def max_double_product(array):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for value in array:
        if value >= max2:
            max1 = max2
            max2 = value
        elif max1 < value < max2:
            max1 = value

    for value in array:
        if value <= min2:
            min1 = min2
            min2 = value
        elif min1 > value > min2:
            min1 = value

    return (max1, max2) if max1 * max2 > min1 * min2 else (min2, min1)


def max_triple_product(array):
    max1 = 0
    max2 = 1
    max3 = 2
    min1 = 0
    min2 = 1
    min3 = 2

    for index, value in enumerate(array):
        if array[max3] <= value:
            max1 = max2
            max2 = max3
            max3 = index
        elif array[max2] <= value < array[max3]:
            max1 = max2
            max2 = index
        elif array[max1] <= value < array[max2]:
            max1 = index

    for index, value in enumerate(array):
        if array[min3] >= value:
            min1 = min2
            min2 = min3
            min3 = index
        elif array[min2] >= value > array[min3]:
            min1 = min2
            min2 = index
        elif array[min1] >= value > array[min2]:
            min1 = index

    unique_values = list(array[i] for i in tuple({min1, min2, min3, max1, max2, max3}))
    print(unique_values)
    combinations = itertools.combinations(unique_values, 3)

    return max(combinations, key=lambda x: x[0] * x[1] * x[2])




arr = tuple(map(int, sys.stdin.read().strip().split()))

# print(*max_double_product(arr))
# a = -28 44 -27 -14 19 27 -22 36 28 -7 -20 -39 41 53 53 -27 20 -25 -16 -43 -53 -51 7
# -26 37 26 -49 -3 -34 24 -22 7 26 46 -43 -23 47 -26 37 41 -41 -6 11 29 28 -31 31 -5
print(*max_triple_product(arr))


def stupid(array):
    print(max(itertools.combinations(array, 3), key=lambda x: x[0] * x[1] * x[2]))


stupid(arr)
