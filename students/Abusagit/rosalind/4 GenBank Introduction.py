from Bio import Entrez
import sys

Entrez.email = "mirotvorez00@gmail.com"

input_ = sys.stdin.read().strip().split('\n')
print(input_)
pattern = '"{0}"[Organism] AND ("{1}"[PDAT] : "{2}"[PDAT])'
handle = Entrez.esearch(db="nucleotide", term=pattern.format(*input_))

record = Entrez.read(handle)
print(record['Count'])