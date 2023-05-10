#!/usr/bin/env python3

"""
Provides decorator function "profile" that counts calls and cumulative execution time for all
decorated functions for the duration of an interpreter session.
"""

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import time

_profiling_data = {}
_called_functions = set()


def profile(function):
  """
  Decorates a function so that the number of calls and cumulative execution time of all calls can
  be reported by call_count() and cumulative_time(), respectively. Execution time is measured by
  calling time.perf_counter() before and after a call to the decorated function.
  """
  # _profiling_data[function] = {'count': 0, 'time': 0.0}
  def wrapper(*args, **kwargs):
    start_time = time.perf_counter()
    result = function(*args, **kwargs)
    end_time = time.perf_counter()

    func_name = function.__qualname__

    if func_name not in _profiling_data:
      _profiling_data[func_name] = {'count': 0, 'time': 0}

    _profiling_data[func_name]['count'] += 1
    _profiling_data[func_name]['time'] += end_time - start_time

    return result
  _called_functions.add(function)
  return wrapper


def call_count(function):
  """
  Returns the number of times a given function has been called during this interpreter session,
  assuming the function has been decorated by profile().
  """
  # return _profiling_data.get(function, {}).get('count', 0)
  func_name = function.__qualname__
  return _profiling_data.get(func_name, {}).get('count', 0)
  # for key in _profiling_data:
  #   if key.__qualname__ == func_name:
  #     return _profiling_data[key]['count']
  # return 0


def call_counts():
  """
  Returns a dictionary mapping functions decorated by profile() to the number of times they have
  been called during this interpreter session.
  """
  return {func.__qualname__: _profiling_data[func.__qualname__]['count'] for func in
          _called_functions}
  # return {func: _profiling_data.get(func, {'count': 0}).get('count', 0) for func in
  #         _called_functions}


def cumulative_time(function):
  """
  Returns the cumulative amount of time (in seconds) that have been spent executing calls to a given
  function during this interpreter session, assuming the function has been decorated by profile().
  """
  # return _profiling_data.get(function, {}).get('time', 0)

  func_name = function.__qualname__
  return _profiling_data.get(func_name, {}).get('time', 0)
  # for key in _profiling_data:
  #   if key.__qualname__ == func_name:
  #     return _profiling_data[key]['time']
  # return 0


def cumulative_times():
  """
  Returns a dictionary mapping functions decorated by profile() to the cumulative amount of time (in
  seconds) that have been spent executing calls to a given function during this interpreter session.
  """
  return {func.__qualname__: _profiling_data[func.__qualname__]['time'] for func in
          _called_functions}
  # return {func: _profiling_data.get(func, {'count': 0}).get('time', 0) for func in
  #         _called_functions}
