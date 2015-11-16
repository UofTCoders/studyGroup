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