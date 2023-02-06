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
import sys

gc_ls = []
dna_len = []
for line in sys.stdin:
  dna = line.upper()
  g_units = dna.count('G')
  c_units = dna.count('C')
  gc_ls.append(g_units)
  gc_ls.append(c_units)
  dna_len.append(len(line.strip()))
  continue
gc_count = sum(gc_ls)
percentage = (gc_count / sum(dna_len)) * 100
# Formatting to round to three digits after decimal point
print(format(percentage, '.6f'))