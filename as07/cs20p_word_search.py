#!/usr/bin/env python3

""" word search to re-traumatize me from my time in school """

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import sys
import os
import argparse

class WordSearch:
  def __init__(self):
    self.dir = [[-1, 0], [1, 0], [1, 1],
                    [1, -1], [-1, -1], [-1, 1],
                    [0, 1], [0, -1]]
