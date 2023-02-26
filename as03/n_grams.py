#!/usr/bin/env python3
"""
CS 20P n-grams!

For the purposes of this assignment, a word shall be defined as a sequence of non-whitespace
characters, with the following characters stripped from either end: !"#%&'()*,-./:;?@\\_¡§¶·¿
"""
__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import sys
from collections import defaultdict, Counter


def token(text: str):
  whitelist = set('abcdefghijklmnopqrstuvwxyz \n')
  valid_words = ''.join(filter(whitelist.__contains__, text.lower()))
  return valid_words.split()


def n_grams(text: str, n_gram_len: int, min_count: int = 2) -> dict[int, list[tuple[str]]]:
  """
  Finds and returns all word n-grams of length `n_gram_len`
  occurring at least `min_count` times in `text`.

  :param text: the text to analyze
  :param n_gram_len: the desired length of n-grams (e.g. 2 for 2-grams)
  :param min_count: the minimum number of times a n-gram must appear in the text to be counted
  :return a dictionary mapping n-gram occurrence counts to a list of the n-grams occurring that
          number of times, as a list of n_gram_len-tuples of strings in ascending
          lexicographic/alphabetical order of the n-gram words.
  """
  words = token(text)

  # Initialize a defaultdict to keep track of the n-grams and their counts
  n_gram_counts = defaultdict(int)

  # Loop over all possible n-grams of the given length and update their counts
  for i in range(len(words) - n_gram_len + 1):
    n_gram = tuple(words[i:i + n_gram_len])
    n_gram_counts[n_gram] += 1

  # Filter the n-grams based on the minimum count and sort them lexicographically
  filtered_n_grams = sorted(
    [(n_gram, count) for n_gram, count in n_gram_counts.items() if count >= min_count],
    key=lambda x: x[0])

  # Group the filtered n-grams by their count
  grouped_n_grams = defaultdict(list)
  for n_gram, count in filtered_n_grams:
    grouped_n_grams[count].append(n_gram)

  # Sort the grouped n-grams by their count and return the result
  return {count: sorted(n_grams, key=lambda x: x) for count, n_grams in grouped_n_grams.items()}


def most_frequent_n_grams(text: str,
                          min_len: int = 1,
                          max_len: int = 10,
                          limit: int = 5) -> dict[int, list[tuple[tuple[str], int]]]:
  """
  Returns a dictionary mapping n-gram lengths to a list of the most frequently occurring word
  n-grams of that length, along with their occurrence counts, for n-grams appearing at least twice.

  :param text: the text to analyze
  :param min_len: the minimum n-gram length
  :param max_len: the maximum n-gram length
  :param limit: the maximum number of n-grams to display for each length
  :return a dictionary mapping n-gram lengths to a list of the most frequently occurring n-grams
          of that length, along with their occurrence counts, as a list of 2-tuples, where
          each tuple contains a tuple of the words in an n-gram and the n-gram's occurrence count.
          The list shall be sorted in descending order of occurrence count, with ties broken in
          ascending lexicographic/alphabetical order of the n-gram words.
  """
  # Initialize an empty dictionary to store n-grams and their counts
  ngram_counts = {}

  # Loop over all n-gram lengths in the given range
  for n in range(min_len, max_len + 1):

    # Initialize a Counter object to count n-grams of length n
    ngram_counter = Counter()

    # Loop over all n-grams of length n in the text
    for i in range(len(text) - n + 1):
      ngram = tuple(text[i:i + n].split())
      if len(ngram) == n:
        ngram_counter[ngram] += 1

    # Add the n-grams and their counts to the dictionary, if they occur at least twice
    ngram_list = [(ngram, count) for ngram, count in ngram_counter.items() if count >= 2]
    if ngram_list:
      ngram_counts[n] = sorted(ngram_list, key=lambda x: (-x[1], x[0]))[:limit]

  # Return the dictionary of n-gram counts
  return ngram_counts


def main():
  """
  Expects one or two command-line arguments:
  sys.argv[1]: A length of n-gram (e.g. 2 for bigrams)
  sys.argv[2] (optional): A minimum occurrence count (2 if unspecified)
  Then prints, in descending order of occurrence count, lines containing (a) the occurrence count
  and (b) a comma-separated list of all n-grams with that occurrence count,
  in ascending alphabetical/lexicographic order.
  """
  pass  # TODO


if __name__ == '__main__':
  main()
