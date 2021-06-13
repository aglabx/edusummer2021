import sys
import math


def trains(a, b, n, m):
    # check if line 1 is wrong:
    if (b * (m - 1) + m - 1) / math.floor(a + 1) <= n <= (b * m + m - 1) / math.ceil(a + 1):
        print('1 case')
        return f'{-1}'
    # check if line 2 is wrong:
    if (a * (n - 1) + n - 1) / math.floor(b + 1) <= m <= (a * n + n - 1) / math.ceil(b + 1):
        print('2 case')
        return f'{-1}'
    minimal = max(n + a * (n - 1), m + b * (m - 1))
    maximum = max(a * n + (n - 1), b * m + (m - 1))

    return f"{minimal} {maximum}"


def trains2(a, b, n, m):
    minimum = max(n + a * (n - 1), m + b * (m - 1))
    maximum = min(n + a * (n + 1), m + b * (m + 1))
    return f"{minimum} {maximum}" if minimum <= maximum else f'{-1}'


a, b, n, m = map(int, sys.stdin.read().strip().split('\n'))
sys.stdout.write(trains2(a, b, n, m))
