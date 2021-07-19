from collections import Counter


def dna_stats(string):
    stats = Counter()
    for base in string:
        stats[base] += 1
    return stats['A'], stats['C'], stats['G'], stats['T']


if __name__ == '__main__':
    name = input()
    with open(fr"D:\Downloads\{name}.txt") as f_read:
        dna = f_read.read().strip()
        print(*dna_stats(dna))