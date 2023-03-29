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
    self.range_length = (stop - start + step - 1) // step

  def __getitem__(self, index):
    if isinstance(index, slice):
      start, stop, step = index.indices(len(self))
      new_start = self.start + self.start * start
      new_stop = self.start + self.step * stop
      if step < 0:
        new_start, new_stop = new_stop + self.step, new_start + self.step
      return CircularRange(new_start, new_stop, self.step * step)
    else:
      if index < 0:
        index = -index
      index = index % self.range_length
      return self.start + index * self.step

  def __len__(self):
    return self.range_length

  def __contains__(self, item):
    if item < self.start or item >= self.stop:
      return False
    return (item - self.start) % self.step == 0
