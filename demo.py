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
for record in SeqIO.parse(input_handle, "fasta") :
    count += SeqIO.write(record, output_handle, "fasta")
    output_handle.write("\t")

output_handle.write('There is ' + str(count) + " sequences in file " + str(param.input))

input_handle.close()
output_handle.close()