#!/usr/bin/env python3
"""
Functions implementing readability tests.
See: https://en.wikipedia.org/wiki/Readability#Popular_readability_formulas
"""

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import re


def text_word(string):
  for w in string.strip().lower().split():
    w = re.sub(r"[^a-z]+", '', w)
    yield w


def words(string):
  return ' '.join(word for word in text_word(string)).split()


def character_count(string):
  char_count = 0
  for character in words(string):
    char_count += len(character)
  return char_count


# function for word count
def word_count(string):
  w_count = 0
  for _ in words(string):
    w_count += 1
  return w_count


# function for sentence count
def sentence_count(string):
  sen_count = 0
  string = re.sub(r'[),"\d]+', '', string)
  string = re.sub(r'\[|\]', '', string)
  string = re.sub(r'\"', '', string)
  word = string.split()
  for letter in word:
    match = re.search(r'[a-zA-Z]([.!?])', letter)
    if match:
      sen_count += 1
  return sen_count


# function to divide words and sentences
def word_sentence_divide(string):
  return word_count(string) / sentence_count(string)


def automated_readability_index(text: str):
  """
  Return the ARI score for the given text.
  See: https://en.wikipedia.org/wiki/Automated_readability_index
  """
  if sentence_count(text) == 0:
    return None
  else:
    ari = (4.71 * (character_count(text) / word_count(text))) + \
          (0.5 * (word_sentence_divide(text)) - 21.43)
    return ari


if __name__ == '__main__':
  import sys
  line = sys.stdin.read()
  if sentence_count(line) == 0:
    print(
      f'0.000\t({character_count(line)} characters '
      f'{word_count(line)} words {sentence_count(line)} sentences)'
    )
  else:
    # ari
    print(
      f'{automated_readability_index(line):.3f}\t({character_count(line)} characters '
      f'{word_count(line)} words {sentence_count(line)} sentences)'
    )
