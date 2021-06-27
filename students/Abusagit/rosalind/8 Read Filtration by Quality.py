from functools import reduce


def get_incorrect_phred(file):
    with open(rf"D:\Downloads\{file}.txt") as f_read:
        threshold, percentage = map(int, f_read.readline().split())

        a = f_read.readlines()
        filtered = 0

        for i in range(3, len(a), 4):
            qualities = [ord(char) - 33 for char in a[i].strip()]
            filt = reduce(lambda x, y: x + (y >= threshold), qualities, 0) / len(qualities) * 100
            filtered += filt >= percentage

    return filtered

if __name__ == '__main__':
    print(get_incorrect_phred(input()))