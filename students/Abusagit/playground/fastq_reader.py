import students.Abusagit.playground.block_reader as block_reader


def iter_fastq_file(fastq_file_name):
    """ Write here the correct doc string.
    """
    ...
    yield header, sequence, strand, quality_string


class FastqData(block_reader.BlockData):
    def __init__(self, path, phred=33):
        super(FastqData, self).__init__(path=path, file_format="fastaq")
        self.phred = phred

    @staticmethod
    def _parse_header(obj):
        pass  # TODO

    def _convert_phred_to_probability(self, char):
        return 10 ** (-0.1 * (ord(char) - self.phred))

    def iter_fastaq_file(self, unpack_generator=True):
        generator = super().iter_block_file(new_block_symbol='@')
        if unpack_generator:
            yield from generator
        else:
            for header, block in generator:
                sequence = next(block)
                strand = next(block)
                quality_string = next(block)
                yield header, sequence, strand, quality_string

    @staticmethod
    def iter_fastq_blocks(sequence, phred_score): # TODO make mor flexible and useful
        # for base, phred_score in zip(sequence, phred_score):
        #     yield base, phred_score
        # the same as:
        yield from zip(sequence, phred_score)


if __name__ == '__main__':
    fq = FastqData(rf"../rosalind/filteredrosalind_bfil")

    # for header, block in fq.iter_fastaq_file():
    #     print(header)
    #     print(block)
    #     print(list(fq.iter_fastq_blocks(block)))

    for i in fq.iter_fastaq_file():
        print(i)

    for i in fq.iter_fastaq_file(unpack_generator=False):
        print(i)