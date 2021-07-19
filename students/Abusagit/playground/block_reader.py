class BlockData:
    path_string = "{0}.{1}"  # 0 - path, 1 - format

    def __init__(self, path, file_format):
        self.path = r"./" if r'/' not in set(path) else path
        self.path_format = BlockData.path_string.format(*(path, file_format))

    def iter_block_objects(self, block_obj):
        yield from block_obj

    def iter_block_file(self, new_block_symbol):
        """
        Write here the correct doc string.
        """
        with open(fr"{self.path_format}") as f_read:
            _i = 1
            block_obj = {0: f_read.readline()}
            for line in f_read:
                if line.startswith(new_block_symbol):
                    yield block_obj[0].strip(), (block_obj[j] for j in range(1, _i))  # header, generator
                    _i = 1
                    block_obj.clear()
                    block_obj[0] = line
                else:
                    block_obj[_i] = line.strip()
                    _i += 1
            else:
                yield block_obj[0].strip(), (block_obj[j] for j in range(1, _i))  # header, generator
            block_obj.clear()


if __name__ == '__main__':
    a = BlockData(path='../rosalind/output', file_format="fasta")
    b = BlockData(path="../rosalind/new", file_format='fasta')

    for i in a.iter_block_file(new_block_symbol='>'):
        print(i, list(a.iter_block_objects(i[1])))

    for i in b.iter_block_file(new_block_symbol='>'):
        print(i, list(a.iter_block_objects(i[1])))
