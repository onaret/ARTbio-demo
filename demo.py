"""
Discovering biopython, using code from http://biopython.org/wiki/SeqIO
"""

from Bio import SeqIO
handle = open("sample.fasta", "rU")
for record in SeqIO.parse(handle, "fasta") :
    print record.id
handle.close()