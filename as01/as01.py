#!/usr/bin/env python3
'''
The GC-content of a DNA string is given by the percentage of symbols
in the string that are 'C' or 'G'.
For example, the GC-content of "AGCTATAG" is 37.5%
Sample Dataset
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
Sample Output
Rosalind_0808
60.919540
'''

__author__ = 'Anthony Torres for CS 12P, altorresmoran@jeff.cis.cabrillo.edu'

import sys
dna = sys.stdin.read()
acgt_ls = [dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')]
gc_ls = [dna.count('C'), dna.count('G')]
acgt_total = sum(acgt_ls)
cg_total = sum(gc_ls)
print((cg_total / acgt_total) * 100)
