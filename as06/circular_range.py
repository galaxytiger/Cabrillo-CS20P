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
    self.range_length = max(0, (stop - start + step - 1) // step)

  def __getitem__(self, index):
    if isinstance(index, slice):
      start, stop, step = index.indices(len(self))
      return CircularRange(self.start + self.step * start, self.start + self.step * stop,
                           self.step * step)
    else:
      if index < 0:
        index += self.range_length
      index = index % self.range_length
      return self.start + index * self.step

  def __len__(self):
    return self.range_length

  def __contains__(self, item):
    if item < self.start or item >= self.stop:
      return False
    return (item - self.start) % self.step == 0

  def __repr__(self):
    return f'CircularRange({self.start}, {self.stop}, {self.step}'
