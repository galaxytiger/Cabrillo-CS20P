#!/usr/bin/env python3

""" word search to re-traumatize me from my time in school """

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import sys


def read_grid():
  grid = [list(line.strip()) for line in sys.stdin]
  return grid


if __name__ == "__main__":
  grid_test = read_grid()
  for row in grid_test:
    print("".join(row))
  print()
