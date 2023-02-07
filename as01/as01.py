#!/usr/bin/env python3
import sys

def valid_dna(dna: str) -> str:
  return ''.join(filter(lambda c: c in 'ACGT', dna.upper().strip()))


def gc_units(string):
  return ''.join(filter(lambda c: c in 'CG', string))

def gc_content(string):
  if len(valid_dna(string)) == 0:
    return len(gc_units(string))
  else:
    return (len(gc_units(string)) / len(valid_dna(string))) * 100

if __name__ == '__main__':
  import sys
  dna = []
  for line in sys.stdin:
    dna.append(valid_dna(line))
    pass
print(gc_content(''.join(dna)))
