# import unittest stuff etc.
import unittest, gc
import numpy as np

# import module we want to test
from module import Var

class TestCase(unittest.TestCase):
  ''' a suite of unit tests '''
  
  def setUp(self):
    ''' setup for all tests '''
    self.var = Var('test',np.random.randn(5,5))
  
  def tearDown(self):
    ''' cleanup for all tests '''
    gc.collect() # for example, call garbage collector...
  
  
  # test cases come here
  
  def testCreate(self):
    ''' test creation of variable objects '''
    self.assertIsInstance(self.var,Var)
  
  def testAdd(self):
    # test in-place addition
    ref_data = self.var.data.copy() + 2
    self.var += 2
    assert np.all( self.var.data == ref_data )
    # test regular addition
    new = self.var + self.var
    self.assertIsInstance(new,Var)
    assert np.all( new.data == self.var.data*2 )
  
  
if __name__ == '__main__':
  
    # run all tests
    unittest.main()