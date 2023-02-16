#!/usr/bin/env python3
"""
Functions implementing readability tests.
See: https://en.wikipedia.org/wiki/Readability#Popular_readability_formulas
"""

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import unicodedata
import re


def strip_accents(text):
  text = unicodedata.normalize('NFD', text)
  text = text.encode('ascii', 'ignore')
  text = text.decode('utf-8')
  return str(text)


def word(string):
  whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  return ''.join(filter(whitelist.__contains__, string))


def character_count(string):
  char_count = 0
  for character in ''.join(word(string).split()):
    char_count += len(character)
  return char_count


# function for word count
def word_count(string):
  w_count = 0
  for _ in word(string).split():
    w_count += 1
  return w_count


def sentence_count(string):
  sen_count = 0
  whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ .?!')
  string = ''.join(filter(whitelist.__contains__, strip_accents(string)))
  words = string.split()
  for letter in words:
    match = re.search(r'[a-zA-Z]([.!?])', letter)
    if match:
      sen_count += 1
  return sen_count


if __name__ == '__main__':
  import sys
  line = sys.stdin.read()
  print(f'{character_count(line)}c {word_count(line)}w {sentence_count(line)}s')
