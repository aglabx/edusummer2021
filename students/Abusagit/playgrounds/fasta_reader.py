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

        while True:
            try:
                header = next(iterator)
                sequence = []
                _part = next(iterator)
                while not _part.startswith('>'):
                    sequence.append(_part)
                    _part = next(iterator)

                yield header, ''.join(sequence)

            except StopIteration:
                yield header, ''.join(sequence)


if __name__ == '__main__':
    print(list(iter_fasta_reader(r"../rosalind/new")))
