#!/usr/bin/env python3

"""
Practice with graphs!
"""

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

from collections import defaultdict


class _Edges(defaultdict):
  pass  # TODO


class Graph(defaultdict):

  def __init__(self):
    super().__init__(_Edges)

  def __delitem__(self, key):

    pass  # TODO

  def __len__(self):
    pass  # TODO

  def __iter__(self):
    pass  # TODO

  def __contains__(self, key):

    pass  # TODO

  def clear(self):

    pass  # TODO

  def copy(self):

    pass  # TODO

  def vertices(self):

    pass  # TODO

  def edges(self):
    pass  # TODO

  def adjacent(self, src, dst):
    pass  # TODO

  def neighbors(self, vertex):
    pass  # TODO

  def degree(self, vertex):
    pass  # TODO

  def path_valid(self, vertices):
    pass  # TODO

  def path_length(self, vertices):
    pass  # TODO

  def is_connected(self):
    pass  # TODO


if __name__ == '__main__':
  g = Graph()
  assert len(g) == 0
  assert 'wat' not in g
  assert not g.vertices()
  edges = ('a', 'c', 8), ('a', 'd', 4), ('c', 'b', 6), ('d', 'b', 10), ('d', 'c', 2)
  for (v_from, v_to, weight) in edges:
    g[v_from][v_to] = weight
  assert len(g) == 4
  assert 'a' in g
  assert 'c' in g['a']
  assert g.vertices() == set('abcd')
  assert g.edges() == set(edges)
  assert g.degree('d') == 2 and not g.degree('b')
  assert g.adjacent('a', 'c')
  assert not g.adjacent('c', 'a')
  assert g.path_valid(('a', 'c', 'b'))
  assert not g.path_valid(('c', 'b', 'a'))
  assert not g.is_connected()
  g['b']['a'] = 1
  assert g.degree('b') == 1 and g.degree('a') == 2
  assert g.path_valid(('c', 'b', 'a'))
  assert g.path_length(('c', 'b', 'a')) == 7
  assert g.is_connected()
  del g['a']
  assert not g.is_connected()
  assert g.vertices() == set('bcd')
  assert g.degree('b') == 0

  g2 = g.copy()
  assert g2 == g
  g2['b']['e'] = 1
  assert g2 != g
  assert g2.vertices() == set('bcde')
  g2['e']['d'] = 15
  assert g2.is_connected()
  assert g2.path_length(('e', 'd', 'c', 'b')) == 23
  del g2['e']['d']
  assert g2.degree('e') == 0
  assert g2.vertices() == set('bcde')
  assert not g2.is_connected()
  g.clear()
  assert len(g) == 0
  assert len(g2) == 4
