import sys


def seq_type(sequence):
    if len(set(sequence)) <= 1:
        return "CONSTANT"

    ascending = True
    descending = True
    weakness = False

    previous = sequence[0]
    for i in range(1, len(sequence)):
        weakness |= sequence[i] == previous
        ascending &= sequence[i] >= previous
        descending &= sequence[i] <= previous
        previous = sequence[i]

    if ascending:
        return "WEAKLY ASCENDING" if weakness else "ASCENDING"
    if descending:
        return "WEAKLY DESCENDING" if weakness else "DESCENDING"
    return "RANDOM"


stdin = list(map(float, sys.stdin.readlines()))
print(seq_type(stdin[:-1]))
