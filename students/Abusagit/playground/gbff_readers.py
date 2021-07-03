import students.Abusagit.playground.block_reader as block_reader
import re


class GBFFData(block_reader.BlockData):
    seq_pattern = re.compile("ORIGIN.*\n")

    def __init__(self, path, file_format):
        super().__init__(path, file_format)

        self.taxon = ...
        self.sequence = {}

        with open(self.path_format) as f_read:
            self.header = f_read.readline()
            print(self.header)
            f_read = f_read.read()
            b = GBFFData.seq_pattern.search(f_read)

            # print(b.end())
            genome = (_.strip().split() for _ in f_read[b.end():].strip().strip('//').strip().split('\n'))

            for number, *line in genome:
                self.sequence[int(number)] = ''.join(line)

        self.locations = tuple(sorted(self.sequence.keys()))
        # self.length = self.locations[-1] + (len(self.sequence[self.locations[-1]]) - 1) # can be found in the 1st line
    def iter_gbff_blocks(self):
        """ Write here the correct doc string.
        """
        ...
        for start_index in super().iter_block_objects(self.sequence):
            yield start_index, self.sequence[start_index]

    def __getitem__(self, item):
        pass  # TODO adjust for index - 1 correction


if __name__ == '__main__':
    a = GBFFData(path=r"D:\Downloads\sequence", file_format="gb")
    # print(a.sequence)
    # print(a.sequence[1])
    # print(a.locations)
    # print(a.__sizeof__())
    # print(a.sequence.__sizeof__())
    # print(a.locations.__sizeof__())
    #