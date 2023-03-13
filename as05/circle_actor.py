#!/usr/bin/env python3
""" Module for the CircleActor class. """
__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'

import math


class CircleActor:
  """ Behaves as a circle in a 2D world centered on an X/Y coordinate. """
  def __init__(self, name: str, radius: float, world_size: tuple[float, float],
               position: tuple[float, float], velocity: tuple[float, float]):
    """
    Constructs a new CircleActor with a given name at a position and with an inherent velocity.

    :param name: the name of the actor, assumed to be non-empty
    :param position: the x/y coordinate of the center of the actor
    :param velocity: the amount in x/y dimensions by which the actor will move on each step
    :param radius: the initial radius of the actor
    """
    self.name = name
    self.radius = radius
    self.world_size = world_size
    self.position = position
    self.velocity = velocity

  def __bool__(self) -> bool:
    """
    Returns True if this actor is still "alive", meaning its radius is
    small enough for the circle to fit within the world and no less than 1.
    """
    return 1 <= self.radius <= min(self.world_size) / 2

  def __contains__(self, other) -> bool:
    """
    Returns True if another actor is "contained within" this one, i.e. whether the two actors
    overlap at all and this actor has a larger radius than the other.
    """
    if not isinstance(other, CircleActor):
      return False
    distance = self - other
    if distance <= 0 and self.radius > other.radius:
      return True
    else:
      return False

  def __repr__(self) -> str:
    """
    Returns a printable representation of this actor, appropriate for eval().
    That is, the return value of this method should be a string that is valid code for
    re-constructing this actor with the same attributes.
    """
    return f"CircleActor('{self.name}', {self.radius}, {self.world_size}, {self.position}," \
           f" {self.velocity})"

  def __str__(self) -> str:
    """
    Returns the name of this actor.
    """
    return self.name

  def __sub__(self, other) -> float:
    """
    Returns the distance between this actor and another,
    i.e. how far the two circles are from touching.
    This value will be negative if the two circles overlap.
    """
    distance = math.dist(self.position, other.position)
    return distance - self.radius - other.radius

  def collide(self, other) -> bool:
    """
    "Collides" this actor with another. If they overlap, the radius of the larger actor shall
    increase by 1 and that of the smaller will decrease by 1.
    """
    # TODO

  def position(self, new_position: tuple[float, float] = None):
    """
    Given no arguments, returns this actor's position.
    Given a tuple[float, float] as an argument, sets this actor's x/y position components.
    """
    if new_position is None:
      return self.position
    else:
      self.position = new_position

  def radius(self, new_radius: int | float = None):
    """
    Given no arguments, returns this actor's radius.
    Given a real number as an argument, sets this actor's radius.
    """
    if new_radius is None:
      return self.radius
    else:
      self.radius = new_radius

  def step(self):
    """
    Moves this actor in the direction of its velocity by one unit of "time",
    i.e. one frame of animation or one discrete event.
    e.g. if position is (4, 5) and velocity is (-1, 1), the new position will be (3, 6).
    """
    x, y = self.position
    dx, dy = self.velocity
    new_x = x + dx
    new_y = y + dy
    updated_position = (new_x, new_y)
    self.position = updated_position

  def velocity(self, new_velocity: tuple[float, float] = None):
    """
    Given no arguments, returns this actor's velocity.
    Given a tuple[float, float] as an argument, sets this actor's x/y velocity components.
    """
    if new_velocity is None:
      return self.velocity
    else:
      self.velocity = new_velocity
