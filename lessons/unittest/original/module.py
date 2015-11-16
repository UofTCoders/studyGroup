''' 
  A class we can use to test unit testing
'''

import numpy as np


class Var(object):
  ''' A container class for numpy arrays and some meta data '''

  def __init__(self, name, data, axes=None, units=None):
    ''' construct variable object with meta data '''
    self.name = name
    self.units = units
    self.axes = axes
    self.data = data
    
  def __iadd__(self, data):
    ''' overload in-place addition function: add number or arrays '''
    self.data += data
    return self
  
  def __add__(self, other):
    ''' overload addition function: add arrays and create new variable '''
    # check input
    if not isinstance(other, Var): return NotImplemented
    # handle more specific errors and print useful info
    if self.axes != other.axes: 
      raise ValueError("Axes mismatch: {:s} != {:s}".format(self.axes,other.axes))
    if self.units != other.units: 
      raise ValueError("Units mismatch: {:s} != {:s}".format(self.units,other.units))
    # add arrays
    data = self.data + other.data
    # create new variable object
    name = self.name + '+' + other.name
    new = Var(name, data, axes=self.axes, units=self.units)
    # return result
    return new
