def get_incorrect_phred(file):
    with open(rf"D:\Downloads\{file}.txt") as f_read:
        threshold = int(f_read.readline())

        a = f_read.readlines()

        below = 0
        for i in range(len(a[1].strip())):
            qualities = sum(ord(a[j][i]) - 33 for j in range(3, len(a), 4)) / (len(a) // 4)

            below += qualities < threshold

    return below


if __name__ == '__main__':
    print(get_incorrect_phred(input()))
