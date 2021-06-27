import sys


def finder(array, x):
    print(sorted(array, key=lambda y: abs(x - y))[0])


n_ = int(sys.stdin.readline().strip())
array_ = tuple(map(int, sys.stdin.readline().split()))
x_ = int(sys.stdin.readline().strip())
finder(array_, x_)