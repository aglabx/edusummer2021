import sys


def is_triangle(first, second, third):

    triangle_inequality = all((first < second + third,
                               second < first + third,
                               third < first + second))

    return 'YES' if triangle_inequality else 'NO'


a, b, c = map(int, sys.stdin.read().strip().split('\n'))
sys.stdout.write(is_triangle(a, b, c))
