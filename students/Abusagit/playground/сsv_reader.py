import pandas as pd


class SeparatedData:
    path_string = "{0}.{1}"

    def __init__(self, path, file_format, comment='#'): # TODO add comment identificator
        self.path = "./" if '/' not in set(path) else path
        self.path_format = self.__class__.path_string.format(*(self.path, file_format))

    def __getattr__(self, item):
        return self.data.__getattr__(item)

    def __getitem__(self, item):
        return self.data.__getitem__(item)

    def __setitem__(self, key, value):
        return self.data.__setitem__(key, value)


class CommaSeparatedData(SeparatedData):
    def __init__(self, path, **kwargs):
        super(CommaSeparatedData, self).__init__(path=path, file_format="csv")
        self.data = pd.read_csv(self.path_format, **kwargs)


if __name__ == '__main__':
    a = CommaSeparatedData(r"C:/Users/Fyodor/PycharmProjects/practise/Crimes")
    print(a.head())

    print(a.iloc[:, 1:3])
    print(a["Primary Type"])
    print(a.iloc[0, 0])
    a.iloc[0, 0] = 1
    print(a.iloc[0, 0])
