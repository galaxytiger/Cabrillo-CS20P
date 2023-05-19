#!/usr/bin/env python3

"""
Practice implementing a hash table!
"""

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

from typing import Iterable, Hashable


class HashSet:
  """
  Implementation of a hash table similar to built-in type set, using an internal list as a table.
  """

  def __init__(self, iterable: Iterable[Hashable] = None):
    """
    Constructs an empty set with a table size of 8, or a set containing the values in `iterable`.

    >>> h = HashSet()
    >>> len(h)
    0
    >>> h = HashSet((1, 9))
    >>> len(h)
    2
    """
    self._table_size = 8
    self.table = [None] * self._table_size
    self.size = 0
    self.load_factor = 2 / 3
    self.used = 0
    self.keys = []

    if iterable:
      for item in iterable:
        self.add(item)

  def __bool__(self):
    """
    Returns ''True'' if the set is non-empty, and ''False'' otherwise.

    >>> h = HashSet((1, 9))
    >>> bool(h)
    True
    >>> h.remove(1)
    >>> bool(h)
    True
    >>> h.remove(9)
    >>> bool(h)
    False
    """
    return self.size > 0

  def __contains__(self, key):
    r"""
    Tests for membership in the set.

    >>> import re
    >>> h = HashSet(re.findall(r"[\w']+", open('/srv/datasets/cat-in-the-hat.txt').read()))
    >>> 'play' in h
    True
    >>> 'plays' in h
    False
    >>> 'NOW' in h
    True
    >>> 100 in h
    False
    >>> None in h
    False
    """
    index = self._get_index(key)
    return self.table[index] is not None

  def __getitem__(self, index):
    """
    Returns the key at the given index of the internal table.

    >>> h = HashSet(range(1, 15, 3))
    >>> [h[i] for i in range(h.table_size())]
    [None, 1, 10, None, 4, 13, None, 7]
    """
    return self.table[index]

  def __iter__(self):
    """
    Yields keys from the internal table in the order encountered.

    >>> h = HashSet([2, 4, 6, 0, 1])
    >>> list(h)
    [0, 1, 2, 4, 6]
    """
    return iter(self.keys)

  def __repr__(self):
    """
    Returns a string representation of this set, suitable for eval().

    >>> h = HashSet([2, 4, 6, 0, 1])
    >>> eval(repr(h))
    HashSet([0, 1, 2, 4, 6])
    """
    return f"HashSet({list(self)})"

  def __len__(self):
    """
    Returns the number of keys in this set.

    >>> h = HashSet(map(str.rstrip, open('/srv/datasets/many-english-words.txt')))
    >>> len(h)
    704240
    """
    return self.size

  def add(self, key):
    """
    Adds a key to this set, if not already present.

    >>> h = HashSet()
    >>> for new_key in range(1, 21, 3):
    ...   h.add(new_key)
    ...   [h[i] for i in range(h.table_size())]
    ...
    [None, 1, None, None, None, None, None, None]
    [None, 1, None, None, 4, None, None, None]
    [None, 1, None, None, 4, None, None, 7]
    [None, 1, 10, None, 4, None, None, 7]
    [None, 1, 10, None, 4, 13, None, 7]
    [None, 1, None, None, 4, None, None, 7, None, None, 10, None, None, 13, None, None, 16, None]
    [None, 1, 19, None, 4, None, None, 7, None, None, 10, None, None, 13, None, None, 16, None]
    """
    if self.used / self._table_size >= self.load_factor:
      self._resize()

    index = self._get_index(key)
    while self.table[index] is not None:
      if self.table[index] == key:
        return
      index = self._linear_probe(index)

    self.table[index] = key
    self.keys.append(key)
    self.size += 1
    self.used += 1

  def clear(self):
    """
    Removes all keys from this set, returning the table to its initial state (size 8).

    >>> h = HashSet(map(str.rstrip, open('/srv/datasets/many-english-words.txt')))
    >>> len(h)
    704240
    >>> h.table_size()
    1376253
    >>> h.clear()
    >>> len(h)
    0
    >>> h.table_size()
    8
    """
    self._table_size = 8
    self.table = [None] * self._table_size
    self.size = 0
    self.used = 0
    self.keys = []

  def remove(self, key):
    """
    Removes a key from the set, if present. Does not raise an error if the key is not present.

    >>> h = HashSet((1, 9))
    >>> [h[i] for i in range(h.table_size())]
    [None, 1, 9, None, None, None, None, None]
    >>> 1 in h
    True
    >>> 9 in h
    True
    >>> 'one' in h
    False
    >>> h.remove(1)
    >>> len(h)
    1
    >>> 1 in h
    False
    >>> 9 in h
    True
    >>> [h[i] for i in range(h.table_size())]
    [None, None, 9, None, None, None, None, None]
    >>> h.remove(9)
    >>> len(h)
    0
    >>> [h[i] for i in range(h.table_size())]
    [None, None, None, None, None, None, None, None]
    """
    index = self._get_index(key)
    while self.table[index] is not None:
      if self.table[index] == key:
        self.table[index] = None
        self.size -= 1
        self.keys.remove(key)
        return
      index = self._linear_probe(index)

  def table_size(self):
    """
    Returns the size of the internal table.

    >>> h = HashSet()
    >>> for v in range(10):
    ...   h.add(v)
    ...   h.table_size()
    ...
    8
    8
    8
    8
    8
    18
    18
    18
    18
    18
    """
    return self._table_size

  def _get_index(self, key):
    return hash(key) % self._table_size

  def _linear_probe(self, index):
    distance = 1
    while True:
      forward_index = (index + distance) % self._table_size
      backward_index = (index - distance) % self._table_size

      if self.table[forward_index] is None or self.table[forward_index] is True:
        return forward_index
      if self.table[backward_index] is None or self.table[backward_index] is True:
        return backward_index

      distance += 1

  def _resize(self):
    new_size = self._table_size * 3
    self._table_size = new_size
    new_table = [None] * new_size

    for key in self.keys:
      index = self._get_index(key)
      while new_table[index] is not None:
        index = self._linear_probe(index)
      new_table[index] = key

    self.table = new_table
    self.used = self.size
