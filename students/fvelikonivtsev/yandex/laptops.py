import sys


def optimize(a, b, c, d):
    squares1 = {
        (a + c) * max(b, d): (a + c, max(b, d)),
        (a + d) * max(b, c): (a + c, max(b, c)),
        (b + c) * max(a, d): (b + c, max(a, d)),
        (b + d) * max(a, c): (b + d, max(a, c))
    }
    a, b = (b, a) if a < b else (a, b)
    c, d = (d, c) if c < d else (c, d)
    a, b, c, d = (c, d, a, b) if a * b < c * d else (a, b, c, d)
    print(a, b, c, d)
    squares2 = {
        (a + c) * max(b, d): (a + c, max(b, d)),
        (a + d) * max(b, c): (a + c, max(b, c)),
        (b + c) * max(a, d): (b + c, max(a, d)),
        (b + d) * max(a, c): (b + d, max(a, c))
    }
    print(squares1.items(), squares2.items())
    return min(squares1[min(squares1.keys())], squares2[min(squares2.keys())])


a, b, c, d = map(int, sys.stdin.readline().strip().split())

print(*optimize(a, b, c, d))
