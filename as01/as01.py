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
# 1. Get DNA String as an input
# 2. Get GC-Content of the DNA string as percentage
# 3. Print the results
dna = input()
# S/O to 50
g_units = dna.upper().count('G')
c_units = dna.upper().count('C')
gc_units = g_units + c_units
# Dividing to get decimal, multiplying to show percentage
percentage = (gc_units / len(dna)) * 100
# Formatting to round to three digits after decimal point
print(format(percentage, '.3f'))