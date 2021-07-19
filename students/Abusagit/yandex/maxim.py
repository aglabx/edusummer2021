import sys


def get_freq_range(initial, frequencies):
    left = 30.0
    right = 4000.0
    prev = initial
    for freq, comment in frequencies:
        expression = round((freq + prev) / 2, 6)
        if comment == "further":
            if freq > prev:
                right = min(right, expression)
            else:
                left = max(left, expression)
        else:
            if freq > prev:
                left = max(left, expression)
            else:
                right = min(right, expression)
        prev = freq

    return left, right


n = int(sys.stdin.readline().strip())
initial_ = float(sys.stdin.readline().strip())
others = ((float(i.split()[0]), i.split()[1]) for i in sys.stdin.readlines())

print(*get_freq_range(initial_, others))