def get_incorrect_phred(file):
    with open(rf"D:\Downloads\{file}.txt") as f_read, open(rf"filtered{file}.fastaq", 'w') as f_write:
        cut_off = int(f_read.readline())
        lines = iter(f_read.readlines())
        while lines:
            try:
                print(next(lines), end='', file=f_write)  # print seq name
                sequence = next(lines).strip()
                delimiter = next(lines)  # '+'
                quality = next(lines).strip()

                i = 0
                j = len(sequence) - 1
                while all((i < len(sequence), j >= 0, i < j,
                           ord(quality[i]) - 33 < cut_off or ord(quality[j]) - 33 < cut_off)):
                    i += (ord(quality[i]) - 33) < cut_off
                    j -= (ord(quality[j]) - 33) < cut_off
                print(i, j)
                print(sequence[i:j + 1], file=f_write)
                print(delimiter, file=f_write, end='')
                print(quality[i:j + 1], file=f_write)
            except StopIteration:
                break
    print("DONE")


if __name__ == '__main__':
    get_incorrect_phred(input())
