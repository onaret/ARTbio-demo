"""
Discovering biopython, using code from http://biopython.org/wiki/SeqIO
"""

import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description='Takes in input any Fasta file and returns in a "results" file \n a) the number of sequences in the file b) \n a tabular list of sequences name \\t sequence length')
parser.add_argument('--input', required=True, help='Input fasta file')
parser.add_argument('--output', required=False, default = 'results.txt', help='Result file')
param = parser.parse_args()

input_handle = open(param.input, "rU")
output_handle = open(param.output, "w")

count=0
output_handle.write("Name\tLength\n")
for record in SeqIO.parse(input_handle, "fasta") :
    output_handle.write(record.id + "\t" + str(len(record.seq)) + "\n")
    count+=1

output_handle.write('\nThere is ' + str(count) + " sequences in file " + str(param.input))

input_handle.close()
output_handle.close()