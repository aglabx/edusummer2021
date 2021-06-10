import sys


def equation(a, b, c):
    # sqrt(a*x + b) = c
    if c < 0:
        return 'NO SOLUTION'
    if a == 0 and b < 0:
        return 'NO SOLUTION'
    if a == 0 and b != c ** 2:  # b >= 0
        return 'NO SOLUTION'
    if a == 0 and b == c ** 2:
        return 'MANY SOLUTIONS'
    return f'{(c ** 2 - b) / a}'


a_, b_, c_ = map(int, sys.stdin.read().strip().split('\n'))

sys.stdout.write(equation(a_, b_, c_))
