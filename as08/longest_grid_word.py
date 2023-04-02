#!/usr/bin/env python3

""" Recursively searching a word-search grid for the longest "snake" word. """

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

from collections.abc import Sequence


class LongestGridWord:
  """ Offers a recursive search for the longest word in a word-search grid. """

  def __init__(self, word_list_file_path: str):
    """
    Constructs a LongestGridWord object prepared to search grids containing words from the given
    word-dictionary file. The file is assumed to be in class spell-checking dictionary format,
    i.e. one word per line.
    """
    with open(word_list_file_path, 'r') as f:
      self.words = set(line.strip().upper() for line in f)

  def longest_word(self, grid: Sequence[Sequence[str]]) -> str:
    """
    Recursively determines the longest word found in a grid by traveling any non-overlapping
    sequence of adjacent grid squares in any horizontal, vertical, or diagonal direction.
    The grid is assumed to consist of uppercase letters, and to be square.
    """
    pass  # TODO
