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
