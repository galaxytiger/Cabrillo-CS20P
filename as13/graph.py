#!/usr/bin/env python3

"""
Practice with graphs!
"""

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

from collections import defaultdict


class _Edges(defaultdict):

  """
  A class used to represent the Edges in a Graph
  """
  def __init__(self, graph):
    super().__init__(int)
    self._graph = graph

  def __missing__(self, key):
    if key not in self._graph:
      raise KeyError(key)
    return 0

  def __delitem__(self, key):
    if key not in self:
      raise KeyError(key)
    super().__delitem__(key)

  def __setitem__(self, key, value):
    if key not in self._graph:
      self._graph[key] = _Edges(self._graph)
    super().__setitem__(key, value)


class Graph(defaultdict):
  """
  A Graph Representation
  """
  def __init__(self):
    super().__init__(_Edges)

  def __missing__(self, key):
    value = self[key] = _Edges(self)
    return value

  def __delitem__(self, key):
    if key not in self:
      raise KeyError(key)
    super().__delitem__(key)
    for vertex_edges in self.values():
      if key in vertex_edges:
        del vertex_edges[key]

  def __len__(self):
    return len(self.keys())

  def __iter__(self):
    return iter(self.keys())

  def __contains__(self, key):
    return key in self.keys()

  def clear(self):
    for key in list(self.keys()):
      del self[key]

  def copy(self):
    new_graph = Graph()
    for vertex, ver_edges in self.items():
      new_graph[vertex].update(ver_edges)
    return new_graph

  def vertices(self):
    return set(self.keys())

  def edges(self):
    return {(src, dst, e_weight) for src, v_edges in self.items() for dst, e_weight in
            v_edges.items()}

  def adjacent(self, src, dst):
    return src in self and dst in self[src]

  def neighbors(self, vertex):
    return set(self[vertex].keys())

  def degree(self, vertex):
    return len(self[vertex])

  def path_valid(self, vertices):
    return all(self.adjacent(vertices[i], vertices[i + 1]) for i in range(len(vertices) - 1))

  def path_length(self, vertices):
    if not self.path_valid(vertices) or len(vertices) <= 1:
      return None
    try:
      return sum(
            self[vertices[i]][vertices[i + 1]]
            # if isinstance(self[vertices[i]][vertices[i + 1]], (int, float))
            # else 0
            for i in range(len(vertices) - 1)
            if vertices[i + 1] in self[vertices[i]]
        )
    except KeyError:
      return None

  def is_connected(self):
    def dfs(start):
      visited = {start}
      stack = [start]
      while stack:
        vtex = stack.pop()
        for neighbor in self[vtex]:
          if neighbor not in visited:
            visited.add(neighbor)
            stack.append(neighbor)
      return visited
    return all(len(dfs(vertex)) == len(self) for vertex in self)


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
