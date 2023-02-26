#!/usr/bin/env python3
"""
CS 20P n-grams!

For the purposes of this assignment, a word shall be defined as a sequence of non-whitespace
characters, with the following characters stripped from either end: !"#%&'()*,-./:;?@\\_¡§¶·¿
"""
__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import sys
from collections import defaultdict, Counter


# def token(string, chars='!#"#%&\'()*,-./:;?@\\_¡§¶·¿'):
#   return string.lower().strip(chars).split()

def token(string):
  whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ\n')
  valid_words = ''.join(filter(whitelist.__contains__, string.lower()))
  return valid_words.split()


def n_grams(text: str, n_gram_len: int, min_count: int = 2) -> dict[int, list[tuple[str]]]:
  """
  Finds and returns all word n-grams of length `n_gram_len`
  occurring at least `min_count` times in `text`.

  :param text: the text to analyze
  :param n_gram_len: the desired length of n-grams (e.g. 2 for 2-grams)
  :param min_count: the minimum number of times an n-gram must appear in the text to be counted
  :return a dictionary mapping n-gram occurrence counts to a list of the n-grams occurring that
          number of times, as a list of n_gram_len-tuples of strings in ascending
          lexicographic/alphabetical order of the n-gram words.
  """
  words = token(text)
  # Count the n-grams and filter based on the minimum count
  n_gram_counts = Counter(zip(*[words[i:] for i in range(n_gram_len)]))
  filtered_n_grams = [(n_gram, count) for n_gram, count in n_gram_counts.items() if
                      count >= min_count]

  # Sort the filtered n-grams lexicographically and group them by count
  sorted_n_grams = sorted(filtered_n_grams, key=lambda x: x[0])
  grouped_n_grams = defaultdict(list)
  for n_gram, count in sorted_n_grams:
    grouped_n_grams[count].append(tuple(sorted(n_gram)))

  # Sort the grouped n-grams by count and return the result
  return {count: n_grams_list for count, n_grams_list in
          sorted(grouped_n_grams.items(), reverse=True)}


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
  # Split the text into words
  words = text.split()

  # Initialize a dictionary to keep track of the n-grams and their counts
  n_gram_counts = defaultdict(Counter)

  # Loop over all possible n-grams of the given lengths and update their counts
  for n in range(min_len, max_len + 1):
    for i in range(len(words) - n + 1):
      n_gram_tuple = tuple(words[i:i + n])
      n_gram_counts[n][n_gram_tuple] += 1

  # Filter the n-grams based on the minimum count and sort them lexicographically
  filtered_n_grams = {}
  for n in range(min_len, max_len + 1):
    filtered_n_grams[n] = sorted(
      [(n_gram, count) for n_gram, count in n_gram_counts[n].items() if count >= 2],
      key=lambda x: (-x[1], x[0]))

  # Truncate the list of n-grams to the specified limit
  truncated_n_grams = {}
  for n in range(min_len, max_len + 1):
    truncated_n_grams[n] = filtered_n_grams[n][:limit]

  return truncated_n_grams


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
