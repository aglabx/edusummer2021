import sys


def equation(a, b, c):
    # sqrt(a*x + b) = c
    if c < 0:
        return "NO SOLUTION"
    if a == 0:
        return "MANY SOLUTIONS" if c ** 2 == b else "NO SOLUTION"
    x = (c ** 2 - b) / a
    return f'{int(x)}' if x.is_integer() else "NO SOLUTION"


a_, b_, c_ = map(int, sys.stdin.read().strip().split('\n'))
sys.stdout.write(equation(a_, b_, c_))
