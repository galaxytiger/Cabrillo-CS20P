#!/usr/bin/env python3
"""
Generator and other functions related to Scrabble® words.
"""
__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

from io import TextIOBase  # for type hints
from typing import Iterable, Iterator  # for type hints
import itertools  # suggested for permutations() and chain.from_iterable()
import re  # suggested for finditer()
import collections

legal_words = set()
with open('/srv/datasets/scrabble-hybrid') as scrabble:
  for line in scrabble:
    line = line.strip().split()
    line = list(filter(None, line))
    # iterating through list to add to set
    for ele in line:
      legal_words.add(ele)
  pass

letter_values = collections.defaultdict(list)
with open('/srv/datasets/scrabble-letter-values') as values:
  for line in values:
    letter, score = line.split()
    letter_values[letter] = score
    pass

 
 
def tokenize_words(file: TextIOBase) -> Iterator[str]:
  """
  Tokenizes the contents of a text-file object (e.g. from open() or sys.stdin) and yields
  all contiguous sequences of English letters from the file, in uppercase.
 
  >>> from pprint import pprint
  >>> pprint(list(tokenize_words(open('/srv/datasets/party.txt'))), compact=True)
  ['THE', 'PARTY', 'TOLD', 'YOU', 'TO', 'REJECT', 'THE', 'EVIDENCE', 'OF', 'YOUR',
   'EYES', 'AND', 'EARS', 'IT', 'WAS', 'THEIR', 'FINAL', 'MOST', 'ESSENTIAL',
   'COMMAND']
  >>> pprint(list(tokenize_words(open('/srv/datasets/phonewords-e.161.txt'))))
  ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
  """
  file_contents = file.read()
  pattern = r'[A-Z]+'
  words = re.findall(pattern, file_contents)
  for word in words:
    yield word.upper()

 
 
def legal_words(words: Iterable[str]) -> Iterator[str]:
  """
  Selects from an iterable collection of strings only those that are legal Scrabble® words.
 
  >>> from pprint import pprint
  >>> pprint(list(legal_words(tokenize_words(open('/srv/datasets/party.txt')))), compact=True)
  ['THE', 'PARTY', 'TOLD', 'YOU', 'TO', 'REJECT', 'THE', 'EVIDENCE', 'OF', 'YOUR',
   'EYES', 'AND', 'EARS', 'IT', 'WAS', 'THEIR', 'FINAL', 'MOST', 'ESSENTIAL',
   'COMMAND']
  >>> pprint(list(legal_words(tokenize_words(open('/srv/datasets/phonewords-e.161.txt')))))
  ['DEF', 'GHI']
  >>> pprint(list(legal_words(tokenize_words(open('/srv/datasets/empty')))))
  []
  >>> list(legal_words(['all', 'in', 'lowercase']))
  []
  """
  pass  # TODO
 
 
def word_score(word: str) -> int:
  """
  Computes the sum of the tile values for a given word, or 0 if the word is illegal.
 
  >>> from pprint import pprint
  >>> pprint([(w, word_score(w)) for w in tokenize_words(open('/srv/datasets/party.txt'))], \
             compact=True)
  [('THE', 6), ('PARTY', 10), ('TOLD', 5), ('YOU', 6), ('TO', 2), ('REJECT', 15),
   ('THE', 6), ('EVIDENCE', 14), ('OF', 5), ('YOUR', 7), ('EYES', 7), ('AND', 4),
   ('EARS', 4), ('IT', 2), ('WAS', 6), ('THEIR', 8), ('FINAL', 8), ('MOST', 6),
   ('ESSENTIAL', 9), ('COMMAND', 14)]
  >>> pprint([(w, word_score(w)) \
                  for w in tokenize_words(open('/srv/datasets/phonewords-e.161.txt'))], \
             compact=True)
  [('ABC', 0), ('DEF', 7), ('GHI', 7), ('JKL', 0), ('MNO', 0), ('PQRS', 0),
   ('TUV', 0), ('WXYZ', 0)]
  >>> word_score('lowercase')
  0
  """
  pass  # TODO
 
 
def highest_value_word(words: Iterable[str]) -> str:
  """
  Selects from an iterable collection of strings the highest-valued Scrabble® word,
  as returned by the word_score() function.
  If multiple words are maximal, the function returns the first one encountered.
  If no words are present, raises an exception of some kind.
 
  >>> highest_value_word(tokenize_words(open('/srv/datasets/party.txt')))
  'REJECT'
  >>> highest_value_word(tokenize_words(open('/srv/datasets/phonewords-e.161.txt')))
  'DEF'
  >>> try:
  ...   highest_value_word(tokenize_words(open('/srv/datasets/empty')))
  ... except Exception as error:
  ...   print('error')
  ... 
  error
  """
  pass  # TODO
 
 
def legal_tile_words(tiles: str) -> list[str]:
  """
  Returns a sorted list of all the legal Scrabble® words that could be formed from the "tiles"
  represented by the argument string.
 
  >>> legal_tile_words('JTQHDEZ')
  ['DE', 'ED', 'EDH', 'EH', 'ET', 'ETH', 'HE', 'HET', 'JET', 'TE', 'TED', 'THE', 'ZED']
  """
  pass  # TODO
 
 
if __name__ == '__main__':
  # Print the total number of legal words on stdin and their total value in points, just for fun
  import sys
  (i1, i2) = itertools.tee(legal_words(tokenize_words(sys.stdin)))
  print(sum(1 for _ in i1), 'legal Scrabble words worth', sum(map(word_score, i2)), 'points')
