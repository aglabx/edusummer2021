import sys


def prefix(s) -> list:
    """
    Creates prefix function for KMP algorithm
    """
    P = [0 for _ in range(len(s))]
    i, j = 0, 1
    while j < len(s):
        if s[i] == s[j]:
            P[j] = i + 1
            i += 1
            j += 1
        # s[i] != s[j]
        elif i:  # i > 0
            i = P[i - 1]
        else:
            P[j] = 0
            j += 1
    return P


def refactor_for_symmetry(length, array):
    for i in range(length):
        start = i
        j = length - 1
        while i < length and j >= 0 and array[i] == array[j]:
            i += 1
            j -= 1
        if j < i:
            additionals = [array[i] for i in range(start - 1, -1, -1)]
            yield (len(additionals), )
            yield additionals
            return
    yield (0,)


length_, *array_ = map(int, sys.stdin.read().strip().split())
for part in refactor_for_symmetry(length_, array_):
    print(*part)
