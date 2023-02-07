#!/usr/bin/env python3
'''
The GC-content of a DNA string is given by the percentage of symbols
in the string that are 'C' or 'G'.
'''

__author__ = 'Anthony Torres for CS 12P, altorresmoran@jeff.cis.cabrillo.edu'

import sys
dna = sys.stdin.read()
acgt_ls = [dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')]
gc_ls = [dna.count('C'), dna.count('G')]
acgt_total = sum(acgt_ls)
cg_total = sum(gc_ls)
if acgt_total == 0:
  print(0.000)
else:
  print((cg_total / acgt_total) * 100)
