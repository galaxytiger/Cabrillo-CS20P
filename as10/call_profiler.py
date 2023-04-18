#!/usr/bin/env python3

"""
Provides decorator function "profile" that counts calls and cumulative execution time for all
decorated functions for the duration of an interpreter session.
"""

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import time


def profile(function):
  """
  Decorates a function so that the number of calls and cumulative execution time of all calls can
  be reported by call_count() and cumulative_time(), respectively. Execution time is measured by
  calling time.perf_counter() before and after a call to the decorated function.
  """
  pass  # TODO


def call_count(function):
  """
  Returns the number of times a given function has been called during this interpreter session,
  assuming the function has been decorated by profile().
  """
  pass  # TODO


def call_counts():
  """
  Returns a dictionary mapping functions decorated by profile() to the number of times they have
  been called during this interpreter session.
  """
  pass  # TODO


def cumulative_time(function):
  """
  Returns the cumulative amount of time (in seconds) that have been spent executing calls to a given
  function during this interpreter session, assuming the function has been decorated by profile().
  """
  pass  # TODO


def cumulative_times():
  """
  Returns a dictionary mapping functions decorated by profile() to the cumulative amount of time (in
  seconds) that have been spent executing calls to a given function during this interpreter session.
  """
  pass  # TODO


Demo
Here is a
module
with a few functions from previous lectures, now decorated with call_profiler.profile:

call_profiler_demo.py
"""
Various functions for experimenting with the call_profiler module.
"""

__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import call_profiler


@call_profiler.profile
def dna(sequence) -> dict[str, int]:
  """
  Counts the bases in a DNA string.

  :param sequence: A DNA string (expected to contain A/C/G/T characters).
  :return: A dict[str, int] with keys in bases 'ACGT', and associated base counts.
  """
  return {base: sequence.count(base) for base in 'ACGT'}


@call_profiler.profile
def euler_004():
  """ Single statement with walrus. """
  return max(a * b
             for a in range(100, 1000)
             for b in range(100, 1000)
             if (prod_str := str(a * b)) == prod_str[::-1])


@call_profiler.profile
def euler_009():
  """ Generator expression passed to next()—we know there can be only one solution. """
  return next(a * b * c
              for a in range(1, 334)
              for b in range(a + 1, 1000 - a)
              if a ** 2 + b ** 2 == (c := 1000 - a - b) ** 2)