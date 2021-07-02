"""
Implements reading .fasta file format
"""


def stupid_fasta_reader(fasta_file_name):
    """

    """
    sequences = []

    return sequences


def iter_fasta_reader(fasta_file_name):
    with open(rf"{fasta_file_name}.fasta") as f_read:
        # print(f_read.readlines())
        iterator = iter(f_read.readlines())
    sequence = {0: next(iterator)}
    i = 1
    for line in iterator:
        if line.startswith('>'):
            yield sequence[0], ''.join(sequence[j] for j in range(1, i))
            i = 1
            sequence.clear()
            sequence[0] = line
        else:
            sequence[i] = line.strip()
            i += 1
    else:
        yield sequence[0], ''.join(sequence[j] for j in range(1, i))


class FastaData:
    def __init__(self, fileobj):
        pass

    def _parse_header(self):
        pass




if __name__ == '__main__':
    for h, s in iter_fasta_reader(rf"../rosalind/output"):
        print(h, repr(s))
        print(len(s))

