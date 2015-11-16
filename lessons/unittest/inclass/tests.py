# import unittest stuff etc.
import unittest, gc

# import module we want to test
from module import Var
import numpy as np

class TestCase(unittest.TestCase):
  ''' a suite of unit tests '''
  
  def setUp(self):
    ''' setup for all tests '''
    self.var1 = Var(name='test', data=np.random.rand(5,5))
    
  def tearDown(self):
    ''' cleanup for all tests '''
    gc.collect() # for example, call garbage collector...
  
  # test cases come here
  
  def testCreate(self):
    ''' test creation of variable objects '''
    #assert isinstance(self.var1,Var)
    self.assertIsInstance(self.var1,Var)
  
  def testAdd(self):
    ''' test addition functions '''
    ref_data = self.var1.data.copy()*1e6
    self.var1 += 1
    assert np.allclose( self.var1.data ,(ref_data+1e6)/1.e6 )
    
    
  
if __name__ == '__main__':
  
    # run all tests
    unittest.main()