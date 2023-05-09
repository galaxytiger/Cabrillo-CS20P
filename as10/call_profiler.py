#!/usr/bin/env python3

"""
Provides decorator function "profile" that counts calls and cumulative execution time for all
decorated functions for the duration of an interpreter session.
"""

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import time

_profiling_data = {}


def profile(function):
  """
  Decorates a function so that the number of calls and cumulative execution time of all calls can
  be reported by call_count() and cumulative_time(), respectively. Execution time is measured by
  calling time.perf_counter() before and after a call to the decorated function.
  """
  _profiling_data[function] = {'count': 0, 'cumulative_time': 0.0}

  def wrapper(*args, **kwargs):
    start_time = time.perf_counter()
    result = function(*args, **kwargs)
    elapsed_time = time.perf_counter() - start_time

    if function in _profiling_data:
      _profiling_data[function]['count'] += 1
      _profiling_data[function]['cumulative_time'] += elapsed_time
    else:
      _profiling_data[function] = {
        'count': 1,
        'cumulative_time': elapsed_time
      }
    return result
  return wrapper


def call_count(function):
  """
  Returns the number of times a given function has been called during this interpreter session,
  assuming the function has been decorated by profile().
  """
  return _profiling_data.get(function, {}).get('count', 0)


def call_counts():
  """
  Returns a dictionary mapping functions decorated by profile() to the number of times they have
  been called during this interpreter session.
  """
  return {func: data['count'] for func, data in _profiling_data.items()}


def cumulative_time(function):
  """
  Returns the cumulative amount of time (in seconds) that have been spent executing calls to a given
  function during this interpreter session, assuming the function has been decorated by profile().
  """
  return _profiling_data.get(function, {}).get('cumulative_time', 0.0)


def cumulative_times():
  """
  Returns a dictionary mapping functions decorated by profile() to the cumulative amount of time (in
  seconds) that have been spent executing calls to a given function during this interpreter session.
  """
  return {func: data['cumulative_time'] for func, data in _profiling_data.items()}
