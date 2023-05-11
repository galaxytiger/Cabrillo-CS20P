#!/usr/bin/env python3

"""
Provides decorator function "profile" that counts calls and cumulative execution time for all
decorated functions for the duration of an interpreter session.
"""

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import time
from functools import wraps

_profiling_data = {}


def profile(function):
  """
  Decorates a function so that the number of calls and cumulative execution time of all calls can
  be reported by call_count() and cumulative_time(), respectively. Execution time is measured by
  calling time.perf_counter() before and after a call to the decorated function.
  """
  _profiling_data[function] = {'count': 0, 'time': 0.0}

  @wraps(function)
  def wrapper(*args, **kwargs):
    start_time = time.perf_counter()
    result = function(*args, **kwargs)
    end_time = time.perf_counter()

    # if function not in _profiling_data:
    #   _profiling_data[function] = {'count': 0, 'time': 0}

    _profiling_data[function]['count'] += 1
    _profiling_data[function]['time'] += end_time - start_time

    return result
  # wrapper.__wrapped__ = function
  return wrapper


def call_count(function):
  """
  Returns the number of times a given function has been called during this interpreter session,
  assuming the function has been decorated by profile().
  """
  # original_function = getattr(function, '__wrapped__', function)
  return _profiling_data[function]['count']


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
  # original_function = getattr(function, '__wrapped__', function)
  return _profiling_data[function]['time']


def cumulative_times():
  """
  Returns a dictionary mapping functions decorated by profile() to the cumulative amount of time (in
  seconds) that have been spent executing calls to a given function during this interpreter session.
  """
  return {func: data['time'] for func, data in _profiling_data.items()}
