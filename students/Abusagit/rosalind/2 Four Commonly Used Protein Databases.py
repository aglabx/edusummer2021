import requests
import re

url = "http://www.uniprot.org/uniprot/{}.txt"
pattern = r"DR   GO; GO:.......; P:[\w\s\d]{1,}"


def protein_db(protein_id):
    global url
    p = url.format(protein_id)
    get = requests.get(p).text
    result = re.findall(pattern, get)
    for res in result:
        yield res[23:]


if __name__ == '__main__':
    protein = input()

    for i in protein_db(protein_id=protein):
        print(i)