#!/usr/bin/env python3

"""
Practice with Path Finding
"""

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import heapq
import csv
from collections import defaultdict


class CaliforniaRoadNetwork:
  """
    A class used to represent the California Road Network
  """
  def __init__(self):
    self._graph = self.edges()
    self._nodes = self.nodes()
    self._names = self.names()

  def nodes(self):
    """
    Returns the nodes in the graph.
    """
    nodes = {}
    with open('/srv/datasets/ca_roads/cal.cnode', 'r') as f:
      reader = csv.reader(f, delimiter=' ')
      for node_id, lon, lat in reader:
        node_id = int(node_id)
        nodes[node_id] = (float(lon), float(lat))
    return nodes

  def edges(self):
    """
    Returns the edges in the graph.
    """
    edges = {}
    with open('/srv/datasets/ca_roads/cal.cedge', 'r') as f:
      reader = csv.reader(f, delimiter=' ')
      for edge_id, start, end, distance in reader:
          edge_id = int(edge_id)
          start = int(start)
          end = int(end)
          distance = float(distance)
          edges[edge_id] = (start, end, distance)
      return edges

  def names(self):
    """
    Returns the names of the nodes in the graph.
    """
    names = {}
    with open('/srv/datasets/ca_roads/cal.cnode.names', 'r') as f:
      reader = csv.reader(f, delimiter=' ')
      for row in reader:
          node_id = int(row[0])
          node_name = ' '.join(row[1:]).strip('"')
          names[node_id] = node_name
    return names
