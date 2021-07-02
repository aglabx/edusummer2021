def iter_fastq_file(fastq_file_name):
    """ Write here the correct doc string.
    """
    ...
    yield header, sequence, strand, quality_string


class FastqData(BlockData):
    ...

    def _parse_header(self):
        # воспользуйтесь документацией иллюмины
        ...

    def _convert_phred_to_probability(self):
        ...


def iter_fastq_blocks(fastq_file_name):
    """ Write here the correct doc string.
    """
    ...
    yield fastq_obj