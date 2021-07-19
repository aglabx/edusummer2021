# 1. Let's Be Practical. http://rosalind.info/problems/ini/

```python
from collections import Counter


def dna_stats(string):
    stats = Counter()
    for base in string:
        stats[base] += 1
    return stats['A'], stats['C'], stats['G'], stats['T']


if __name__ == '__main__':
    name = input()
    with open(fr"D:\Downloads\{name}.txt") as f_read:
        dna = f_read.read().strip()
        print(*dna_stats(dna))
```



# 2. Four Commonly Used Protein Databases. http://rosalind.info/problems/dbpr/



```python
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
```



# 3. New Motif Discovery. http://rosalind.info/problems/meme/



```python
# Had to install meme toolkit on PC

import os
from subprocess import call

data = input("data: ")
width = input("width: ")
output = input("otput: ")
CMD = f"meme {data} -text -nostatus -protein -minw {width} > {output}"

if __name__ == '__main__':
    c = call(CMD, shell=True)

    with open(output) as outfile:
        for line in outfile:
            if 'regular expression' in line:
                separator = outfile.readline()
                regex = outfile.readline().rstrip()
                break

    os.remove('outfile')
    print(regex)
```



# 4. GenBank Introduction. http://rosalind.info/problems/gbk/



```python
from Bio import Entrez
import sys

Entrez.email = "mirotvorez00@gmail.com"

input_ = sys.stdin.read().strip().split('\n')
print(input_)
pattern = '"{0}"[Organism] AND ("{1}"[PDAT] : "{2}"[PDAT])'
handle = Entrez.esearch(db="nucleotide", term=pattern.format(*input_))

record = Entrez.read(handle)
print(record['Count'])
```



# 5. Data Formats. http://rosalind.info/problems/frmt/



```python
import sys
from Bio import Entrez
from Bio import SeqIO


Entrez.email = "mirotvorez00@gmail.com"

with open(r"D:\Downloads\rosalind_frmt (3).txt" ) as f_read:
    input_ids = f_read.read().strip()

handle = Entrez.efetch(db="nucleotide", id=[input_ids], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
print(records)
for f in records:
    print(f.name, len(f.seq))
SeqIO.write(min(records, key=lambda x: len(x.seq)), "output.fasta", "fasta")
```



# 6. FASTQ format introduction http://rosalind.info/problems/tfsq/



```python
file = input()

with open(fr"D:\Downloads\{file}.txt") as f_read, open("new.fasta", 'w') as f_write:
    for line in f_read:
        f_write.write(line.replace('@', '>'))
        f_write.write(f_read.readline())
        f_read.readline()
        f_read.readline()
```



# 7. Read Quality Distribution. http://rosalind.info/problems/phre/



```python
import sys
from functools import reduce


def get_incorrect_phred(file):
    with open(rf"D:\Downloads\{file}.txt") as f_read:
        threshold = int(f_read.readline())

        a = f_read.readlines()
        qualities = [None for _ in range(len(a) // 4)]
        for i in range(3, len(a), 4):
            qualities[i // 4] = sum(ord(char) - 33 for char in a[i].strip()) // len(a[i].strip())

        return reduce(lambda x, y: x + (y < threshold), qualities, 0)


if __name__ == '__main__':
    print(get_incorrect_phred(input()))
```



# 8. Read Filtration by Quality. http://rosalind.info/problems/filt/



```python
from functools import reduce


def get_incorrect_phred(file):
    with open(rf"D:\Downloads\{file}.txt") as f_read:
        threshold, percentage = map(int, f_read.readline().split())

        a = f_read.readlines()
        filtered = 0

        for i in range(3, len(a), 4):
            qualities = [ord(char) - 33 for char in a[i].strip()]
            filt = reduce(lambda x, y: x + (y >= threshold), qualities, 0) / len(qualities) * 100
            filtered += filt >= percentage

    return filtered

if __name__ == '__main__':
    print(get_incorrect_phred(input()))
```



# 9. Base Quality Distribution. http://rosalind.info/problems/bphr/



```python
def get_incorrect_phred(file):
    with open(rf"D:\Downloads\{file}.txt") as f_read:
        threshold = int(f_read.readline())

        a = f_read.readlines()

        below = 0
        for i in range(len(a[1].strip())):
            qualities = sum(ord(a[j][i]) - 33 for j in range(3, len(a), 4)) / (len(a) // 4)

            below += qualities < threshold

    return below


if __name__ == '__main__':
    print(get_incorrect_phred(input()))
```



# 10. Base Filtration by Quality. http://rosalind.info/problems/bfil/



```python
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

```

