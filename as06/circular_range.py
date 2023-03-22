#!/usr/bin/env python3

""" Module for the CircularRange class. """

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import collections.abc


class CircularRange(collections.abc.Sequence):

  def __init__(self, start, stop, step=1):
    """Constructs a CircularRange with the given start/stop/step values."""
    self.start = start
    self.stop = stop
    self.step = step

  def __getitem__(self, index):
    pass  # TODO

  def __len__(self):
    pass  # TODO
