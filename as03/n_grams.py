#!/usr/bin/env python3
"""
CS 20P n-grams!

For the purposes of this assignment, a word shall be defined as a sequence of non-whitespace
characters, with the following characters stripped from either end: !"#%&'()*,-./:;?@\\_¡§¶·¿
"""
__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import sys
from collections import defaultdict, Counter


def token(text):
  strip_chars = set("!\"#%&'()*,-./:;?@\\_¡§¶·¿")
  words = text.split()
  processed_words = []
  for word in words:
    # Strip characters from either end
    word = word.lower().strip()
    while word and word[0] in strip_chars:
      word = word[1:]
    while word and word[-1] in strip_chars:
      word = word[:-1]
    # Append result to list
    if word:
      processed_words.append(word)
  return processed_words


def find_ngrams(text, n):
  return zip(*[text[i:] for i in range(n)])


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

  # loop over all possible n-grams of the given length and update their counts
  n_gram_counts = Counter(find_ngrams(words, n_gram_len))

  # filter the n-grams based on the minimum count and sort them lexicographically
  filtered_n_grams = sorted(
    [(n_gram, count) for n_gram, count in n_gram_counts.items() if count >= min_count],
    key=lambda x: x[0])

  # group the filtered n-grams by their count
  grouped_n_grams = defaultdict(list)
  for n_gram, count in filtered_n_grams:
    grouped_n_grams[count].append(n_gram)

  # sort the grouped n-grams by their count and return the result
  return {count: sorted(n_gram_tuple, key=lambda x: x) for count, n_gram_tuple in
          grouped_n_grams.items()}


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
  # create dictionary
  n_grams_counts = defaultdict(Counter)
  # loop over n-gram lengths
  for n in range(min_len, max_len + 1):
    n_gram_dict = n_grams(text, n)
    for count, n_gram_list in n_gram_dict.items():
      for n_gram in n_gram_list:
        n_grams_counts[n][n_gram] += count
  # dictionary for final output
  result = {}
  # loop over n-gram lengths
  for n, n_gram_count in n_grams_counts.items():
    # filter out n-grams with count < 2
    n_gram_count = {k: v for k, v in n_gram_count.items() if v >= 2}
    # sort the n-grams by count (descending) and then lexicographically (ascending)
    sorted_n_grams = sorted(n_gram_count.items(), key=lambda x: (-x[1], x[0]))
    # take only the top `limit` n-grams
    top_n_grams = sorted_n_grams[:limit]
    # store the top n-grams in the final result dictionary
    result[n] = [(tuple(n_gram), count) for n_gram, count in top_n_grams]

  return result


def main():
  """
  Expects one or two command-line arguments:
  sys.argv[1]: A length of n-gram (e.g. 2 for bigrams)
  sys.argv[2] (optional): A minimum occurrence count (2 if unspecified)
  Then prints, in descending order of occurrence count, lines containing (a) the occurrence count
  and (b) a comma-separated list of all n-grams with that occurrence count,
  in ascending alphabetical/lexicographic order.
  """
  if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('why are you wasting electricity?')
    return

  try:
    n_gram_len = int(sys.argv[1])
    if len(sys.argv) == 3:
      min_count = int(sys.argv[2])
    else:
      min_count = 2
  except ValueError:
    print('NUMBERS ONLY!!!')
    return

  text = ' '.join(sys.stdin.readlines())

  n_grams_dict = n_grams(text, n_gram_len, min_count)

  for count in sorted(n_grams_dict.keys(), reverse=True):
    n_grams_list = n_grams_dict[count]
    n_grams_str = ', '.join([' '.join(n_gram) for n_gram in n_grams_list])
    print(f'{count} {n_grams_str}')


if __name__ == '__main__':
  main()
