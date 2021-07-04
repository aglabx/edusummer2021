# 1. Let's Be Practical. http://rosalind.info/problems/ini/

```python
from collections import Counter
with open('/home/unity/Downloads/rosalind_ini.txt') as file:
    f = file.readline().rstrip()
    cnt = Counter(f)
    print(cnt['A'], cnt['C'], cnt['G'], cnt['T'])
```

# 2. Four Commonly Used Protein Databases. http://rosalind.info/problems/dbpr/

```python
import re
from bioservices import UniProt
uni = UniProt()
res = uni.search('Q5SLP9', frmt='tab', columns='go(biological process)').rstrip()
print(res)
res_split = re.split('[\n[;]', res)
print(res_split)
print(res_split[1], res_split[3], res_split[5], sep='\n')
```

# 3. New Motif Discovery. http://rosalind.info/problems/meme/

```python
with open('/home/unity/Downloads/meme.txt', 'r') as f:
    list_motifs = []
    for line in f:
        if 'regular expression' in line:
            next(f)
            line = f.readline().rstrip()
            list_motifs.append(line)
    print(list_motifs[0])
```

# 4. GenBank Introduction. http://rosalind.info/problems/gbk/

```python
from Bio import Entrez
Entrez.email = 'alex.kushnareva99@gmail.com'
with open('/home/unity/Downloads/rosalind_gbk.txt') as file:
    genus, date_begin, date_end = [line.strip() for line in file.readlines()]
    search = Entrez.esearch(db="nucleotide", term=genus+'[Organism]', 
                            mindate=date_begin, maxdate=date_end, datetype='pdat')
    record = Entrez.read(search)
    print(record['Count'])
```

# 5. Data Formats. http://rosalind.info/problems/frmt/

```python
from Bio import Entrez
from Bio import SeqIO
Entrez.email='alex.kushnareva99@gmail.com'
with open('/home/unity/Downloads/rosalind_frmt.txt') as file:
    ids = file.read().strip().split()
    handle = Entrez.efetch(db = "nucleotide", id = ids, rettype = "fasta")
    records = list (SeqIO.parse(handle, "fasta"))
    min_rec = min(records, key = lambda x: len(x.seq))
    print(">{}\n{}".format(min_rec.description, min_rec.seq))
```

# 6. FASTQ format introduction. http://rosalind.info/problems/tfsq/

```python
from io import StringIO
from Bio import SeqIO
with open('/home/unity/Downloads/rosalind_tfsq.txt') as infile:
    fastq_string = StringIO("")
    SeqIO.convert(infile, "fastq", fastq_string, "fasta")
    print(fastq_string.getvalue())
```

# 7. Read Quality Distribution. http://rosalind.info/problems/phre/

```python
from Bio import SeqIO
with open('/home/unity/Downloads/rosalind_phre.txt') as file:
    threshold = int(file.readline())
    reads = 0
    for record in SeqIO.parse(file, "fastq"):
        quality = record.letter_annotations["phred_quality"]
        av_q = sum(quality)/len(quality)
        if av_q < threshold:
            reads += 1
    print(reads)
```

# 8. Read Filtration by Quality. http://rosalind.info/problems/filt/

```python
from Bio import SeqIO
with open('/home/unity/Downloads/rosalind_filt.txt') as file:
    threshold, percentage = map(int, file.readline().strip().split())
    reads = 0
    for record in SeqIO.parse(file, "fastq"):
        quality = record.letter_annotations["phred_quality"]
        reads_above_t = 0
        for i in quality:
            if i >= threshold:
                reads_above_t += 1
        if (reads_above_t / len(quality)) * 100 >= percentage:
            reads += 1
    print(reads)
```

# 9. Base Quality Distribution. http://rosalind.info/problems/bphr/

```python
from Bio import SeqIO
with open('/home/unity/Downloads/rosalind_bphr.txt') as f:
    reads = 0
    q = []
    threshold = int(f.readline())
    for record in SeqIO.parse(f, "fastq"):
        quality = record.letter_annotations["phred_quality"]
        q.append(quality)
    for i in range(len(q[0])):
        if sum([qual[i] for qual in q])/len(q) < threshold:
            reads += 1
    print(reads)
```

# 10. Base Filtration by Quality. http://rosalind.info/problems/bfil/

```python
from Bio import SeqIO
with open('/home/unity/Downloads/rosalind_bfil.txt') as f:
    qual_cutoff = int(f.readline().strip())
    for record in SeqIO.parse(f, "fastq"):
        phred = record.letter_annotations["phred_quality"]
        s = 0
        e = 0
        while phred[s] < qual_cutoff:
            s += 1
        while phred[e - 1] < qual_cutoff:
            e -= 1
        print(record[s:e].format('fastq'))
```
