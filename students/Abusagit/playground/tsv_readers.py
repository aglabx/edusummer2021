import pandas as pd
import students.Abusagit.playground.сsv_reader as csv_reader


class TabSeparatedData(csv_reader.SeparatedData):
    def __init__(self, path, **kwargs):
        super(TabSeparatedData, self).__init__(path=path, file_format="tsv")
        self.data = pd.read_csv(self.path_format, sep='\t', **kwargs)


class GeneralFeatureFormat3(csv_reader.SeparatedData):
    def __init__(self, path, **kwargs):
        super().__init__(path, file_format=".gff")

        self.data = pd.read_table(
            self.path_format,
            comment='#',
            sep='\t',
            names=['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute'],
            **kwargs,
        )


class VariantCallFormat(csv_reader.SeparatedData):
    def __init__(self, path, **kwargs):
        super().__init__(path, file_format=".vcf")
        with open(path) as f_read:
            # self.comments = ''.join(l for l in f if l.startswith('##'))
            lines = f_read.readlines()
            for index, line in enumerate(lines):
                if not line.startswith("##"):
                    break

        self.__doc__ = '\n'.join(lines[:index])

        self.data = pd.read_csv(
            self.path_format,
            dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
                   'QUAL': str, 'FILTER': str, 'INFO': str},
            sep='\t',
            comment="##",
            **kwargs,
        ).rename(columns={'#CHROM': 'CHROM'})

        del lines

    def info(self):
        return self.__doc__


class BrowserExtensibleData(csv_reader.SeparatedData):

    def __init__(self, path, **kwargs):
        super().__init__(path, file_format=".bed")


class SequenceAlignmentMapData(csv_reader.SeparatedData):

    def __init__(self, path, **kwargs):
        super().__init__(path, file_format="sam")


