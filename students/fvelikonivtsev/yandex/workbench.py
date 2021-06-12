import sys
import random


def details(n, k, m):
    mass = n
    parts_per_piece = k // m
    if parts_per_piece:
        while mass >= k:
            mass -= parts_per_piece * (mass // k) * m
        return (n - mass) // m
    return 0


if __name__ == '__main__':
    # n, k, m = map(int, sys.stdin.readline().strip().split())
    # print(details(n, k, m))
    def test():
        while True:
            a, b, c = (random.randint(1, 200) for _ in range(3))
            print(f'Testing {a, b, c}........')
            details(a, b, c)
            print('Done!!!!!!!!!!!!!!!!')


    test()
