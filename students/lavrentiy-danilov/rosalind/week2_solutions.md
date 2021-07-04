# 1. Let's Be Practical (http://rosalind.info/problems/ini/)

```python
def count_letters_DNA(path):
    with open(path) as fl:
        seq = fl.readline()[:-1]
        seq_right = seq.upper()
    return "{} {} {} {}".format(seq_right.count('A'), seq_right.count('C'), seq_right.count('G'), seq_right.count('T'))
```

# 2. Four Commonly Used Protein Databases


```python
from Bio import ExPASy
from Bio import SwissProt

def get_go_protein(protein_name)

    handle = ExPASy.get_sprot_raw(protein_name)
    record = SwissProt.read(handle)

    bio_proc = []
    for item in record.cross_references:
        if item[0] == 'GO' and item[2][0]=='P':
            bio_proc.append(item[2].lstrip('P:'))

    return '\n'.join(bio_proc)
```


# 3. New Motif Discovery http://rosalind.info/problems/meme/

```python
import os
from subprocess import call

data, width, output= input().split()
CMD = f"meme {data} -text -protein -minw {width} > {output}"

if __name__ == '__main__':
    c = call(CMD, shell=True)

    with open(output) as outfile:
        for line in outfile:
            if 'regular expression' in line:
                separator = outfile.readline()
                reg = outfile.readline().rstrip()
                break

    os.remove('outfile')
    print(reg)
```

# 4. GenBank Introduction http://rosalind.info/problems/gbk/

```python
from Bio import Entrez

def genbank(path_to_file):
    with open(path_to_file, 'r') as fl:
        lines = [line.rstrip('\n') for line in fl]
    Entrez.email = "lavrentydanilov@gmail.com"
    term = '%s[Organism] AND (%s[Publication Date] : %s[Publication Date])' % (lines[0], lines[1], lines[2])
    handle = Entrez.esearch(db="nucleotide", term=term)
    record = Entrez.read(handle)
    return record["Count"]
```

# 5. Data Formats http://rosalind.info/problems/frmt/

```python
from Bio import Entrez
from Bio import SeqIO

def genbank_short_seq(path_ids):
    Entrez.email = "lavrentydanilov@gmail.com"
    with open(path_ids, 'r') as fl:
        ids = fl.readline()
    ids = ids.replace(" ", ", ")

    # Fetch data from GenBank server
    handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))
    
    rec = min(records, key=len)
    
    print('>' + rec.description)
    print(rec.seq)
genbank_short_seq('rosalind_frmt.txt')
```

# 6. FASTQ format introduction http://rosalind.info/problems/tfsq/

```python
from Bio import SeqIO

def converter(fastq):
    SeqIO.convert(fastq, "fastq", "tfsq_fasta.txt", "fasta")
    
    
converter('rosalind_tfsq.txt')
```


# 7. Read Quality Distribution http://rosalind.info/problems/phre/

```python
from Bio import SeqIO

def create_files(path_to_file):

    with open('rosalind_phre.txt', 'r') as f:
        threshold = f.readline()
        lines = f.readlines()

    with open('rosalind_phre_1.txt', 'w') as f:
        f.writelines(lines[:])

def average(l):
    return sum(l) / float(len(l))

def qthreshold(threshold, fastq):
    handle = SeqIO.parse(fastq, "fastq")

    belowthreshold = 0
    for record in handle:
        if average(record.letter_annotations["phred_quality"]) < int(threshold):
            belowthreshold += 1

    return belowthreshold

if __name__ = '__main__':
    create_files('rosalind_phre.txt')
    qthreshold(threshold, 'rosalind_phre_1.txt')
```

# 8. Read Filtration by Quality http://rosalind.info/problems/filt/

```python
from functools import reduce


def get_incorrect_phred(path):
    with open(path, 'r') as f_read:
        threshold, percentage = map(int, f_read.readline().split())

        a = f_read.readlines()
        filtered = 0

        for i in range(3, len(a), 4):
            qualities = [ord(char) - 33 for char in a[i].strip()]
            filt = reduce(lambda x, y: x + (y >= threshold), qualities, 0) / len(qualities) * 100
            filtered += filt >= percentage

    return filtered


get_incorrect_phred(input())
```

# 9. Base Quality Distribution http://rosalind.info/problems/bphr/

```python
def quality_distribution(path):
    with open(path) as fr:
        threshold = int(fr.readline())

        a = fr.readlines()
        low = 0
        for i in range(len(a[1].strip())):
            qualities = sum(ord(a[j][i]) - 33 for j in range(3, len(a), 4)) / (len(a) // 4)

            low += qualities < threshold

    return low

quality_distribution('rosalind_bphr.txt')
```

# 10. Base Filtration by Quality http://rosalind.info/problems/bfil/
```python
from Bio import SeqIO

def Base_Filtration_Quality(data):
    records = []
    with open(data, "r") as f:
        t = int(f.readline().strip())
        for record in SeqIO.parse(f, "fastq"):
            phred = record.letter_annotations["phred_quality"]
            start, end = 0, len(phred)
            while phred[start] < t:
                start += 1
            while phred[end-1] < t:
                end -= 1
            print(record[start:end].format('fastq'))

if __name__ == "__main__":
    data = input()
    Base_Filtration_Quality(data)
```
