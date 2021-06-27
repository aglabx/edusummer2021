import sys
from functools import reduce


def get_incorrect_phred(file):
    with open(rf"D:\Downloads\{file}.txt") as f_read:
        threshold = int(f_read.readline())

        a = f_read.readlines()
        qualities = [None for _ in range(len(a) // 4)]
        for i in range(3, len(a), 4):
            qualities[i // 4] = sum(ord(char) - 33 for char in a[i].strip()) // len(a[i].strip())

        return reduce(lambda x, y: x + (y < threshold), qualities, 0)


if __name__ == '__main__':
    print(get_incorrect_phred(input()))