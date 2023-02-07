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


def valid_dna(dna: str) -> str:
  return ''.join(filter(lambda c: c in 'ACGT', dna.upper()))


def gc_units(string):
  return ''.join(filter(lambda c: c in 'CG', string))


def gc_content(string):
  if len(valid_dna(string)) == 0:
    return len(gc_units(string))
  else:
    return (len(gc_units(string)) / len(valid_dna(string))) * 100


if __name__ == '__main__':
  import sys
  dna_input = []
  for line in sys.stdin:
    dna_input.append(valid_dna(line))
    pass
  print(''.join(dna_input))
  print(gc_content(''.join(dna_input)))
