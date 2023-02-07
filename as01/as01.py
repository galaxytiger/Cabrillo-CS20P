#!/usr/bin/env python3

import sys
def valid_dna(dna: str) -> str:
  return ''.join(filter(lambda c: c in 'ACGT', dna.upper().strip()))

if __name__ == '__main__':
  dna_len = []
  g_total = []
  c_total = []
  dna = []
  for line in sys.stdin:
    dna.append(valid_dna(line))
    pass
  print(len(dna))
  # gc_sum = (sum(g_total)) + (sum(c_total))
  # dna_sum = sum(dna_len)

  # # print(gc_sum, dna_sum)
  # if dna_sum == 0:
  #   print(gc_sum)
  # else:
  #   print((gc_sum / dna_sum) * 100)
  # result = ""
  #   for char in dna:
  #       if char in "ACGTacgt":
  #           result += char
  #   return result
# valid = set("ACGT")
# dna_len = []
# g_total = []
# c_total = []
# for line in sys.stdin:
#   dna = line.upper().strip()

#   g_total.append(dna.count('G'))
#   c_total.append(dna.count('C'))
#   dna_len.append(len(dna))
#   pass
# gc_sum = (sum(g_total)) + (sum(c_total))
# dna_sum = sum(dna_len)

# # print(gc_sum, dna_len)
# if dna_sum == 0:
#   print(gc_sum)
# else:
#   print((gc_sum / dna_sum) * 100)
