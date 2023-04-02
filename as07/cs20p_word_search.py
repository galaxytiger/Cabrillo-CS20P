#!/usr/bin/env python3

""" word search to re-traumatize me from my time in school """

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'
import sys
from bisect import bisect_left


def read_grid():
  """
  Reads word search grid from stdin and returns
  a list of lists containing the characters.
  """
  grid = [list(line.strip()) for line in sys.stdin]
  return grid


def load_dictionary(dict_file, min_length):
  """
  Reads a dictionary file, filters out words shorter than min_length,
  and sorts alphabetically.
  """
  with open(dict_file, "r") as file:
    dictionary = sorted(line.strip().upper() for line in file if len(line.strip()) >= min_length)
  return dictionary


def binary_search(dictionary, word):
  """
  Performs a binary search in the dictionary to check if
  a given word is present.
  """
  # using bisect_left to perform a binary search on
  pos = bisect_left(dictionary, word)
  return (pos != len(dictionary)) and (dictionary[pos] == word)


def find_valid_word(grid, min_length, dictionary):
  """
  Searches for valid words in the grid using the dictionary and
  iterates through each cell in the grid ala 'Espejeando by Los Tucanes De Tijuana' plus
  diagonally. Uses binary search function to verify if word is in dict and adds to found_words set.
  """
  directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
  found_words = set()
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      for dr, dc in directions:
        word = []
        r, c = row, col
        # loop to check if current row (r and c) are within
        # grids boundaries
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
          word.append(grid[r][c])
          # check if length of word is greater or equal to min length and
          # if word in dict using binary search.
          # if word is valid, adds to set
          if len(word) >= min_length and binary_search(dictionary, ''.join(word)):
            found_words.add(''.join(word))
          # update current row and column
          r += dr
          c += dc
  return found_words


def main(min_length, dict_file):
  grid = read_grid()
  dictionary = load_dictionary(dict_file, min_length)
  valid_words = find_valid_word(grid, min_length, dictionary)

  for word in sorted(valid_words):
    print(word)


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Why are you wasting electricity")
    sys.exit(1)

  min_length = int(sys.argv[1])
  dict_file = sys.argv[2]

  main(min_length, dict_file)
