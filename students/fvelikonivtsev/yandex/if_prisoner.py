import sys


def escape(a, b, c, d, e):
    hole = d * e

    min_size = min((
        a * b,
        b * c,
        c * a
    ))

    return "YES" if hole >= min_size else "NO"


def escape2(a, b, c, d, e):
    sizes = sorted((a, b, c))
    size1, size2 = sizes[0], sizes[1]
    return "YES" if any((size1 <= d and size2 <= e, size1 <= e and size2 <= d)) else "NO"


A, B, C, D, E = map(int, sys.stdin.read().strip().split('\n'))
print(escape2(A, B, C, D, E))
