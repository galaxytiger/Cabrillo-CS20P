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
    self.table_size = 8
    self.table = [None] * self.table_size
    self.num_keys = 0
    self.deleted = [False] * self.table_size
    if iterable is not None:
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
    return self.num_keys > 0

  def __contains__(self, key):
    """
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
    idx = self._find_key(key)
    return self.table[idx] is not None and not self.deleted[idx]

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
    for key in self.table:
      if key is not None:
        yield key

  def __repr__(self):
    """
    Returns a string representation of this set, suitable for eval().

    >>> h = HashSet([2, 4, 6, 0, 1])
    >>> eval(repr(h))
    HashSet([0, 1, 2, 4, 6])
    """
    items = ', '.join(map(str, self))
    return f'HashSet([{items}])'

  def __len__(self):
    """
    Returns the number of keys in this set.

    >>> h = HashSet(map(str.rstrip, open('/srv/datasets/many-english-words.txt')))
    >>> len(h)
    704240
    """
    return self.num_keys

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
    if key in self:
      return
    if self.num_keys == len(self.table):
      self._resize_table()
    idx = self._find_key(key)
    self.table[idx] = key
    self.deleted[idx] = False
    self.num_keys += 1

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
    self.table_size = 8
    self.table = [None] * self.table_size
    self.num_keys = 0

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
    idx = self._find_key(key)
    if self.table[idx] is not None:
      self.table[idx] = None
      self.deleted[idx] = True
      self.num_keys -= 1

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
    return len(self.table)

  def _resize_table(self):
    old_table = self.table
    self.table_size *= 2
    self.table = [None] * self.table_size
    self.deleted = [False] * self.table_size
    self.num_keys = 0
    for key in old_table:
      if key is not None:
        self.add(key)

  def _find_key(self, key):
    idx = hash(key) % len(self.table)
    while self.table[idx] is not None and self.table[idx] != key:
      if not self.deleted[idx]:
        idx = (idx + 1) % len(self.table)
    return idx
